# from moviepy.video.io.VideoFileClip import VideoFileClip
# import moviepy.editor as mp
from moviepy.editor import *


# IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe'


class videoClip:

    def __init__(self):
        self.clip = None

    def make_clip(self, clip, start_time, end_time, fps= 29.97):
        """
        Slices a video file between two time frames to create a gif
        :param clip: Name of video file
        :param start_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param end_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        """
        self.clip = VideoFileClip(clip).subclip(start_time, end_time).set_fps(fps)

    def resize(self, new_size):
        """
        Uses moviepy.video.fx.all.resize module
        :param new_size: Can be wither(width,height) in pixels or a float
                         A scaling factor, like 0.5
                         A function of time returning one of these.
        """
        self.clip = self.clip.resize(new_size)

    def crop(self, aspectRatio = None, x1=None, y1=None, x2=None, y2=None,
             width=None, height=None, x_center=None, y_center=None):
        """
        Uses moviepy.video.fx.crop module. From documentation:
        Returns a new clip in which just a rectangular subregion of the
        original clip is conserved. x1,y1 indicates the top left corner and
        x2,y2 is the lower right corner of the croped region.
        All coordinates are in pixels. Float numbers are accepted.
        :param x1: top left corner x-axis
        :param y1: top left corner y-axis
        :param x2: bottom right corner x-axis
        :param y2: bottom right corner y-axis
        :param width: width of rectangle
        :param height: height of rectangle
        :param x_center: x-axis center
        :param y_center: y-axis center
        """
        if aspectRatio:
            if aspectRatio == "4:3" or aspectRatio == "1.33.1":
                self.clip = self.clip.crop(width=self.clip.h*4/3, height=self.clip.h,
                                           x_center=self.clip.w/2, y_center=self.clip.h/2)
            elif aspectRatio == "16:9" or aspectRatio == "widescreen" or aspectRatio == "1.77.1":
                    self.clip = self.clip.crop(width=self.clip.h * 16 / 9, height=self.clip.h,
                                               x_center=self.clip.w / 2, y_center=self.clip.h / 2)
            elif aspectRatio == "square" or aspectRatio == "1:1":
                self.clip = self.clip.crop(width=self.clip.h, height=self.clip.h,
                                           x_center=self.clip.w / 2, y_center=self.clip.h / 2)
            elif aspectRatio == "cinemascope" or aspectRatio == "21:9" or aspectRatio == "2.33.1":
                self.clip = self.clip.crop(width=self.clip.h*21/9, height=self.clip.h,
                                           x_center=self.clip.w / 2, y_center=self.clip.h / 2)
            elif aspectRatio == "DCI" or aspectRatio == "2.39:1":
                self.clip = self.clip.crop(width=self.clip.h * 2.39, height=self.clip.h,
                                           x_center=self.clip.w / 2, y_center=self.clip.h / 2)
        else:
            self.clip = self.clip.crop(x1=x1, y1=y1, x2=x2, y2=y2,
                                       width=width, height=height,
                                       x_center=x_center, y_center=y_center)

    def writeClip(self, output):
        # TODO: gif that loops fluidly
        # self.clip = self.clip.fx(concatenate([self.clip, self.clip.fx(vfx.time_mirror)]))
        # self.clip = self.clip.crossfadein(self.clip.duration / 2)
        # self.clip = (CompositeVideoClip([self.clip,
        #                                  self.clip.set_start(self.clip.duration / 2),
        #                                  self.clip.set_start(self.clip.duration)])
        #              .subclip(self.clip.duration / 2, 3 * self.clip.duration / 2))

        self.clip.write_videofile(output)

    def add_text(self, text, font_size, color, font, interline, pos, duration):
        text = TextClip(text, fontsize=font_size, color=color,
                        font=font, interline=interline).set_pos(pos).set_duration(duration)
        self.clip = CompositeVideoClip([self.clip, text])
