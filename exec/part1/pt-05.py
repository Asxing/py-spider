import urllib.request
import urllib.parse

'''
Get 和 Post 请求
'''

# get 请求
# keyword = "hello"
# keycode = urllib.request.quote(keyword)
# url = "http://www.baidu.com/s?wd=" + keycode
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()
# fHandle = open("exec/part1/3.html", "wb")
# fHandle.write(data)
# fHandle.close()


# Post 请求
postUrl = "https://newdaichao.test.jinyinduo.com/mall/bonus/send"
postData = urllib.parse.urlencode({
    "bounsType": "INTEREST_FREE_100"
}).encode("utf-8")

req1 = urllib.request.Request(postUrl, postData)
req1.add_header("Authorization", "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDkiLCJhdXRoIjoiUk9MRV9VU0VSIiwiZXhwIjoxNTU5ODkxOTU5fQ.ZmbhbSAHdzixPRLzYb-HLP5xpKSzlOC7H83IIZDQn6WTXRCFb2azRHIisJKQVCq8O_82Gistqhbwg0LC8demHw")
req1.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
data1 = urllib.request.urlopen(req1).read()
fHandl1 = open("exec/part1/4.html", "wb")
fHandl1.write(data1)
fHandl1.close()
