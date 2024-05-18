from flask import Flask, request
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    download_type = request.args.get('type')
    output_path = "C:/Users/Mesh/Downloads/FromYoutube"
    yt = YouTube(url)

    try:
        if download_type == "video":
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path)
        elif download_type == "audio":
            stream = yt.streams.filter(only_audio=True).first()
            audio_path = stream.download(output_path)
            base, ext = os.path.splitext(audio_path)
            mp3_path = base + '.mp3'

            logging.debug(f"audio_path: {audio_path}")
            logging.debug(f"mp3_path: {mp3_path}")

            try:
                audio_clip = AudioFileClip(audio_path)
                audio_clip.write_audiofile(mp3_path)
                audio_clip.close()

                os.remove(audio_path)
            except Exception as e:
                logging.error(f"Error converting audio: {str(e)}")
                return f"Error converting audio: {str(e)}", 500
        else:
            return "Invalid type", 400

        return "Download started"
    except Exception as e:
        logging.error(f"Error processing download: {str(e)}")
        return f"Error processing download: {str(e)}", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
