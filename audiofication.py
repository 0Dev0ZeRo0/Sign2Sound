from gtts import gTTS
from playsound import playsound
import os
import tempfile
import platform

OUTPUT_PATH = 'output'
os.makedirs(OUTPUT_PATH, exist_ok=True)

def generate_audio(text):

    if not text:
        print("Warning: No text provided for audio generation.")
        return False
    
    try:
        # Use temporary file to avoid permission issues
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            audio_path = temp_file.name
        
        # Generate audio with gTTS
        tts = gTTS(text=text, lang='en')
        tts.save(audio_path)
        print(f"Audio file saved to {audio_path}")
        
        if platform.system() == "Windows":
        # Play audio
            # On Windows, use playsound with absolute path
            playsound(audio_path)
        else:
            # On other systems, use system default player
            os.system(f"mpg123 {audio_path}" if os.name != "nt" else f"start {audio_path}")
        
        print(f"Audio played successfully for: {text}")
        # Clean up
        os.remove(audio_path)
        return True
    
    except PermissionError as e:
        print(f"Permission error: Could not save or play audio. {str(e)}")
        print("Try running as administrator or check output directory permissions.")
        return False
    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        return False

if __name__ == "__main__":
    # Test audiofication
    test_text = "I love you"
    success = generate_audio(test_text)
    if success:
        print("Test audio played successfully.")
    else:
        print("Test audio failed.")