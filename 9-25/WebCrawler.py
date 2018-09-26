# coding:utf-8
import re
import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def get_img(html):
    html = html.decode('utf-8')
    reg = r'src="(.+?\.jpg)"'
    reg_img = re.compile(reg)
    img_list = re.findall(reg_img, html)
    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1


html = get_html("https://tieba.baidu.com/p/1753935195")
print(get_img(html))
"""
    return img_list

html = get_html("https://tieba.baidu.com/p/1753935195")
print(get_img(html))


print("please input url")
url = input()
if url:
    pass
else:
    url = "https://tieba.baidu.com/p/1753935195"
"""


"""
html_code = get_html(url)
get_img(html_code)

    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1
    html = get_html("https://tieba.baidu.com/p/1753935195")
    print(get_img(html))
"""