from moviepy.editor import *
from animations.BaseClip import BaseClip


class finalVideo(BaseClip):

    def __init__(self):
        self.clip = None
        self.duration = 0

    def _start_clip(self, clip):
        """
        Slices a video file between two time frames to create a gif
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
        :param clip: Moviepy clip object
        :return: None
        """
        self.clip = CompositeVideoClip(clips=[self.clip, clip])

    def concatenate_clip(self, clip):
        """
        Adds a clip to the self.cliplist to be used with the build_clip method.
        :param clip: Moviepy clip object
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
