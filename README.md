# 3D Interactive Textbook Engine

An open-source educational platform that transforms static STEM textbook chapters (PDFs) into interactive, browser-based **3D visualizations** with real-time physics/molecular simulations and concept checks.

🔗 **Live Demo:** [https://Hatem-Alyatim.github.io/3d-interactive-textbook/](https://Hatem-Alyatim.github.io/3d-interactive-textbook/)

---

## Key Features
- **Zero-Install WebGL/Three.js Renderer:** Runs smoothly at 60 FPS on desktop and mobile browsers without plugins.
- **Interactive STEM Modules:** Includes real-time 3D simulations for Chemistry (Bohr Atomic Model), Physics (Orbital Mechanics), and Biology (DNA Double Helix).
- **Dynamic Simulation Controls:** Real-time speed adjustment, model scaling, 360-degree camera orbit, and zoom.
- **Automated PDF Content Pipeline:** Python extraction engine (`PyMuPDF`) that parses textbook PDFs into structured JSON modules.
- **Built-in Concept Checks:** Instant interactive quizzes tied to each 3D visual module.

---

## Tech Stack
- **Frontend & 3D Graphics:** HTML5, CSS3, JavaScript (ES6 Modules), Three.js
- **Data Extraction Pipeline:** Python 3.12+, PyMuPDF (`fitz`), JSON
- **Deployment:** GitHub Pages

---

## Quick Start

### 1. Run the 3D Web Platform
Simply open `index.html` in any modern web browser, or serve it locally:
```bash
python -m http.server 8000