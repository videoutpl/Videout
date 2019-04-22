import os

from animations.gif import Gif
from animations.videoClip import videoClip

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# This file is only used to test methods!!!!
def main():
    aspectRatios = ["vertical", "square", "letterbox", "widescreen", "cinemascope", "anamorphic", "DCI", "Digital IMAX"]
    for ratio in aspectRatios:
        clip = os.getenv('USERPROFILE') + '\\Videos\\llama_transformation.mp4'
        vclip = videoClip()
        vclip.make_clip(clip=clip, start_time=(0, 24), end_time=(0, 27), fps=23.98)
        # vclip.resize(new_size=0.6)
        #  vclip.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
        #               font='Amiri-Bold', interline=-10, pos=(20, 190), duration=vclip.clip.duration)
        vclip.crop(aspect_ratio=ratio)
        vclip.writeClip(output=(ratio + 'Test.mp4'))


def test_gif():
    clip = f'{BASE_DIR}\\video\\CHOLO Voice Trolling on FORTNITE ft. Lil Moco!.mp4'
    gif = Gif()
    gif.make_gif(clip=clip, start_time=(0, 24), end_time=(0, 27))
    gif.resize(new_size=0.6)
    gif.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
                 font='Amiri-Bold', interline=-10, pos=(20, 190), duration=1)
    gif.crop(aspect_ratio='square')
    gif.add_text(text='Get out of my swamp!', font_size=40, color='blue',
                 font='Amiri-Bold', interline=-10, pos=(40, 190), duration=4)
    gif.create_gif(output=f'{BASE_DIR}\\gif\\test.gif')


test_gif()
