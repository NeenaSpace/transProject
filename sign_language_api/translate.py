import os
from google.cloud import translate_v2 as translate

def translate_text(text, target_language='es'):
    # Load credentials from the environment variable
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    print("Using credentials from:", creds_path)

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path

    # Initialize the translation client
    try:
        translate_client = translate.Client()
        print("Google Translate client created successfully")
    except Exception as e:
        print(f"Error creating Google Translate client: {e}")
        raise

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Perform the translation
    try:
        result = translate_client.translate(text, target_language=target_language)
        print(f"Translation result: {result}")
        return result["translatedText"]
    except Exception as e:
        print(f"Error during translation: {e}")
        raise