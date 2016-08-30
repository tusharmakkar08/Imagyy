Imagyy
======

|Build\_Status| |GitHub\_issues| |GitHub\_stars| |GitHub\_license|
|PyPI|

Imagyy aims to solve the following issues:

-  Due to the advent of Post Search, it’s difficult to use the feature
   of “Photos of” which was earlier done using graph search.
-  Downloads profile images from popular platforms like Linkedin, Quora,
   Github, Instagram, Facebook etc.

You can read more about the project `here`_.

Installation :
==============

``facebook_image_search`` is a Python2.7 library.

::

    pip install imagyy

Preconditions :
===============

Graph search doesn’t work until you are logged into your account while
the extension works otherwise also. This is a command line tool.

Usage :
=======

::

    usage: imagyy [-h] [-fb] [-ig] [-qr] [-ln] [-gb] [-n username]
                          [-u url] [-i id] [-d directory]

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
      -d directory, --directory directory
                            Directory to download photos/Name of downloaded file

Examples
========

-  For facebook related photos from username

   ::

       imagyy -fb -n zuck 

-  For facebook related photos from url

   ::

       imagyy -fb -u http://facebook.com/zuck

-  For Instagram related photos from username

   ::

       imagyy -ig -n tusharmakkar08

-  For Quora related photos from username

   ::

       imagyy -qr -n Tushar-Makkar

-  For Github related photos from username

   ::

       imagyy -gb -n tusharmakkar08

-  For Linkedin related photos from username

   ::

       imagyy -ln -n in/tusharmakkar08

License
=======

The mighty MIT license. Please check ``LICENSE`` for more details.

.. _here: http://tusharmakkar08.github.io/Imagyy/

.. |Build_Status| image:: https://travis-ci.org/tusharmakkar08/Imagyy.svg?branch=master
   :target: https://travis-ci.org/tusharmakkar08/Imagyy
.. |GitHub_issues| image:: https://img.shields.io/github/issues/tusharmakkar08/Imagyy.svg
   :target: https://github.com/tusharmakkar08/Imagyy/issues
.. |GitHub_stars| image:: https://img.shields.io/github/stars/tusharmakkar08/Imagyy.svg
   :target: https://github.com/tusharmakkar08/Imagyy/stargazers
.. |GitHub_license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/tusharmakkar08/Imagyy/master/LICENSE
.. |PyPI| image:: https://img.shields.io/pypi/v/Imagyy.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/imagyy
