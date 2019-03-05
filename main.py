import os

from animations.gif import Gif


def main():
    clip = os.getenv('USERPROFILE') + '\\Downloads\\CHOLO Voice Trolling on FORTNITE ft. Lil Moco!.mp4'
    gif = Gif()
    gif.make_gif(clip=clip, start_time=(0, 24), end_time=(0, 27))
    gif.resize(new_size=0.6)
    # gif.clip = gif.clip.crop(x1=60, x2=300)
    gif.clip.write_gif('test1.gif')


if __name__ == '__main__':
    main()
