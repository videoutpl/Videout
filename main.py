import os

from animations.clip_classes import VideoClip, FinalVideo, PhotoClip


# This file is only used to test methods!!!!
def main():
    aspect_ratios = ["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI",
                     "Digital IMAX"]

    clip = os.getenv('USERPROFILE') + '\\Videos\\BuschMorning.mp4'

    vclip = VideoClip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
    vclip2 = VideoClip(clip=clip, start_time=(0, 29), end_time=(0, 32), fps=23.98)

    clip = os.getenv('USERPROFILE') + '\\Pictures\\VR.jpg'
    pclip = PhotoClip(image=clip, duration=10)

    vclip2.resize(2)
    pclip.resize(.3)

    final = FinalVideo()
    final.concatenate_clip(vclip)
    final.concatenate_clip(vclip2)
    final.concatenate_clip(pclip)

    final.crop(aspect_ratio=aspect_ratios[4])
    final.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
                   font='Amiri-Bold', interline=-10, pos=(20, 190), duration=final.duration)

    final.write_video(filename=(aspect_ratios[4] + 'Test.mp4'))


if __name__ == '__main__':
    main()
