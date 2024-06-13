# transProject
 This project provides a simple backend API service for a sign language-translation tool. The API allows users to submit text input and receive a translation in a specified target language.

## Requirements

- Python 3.x
- Flask
- Flask-Bcrypt
- Flask-JWT-Extended
- google-cloud-translate

## Setup

1. **Install the required libraries**:
    ```bash
    pip3 install -r requirements.txt
    ```

2. **Set environment variables**:
    ```bash
    export GOOGLE_PROJECT_ID="translatebackend-426005"
    export GOOGLE_LOCATION="global"
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service_account_key.json"
    ```

3. **Run the Flask application**:
    ```bash
    python3 app.py
    ```

## API Endpoints

### Register a new user

**Endpoint**: `/register`

**Method**: `POST`

**Request Body**:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
## test

### export credential key
    export GOOGLE_APPLICATION_CREDENTIALS=...

### register 
    curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'

### log in 
    curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'   

### translate
    curl -X POST http://127.0.0.1:5000/translate -H "Content-Type: application/json" -d '{"text": "Hello", "target_language": "es"}'         