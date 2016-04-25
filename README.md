Fb AutoLiker
====================

Read publications and gives likes

Installation
------------
```sh
    git clone https://github.com/diegordzr/fbliker
```
Requirements
------------
```sh
    cd fbliker
    pip install -r requirements.txt
```
Usage
-----
Get profile information:
```sh
    scrapy crawl fb_profile
```
Gives likes to listed users in the "data/fb_users.txt" file.
```sh
	scrapy crawl fb_stories
```