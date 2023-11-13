import ffmpeg
import os


def video_to_gif():
    for file in os.listdir("video"):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split(".")[0]
            gif_file = file_name + ".gif"
            
            stream = ffmpeg.input(f"video/{file}")
            stream = ffmpeg.filter(stream, "fps", fps=2)
            stream = ffmpeg.output(stream, f"gif/{gif_file}")
            ffmpeg.run(stream)
            
video_to_gif()
