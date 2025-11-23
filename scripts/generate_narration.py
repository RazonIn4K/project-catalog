import os
import requests
import json
import sys
from dotenv import load_dotenv

# Load env vars
load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not API_KEY:
    print("Error: ELEVENLABS_API_KEY not found in .env")
    sys.exit(1)

# Configuration
VOICE_ID = "1SM7GgM6IMuvQlz2BwM3"  # Mark - ConvoAI
MODEL_ID = "eleven_v3"
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"


def generate_audio(text, output_filename):
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}

    # Specific settings for Mark - ConvoAI v3
    data = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,  # Natural (0.0 = Creative, 0.5 = Natural, 1.0 = Robust)
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }

    print(f"Generating audio for: '{text[:30]}...'")
    response = requests.post(URL, json=data, headers=headers)

    if response.status_code == 200:
        with open(output_filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved to {output_filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_narration.py <text_or_file> <output_filename>")
        sys.exit(1)

    input_data = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input is a file
    if os.path.isfile(input_data):
        with open(input_data, "r") as f:
            text_to_speak = f.read()
    else:
        text_to_speak = input_data

    generate_audio(text_to_speak, output_file)
