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
