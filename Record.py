#Version in order to verify that the stream is up and running and file plays well

from threading import Thread
from time import sleep
import gi
gi.require_version("Gst","1.0")
from gi.repository import Gst
from gi.repository import GLib
import signal


signal.signal(signal.SIGTSTP, signal.SIG_IGN)		#Maybe ToFix, when Ctrl + Z is pressed file is not playable (this command ignores Ctrl + Z)
print("In order to stop press: Ctrl C.")


Gst.init()
main_loop = GLib.MainLoop()
main_loop_thread = Thread(target = main_loop.run)
main_loop_thread.start()

pipeline = Gst.parse_launch('autoaudiosrc ! audioconvert ! tee name="source" ! vorbisenc ! oggmux ! filesink location=file.ogg source. ! queue ! appsink')	#ToDo kick pulsesink mb audioconvert + queue //

pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        sleep(0.1)

except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()
