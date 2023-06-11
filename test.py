# Import Library
from moviepy.editor import *

# Wadah Video
clip = VideoFileClip("before.mp4").subclip(0, 10)

# Teks Watermark
text_clip = TextClip("Elzains Studio", fontsize=100, color="white")

# Posisi Teks
text_clip = text_clip.set_position("center").set_duration(10)

# Join Assets
video = CompositeVideoClip([clip, text_clip])

# Simpan
video.write_videofile("geprek.mp4")
