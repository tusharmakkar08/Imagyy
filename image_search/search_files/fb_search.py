__author__ = 'tusharmakkar08'

import json
import urllib
import webbrowser
from bs4 import BeautifulSoup
import requests


def __get_profile_id_fbv1(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']


def __get_profile_id_fbv2(username):
    """
    Input : Username
    Output : Profile Id HTML 
    """
    request_data = requests.post("http://findmyfbid.com/", data={'url': username})
    return request_data.text


def __get_user_id(html_string):
    """
    Input : HTML String from POST
    Output : Profile Id  
    """
    return BeautifulSoup(html_string, "html.parser").code.string


def _open_image_page(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with graph search results
    """
    try:
        new_url = "https://www.facebook.com/search/" + profile_id + "/photos-of"
        webbrowser.open_new_tab(new_url)
        return 1
    except Exception, e:
        print(e)
        return -1


def _open_profile_pic(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with profile picture of the username
    """
    try:
        new_url = "https://graph.facebook.com/" + profile_id + "/picture?width=800"
        webbrowser.open_new_tab(new_url)
        return 1
    except Exception, e:
        print(e)
        return -1


def _open_public_images(username):
    """
    :param username: username of a given person
    :return:
    """
    try:
        new_url = "https://www.facebook.com/" + username + "/photos_all"
        webbrowser.open_new_tab(new_url)
        return 1
    except Exception, e:
        print(e)
        return -1


def _download_profile_pic(profile_id, file_name):
    """
    :param file_name: File name to store
    :return:
    """
    image_link = "https://graph.facebook.com/" + profile_id + "/picture?width=800"
    urllib.urlretrieve(image_link, file_name)


def facebook_image_search(username, user_id=None, directory_to_download=None):
    """
    :param username: Username of the person to search eg: tusharmakkar08
    :param user_id: User Id of the person (integral number) eg: 647452998
    :return:
    """
    try:
        if not user_id:
            user_html = __get_profile_id_fbv2(username)
            user_id = __get_user_id(user_html)
            _open_public_images(username)
        else:
            new_url = "https://www.facebook.com/profile.php?id="+user_id+"&sk=photos"
            webbrowser.open_new_tab(new_url)
        _open_image_page(user_id)
        _open_profile_pic(user_id)
        if not directory_to_download:
            if username:
                directory_to_download = username + ".jpg"
            else:
                directory_to_download = user_id + ".jpg"
        _download_profile_pic(user_id, directory_to_download)
        return 1
    except Exception, e:
        print(e)
        return -1
