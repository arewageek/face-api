# Face API Service

A simple and robust FastAPI service for face verification and detection using the [DeepFace](https://github.com/serengil/deepface) library.

## Features

- **Face Verification**: Compare two images to determine if they belong to the same person.
- **Face Detection**: Extract and locate faces within an image with confidence scores.
- **Base64 Support**: Easily handle images transmitted as base64-encoded strings.

## Getting Started

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd face-api
    ```

2.  **Set up a virtual environment**:
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    uv pip install -r requirements.txt
    ```

### Running the API

Start the server using `uvicorn`:

```bash
uvicorn main:api --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### 1. Face Verification

Compares a reference image against a photo.

-   **Endpoint**: `POST /verify`
-   **Request Body**:
    ```json
    {
        "reference": "data:image/jpeg;base64,...",
        "photo": "data:image/jpeg;base64,..."
    }
    ```
-   **Success Response**: returns the verification result from DeepFace.

### 2. Face Detection

Extracts faces and provides bounding box coordinates.

-   **Endpoint**: `POST /detect`
-   **Request Body**:
    ```json
    {
        "photo": "data:image/jpeg;base64,..."
    }
    ```
-   **Success Response**:
    ```json
    {
        "status": "success",
        "status_code": 200,
        "data": {
            "facial_area": { "x": 100, "y": 100, "w": 50, "h": 50 },
            "confidence": 0.99
        }
    }
    ```

## Tech Stack

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python.
- **DeepFace**: A lightweight face recognition and facial attribute analysis framework.
- **Uvicorn**: An ASGI web server implementation for Python.
