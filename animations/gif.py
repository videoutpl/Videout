# from moviepy.video.io.VideoFileClip import VideoFileClip
# import moviepy.editor as mp
from moviepy.editor import *


# IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe'


class Gif:

    def __init__(self):
        self.clip = None

    def make_gif(self, clip, start_time, end_time):
        """
        Slices a video file between two time frames to create a gif
        :param clip: Name of video file
        :param start_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param end_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        """
        self.clip = VideoFileClip(clip).subclip(start_time, end_time)

    def resize(self, new_size):
        """
        Uses moviepy.video.fx.all.resize module
        :param new_size: Can be wither(width,height) in pixels or a float
                         A scaling factor, like 0.5
                         A function of time returning one of these.
        """
        self.clip = self.clip.resize(new_size)

    def crop(self, x1=None, y1=None, x2=None, y2=None,
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
        self.clip = self.clip.crop(x1=x1, y1=y1, x2=x2, y2=y2,
                                   width=width, height=height,
                                   x_center=x_center, y_center=y_center)

    def create_gif(self, output):
        # TODO: gif that loops fluidly
        # self.clip = self.clip.fx(concatenate([self.clip, self.clip.fx(vfx.time_mirror)]))
        # self.clip = self.clip.crossfadein(self.clip.duration / 2)
        self.clip = (CompositeVideoClip([self.clip,
                                         self.clip.set_start(self.clip.duration / 2),
                                         self.clip.set_start(self.clip.duration)])
                     .subclip(self.clip.duration / 2, 3 * self.clip.duration / 2))

        self.clip.write_videofile(output)

    def add_text(self, text, font_size, color, font, interline, pos, duration):
        text = TextClip(text, fontsize=font_size, color=color,
                        font=font, interline=interline).set_pos(pos).set_duration(duration)
        self.clip = CompositeVideoClip([self.clip, text])
