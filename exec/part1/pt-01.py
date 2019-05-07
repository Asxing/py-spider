import urllib.request

file =urllib.request.urlopen("http://www.baidu.com")
data = file.read()
print(data)