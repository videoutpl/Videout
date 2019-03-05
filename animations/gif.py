# from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as mp


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
        self.clip = mp.VideoFileClip(clip).subclip(start_time, end_time)

    def resize(self, new_size):
        """
        Uses moviepy.video.fx.all.resize module
        :param new_size: Can be wither(width,height) in pixels or a float
                         A scaling factor, like 0.5
                         A function of time returning one of these.
        """
        self.clip = self.clip.resize(new_size)
