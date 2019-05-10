# Welcome to Videout!

Videout is a language design to edit *videos/gifs* through coding. This way programmers that have
no experience with media editing programs, can do projects that involve said task. The language was 
designed as an assignment for the Programming Language course at UPRM. 

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

The crop method work by adjusting the aspect ratio of a video. You can decide the aspect ratio from the next:
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