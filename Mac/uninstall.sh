#!/bin/bash

launchctl unload in.vivekja.bing-potd.plist 2> /dev/null
rm -f ~/Library/LaunchAgents/in.vivekja.bing-potd.plist ~/Library/Scripts/bing-potd.py
