import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

# 读取文件
data = file.read()
# 文件信息
print(file.info())

# 获取 URL
file.geturl()

# 按行读取文件
datafile = file.readline()

print(datafile)
print(data)

# 打开文件 1.html
fHandle = open("1.html", "wb")
# 写入数据
fHandle.write(data)
fHandle.close()
