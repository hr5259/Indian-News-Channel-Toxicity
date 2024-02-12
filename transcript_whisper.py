import whisper
import os

def transcript_generator(audio_path,file_name):
    model = whisper.load_model("base")
    # Transcribe the audio
    result = model.transcribe(audio_path)
    file_name_without_extension = os.path.splitext(file_name)[0] + '.txt'
    output_path = os.path.join("transcripts", file_name_without_extension)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result['text'])

def main():
    folder_path = 'downloaded_audios'
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        print("Generating transcript for: ",file_name)
        # Path to your audio file
        audio_path = os.path.join("downloaded_audios", file_name)
        transcript_generator(audio_path, file_name)

if __name__ == '__main__':
    main()