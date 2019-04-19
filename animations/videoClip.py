# from moviepy.video.io.VideoFileClip import VideoFileClip
# import moviepy.editor as mp
from moviepy.editor import *


# IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe'


class videoClip:

    def __init__(self):
        self.clip = None
        self.duration = 0

    def make_clip(self, clip, start_time, end_time, fps= 29.97):
        """
        Slices a video file between two time frames to create a gif
        :param clip: Name of video file
        :param start_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param end_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        """
        self.clip = VideoFileClip(clip).subclip(start_time, end_time).set_fps(fps)
        self.duration = self.clip.duration


    def resize(self, new_size):
        """
        Uses moviepy.video.fx.all.resize module
        :param new_size: Can be wither(width,height) in pixels or a float
                         A scaling factor, like 0.5
                         A function of time returning one of these.
        """
        self.clip = self.clip.resize(new_size)

    def crop(self, aspectRatio = None, x1=None, y1=None, x2=None, y2=None,
             width=None, height=None, x_center= None, y_center= None):
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

        # If a preselected aspect ratio was selected.
        if aspectRatio:
            if not x_center:
                x_center = self.clip.w/2
            if not y_center:
                y_center = self.clip.h/2

            # Vertical/Phone ratio
            if aspectRatio == "vertical" or aspectRatio == "9:16" or aspectRatio == "phone":
                self.clip = self.clip.crop(width=self.clip.h*9/16, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # Square ratio
            elif aspectRatio == "square" or aspectRatio == "1:1":
                self.clip = self.clip.crop(width=self.clip.h, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # 4:3/Letterbox ratio
            elif aspectRatio == "4:3" or aspectRatio == "1.33:1" or aspectRatio == "letterbox":
                self.clip = self.clip.crop(width=self.clip.h*1.33, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # 16:9/Widescreen ratio
            elif aspectRatio == "16:9" or aspectRatio == "widescreen" or aspectRatio == "1.77:1":
                    self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w/1.77,
                                               x_center=x_center, y_center=y_center)

            # 21:9/Cinemascope ratio
            elif aspectRatio == "cinemascope" or aspectRatio == "21:9" or aspectRatio == "2.33:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w/2.33,
                                           x_center=x_center, y_center=y_center)

            # 2.35:1/Anamorphic ratio
            elif aspectRatio == "anamorphic" or aspectRatio == "2.35:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w/2.35,
                                           x_center=x_center, y_center=y_center)

            # 2.39:1/DCI ratio
            elif aspectRatio == "DCI" or aspectRatio == "2.39:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w/2.39,
                                           x_center=x_center, y_center=y_center)

            # 2.9:1/Digital IMAX ratio
            elif aspectRatio == "Digital IMAX" or aspectRatio == "2.9:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w/2.9,
                                           x_center=x_center, y_center=y_center)

            # If an invalid aspect ratio was specified, raise an exception.
            else:
                raise AttributeError("Invalid Aspect Ratio specified: '" + str(aspectRatio) + "'")

        # If no preset ratio was selected, use other crop parameters.
        else:
            self.clip = self.clip.crop(x1=x1, y1=y1, x2=x2, y2=y2,
                                       width=width, height=height,
                                       x_center=x_center, y_center=y_center)

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


    # We shouldn't add text here.
    # def add_text(self, text, font_size, color, font, interline, pos, duration):
    #     text = TextClip(text, fontsize=font_size, color=color,
    #                     font=font, interline=interline).set_pos(pos).set_duration(duration)
    #     self.clip = CompositeVideoClip([self.clip, text])
