# Clickjackin

Python3
This is a tool to test a list of urls for clickjacking vulnerability, and returns results as screenshots.

<b>Requirements:</b>
python3
Must have selenium, google-chrome and chromedriver installed.
chromedriver version must support chrome version, otherwise you'll get errors.
Download the right version of chromedriver here:
https://chromedriver.chromium.org/downloads

The path to google chrome and chromedriver can be found in cj.py source code. 
Change the paths if you have google-chrome and chromedriver located somewhere else.

opts.binary_location = '/opt/google/chrome/google-chrome'
service = Service('/usr/bin/chromedriver')

<b>Usage:</b>
// Must create screenshots directory before running the script.<br>
$ mkdir screenshots<br>
$ ./cjlist.sh domains-list.txt

//When test completed, you can view urls screenshots.<br>
$ cd screenshots<br>
$display *.png

Then click on image to display imagemagic menu to keep moving to next screenshots with File > Next or > Former, 
but it's easier to use the keyboard shortcuts (Spacebar for the next image and Backspace for the previous).

Results:
If the page is blank or blocked, then it's not vulnerable. 
If the page was rendered, then it's vulnerable to clickjacking.
