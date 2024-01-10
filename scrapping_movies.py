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
        try:
            href, label = u.split('(',1)
        except:
            href, label = u, 'Trailer_'
        link = '<a href="'+href+'">'+label[:-1]+'</a><br>'
        result += link
    return result, name

# headers
buffer = '''<html><head><style>
body {
    background-color: #051465;
    box-sizing: border-box;
    font-family : sans-serif;
  
}

.swap-on-hover {
  position: relative;
  float : left;
  margin:  0 auto;
  max-width: 200px;
  text-transform: uppercase;
}

.swap-on-hover img {
  position: absolute;
  top:0;
  left:0;
  overflow: hidden;
  /* Sets the width and height for the images*/
  width: 200px;
  height: 300px;
}

.swap-on-hover .swap-on-hover__front-image {
  z-index: 9999;
  transition: .5s ease-in-out;
  cursor: pointer;
}

.swap-on-hover:hover > .swap-on-hover__front-image{
  opacity: 0;
  height : 0;
  transition: .5s ease-in-out;
}
.swap-on-hover:hover > .swap-on-hover__back-image{
  font-size: 15px;
	font-weight:bold;
  color: #ff9800;
  opacity : 1;
  transition: .5s ease-in-out;
}
.swap-on-hover__back-image {
  /*border: 1px solid lightgray;*/
  height : 288px;
  width : 188px;
  padding : 5px;
  font-family : tahoma;
  font-size : 50px;
  opacity : 0;
  transition: .5s ease-in-out;
  overflow : hidden;
}
p, hr {
	clear:both;
}

div {
	position:relative;
	float:left;
	width:50%;
	margin:0 auto;
}

a,i {
	color:white;
  padding-right: 20px;
  text-decoration:none;
  font-weight:normal;
	 font-size: 13px;
}

div, h1
{ color:#eff4f2;}


h1 {border:1px solid;
  text-align:center;
  background-color:#8b0221;
}

a:hover {
  font-size:larger;
}

figure {
  padding: 5px;
}</style></head>
<body>

<h1>Free movies
<br>Better viewed with Brave : https://brave.com/</h1>'''

# show result
print(len(match2), 'free movies')

# get n movies and create html page
n = 50
for name,url,image,fanart in match2[5:n]:
    #print(name,url,image,fanart)
    
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
    
# saving
print("Saving html page ...")
with open('movies.html', 'w') as fp:
    fp.write(buffer)
