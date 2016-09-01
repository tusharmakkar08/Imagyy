__author__ = 'tusharmakkar08'

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, urlretrieve
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
    from urllib import urlretrieve


import re
import uuid
import os

URL_REGEX = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
PIC_EXTENSION = '.jpeg'
DEFAULT_DIRECTORY = os.path.join(os.getcwd(), "quora_images")


def quora_image_downloader(url, directory_to_download=None):
    """
    Downloads Quora images in a particular directory
    :param url: Quora username url eg: https://www.quora.com/profile/Tushar-Makkar
    :param directory_to_download: Directory where files will be downloaded ,
    if this is none then files downloaded to default directory
    :return:
    """
    response = urlopen(url)
    html = response.read().decode('utf-8')
    image_links = {link for link in re.findall(URL_REGEX, html) if PIC_EXTENSION in link and "200" in link}
    download_directory = os.path.join(DEFAULT_DIRECTORY, directory_to_download) if directory_to_download else \
        os.path.join(DEFAULT_DIRECTORY, url.split(".com/profile/")[1].strip("/"))
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    for image_link in image_links:
        download_location = os.path.join(download_directory, str(uuid.uuid4()) + PIC_EXTENSION)
        urlretrieve(image_link, download_location)
