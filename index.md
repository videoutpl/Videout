# Welcome to Videout!
![Code Quality](https://img.shields.io/pypi/status/Django.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
      ```
      venv/Lib/site-packages/moviepy/config_defaults.py
      ```


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
desired audio and setting it with the boundaries of where its going to play in the video.The user can also 
decide what part of the audio should be used inside of a time frame `start,end`

It's important to add the path as a string with `" "` and that the dashes are double `\\`.

```
>> addAudio "C:\\User\\user\\Music\\dropbeat.mp3" to clip between 3,7 
```

There is also a function that allows you to extract the audio from a clip, and add that audio to another desired 
clip. Making the re-use of audio much easier than using ``addAudio`` each time. . 

````
>> extractAudio clip2 to clip1 between 0,15.
````

### Gif:

From any desired video, the user has the chance of turning it into a gif. This means that the video will
constantly loop. The rendering of this type of media takes as input, a variable that already holds 
the video.
```
>> renderGif from clip
```

### Photo:

Another function that can be done is making a variable hold an image. Later that image can be concatenated 
at any clip already made. This can be done for titles or just an ending image of the video. Making this 
variable is just as making the one for videos, but instead of a time frame, you decide how much its going to 
last that image being shown when its concatenated. 


The time is taken in consideration as seconds.

````
>> pic = photo from "C:\\User\\user\\Photos\image.jpg" lasting 5
````


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

### Concatenation
Lastly, there is also a function that allows you to concatenate 2 videos (or video and image), making a new clip of it. The order 
of the concatenation matters, since its going to be added from left to right. This means that if you use the video before a picture
the result will be a video with that image at the end.

````
>> concat = concatenateClip clip and pic
````

If the user wants to add the image first, it most be specified that way

````
>> concat = concatenateClip pic and clip
````

### Sample code:

````
>>clip = video from "C:\\Users\\lexdy\\Desktop\\PL_Project\\Videout\\Test\\video\\The Simpsons-BartRap.mp4" between 0,40 and 0,70 
>>addAudio "C:\\Users\\lexdy\\Desktop\\PL_Project\\Videout\\Test\\audio\\Eminem-LoseYourself.mp3" to clip between 0,35
>>pic = photo from "C:\\Users\\lexdy\\Desktop\\PL_Project\\Videout\\Test\\photos\\BartPic.jpg" lasting 5
>>concat = concatenateClip clip and pic
>>renderVid concat
````
At this point it will start to load the rendering of the clip

````
>>clip2 = video from "C:\\Users\\lexdy\\Desktop\\PL_Project\\Videout\\src\\concat.mp4" between 0,5 and 0,10
>>renderGif clip2
````
Then it will start to render the gif


## Video Demonstration

This is the [desmonstration]() of how to make the rendering of a video, including adding audio and concatenation. And [this]() would be
the result of said rendering. The videos are going to be saved on the src folder with the name of the variable as its name. 

Then [this]() would be the deomstration of how to render a gif, with its [result]() being saved on the src folder as well.


## Authors 

[Brian Rodriguez Badillo](https://github.com/TheParodicts)  
[Christian Perez](https://github.com/ChristianPerez34)  
[Alejandro Reyes](https://github.com/alejoreyes96)  
[Lexdyel J. Mendez Rios](https://github.com/lexdyel-mendez)


## License

MIT License.
