# GStreamer-mic-Record-and-Play
A GStreamer implementation using python that creates a media file (.ogg) from user's mic. When done recording you can play it back using the Play.py script.

For GStreamer installation check: https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=python

*Project created in Python3 and executed at Ubuntu 20.04*
**Run both scripts from same folder**

*Usage:*
1) Execute `Record.py`
2) Your microphone input is being recorder at a file named file.ogg at the folder where your .py files are
3) Press `Ctrl + C` when recording has been completed
4) Execurte `Play.py` file that plays at user output (headsets or speakers) the recorded file


IF YOU WANT TO HEAR WHAT'S BEEN RECORDED SIMULTANEOUSLY TRY CHANGING THE PIPELINE ON `Record.py ~ line 21` 

to 

``autoaudiosrc ! audioconvert ! tee name="source" ! queue ! vorbisenc ! oggmux ! filesink location=file.ogg source. ! queue ! audioconvert ! pulsesink``
