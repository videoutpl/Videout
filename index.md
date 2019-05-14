# Welcome to Videout!
![Code Quality](https://img.shields.io/pypi/status/Django.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

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

Keep in mind that this method will cut part of the video if it's to a smaller aspect ratio. 
The user can decide between any of this different aspect ratios. 

Token | Aspect ratio
------ | -----------
vertical | 9:16
phone | 9:16
square | 1:1 
letterbox | 4:3 or 1.33:1
widescreen | 16:9 or 1.77:1
cinemascope | 21:9 or 2.33:1
anamorphic | 2.35:1
DCI | 2.39:1
Digital IMAX | 2.9:1

Take in consideration that it's caps sensitive. therefore the token of the desired aspect ration most 
be written exactly as it is in the table.

```
>> crop clip by widescreen
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

It's important to add the path as a string with `" "` and that the dashes are double `\\`.

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

### Text:

Lastly, one of the features is adding text to a desired video. This process is just as simple as 
deciding what text you want to add to what video, and then the desired time that the user wants 
the text to appear at. The user can decide any of this positions 

positions | positions
----------|-----------
top|bottom
left|right
top-left|top-right
bottom-left|bottom-right
top-center|bottom-center
center|

An example of this line of code would be:

```
>> addText "I like trains..." to clip to bottom
```

## Video Demonstration


## Authors 

[Brian Rodriguez Badillo](https://github.com/TheParodicts)  
[Christian Perez](https://github.com/ChristianPerez34)  
[Alejandro Reyes](https://github.com/alejoreyes96)  
[Lexdyel J. Mendez Rios](https://github.com/lexdyel-mendez)


## License

MIT License

Copyright (c) 2019 Videout

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.