# -*- coding:utf-8 -*-

"""
A USB copy script, auto check whether USB device insert and copy it
run it at daemon
"""

import os
import time
from datetime import datetime
import shutil
import getpass

username = getpass.getuser()
save_path = os.getcwd()
save_list = []

while True:
    USBlist = os.listdir("/media/%s/" % username)
    if not USBlist:
        time.sleep(200)
    else:
        for usb in USBlist:
            path = "/media/%s/" % username + usb
            if os.path.exists(path) and (usb not in save_list):
                shutil.copytree(path, os.path.join(
                    save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
                save_list.append(usb)
                # break

with open("usb_names.txt", "a+") as f:
    f.write(save_list)
