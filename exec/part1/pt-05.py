import urllib.request

keyword = "hello"
url = "http://www.baidu.com/s?wd=" + keyword
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fHandle = open("3.html", "wb")
fHandle.write(data)
fHandle.close()
``
