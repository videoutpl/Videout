import os

from animations.gif import Gif
from animations.videoClip import videoClip


# This file is only used to test methods!!!!
def main():
    # aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]
    # for ratio in aspectRatios:

    clip = os.getenv('USERPROFILE') + '\\Videos\\llama_transformation.mp4'
    vclip = videoClip()
    clipForAudio = os.getenv('USERPROFILE') + '\\Videos\\LoveIsWar.mp4'
    audio = os.getenv('USERPROFILE') + '\\Music\\InTheEnd.mp3'
    vclip.make_clip(clip=clip, start_time=(0, 1), end_time=(0, 60), fps=23.98)
    # vclip.resize(new_size=0.6)
    #  vclip.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
    #               font='Amiri-Bold', interline=-10, pos=(20, 190), duration=vclip.clip.duration)
    #  vclip.crop(aspectRatio=ratio)
    vclip.addAudioFromClip(clipToExtract=clipForAudio, start_time=(5), end_time=(65.1))
    vclip.writeClip(output='LlamasWithLW.mp4')

    clip2 = os.getenv('USERPROFILE') + '\\Videos\\TakeOnMe_Weezer.mp4'
    vclip = videoClip()
    vclip.make_clip(clip=clip2, start_time=(0, 74), end_time=(0, 260), fps=23.98)
    # vclip.resize(new_size=0.6)
    #  vclip.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
    #               font='Amiri-Bold', interline=-10, pos=(20, 190), duration=vclip.clip.duration)
    #  vclip.crop(aspectRatio=ratio)
    #  vclip.addAudioFromFile(audio)
    vclip.addAudioFromFile(audio=audio, start_time=(0), end_time=(186.1))
    vclip.writeClip(output='TakeOnMeLP.mp4')


if __name__ == '__main__':
    main()
