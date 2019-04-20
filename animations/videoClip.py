from moviepy.editor import VideoFileClip
from animations.BaseClip import BaseClip

class videoClip(BaseClip):

    def __init__(self, clip, start_time, end_time, fps= 29.97):
        BaseClip.__init__(self, VideoFileClip(clip).subclip(start_time, end_time).set_fps(fps))
