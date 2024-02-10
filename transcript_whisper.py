import whisper
import os
import pandas as pd



# Path to your audio file
audio_path = os.path.join("downloaded_audios", "Watch_ Viewpoint With Bhupendra Chaubey.mp3")
print(audio_path)
model = whisper.load_model("base")

# Transcribe the audio
result = model.transcribe(audio_path)

output_path = os.path.join("transcripts", "transcript.txt")

# Access the transcript and other information
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result['text'])
