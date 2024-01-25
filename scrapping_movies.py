import requests
import re

print("Get xml ...")
url = 'https://raw.githubusercontent.com/tombebbs1/MagicDragonKodi18/main/newreleases1.xml'
response = requests.get(url)

print("Recompiling data ...")
HTML2 = response.content.decode("utf8")
match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)/fanart>',re.DOTALL).findall(str(HTML2))    

def new_render(url, name):
    name = name.replace('[COLORwhite]','')
    name = name.replace('[/COLOR]','')
    #url = url.split('\r\n')
    urls = re.compile('<sublink>(.+?)</sublink>',re.DOTALL).findall(url)
    result = ''
    for u in urls:
        #print(u,name)
        u=re.sub(r'[^\x00-\x7F]','', u)
        try:
            href, label = u.split('(',1)
        except:
            href, label = u, 'Trailer_'
        link = '<a href="'+href+'">'+label[:-1]+'</a><br>'
        result += link
    return result, name

#headers
from headers import buffer

# show result
print(len(match2), 'free movies')

# get n movies and create html page
n = len(match2)
for i,(name,url,image,fanart) in enumerate(match2[:n+1]):
    #print(name,url,image,fanart)
    if i%10==0: print('\r',i,'/',n,end='')
    if '<sublink>' in url: 
            if fanart == '<':
                fanart = FANART
            else:
                fanart = fanart.replace('<','')
                         
                url, name = new_render(url, name)
                url = name + '<br>' + url
                # is image link valid ?
                try:
                    response = requests.get(image)
                    #print(response)
                    if response.status_code != 200:
                        no_image = True
                        n+=1
                        #replace invalid link image
                        image='https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
                    else:
                        no_image = False
                except:                    
                    no_image = True
                    #replace invalid image
                    image='https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
               
                buffer+='<figure class="swap-on-hover">'
                buffer+='<img class="swap-on-hover__front-image" src="'+image+'"/>'
                buffer+='<div class="swap-on-hover__back-image">'+url+'</div> </figure>\n'                                                               
    #print(buffer)
buffer += '</body></html>'
#buffer=buffer.replace('┊','')   # error charmap   
# saving
print("\nSaving html page ...")
with open('test.html', 'w') as fp:
    fp.write(buffer)
