import os

from animations.ClipClasses import videoClip


# This file is only used to test methods!!!!
def main():
    clip = os.getenv('USERPROFILE') + '\\Videos\\llama_transformation.mp4'
    clip2 = os.getenv('USERPROFILE') + '\\Videos\\TakeOnMe_Weezer.mp4'
    clipForAudio = os.getenv('USERPROFILE') + '\\Videos\\LoveIsWar.mp4'
    audio = os.getenv('USERPROFILE') + '\\Music\\InTheEnd.mp3'

   
    aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]

    # clip = os.getenv('USERPROFILE') + '\\Videos\\BuschMorning.mp4'

    vclip = videoClip(clip=clip, start_time=(0, 1), end_time=(0, 60), fps=23.98)
    vclip2 = videoClip(clip=clip2, start_time=(0, 74), end_time=(0, 130), fps=23.98)

    # clip = os.getenv('USERPROFILE') + '\\Pictures\\VR.jpg'
    # pclip =photoClip(image=clip, duration=10)

    # vclip2.resize(2)
    # pclip.resize(.3)

    vclip.addAudioFromClip(clipToExtract=clipForAudio, start_time=(5), end_time=(65.1))
    vclip2.addAudioFromFile(audio=audio, start_time=(0), end_time=(186.1))

    # final = finalVideo()
    # final.concatenate_clip(vclip)
    # final.concatenate_clip(vclip2)
    # final.concatenate_clip(pclip)

    vclip.crop(aspectRatio=aspectRatios[4])
    # final.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
    #                font='Amiri-Bold', interline=-10, pos=(20, 190), duration=final.duration)

    vclip.writeVideo(filename=(aspectRatios[4] + 'Test.mp4'))
    vclip.create_gif(filename="testgif.gif")

    

if __name__ == '__main__':
    main()
