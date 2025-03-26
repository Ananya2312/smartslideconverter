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
# Technology Stack
Frontend
React.js

Backend
FastAPI

Database
MongoDB

AI/ML Components

OpenCV (frame extraction and preprocessing)

EasyOCR (primary OCR engine)

Microsoft TrOCR (handwritten text recognition)

Facebook BART (text categorization and enhancement)
# Deployment
Web API via FastAPI

React-based frontend

Google Colab integration for testing
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
