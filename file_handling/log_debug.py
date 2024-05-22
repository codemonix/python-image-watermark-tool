""" This module provide a tool for monitoring events in desired stage and location 
for debugging and monitoring
"""
import inspect
import os
from datetime import datetime

def print_cmd(note=None):

    frame = inspect.currentframe().f_back
    filename = inspect.getframeinfo(frame).filename
    line_number = frame.f_lineno
    filename = filename.rsplit('/', 1)[1]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} file: {filename} -> {line_number} -> {note}")

