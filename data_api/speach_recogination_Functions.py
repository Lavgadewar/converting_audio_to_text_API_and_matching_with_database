import speech_recognition as sr

def recognizing(audio_file_name):
      
    # print(f"audio_file_name: {audio_file_name}\n")
    # audio_file = str("G:\\speech recogination\\voice230103191025.wav")
    
    audio_file= str(audio_file_name)

    # print(f"audio_file: {audio_file}\n")
    # create a speech recognition Recognizer instance 
    recognizer = sr.Recognizer()

    # open the audio file and record audio
    with sr.AudioFile(audio_file ) as source:

      # adjust the recognizer for ambient noise
      recognizer.adjust_for_ambient_noise(source)

      #record audio from the source
      audio = recognizer.record(source)

      # print("recognizing...")
      # convert  the audio using Google Speech Recognition to text
      audio_text = recognizer.recognize_google(audio, language= 'en-in')

      # print(f"user said: {output_text}\n")
    # return the audio text
    return audio_text















