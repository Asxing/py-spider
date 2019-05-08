import urllib.request
import re

'''
正则抓数据,循环保存

抓取jd图片,保存本地
'''


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<ul class="gl-warp clearfix">.+? <div class="clr"></div>'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imageList = re.compile(pat2).findall(result1)
    x = 1
    for imageUrl in imageList:
        imagePath = "exec/part2/tmp01/" + str(page) + "-" + str(x) + ".jpg"
        if imageUrl.startswith("http"):
            print("image has no http profix")
        else:
            imageUrl = "http://" + imageUrl
        try:
            urllib.request.urlretrieve(imageUrl, filename=imagePath)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print("code: " + imageUrl)
            if hasattr(e, "reason"):
                print("reason: " + imagePath)
        x += 1


for i in range(1, 20):
    craw("http://list.jd.com/list.html?cat=9987,653,655&page="+str(1), 1)
