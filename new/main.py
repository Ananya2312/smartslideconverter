import cv2
import numpy as np
import easyocr
import shutil
import io
import os
import time
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
from PIL import Image
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI App
app = FastAPI()

# ✅ Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Initialize OCR reader
reader = easyocr.Reader(["en"])

# ✅ Directory to store files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ✅ Live Camera Feed Setup
camera = None  # Global variable for video feed


def preprocess_image(image):
    """Converts image to grayscale and applies denoising."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
    return denoised


def extract_text(image):
    """Extracts text from the processed image."""
    processed_image = preprocess_image(image)
    results = reader.readtext(processed_image, detail=0)
    return "\n".join(results)


def generate_pdf(text, filename="extracted_text.pdf"):
    """Generates a PDF with extracted text."""
    # Ensure the file has a .pdf extension
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    
    pdf_path = os.path.join(UPLOAD_DIR, filename)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Extracted Text", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)
    return pdf_path


@app.post("/extract_text/")  # For image text extraction
async def extract_text_from_image(file: UploadFile = File(...)):
    """Handles image file upload and returns extracted text."""
    try:
        image = Image.open(io.BytesIO(file.file.read()))
        image = np.array(image)
        extracted_text = extract_text(image)
        pdf_path = generate_pdf(extracted_text)

        # Ensure the filename in the response is correct (with .pdf extension)
        pdf_filename = os.path.basename(pdf_path)
        logger.info(f"PDF generated at: {pdf_filename}")
        return JSONResponse({"extracted_text": extracted_text, "pdf_path": pdf_filename})
    except Exception as e:
        logger.error(f"Error extracting text from image: {e}")
        raise HTTPException(status_code=500, detail="Error processing the image")


@app.post("/extract_text_from_video/")  # For video text extraction
async def extract_text_from_video(file: UploadFile = File(...)):
    """Processes video frame-by-frame and extracts text."""
    try:
        video_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        cap = cv2.VideoCapture(video_path)
        full_text = []

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % 10 == 0:  # Every 10th frame (can be adjusted)
                text = extract_text(frame)
                full_text.append(text)
            frame_count += 1

        cap.release()

        extracted_text = "\n".join(full_text)
        pdf_path = generate_pdf(extracted_text)

        # Ensure the filename in the response is correct (with .pdf extension)
        pdf_filename = os.path.basename(pdf_path)
        logger.info(f"PDF generated at: {pdf_filename}")
        return JSONResponse({"extracted_text": extracted_text, "pdf_path": pdf_filename})
    except Exception as e:
        logger.error(f"Error extracting text from video: {e}")
        raise HTTPException(status_code=500, detail="Error processing the video")


@app.post("/extract_text_from_camera/")  # For live camera text extraction
async def extract_text_from_camera():
    """Captures a single frame from live camera and extracts text."""
    try:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        if not ret:
            cap.release()
            logger.error("Could not capture frame from camera")
            raise HTTPException(status_code=500, detail="Could not capture frame from camera")

        extracted_text = extract_text(frame)
        pdf_path = generate_pdf(extracted_text)

        # Ensure the filename in the response is correct (with .pdf extension)
        pdf_filename = os.path.basename(pdf_path)
        cap.release()  # Ensure to release the camera resource
        logger.info(f"PDF generated at: {pdf_filename}")
        return JSONResponse({"extracted_text": extracted_text, "pdf_path": pdf_filename})
    except Exception as e:
        cap.release()  # Release camera on error
        logger.error(f"Error extracting text from camera: {e}")
        raise HTTPException(status_code=500, detail="Error processing the camera")


@app.get("/download_pdf/{filename}")  # Download PDF of extracted text
async def download_pdf(filename: str):
    """Serves the extracted text PDF for download."""
    # Ensure the file has a .pdf extension
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    pdf_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, media_type="application/pdf", filename=filename)
    raise HTTPException(status_code=404, detail="PDF not found")


@app.get("/video_feed")  # For live camera feed streaming
async def video_feed():
    """Streams live video feed from the camera."""
    global camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        logger.error("Camera not accessible")
        raise HTTPException(status_code=500, detail="Camera not accessible")

    def generate_frames():
        while True:
            success, frame = camera.read()
            if not success:
                break

            # Resize frame to reduce load
            frame_resized = cv2.resize(frame, (640, 480))  # Resized frame

            # Encode frame as JPEG
            ret, buffer = cv2.imencode(".jpg", frame_resized)
            if not ret:
                continue

            # Yield frame as part of multipart response
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
            
            time.sleep(0.033)  # Limiting the frame rate to ~30 FPS

    # Return the frames in a streaming response
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")


@app.on_event("shutdown")  # Release camera resources on shutdown
def shutdown_event():
    """Release camera resources on shutdown."""
    global camera
    if camera is not None:
        camera.release()
        logger.info("Camera resources released")


if __name__ == "__main__":  # Run the FastAPI app
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
