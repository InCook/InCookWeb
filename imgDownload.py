import os
import sys
import urllib.request

from web.models import *

def download_photo(img_url, filename):
    file_path = "%s%s" % (os.path.join(os.getcwd() + "/static/recipe/img/"), filename)
    downloaded_image = open(file_path, "wb")

    image_on_web = urllib.request.urlopen(img_url)
    while True:
        buf = image_on_web.read(100000000)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)

    downloaded_image.close()
    image_on_web.close()

    return file_path

food = cook.objects.all()
for i in food:
    download_photo(i.image, i.name)
# call
#download_photo("https://www.edamam.com/web-img/1f4/1f4f0a545545954d3a167882dc07aa68.jpg", "Salmon with cucumbers.jpg")
