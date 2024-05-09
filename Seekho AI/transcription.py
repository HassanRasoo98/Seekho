from moviepy.editor import VideoFileClip
import whisper

def whisper_transcribe(video_path):
    # video_path = f'/content/{yt.title}.mp4'.replace('#', '').replace(':', '')
    # Load the Whisper model
    model = whisper.load_model('small')
    print("Whisper model loaded successfully")

    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile('/content/audio.wav')

    # Transcribe the audio using Whisper
    result = whisper.transcribe(model, '/content/audio.wav')

    print(result['text'])
    # fhandle = open('transcribed_audio.txt', 'w')
    # fhandle.write(result['text'])
    # fhandle.close()

    return result['text']