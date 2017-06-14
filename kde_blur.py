#!/usr/bin/python
import subprocess

konsole_id = subprocess.getoutput('xdotool getactivewindow')
blur = 'xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id '

if konsole_id is not None:
    for k_id in konsole_id.splitlines():
        subprocess.getoutput(blur + konsole_id)
