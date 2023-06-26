# Import Library Moviepy
from moviepy.editor import *

# Wadah Citra Video
clip = VideoFileClip("before.mp4").subclip(0, 10)

# Teks Watermark
text_clip = TextClip("Elzains Startup", fontsize=100, color="white")

# Posisi Watermark
text_clip = text_clip.set_position("center").set_duration(10)

# Join Video + Video
video = CompositeVideoClip([clip, text_clip])

# Simpan
video.write_videofile("geprek.mp4")






# ffmpeg -i geprek.mp4 -vf "delogo=x=100:y=100:w=900:h=50:show=0" -c:a copy output_video.mp4

