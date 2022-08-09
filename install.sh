#!/bin/bash

scriptname="sitedorks.py"

pip3 install -r requirements.txt

dir=$(pwd)

2ulb 2&>/dev/null
	if [ $? -eq 127 ]
	then	
		echo "2ulb not found, install 2ulb? [y/n]: "
		while true; do
			read yn -p
			case $yn in
			    [Yy]*) cd .. || exit; git clone https://github.com/Zarcolio/2ulb ; sudo python3 2ulb/2ulb.py 2ulb/2ulb.py ; cd "$dir" || exit; sudo 2ulb $scriptname; exit 0 ;;  
			    [Nn]*) echo "Aborted" ; exit 1 ;;
			esac
		done
	else
		sudo 2ulb $scriptname
	fi
