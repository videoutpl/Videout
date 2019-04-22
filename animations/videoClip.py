# from moviepy.video.io.VideoFileClip import VideoFileClip
# import moviepy.editor as mp
from moviepy.editor import *

# IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe'
from animations.base_clip import BaseClip


class videoClip(BaseClip):

    def make_clip(self, clip, start_time, end_time, fps=29.97):
        """
        Slices a video file between two time frames to create a gif
        :param clip: Name of video file
        :param start_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param end_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        """
        self.clip = VideoFileClip(clip).subclip(start_time, end_time).set_fps(fps)

    def writeClip(self, output):
        # self.clip = self.clip.fx(concatenate([self.clip, self.clip.fx(vfx.time_mirror)]))
        # self.clip = self.clip.crossfadein(self.clip.duration / 2)
        # self.clip = (CompositeVideoClip([self.clip,
        #                                  self.clip.set_start(self.clip.duration / 2),
        #                                  self.clip.set_start(self.clip.duration)])
        #              .subclip(self.clip.duration / 2, 3 * self.clip.duration / 2))

        self.clip.write_videofile(output)
        self.clip.reader.close()
        self.clip.audio.reader.close_proc()
