import urllib.request
import urllib.error

'''
学习异常处理
'''

try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.HTTPError as e:
    print(e.reason)
    print(e.code)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print("code: " + e.code)
    if hasattr(e, "reason"):
        print("reason: " + e.reason)
