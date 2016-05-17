__author__ = 'tusharmakkar08'

import json
import urllib
import webbrowser

from bs4 import BeautifulSoup
import requests


def get_profile_id_fbv1(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']


def get_profile_id_fbv2(username):
    """
    Input : Username
    Output : Profile Id HTML 
    """
    request_data = requests.post("http://findmyfbid.com/", data={'url': username})
    return request_data.text


def get_user_id(html_string):
    """
    Input : HTML String from POST
    Output : Profile Id  
    """
    return BeautifulSoup(html_string, "html.parser").code.string


def open_image_page(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with graph search results
    """
    new_url = "https://www.facebook.com/search/" + profile_id + "/photos-of"
    webbrowser.open_new_tab(new_url)


def open_profile_pic(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with profile picture of the username
    """
    new_url = "https://graph.facebook.com/" + profile_id + "/picture?width=800"
    webbrowser.open_new_tab(new_url)


def main():
    username = raw_input("Enter the Username : ")
    user_html = get_profile_id_fbv2(username)
    user_id = get_user_id(user_html)
    open_image_page(user_id)
    open_profile_pic(user_id)
    print ""
    return 0


if __name__ == '__main__':
    main()
