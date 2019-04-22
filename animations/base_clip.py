from moviepy.editor import CompositeVideoClip, TextClip


class BaseClip:

    def __init__(self, clip):
        self.clip = CompositeVideoClip(clips=[clip])
        self.duration = self.clip.duration

    def add_text(self, text, font_size, color, font, interline, pos, duration):
        """
        Adds a layer of text over the selected clip.
        :param text: text to add
        :param font_size: size of text
        :param color: color of text
        :param font: font of text
        :param interline: line spacing of text
        :param pos: position of text
        :param duration: duration text is going to be visible
        """
        text = TextClip(text, fontsize=font_size, color=color,
                        font=font, interline=interline).set_pos(pos).set_duration(duration)
        self.clip = CompositeVideoClip([self.clip, text])

    def resize(self, new_size):
        """
        Uses moviepy.video.fx.all.resize module
        :param new_size: Can be wither(width,height) in pixels or a float
                         A scaling factor, like 0.5
                         A function of time returning one of these.
        """
        self.clip = self.clip.resize(new_size)

    def crop(self, aspect_ratio=None, x1=None, y1=None, x2=None, y2=None,
             width=None, height=None, x_center=None, y_center=None):
        """
        Uses moviepy.video.fx.crop module. From documentation:
        Returns a new clip in which just a rectangular subregion of the
        original clip is conserved. x1,y1 indicates the top left corner and
        x2,y2 is the lower right corner of the croped region.
        All coordinates are in pixels. Float numbers are accepted.
        :param aspect_ratio: predetermined size
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
        if aspect_ratio:
            if not x_center:
                x_center = self.clip.w / 2
            if not y_center:
                y_center = self.clip.h / 2

            # Vertical/Phone ratio
            if aspect_ratio == "vertical" or aspect_ratio == "9:16" or aspect_ratio == "phone":
                self.clip = self.clip.crop(width=self.clip.h * 9 / 16, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # Square ratio
            elif aspect_ratio == "square" or aspect_ratio == "1:1":
                self.clip = self.clip.crop(width=self.clip.h, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # 4:3/Letterbox ratio
            elif aspect_ratio == "4:3" or aspect_ratio == "1.33:1" or aspect_ratio == "letterbox":
                self.clip = self.clip.crop(width=self.clip.h * 1.33, height=self.clip.h,
                                           x_center=x_center, y_center=y_center)

            # 16:9/Widescreen ratio
            elif aspect_ratio == "16:9" or aspect_ratio == "widescreen" or aspect_ratio == "1.77:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w / 1.77,
                                           x_center=x_center, y_center=y_center)

            # 21:9/Cinemascope ratio
            elif aspect_ratio == "cinemascope" or aspect_ratio == "21:9" or aspect_ratio == "2.33:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w / 2.33,
                                           x_center=x_center, y_center=y_center)

            # 2.35:1/Anamorphic ratio
            elif aspect_ratio == "anamorphic" or aspect_ratio == "2.35:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w / 2.35,
                                           x_center=x_center, y_center=y_center)

            # 2.39:1/DCI ratio
            elif aspect_ratio == "DCI" or aspect_ratio == "2.39:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w / 2.39,
                                           x_center=x_center, y_center=y_center)

            # 2.9:1/Digital IMAX ratio
            elif aspect_ratio == "Digital IMAX" or aspect_ratio == "2.9:1":
                self.clip = self.clip.crop(width=self.clip.w, height=self.clip.w / 2.9,
                                           x_center=x_center, y_center=y_center)

            # If an invalid aspect ratio was specified, raise an exception.
            else:
                raise AttributeError("Invalid Aspect Ratio specified: '" + str(aspect_ratio) + "'")

        # If no preset ratio was selected, use other crop parameters.
        else:
            self.clip = self.clip.crop(x1=x1, y1=y1, x2=x2, y2=y2,
                                       width=width, height=height,
                                       x_center=x_center, y_center=y_center)
