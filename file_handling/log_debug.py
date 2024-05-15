
import inspect

def print_cmd(note=None):
    frame = inspect.currentframe().f_back
    filename = inspect.getframeinfo(frame).filename
    line_number = frame.f_lineno
    filename = filename.rsplit('/', 1)[1]
    print(f"file: {filename} -> {line_number} -> {note}")

