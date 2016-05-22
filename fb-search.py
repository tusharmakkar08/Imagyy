__author__ = 'tusharmakkar08'

import argparse
import json
import urllib
import webbrowser

from bs4 import BeautifulSoup
import requests


def _get_profile_id_fbv1(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']


def _get_profile_id_fbv2(username):
    """
    Input : Username
    Output : Profile Id HTML 
    """
    request_data = requests.post("http://findmyfbid.com/", data={'url': username})
    return request_data.text


def _get_user_id(html_string):
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
    try:
        new_url = "https://www.facebook.com/search/" + profile_id + "/photos-of"
        webbrowser.open_new_tab(new_url)
        return 1
    except Exception, e:
        print(e)
        return -1


def open_profile_pic(profile_id):
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


def open_public_images(username):
    """
    :param username: username of a given person
    :return:
    """
    try:
        new_url = "https://www.facebook.com/"+username+"/photos_all"
        webbrowser.open_new_tab(new_url)
        return 1
    except Exception, e:
        print(e)
        return -1


def _get_parser():
    parser = argparse.ArgumentParser(description='Tool for fetching photos from facebook')
    parser.add_argument('-n', '--username', metavar='username', type=str,
                        help='Username to analyze')
    parser.add_argument('-u', '--url', metavar='url', type=str,
                        help='Profile Url to analyze')
    parser.add_argument('-i', '--id', metavar='id', type=str,
                        help='Profile Id to analyze')
    return parser


def main(username, user_id=None):
    try:
        if not user_id:
            user_html = _get_profile_id_fbv2(username)
            user_id = _get_user_id(user_html)
            open_public_images(username)
        else:
            new_url = "https://www.facebook.com/profile.php?id="+user_id+"&sk=photos"
            webbrowser.open_new_tab(new_url)
        open_image_page(user_id)
        open_profile_pic(user_id)
        return 1
    except Exception, e:
        print(e)
        return -1


def command_line_runner():
    parser = _get_parser()
    args = vars(parser.parse_args())
    if not (args['username'] or args['url'] or args['id']):
        parser.print_help()
    elif args['username']:
        main(args['username'])
    elif args['url']:
        username = args['url'].split(".com/")[1].split("/")[0]
        if ".php" in username:
            user_id = username.split('=')[1]
            main("", user_id)
        else:
            main(username)
    else:
        user_id = args['id']
        main("", user_id)
    return

if __name__ == '__main__':
    command_line_runner()
