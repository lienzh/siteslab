# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import time
 
url = 'http://www.javlibrary.com/tw/vl_bestrated.php?&mode=&page='
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

def getdata(url=url, headers=headers, page=2):
    try:
        request = urllib2.Request(url+str(page),headers = headers)
        response = urllib2.urlopen(request)
        with open('file.txt','wb') as f:
            f.write(response.read())
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
    	    print e.reason


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
#    getdata()
#    with open('file.txt','rb') as f:
#        data = f.read()
#    getav(data)
    for i in range(5):
        if i > 0:
            print "+++++++======================++++++++"
            print u"第 %s 页" % str(i)
            getdata(page=i)
            with open('file.txt','rb') as f:
                data = f.read()
            getav(data)
            time.sleep(10)
