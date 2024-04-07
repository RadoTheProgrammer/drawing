import os

from pyparsing import C
DIR="drawings"
CURRENT_FILE=os.path.join(DIR,"current.png")

def switch():
    global filename
    filename=os.path.join(DIR,filename_tag)
    os.remove(CURRENT_FILE)
    os.symlink(filename_tag,CURRENT_FILE)

if os.path.exists(DIR):
    filename_tag=os.readlink(os.path.join(DIR,CURRENT_FILE))
    filename=os.path.join(DIR,filename_tag)
else:
    os.mkdir(DIR)
    filename_tag="drawing_0.png"
    