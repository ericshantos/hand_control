[🇧🇷] Leia em português

# Hand Control

<div>
<img src="https://img.shields.io/badge/pre--commit-verified-blue?logo=pre-commit" alt="pre-commit enabled" />
<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="used python 3.12" />
<img src="https://img.shields.io/badge/Status-Active-success" alt="project completed" />
<img src="https://img.shields.io/badge/Dependencies-Managed-blue" alt="Dependencies managed" />
</div>

## Description

The **Hand Control** project is an application that allows controlling the system volume and screen brightness using hand gestures captured by a camera. It uses the **MediaPipe** library for hand tracking and calculates the distance between fingers to adjust system properties.

## Technologies Used

- **Python**: Main programming language of the project.
- **OpenCV**: Image capture and processing.
- **MediaPipe**: Hand detection and tracking.
- **Pycaw**: System volume control (Windows only).
- **screen_brightness_control**: Screen brightness adjustment.

## Features

- Real-time hand detection.
- Calculation of the distance between thumb and index finger.
- System volume adjustment when the left hand is detected.
- Screen brightness adjustment when the right hand is detected.
- Display of processed hands on the screen.

## Project Structure

```
Hand Control/
│-- src/
│   │-- controllers/
│   │   │-- brightness.py
│   │   │-- volume.py
│   │   │-- controller.py
│   │-- utils/
│   │   │-- distance_calculator.py
│   │-- hand_tracker/
│   │   │-- initialize_detector.py
│   │   │-- landmark_processor.py
│-- main.py
│-- pre-commit-config.yaml
│-- setup.py
│-- .gitignore
│-- requirements.txt
│-- README.md
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ericshantos/hand-control.git
   cd hand-control
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up pre-commit:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. To manually test pre-commit:
   ```bash
   pre-commit run --all-files
   ```

6. Run the main script:
   ```bash
   python main.py
   ```

## Author

Developed by **Eric dos Santos**.

- GitHub: [github.com/ericshantos](https://github.com/ericshantos)
- LinkedIn: [linkedin.com/in/eric-sh](https://linkedin.com/in/eric-sh)
- Email: ericshantos13@gmail.com

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
