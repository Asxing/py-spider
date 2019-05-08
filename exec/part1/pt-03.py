import urllib.request

'''
添加请求头
'''
url = "https://juejin.im/"
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
# 借助 opener 代理
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#
# 使用 opener 进行读取
data = opener.open(url).read()
print(data)
