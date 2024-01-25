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