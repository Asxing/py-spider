import urllib.request

filename = urllib.request.urlretrieve(
    "http://edu.51cto.com", filename="2.html")

# 进行解码
urllib.request.unquote("http%3A//www.sina.com.cn")

# 解码爬虫
# filename = urllib.request.urlretrieve(urllib.request.unquote("http%3A//www.sina.com.cn"), filename="2.html")

# 进行编码
urllib.request.quote("http://www.sina.com.cn")

# 使用 urlretrieve 可以直接下载，这种方式直接下载文件，没有业务处理
urllib.request.urlcleanup()
