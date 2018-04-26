# -*- coding:utf-8 -*-
import re

with open('javlab.html','rb') as f:
    data = f.read()

#获取番号、片名、演员、图片
#re.S，.也可以表示换行符
#.*?任意多字符，非贪婪模式
#avpattern = re.compile(r'.*?vid_jav.*?href="(.*?)".*?title="(.*?)">.*?src="(.*?)".*?', re.S)

def getav(data):
    avpattern = re.compile(r'.*?vid_jav.*?href="(.*?)".*?"id">(.*?)<.*?src="(.*?)".*?class="title".*?>(.*?)</.*?', re.S)
    items = re.findall(avpattern,data)
    for item in items:
        print "详细内容链接: %s" % item[0]
        print "番号: %s" % item[1]
        print "描述: %s" % item[3]
        print "图片链接: %s" % item[2]
        print "----------------------"

if __name__ == "__main__":
    getav(data)
