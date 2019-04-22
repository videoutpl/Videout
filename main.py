import os

from animations.ClipClasses import videoClip, finalVideo, photoClip



# This file is only used to test methods!!!!
def main():
    aspectRatios=["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]

    clip = os.getenv('USERPROFILE') + '\\Videos\\BuschMorning.mp4'

    vclip = videoClip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
    vclip2 = videoClip(clip=clip, start_time=(0, 29), end_time=(0, 32), fps=23.98)

    clip = os.getenv('USERPROFILE') + '\\Pictures\\VR.jpg'
    pclip =photoClip(image=clip, duration=10)

    vclip2.resize(2)
    pclip.resize(.3)

    final = finalVideo()
    final.concatenate_clip(vclip)
    final.concatenate_clip(vclip2)
    final.concatenate_clip(pclip)

    final.crop(aspectRatio=aspectRatios[4])
    final.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
                   font='Amiri-Bold', interline=-10, pos=(20, 190), duration=final.duration)

    final.writeVideo(filename=(aspectRatios[4] + 'Test.mp4'))
    final.create_gif(filename="testgif.gif")



if __name__ == '__main__':
    main()
