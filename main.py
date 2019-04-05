import os

from animations.gif import Gif


# This file is only used to test methods!!!!
def main():
    clip = os.getenv('USERPROFILE') + '\\Downloads\\CHOLO Voice Trolling on FORTNITE ft. Lil Moco!.mp4'
    gif = Gif()
    gif.make_gif(clip=clip, start_time=(0, 24), end_time=(0, 27))
    gif.resize(new_size=0.6)
    gif.add_text(text='In my nightmares\nI see rabbits.', font_size=30, color='white',
                 font='Amiri-Bold', interline=-10, pos=(20, 190), duration=gif.clip.duration)
    gif.create_gif(output='test9.gif')


if __name__ == '__main__':
    main()
