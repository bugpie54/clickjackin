import os
import sys
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep


if len(sys.argv) != 2:
        print ('\n[+] Description: %s can quickly verify if a web page is vulnerable to clickjacking') % __file__
        print ('[+] Usage: python %s <url>\n') % __file__
        exit(0)

url = sys.argv[1]

html = '''
<html>
        <head>
                <title>Clickjacking Test Page</title>
        </head>
        <body>
                                <p>Target: <a href="%s">%s</a></p>
                <p>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</p>
                <iframe width="900" height="600" src="%s"></iframe>
                <iframe style="position: absolute; left: 20px; top: 250px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-test.html"></iframe>
        </body>
</html>
''' % (url, url, url)

html2 = '''
<html>
        <div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
                <center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
                <br>normally invisible</center>
        </div>
</html>
'''

cjv = os.path.abspath('cj-victim.html')
cjt = os.path.abspath('cj-test.html')
localurl = 'file://' + cjv

with open(cjv, 'w') as v, open (cjt, 'w') as t:
        v.write(html)
        t.write(html2)

opts = Options()
opts.binary_location = '/opt/google/chrome/google-chrome'
opts.add_argument('--headless')

opts.add_argument('--no-sandbox')
#opts.add_argument('--disable-dev-shm-usage')

opts.add_argument("--window-size=1920x1080")
opts.add_argument("enable-automation")
#opts.add_argument("--disable-notifications")
#opts.add_argument("--disable-extenstions")
#opts.add_argument("--disable-gpu")
#opts.add_argument("--dns-prefetch-disable")
#opts.add_argument("disable-infoars")
#opts.add_argument("force-device-scale-factor=0.65")
#opts.add_argument("high-dpi-support=0.65")

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(options=opts, service=service)

driver.get(localurl)
sleep(1)
png = url[url.find('/')+2:]
png = png.replace('/', '-') + '.png'

driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', png))

driver.quit()

print(url)
print(png)
#print ('\n[+] Test Complete!')
