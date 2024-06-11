from flask import request, jsonify
from app import app, bcrypt
from flask_jwt_extended import create_access_token
from translate import translate_text

@app.route('/translate', methods=['POST'])
def translate_text_endpoint():
    print("Translate endpoint hit")
    data = request.get_json()
    print("Received data:", data)
    text = data.get('text')
    target_language = data.get('target_language', 'es')

    if not text:
        return jsonify({'message': 'Text input is required'}), 400

    translated_text = translate_text(text, target_language)
    print("Translated text:", translated_text)

    return jsonify({'message': 'Translation successful', 'translated_text': translated_text}), 200

@app.route('/register', methods=['POST'])
def register():
    print("Register endpoint hit")
    data = request.get_json()
    print("Received data:", data)
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    print("Hashed password:", hashed_password)
    # Normally, you would save the user to the database here
    return jsonify({'message': 'User registered successfully', 'username': username}), 201

@app.route('/login', methods=['POST'])
def login():
    print("Login endpoint hit")
    data = request.get_json()
    print("Received data:", data)
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Normally, you would fetch the user from the database here
    # For now, assume any username/password is correct
    token = create_access_token(identity=username)
    print("Generated token:", token)
    return jsonify({'token': token}), 200