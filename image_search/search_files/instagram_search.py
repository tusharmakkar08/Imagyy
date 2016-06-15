__author__ = 'tusharmakkar08'

import urllib2
import urllib
import re
import os

URL_REGEX = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
PIC_EXTENSION = '.jpg'
DEFAULT_DIRECTORY = os.path.join(os.getcwd(), "instagram_images")


def instagram_image_downloader(url, directory_to_download=None):
    """
    Downloads Instagram images in a particular directory
    :param url: Instagram username url eg: https://www.instagram.com/tusharmakkar08/
    :param directory_to_download: Directory where files will be downloaded ,
    if this is none then files downloaded to default directory
    :return:
    """
    response = urllib2.urlopen(url)
    html = response.read()
    image_links = {link for link in re.findall(URL_REGEX, html) if PIC_EXTENSION in link}
    unique_image_set = set()
    download_directory = os.path.join(DEFAULT_DIRECTORY, directory_to_download) if directory_to_download else \
        os.path.join(DEFAULT_DIRECTORY, url.split(".com/")[1].strip("/"))
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    for image_link in image_links:
        image_id = image_link.split(PIC_EXTENSION)[0].split("/")[-1]
        if image_id not in unique_image_set:
            unique_image_set.add(image_id)
            download_location = os.path.join(download_directory, image_id + PIC_EXTENSION)
            urllib.urlretrieve(image_link, download_location)
