
'''
代理使用
'''


def use_proxy(proxy_addr, url):
    import urllib.request
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpsh = urllib.request.HTTPSHandler(debuglevel=1)
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, httphd, httpsh)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


proxy_addr = "45.125.32.181:3128"
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))
