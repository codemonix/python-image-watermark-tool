# 🖼️ Python Image Watermark Tool

A desktop application for batch image watermarking with an interactive GUI, built using Python and Tkinter.

> ⚠️ This project was developed during my early Python learning phase. It demonstrates my ability to build non-trivial applications involving GUI design, image processing, and file handling.
> I am currently focused on modern full-stack development using React, Node.js, and cloud technologies.


## 🚀 Features

* 📝 Add custom text watermarks to images
* 🖱️ Drag & drop positioning of watermark on image preview
* 🎨 Customize:

  * Font family
  * Font size
  * Text color
  * Background color
  * Transparency
* 📂 Batch processing of entire folders
* 🖼️ Live preview before applying watermark
* 💾 Save and load configuration settings
* ⏳ Progress bar with cancel support for long operations


## 🧱 Tech Stack

* **Language:** Python
* **GUI:** Tkinter
* **Image Processing:** Pillow (PIL)
* **Utilities:** Matplotlib (font discovery), threading


## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/python-image-watermark-tool.git
cd python-image-watermark-tool

### 2. Create virtual environment


python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

### 3. Install dependencies


pip install -r requirements.txt


## ▶️ Run the application

python app.py

## 🐳 Docker (optional)

A Dockerfile is included for running the application in a containerized environment.

docker build -t watermark-app .
docker run -it --rm watermark-app

> ⚠️ Running GUI apps with Docker requires additional configuration (X11 forwarding).


## 📂 Project Structure

.
├── core/              # Image processing logic
├── gui/               # UI components and windows
├── file_handling/     # File operations and persistence
├── utils/             # Helper utilities (fonts, colors, settings)
├── resources/         # Sample images and assets
├── app.py             # Main entry point
└── requirements.txt


## 🧠 What I Learned

* Building desktop applications with Tkinter
* Image processing using Pillow
* Managing application state across multiple UI components
* Handling file systems and batch operations
* Designing user-interactive tools (drag & drop, previews, progress feedback)


## 🔧 Possible Improvements

If I were to rebuild this project today, I would:

* Remove global state (singleton pattern) and introduce cleaner state management
* Separate UI from business logic (service layer)
* Add proper automated tests (e.g. pytest)
* Introduce a CLI interface for headless usage
* Improve error handling and logging using Python's `logging` module
* Refactor UI for better maintainability

## 📌 Status

This project is no longer actively developed, but remains as a reference for my early work in Python and desktop application development.

## 👤 Author

Saeid Monfared

* GitHub: https://github.com/YOUR_USERNAME
* (Optional) LinkedIn: add your link here


## ⭐️ Notes

If you find this project useful or interesting, feel free to give it a star.
