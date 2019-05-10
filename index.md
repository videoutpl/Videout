# Welcome to Videout!
![Code Quality](https://img.shields.io/pypi/status/Django.svg)

Videout is a language designed to facilitate the creation of short videos by means of text, 
simple animations, and basic video editing for users who are not adept at utilizing 
video editing software, or beginner users who have yet to be exposed to advanced video editing 
software but are familiar with programming.

## Motivation
The basis of this language is to allow the user to generate simple, customizable videos using
programming concepts as an alternative to a film editing suite. Due to the complicated and
computationally demanding nature of video editing, this approach will attempt to generate videos 
by stripping away many elaborate features; such as video stabilization, rotoscoping tools, keying 
software, etc. Consequently, this approach will retain the essential tools needed to make a video by 
trimming and organizing clips, generating titles, importing still images,  and adding sound/music. 
Ideally, due to the different nature of computer video files, the language will allow the video to 
be rendered in different formats to ensure playback with a given player on a given system supporting 
the following formats:
* .h264
* .mov
* .wmv 

## Installation
Must have installed **Python3.6**. 
Run the following commands in command prompt (Windows) or terminal (Ubuntu/MacOs).

Assuming project root
* MacOs/Ubuntu
``` Shell
source venv/bin/activate
```
* Windows
```Shell
.\venv\Scripts\activate
```
```Shell
pip install -r requirements.txt
```

### Required Software
* [ImageMagick](https://www.imagemagick.org/script/download.php)
   
   * Once installed make sure to read the following directory to set up **ImageMagick**
      ```Shell
      venv/Lib/site-packages/moviepy/config_defaults.py


## Basic Language Syntax and Operations

The video editing tools that this language allows you to use are: 
* Crop
* Resize
* Add text to video
* Adding sound/music
* Importing still images 

When it comes to __rendering__, the user is able to render both videos or gifs. 
Unlike many video editing software, the steps required to do the rendering are 
very simple. 

```
>> clip =  video from "C:\\Users\\user\\Videos\\LoveIsWar.mp4" between 0,1 and 0,30
>> renderVid clip
```

And the rest of the tools are just as simple to implement.

### Crop:

The crop method work by adjusting the aspect ratio of a video. The user can decide 
the aspect ratio from any of the next:
* 16:9
* 4:3
* 2.35:1 
    * which is cinemascope
* 17:9
    * typically used for 4K

Keep in mind that this method will cut part of the video if it's to a smaller aspect ratio. 
```
>> crop clip by 16:9
```

### Resize: 

The resize method is a method that changes the size, but unlike crop, it keeps the entire image of the video. 
An example of how it works would be:
```
>> resize clip by 3
```

### Audio:

The user can edit the audio of the video at any desired part of it. This works by taking a file with the 
desired audio and setting it with the boundaries of where its going to play in the video.
```
>> addAudio "C:\\User\\user\\Music\\dropbeat.mp3" to clip between 3,5 
```

### Gif:

From any desired video, the user has the chance of turning it into a gif. This means that the video will
constantly loop. The rendering of this type of media takes as input, a variable that already holds 
the video.
```
>> renderGif from clip
```

## Video Demonstration


## Authors 

[Brian Rodriguez Badillo](https://github.com/TheParodicts)  
[Christian Perez](https://github.com/ChristianPerez34)  
[Alejandro Reyes](https://github.com/alejoreyes96)  
[Lexdyel J. Mendez Rios](https://github.com/lexdyel-mendez)


## License