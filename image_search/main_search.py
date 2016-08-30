__author__ = 'tusharmakkar08'

import argparse

from image_search.search_files.instagram_search import instagram_image_downloader
from image_search.search_files.fb_search import facebook_image_search
from image_search.search_files.github_search import github_image_downloader
from image_search.search_files.quora_search import quora_image_downloader
from image_search.search_files.linkedin_search import linkedin_image_downloader


def _get_parser():
    """
    Command line Parser for search
    :return:
    """
    parser = argparse.ArgumentParser(description='Tool for fetching photos from facebook')
    parser.add_argument('-fb', '--facebook', action='store_true',
                        help='Fetch Facebook Photos (Default)')
    parser.add_argument('-ig', '--instagram', action='store_true',
                        help='Fetch Instagram Photos')
    parser.add_argument('-qr', '--quora', action='store_true',
                        help='Fetch Instagram Photos')
    parser.add_argument('-ln', '--linkedin', action='store_true',
                        help='Fetch LinkedIn Profile Photo')
    parser.add_argument('-gb', '--github', action='store_true',
                        help='Fetch Github Profile Photo')
    parser.add_argument('-n', '--username', metavar='username', type=str,
                        help='Username to analyze (For Linkedin add everything after ".com" eg: in/tusharmakkar08)')
    parser.add_argument('-u', '--url', metavar='url', type=str,
                        help='Profile Url to analyze')
    parser.add_argument('-i', '--id', metavar='id', type=str,
                        help='Profile Id to analyze (only for facebook)')
    parser.add_argument('-d', '--directory', metavar='directory', type=str, default=None,
                        help='Directory to download photos')
    return parser


def command_line_runner():
    """
    Entry point for script; Modify to add another search script
    :return:
    """
    parser = _get_parser()
    args = vars(parser.parse_args())
    if args["instagram"] and (args['username'] or args['url']):
        instagram_url = args['url'] if args['url'] else "https://www.instagram.com/" + args['username']
        instagram_image_downloader(instagram_url, args['directory'])
    elif args["github"] and (args['username'] or args['url']):
        github_url = args['url'] if args['url'] else "https://github.com/" + args['username']
        github_image_downloader(github_url, args['directory'])
    elif args["quora"] and (args['username'] or args['url']):
        quora_url = args['url'] if args['url'] else "https://www.quora.com/profile/" + args['username']
        quora_image_downloader(quora_url, args['directory'])
    elif args["linkedin"] and (args['username'] or args['url']):
        linkedin_url = args['url'] if args['url'] else "https://www.linkedin.com/" + args['username']
        linkedin_image_downloader(linkedin_url, args['directory'])
    elif not (args['username'] or args['url'] or args['id']):
        parser.print_help()
    elif args['username']:
        facebook_image_search(args['username'], directory_to_download=args['directory'])
    elif args['url']:
        username = args['url'].split(".com/")[1].split("/")[0]
        if ".php" in username:
            user_id = username.split('=')[1]
            facebook_image_search("", user_id, directory_to_download=args['directory'])
        else:
            facebook_image_search(username, directory_to_download=args['directory'])
    elif args['id']:
        user_id = args['id']
        facebook_image_search("", user_id, directory_to_download=args['directory'])
    else:
        parser.print_help()
    return


if __name__ == '__main__':
    command_line_runner()
