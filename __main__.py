import os
import time
import datetime
import shutil
from PIL import Image


# work DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file_src = os.path.join(ROOT_DIR, 'src/')
file_tar = os.path.join(ROOT_DIR,'archieve/')

# Treading file list
file_list = os.listdir(file_src)
cnt=1

# Extracting Dates
for file in file_list :
    old_name = file_src+file
    ext = os.path.splitext(file)[1]
    try :
        p = Image.open(file_src+file)
        meta = p._getexif()
        time = meta[36867]
        year = time.split(':')[0]
        month = time.split(':')[1]
        tar_dir = file_tar+year+"/"+month+"/"
        if not os.path.isdir(tar_dir):
            os.makedirs(tar_dir)

        time = time.replace(':','-')
        time = time.split(' ')[0]
        time = time+"_"+str(cnt)
        new_name = tar_dir+time+ext
        cnt+=1
        p.close()

    except Exception :
        create_time = os.path.getctime(file_src+"/"+file)
        create_time = datetime.datetime.fromtimestamp(create_time)
        tar_dir = file_tar+datetime.datetime.strftime(create_time, '%Y/%m/')
        if not os.path.isdir(tar_dir):
            os.makedirs(tar_dir)

        create_time = datetime.datetime.strftime(create_time, '%Y-%m-%d')
        new_name = tar_dir+create_time+"_"+str(cnt)+ext
        cnt+=1

    # Change file name
    shutil.copy2(old_name, new_name)

# Done
print("[INFO] Date Labeling Completed!")