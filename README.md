# rename-yt-dlp
This script help to rename files youtube video downloaded by yt-dlp parts

## Download youtube video by parts 
```
 yt-dlp --split-chapters -f "bv*[ext=mp4]+ba[ext=m4a]" -o "%(section_title)s.%(ext)s" https://www.youtube.com/watch\?v\=0000000
```
