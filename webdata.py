# -*- coding:utf-8 -*-
import urllib
import urllib2
 
#url = 'http://www.javlibrary.com/tw/vl_bestrated.php'
#url = 'http://www.cool18.com/bbs4/index.php'
url ='http://g.91p11.space/viewthread.php?tid=272348'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
#    print response.read()
    with open('file.txt','wb') as f:
        f.write(response.read())
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
	print e.reason
