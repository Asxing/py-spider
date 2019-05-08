import urllib.request
import re


def getlink(url):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())

    regx = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(regx).findall(data)
    link = list(set(link))
    return link


linkList = getlink("http://blog.csdn.net/")
for link in linkList:
    print(link[0])
