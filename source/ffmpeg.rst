FFmpeg
======

.. option:: m4a_to_mp3

	``ffmpeg -i %1 -c:a libmp3lame -q:a 8 %1.mp3``

.. option:: image_to_video

	``ffmpeg -framerate 1 -i %04d.png -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4``

	``ffmpeg -framerate 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4``

=========
Reference
=========

#. https://www.ffmpeg.org