Image Search
=============

[![GitHub issues](https://img.shields.io/github/issues/tusharmakkar08/Facebook_Graph_Search_Images.svg)](https://github.com/tusharmakkar08/Facebook_Graph_Search_Images/issues)
[![GitHub stars](https://img.shields.io/github/stars/tusharmakkar08/Facebook_Graph_Search_Images.svg)](https://github.com/tusharmakkar08/Facebook_Graph_Search_Images/stargazers)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/tusharmakkar08/Facebook_Graph_Search_Images/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/facebook-image-search.svg?maxAge=2592000)](https://pypi.python.org/pypi/facebook_image_search)

This application aims to solve the following issues:

* Due to the advent of Post Search, it's difficult to use the feature of "Photos of" which was earlier done using 
graph search. 
* Downloads profile images from popular platforms like Linkedin, Quora, Github, Instagram, Facebook etc. 

You can read more about the project [here](http://tusharmakkar08.github.io/Facebook_Graph_Search_Images/). 


#  Installation : 


`facebook_image_search` is a Python2.7 library. 

    pip install facebook_image_search


# Preconditions :


Graph search doesn't work until you are logged into your account while the extension works otherwise also. 
This is a command line tool. 

# Usage :


    usage: main_search.py [-h] [-fb] [-ig] [-qr] [-ln] [-gb] [-n username]
                      [-u url] [-i id] [-d DIRECTORY]

    Tool for fetching photos from facebook
    
    optional arguments:
      -h, --help            show this help message and exit
      -fb, --facebook       Fetch Facebook Photos (Default)
      -ig, --instagram      Fetch Instagram Photos
      -qr, --quora          Fetch Instagram Photos
      -ln, --linkedin       Fetch LinkedIn Profile Photo
      -gb, --github         Fetch Github Profile Photo
      -n username, --username username
                            Username to analyze (For Linkedin add everything after
                            ".com" eg: in/tusharmakkar08)
      -u url, --url url     Profile Url to analyze
      -i id, --id id        Profile Id to analyze (only for facebook)
      -d DIRECTORY, --directory DIRECTORY
                            Directory to download photos (except Facebook)

# License

The mighty MIT license. Please check `LICENSE` for more details.
