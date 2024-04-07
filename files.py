import os
DIR="drawings"

if os.path.exists(DIR):
    filename_tag=os.readlink(os.path.join(DIR,"current.png"))
    filename=os.path.join(DIR,filename_tag)
else:
    os.mkdir(DIR)
    filename_tag="drawing_0.png"