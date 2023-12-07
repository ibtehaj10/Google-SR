import speech_recognition as sr

# Initialize recognizer


# Load your audio file
def STT(filename):
    audio_file_path = 'audios/'+filename  # replace with your file path
    recognizer = sr.Recognizer()
    # Use the audio file as the source
    with sr.AudioFile(audio_file_path) as source:
        # Record the audio file
        audio_data = recognizer.record(source)

        # Recognize the content
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            return text  # Urdu - Pakistan
            print("Recognized text:", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")



STT('your path to wav file')