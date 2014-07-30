#!/bin/bash

launchctl unload in.vivekja.potd.plist 2> /dev/null
rm -f ~/Library/LaunchAgents/in.vivekja.potd.plist ~/Library/Scripts/potd.py
