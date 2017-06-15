#!/bin/bash

blur='xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id '
konsole_id=$(xdotool getactivewindow)

if [ -n $konsole_id ] 
then
	for kid in $konsole_id;
	do $blur $kid;
	done;
fi
