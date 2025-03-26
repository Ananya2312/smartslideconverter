#  Smart Board to Slide Deck Converter
Project Overview

An AI-powered solution to convert handwritten content from smart boards (images/videos) into structured slide decks. This system addresses the challenges of extracting handwritten text under varying conditions and transforms it into well-formatted digital documents(PDF).

[![Presentation](https://img.shields.io/badge/View-Presentation-FF5722?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](https://docs.google.com/presentation/d/1IcPPLynenFyypGG41a6aduPObdpG1rCB/edit?usp=sharing&ouid=107016641315213345291&rtpof=true&sd=true)

[![Demo](https://img.shields.io/badge/Watch-Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/file/d/1InaBE2eqVDYx2xfHRz2M20sWVeFG6DVl/view?usp=sharing)
# Traditional OCR models:
Varying handwriting styles

Poor lighting conditions

Motion blur in videos

Structure preservation

Mathematical equation recognition
# Key Features
Video Frame Extraction: Captures key moments from lecture/meeting videos

Advanced OCR: Combines EasyOCR and TrOCR for handwritten text recognition

AI Enhancement: Improves accuracy and formatting of extracted content

Multi-element Processing: Handles text, diagrams, and mathematical equations

Structured Output: Generates searchable PDF documents
## Resources
- **Presentation Slides**: [Neural_Ninjas.pptx](https://docs.google.com/presentation/d/1IcPPLynenFyypGG41a6aduPObdpG1rCB/edit?usp=sharing&ouid=107016641315213345291&rtpof=true&sd=true
) - Our complete project presentation

- **Demo Video**: [Watch Demo](https://drive.google.com/file/d/1InaBE2eqVDYx2xfHRz2M20sWVeFG6DVl/view?usp=drive_link) - Live demonstration of the system
## 🛠️ Tech Stack

### Frontend
<p align="left">
  <a href="https://reactjs.org/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/-React-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React">
    <img src="https://img.icons8.com/office/40/000000/react.png" alt="React" width="40" height="40"/>
  </a>
</p>

### Backend
<p align="left">
  <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="40" height="40"/>
  </a>
</p>

## 🤖 AI/ML Components

| Component | Symbol | Badge | Description |
|-----------|--------|-------|-------------|
| **OpenCV** | 📸 | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) | Frame extraction and preprocessing |
| **EasyOCR** | 🔍 | ![EasyOCR](https://img.shields.io/badge/EasyOCR-00B0FF?style=flat&logo=python&logoColor=white) | Primary OCR engine |
| **Microsoft TrOCR** | ✍️ | ![TrOCR](https://img.shields.io/badge/TrOCR-0078D4?style=flat&logo=microsoft&logoColor=white) | Handwritten text recognition |
| **Facebook BART** | 📖 | ![BART](https://img.shields.io/badge/BART-4267B2?style=flat&logo=facebook&logoColor=white) | Text categorization and enhancement |

## Alternative Visual Presentation

### 🖥️ Computer Vision
<p align="left">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white" alt="OpenCV" title="Frame extraction">
  <img src="https://img.icons8.com/color/48/000000/opencv.png" width="30" alt="OpenCV">
</p>

### 🔤 Text Recognition
<p align="left">
  <img src="https://img.shields.io/badge/EasyOCR-00B0FF?logo=python&logoColor=white" alt="EasyOCR">
  <img src="https://img.shields.io/badge/TrOCR-0078D4?logo=microsoft&logoColor=white" alt="Microsoft TrOCR">
</p>

## 🚀 Deployment

### Backend API
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)  
- 🌐 Web API deployment
- 📡 Auto-generated docs

### Frontend
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=white)  
- 🖥️ Hosted on Vercel/Netlify
- 🔗 API integration

### Testing
![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=google-colab&logoColor=white)  
- � Notebook testing
- 🆓 Free GPU access
- 
# Implementation Workflow
Frame Extraction: Extract and preprocess frames from input videos

Text Recognition: Detect and extract handwritten content using OCR

Content Enhancement:

Correct OCR errors

Improve formatting

Preserve bullet points and structure

Convert equations to LaTeX format

Document Generation: Create structured PDF output
# Installation
1.Clone the repository:git clone https://github.com/Ananya2312/smartslideconverter

2.Set up backend:  cd backend
                   
                   pip install -r requirements.txt

3.Set up frontend:   cd ../frontend
                     
                     npm install
# Future Enhancements
AI-driven auto-correction for handwriting clarity

Real-time processing capabilities

Voice-to-text integration

Cloud storage collaboration (Google Drive, OneDrive)

Multi-language and multi-subject support
# Contributors
1.Uday N

2.Sanjana S N

3.Ananya A S

4.Archana A L

5.Pavitra Biradar
