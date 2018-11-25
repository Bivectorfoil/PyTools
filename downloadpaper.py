#!/usr/bin/env python
# encoding: utf-8

import requests
import re


'''A small crawler to crawl wallpaper from wallpaper web you like.'''


def getHtml(url):
    req = requests.get(url)
    response = req.content
    return response


def getUrl(url):
    img_list = []
    content = getHtml(url)
    pastern = re.compile('http[^<]*?m.jpg')
    url_list = re.findall(pastern, content)
    for u in url_list:
        url = re.sub('m.jpg', 'o.jpg', u)
        img_list.append(url)
    return img_list


def DownloadImg(page, url):
    conuts = 1
    img_list = getUrl(url)
    for img in img_list:
        req = requests.get(img, timeout=6)
        response = req.content
        img_name = 'page%simg%s' % (page, str(conuts))
        with open(img_name + '.jpg', 'wb') as f:
            f.write(response)
        print 'download %s successfully ' % img_name
        conuts += 1


def main():
    base_url = 'http://www.topit.me/tag/PC%E5%A3%81%E7%BA%B8?p='
    for i in range(1, 3):
        page = str(i)
        url = base_url + page
        DownloadImg(page, url)


if __name__ == '__main__':
    main()
