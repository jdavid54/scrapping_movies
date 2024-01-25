import requests
import re

print("Get xml ...")
url = 'https://raw.githubusercontent.com/tombebbs1/MagicDragonKodi18/main/newreleases1.xml'
response = requests.get(url)

print("Recompiling data ...")
HTML2 = response.content.decode("utf8")
match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)/fanart>',re.DOTALL).findall(str(HTML2))    
buffer = ''

for i,(name,url,image,fanart) in enumerate(match2[5:]):
    name = name.replace('[COLORwhite]','')
    name = name.replace('[/COLOR]','')
    #print(i,name)
    buffer += str(i+1)+' '+name+'\n'

with open('movies_listing.txt', 'w') as fp:
    fp.write(buffer)