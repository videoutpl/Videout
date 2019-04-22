from moviepy.editor import *
from animations.BaseClip import BaseClip


class videoClip(BaseClip):

    def __init__(self, clip, start_time, end_time, fps= 29.97):
        BaseClip.__init__(self, VideoFileClip(clip).subclip(start_time, end_time).set_fps(fps))


class photoClip(BaseClip):
    def __init__(self, image, duration=5):
        BaseClip.__init__(self, ImageClip(img=image, duration=duration))


class finalVideo(BaseClip):

    def __init__(self):
        self.clip = None
        self.duration = 0

    def _start_clip(self, clip):
        """
        Initialize the self.clip to a compositeVideoClip of only one clip.
        :param clip: Name of video file
        """
        self.clip = CompositeVideoClip(clips=clip)

    def _add_clip(self, clip):
        """
        Replace self.clip with a new CompositeVideoClip that starts with itself and the new clip.

        Replaces self.clip with a new CompositeVideoClip with a new instance
            of the same object, containing a list of clips that starts with
            itself, and followed by the newly inserted clip object. The
            clip object will start wherever it is designated to start independently,
            so it will not necessarily play at the end of the existing video.
        :param clip: BaseClip object
        :return: None
        """
        self.clip = CompositeVideoClip(clips=[self.clip, clip])

    def concatenate_clip(self, clip):
        """
        Adds a clip to the end of the current self.clip.
        :param clip: BaseClip object
        :return: None
        """
        if self.duration is 0:
            self._start_clip([clip.clip])
        else:
            self._add_clip(clip.clip.set_start(self.duration))

        self.duration += clip.duration

    def writeVideo(self, filename):
        """
        Write the video to a file.
        :param filename: name and format of output file.
        :return:
        """
        self.clip.write_videofile(filename)


    def create_gif(self, filename):
        # TODO: gif that loops fluidly
        # self.clip = self.clip.fx(concatenate([self.clip, self.clip.fx(vfx.time_mirror)]))
        # self.clip = self.clip.crossfadein(self.clip.duration / 2)
        # self.clip = (CompositeVideoClip([self.clip,
        #                                  self.clip.set_start(self.clip.duration / 2),
        #                                  self.clip.set_start(self.clip.duration)])
        #              .subclip(self.clip.duration / 2, 3 * self.clip.duration / 2))

        self.clip.write_gif(filename)
