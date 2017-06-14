#!/usr/bin/python
import subprocess

blur = 'xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id '
konsole_id = subprocess.getoutput('xdotool getactivewindow')

if konsole_id is not None:
    subprocess.getoutput(blur + konsole_id)
