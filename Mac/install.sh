#!/bin/bash

cd `dirname "$0"` # Set working directory to the parent directory of this script
mkdir -p ~/Library/Scripts/
cp bing-potd.py ~/Library/Scripts/
cp in.vivekja.bing-potd.plist ~/Library/LaunchAgents/
launchctl unload in.vivekja.bing-potd.plist 2> /dev/null
launchctl load ~/Library/LaunchAgents/in.vivekja.bing-potd.plist
