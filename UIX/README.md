# Quantum Garnet Casino Web Application

This project is a web-based application for Quantum Garnet Casino. It provides users with tier-based benefits, interactive navigation, and account management features. The application is built using Python and Flask.

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.8.10**
   - This project is developed and tested with Python 3.8.10. Ensure this version is installed to avoid compatibility issues.
   - [Download Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

2. **pip 21.1.1**
   - Ensure you have pip installed to manage Python packages. If pip is not already installed, it comes bundled with Python. Verify the version using:
     ```bash
     pip --version
     ```
   - If pip is outdated, update it using:
     ```bash
     python -m pip install --upgrade pip
     ```

3. **Flask 3.0.3**
   - Flask is the core framework used to build this application. The specified version is required to ensure compatibility.

4. **Werkzeug 3.0.6**
   - Werkzeug is a WSGI utility library used by Flask for handling HTTP requests.

## Installation Instructions

Follow these steps to set up and run the application:

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
```
### 2. Change into the project directory:

```bash
cd <project-directory>
```
### 3. Install the required dependencies using pip.
```bash
pip install Flask==3.0.3 Werkzeug==3.0.6
```

### 4.Start the Flask development server:
```bash
python app.py
```
The server will start on http://127.0.0.1:5000 by default.

Open a web browser and navigate to http://127.0.0.1:5000 to access the application.
