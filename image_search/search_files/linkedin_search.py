__author__ = 'tusharmakkar08'

import urllib2
import urllib
import re
import uuid
import os

URL_REGEX = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
PIC_EXTENSION = '.jpg'
DEFAULT_DIRECTORY = os.path.join(os.getcwd(), "linkedin_images")


def linkedin_image_downloader(url, directory_to_download=None):
    """
    Downloads LinkedIn images in a particular directory
    :param url: LinkedIn username url eg: https://www.linkedin.com/in/tusharmakkar08
    :param directory_to_download: Directory where files will be downloaded ,
    if this is none then files downloaded to default directory
    :return:
    """
    urlopener = urllib2.build_opener()
    # Linkedin doesn't allow direct html access.
    urlopener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = urlopener.open(url).read()
    image_links = {link for link in re.findall(URL_REGEX, html) if PIC_EXTENSION in link and "shrinknp_200_200" in link}
    download_directory = os.path.join(DEFAULT_DIRECTORY, directory_to_download) if directory_to_download else \
        os.path.join(DEFAULT_DIRECTORY, url.strip("/").split("/")[-1])
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    for image_link in image_links:
        download_location = os.path.join(download_directory, str(uuid.uuid4()) + PIC_EXTENSION)
        urllib.urlretrieve(image_link, download_location)
