import os

from animations.gif import Gif
from animations.videoClip import videoClip
from animations.finalVideo import finalVideo


# This file is only used to test methods!!!!
def main():
    aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]

    clip = os.getenv('USERPROFILE') + '\\Videos\\BuschMorning.mp4'

    vclip = videoClip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
    vclip2 = videoClip(clip=clip, start_time=(0, 29), end_time=(0, 32), fps=23.98)

    vclip2.resize(2)

    final = finalVideo()
    final.concatenate_clip(vclip)
    final.concatenate_clip(vclip2)

    final.crop(aspectRatio=aspectRatios[2])
    final.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
                   font='Amiri-Bold', interline=-10, pos=(20, 190), duration=final.duration)

    final.writeVideo(filename=(aspectRatios[2] + 'Test.mp4'))



if __name__ == '__main__':
    main()
