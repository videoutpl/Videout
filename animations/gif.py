from moviepy.video.io.VideoFileClip import VideoFileClip


class Gif:

    def __init__(self):
        self.clip = None

    def create_gif(self, clip, start_time, end_time, resize=None):
        """
        Slices a video file between two time frames to create a gif
        :param clip: Name of video file
        :param start_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param end_time: Tuple stating time in (hour, min, sec), (min, sec) or (sec)
        :param resize: Resize's video
        """
        self.clip = VideoFileClip(clip).subclip(start_time, end_time).resize(resize)
