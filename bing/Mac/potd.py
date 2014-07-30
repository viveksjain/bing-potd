import os
import time
import shutil
import sys
import urllib
import urllib2
import json

# Directory to download the images into
dest_dir = os.path.expanduser('~/Pictures/potd')

# Returns when an internet connection is available. Waits up to about 15
# minutes and if internet is still unavailable after that, exits.
def wait_for_internet():
    timeout = 1
    while True:
        try:
            # Try to open the IP address of google.com
            urllib2.urlopen('http://74.125.228.100', timeout=1)
            return
        except urllib2.URLError:
            if timeout > 512:
                sys.exit(1)
            time.sleep(timeout)
            timeout *= 2

# Set the desktop background to the given path.
def set_background(image_file):
    from AppKit import NSWorkspace, NSScreen
    from Foundation import NSURL
    file_url = NSURL.fileURLWithPath_(image_file)
    ws = NSWorkspace.sharedWorkspace()
    for screen in NSScreen.screens():
        ws.setDesktopImageURL_forScreen_options_error_(file_url, screen, {}, None)

dest = os.path.join(dest_dir, time.strftime('%y-%m-%d.jpg'))
if os.path.exists(dest): # The script has already run today
    if not (len(sys.argv) == 2 and sys.argv[1] == '-f'):
        sys.exit(0)

if os.path.exists(dest_dir): # Delete old pictures if they exist
    shutil.rmtree(dest_dir)
os.mkdir(dest_dir)
wait_for_internet()

data = urllib2.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1').read()
link = 'http://www.bing.com' + json.loads(data)['images'][0]['url']
urllib.URLopener().retrieve(link, dest)
set_background(dest)
