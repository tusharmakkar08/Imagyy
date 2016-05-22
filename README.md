Facebook Image Graph Search
===========================

Due to the advent of Post Search , it's difficult to use the feature of "Photos of" which was earlier done using 
graph search . This application aims to solve that problem. 

Extension 1 :
-------------

The profile picture of a given username is also opened in a new tab with original (maximum) size. 

Extension 2 :
-------------

Gets the open images of a public profile. 

Installation : 
---------------

It can be installed via pip. 

`pip install facebook_image_search`


Preconditions :
---------------

Graph search doesn't work until you are logged into your account while the extension works otherwise also. 
This is a command line tool. 

Usage :
--------


    usage: fb-search.py [-h] [-n username] [-u url] [-i id]
    
    Tool for fetching photos from facebook
    
    optional arguments:
      -h, --help            show this help message and exit
      -n username, --username username
                            Username to analyze
      -u url, --url url     Profile Url to analyze
      -i id, --id id        Profile Id to analyze


Requirements :
--------------

* Python 2.7
