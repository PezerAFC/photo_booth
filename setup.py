import sys
from cx_Freeze import setup, Executable

# Include required packages
build_exe_options = {"packages": ["cv2", "PIL", "tkinter"]}

# Specify the script and the executable name
executables = [Executable("take_picture.py", base=None)]

setup(
    name = "TakePicture",
    options = {"build_exe": build_exe_options},
    version = "1.0",
    description = "Take a picture using OpenCV and Tkinter",
    executables = executables
)
