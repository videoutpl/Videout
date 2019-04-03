import os

from animations.gif import Gif
from animations.videoClip import videoClip


# This file is only used to test methods!!!!
def main():
    aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]
    for ratio in aspectRatios:

        clip = os.getenv('USERPROFILE') + '\\Videos\\llama_transformation.mp4'
        vclip = videoClip()
        vclip.make_clip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
       # vclip.resize(new_size=0.6)
       #  vclip.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
       #               font='Amiri-Bold', interline=-10, pos=(20, 190), duration=vclip.clip.duration)
        vclip.crop(aspectRatio=ratio)
        vclip.writeClip(output=(ratio + 'Test.mp4'))



if __name__ == '__main__':
    main()
