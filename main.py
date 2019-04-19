import os

from animations.gif import Gif
from animations.videoClip import videoClip
from animations.finalVideo import finalVideo


# This file is only used to test methods!!!!
def main():
    aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]

    clip = os.getenv('USERPROFILE') + '\\Videos\\BuschMorning.mp4'
    cliplist = []
    vclip = videoClip()
    vclip.make_clip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
    vclip2 = videoClip()
    vclip2.make_clip(clip=clip, start_time=(0, 29), end_time=(0, 32), fps=23.98)

    vclip2.resize(2)
    final = finalVideo()
    final.concatenate_clip(vclip)
    final.concatenate_clip(vclip2)
    final.build_clip()


    final.crop(aspectRatio=aspectRatios[2])
    final.writeClip(output=(aspectRatios[2] + 'Test.mp4'))



if __name__ == '__main__':
    main()
