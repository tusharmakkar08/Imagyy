Facebook Image Graph Search
===========================

Due to the advent of Post Search, it's difficult to use the feature of "Photos of" which was earlier done using 
graph search. This application aims to solve that problem. You can read more about the project [here](http://tusharmakkar08.github.io/Facebook_Graph_Search_Images/). 

Extension 1 :
-------------

The profile picture of a given username is also opened in a new tab with original (maximum) size. 

Extension 2 :
-------------

Gets the open images of a public profile. 

Extension 3 :
-------------

Downloads instagram images in a folder. 

#  Installation : 


`facebook_image_search` is a Python2.7 library. 

    pip install facebook_image_search


# Preconditions :


Graph search doesn't work until you are logged into your account while the extension works otherwise also. 
This is a command line tool. 

# Usage :


    usage: fb_search.py [-h] [-fb] [-ig] [-n username] [-u url] [-i id]
                    [-d DIRECTORY]

    Tool for fetching photos from facebook and instagram
    
    optional arguments:
      -h, --help            show this help message and exit
      -fb, --facebook       Fetch Facebook Photos (Default)
      -ig, --instagram      Fetch Instagram Photos
      -n username, --username username
                            Username to analyze
      -u url, --url url     Profile Url to analyze
      -i id, --id id        Profile Id to analyze (only for facebook)
      -d DIRECTORY, --directory DIRECTORY
                            Directory to download photos (only for instagram)



# License

The mighty MIT license. Please check `LICENSE` for more details.
