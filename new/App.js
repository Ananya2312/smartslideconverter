import React, { useState } from "react";
import axios from "axios";


function App() {
    const [option, setOption] = useState("image");
    const [file, setFile] = useState(null);
    const [extractedText, setExtractedText] = useState("");

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleExtract = async () => {
        if (option === "camera") {
            try {
                const response = await axios.post("http://127.0.0.1:8000/extract_text_from_camera/");
                setExtractedText(response.data.extracted_text);
            } catch (error) {
                console.error("Error extracting text:", error);
            }
        } else if (file) {
            const formData = new FormData();
            formData.append("file", file);

            let url = option === "image" ? "http://127.0.0.1:8000/extract_text/" : "http://127.0.0.1:8000/extract_text_from_video/";

            try {
                const response = await axios.post(url, formData, {
                    headers: { "Content-Type": "multipart/form-data" }
                });
                setExtractedText(response.data.extracted_text);
            } catch (error) {
                console.error("Error extracting text:", error);
            }
        } else {
            alert("Please select a file!");
        }
    };

    return (
        <div className="container">
            <h1>OCR Text Extraction</h1>

            <label>Choose Input Method:</label>
            <select onChange={(e) => setOption(e.target.value)}>
                <option value="image">Upload Image</option>
                <option value="video">Upload Video</option>
                <option value="camera">Live Camera</option>
            </select>

            {option !== "camera" && <input type="file" onChange={handleFileChange} />}

            <button onClick={handleExtract}>Extract Text</button>

            {extractedText && (
                <div>
                    <h2>Extracted Text</h2>
                    <textarea value={extractedText} readOnly />
                </div>
            )}
        </div>
    );
}

export default App;
