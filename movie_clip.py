# -*- coding:utf-8 -*-

import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip


'''
A script to batch clip video
'''

path = raw_input("Enter the absolute path: ")  # absolute path
directory = os.listdir(path)  # get the video files' name
print "start time, whatever u want, it's the beginning of the new cliped video\
        like this:\
        original-------------------------end\
        <--clipped part-->t1-------------end"
t1 = raw_input("Enter t1 please(float point number): ")

for f in directory:
    clip_file_name = path + f  # the absolute path of the video file
    print clip_file_name
    # get the length of the video
    # t2 can be whatever u want, it's the end of the new clipped video.
    # as follow, it's the length of original video.
    t2 = VideoFileClip(clip_file_name).duration
    print t2
    # absolte path, its name shuld NOT be the same as original video
    tar_name = path + 'test_' + f
    print tar_name
    try:
        ffmpeg_extract_subclip(clip_file_name, t1, t2,
                               targetname=tar_name)
    except Exception as e:
        print e
