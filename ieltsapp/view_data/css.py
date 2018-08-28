
class NaCss(object):
    def table(self):
        css = []
        css.append("table, th, td {")
        css.append("border: none;")
        css.append("border-collapse: collapse;")
        css.append("border-spacing: 5px;")
        css.append("}")
        return css
    def li(self):
        css = []
        css.append(".li-menu {")
        #css.append("margin-left: -1.5em;")
        css.append("}")
        return css
    def floating(self):
        css = []
        css.append(".floating-text {")
        css.append("float: left;")
        css.append("width: 500px;")
        css.append("height: 75px;")
        css.append("min-height:300px")
        css.append("}")
        css.append(".floating-box {")
        css.append("float: left;")
        css.append("background-color:powderblue;")
        css.append("width: 250px;")
        css.append("height: 75px;")
        css.append("margin: 10px;")
        css.append("display: grid;")
        css.append("min-height:300px")
        css.append("}")
        css.append(".floating-content {")
        css.append("float: left;")
        css.append("background-color:powderblue;")
        css.append("width: 900px;")
        css.append("height: 75px;")
        css.append("margin: 10px;")
        #css.append("border: 3px solid #73AD21;")
        css.append("display: grid;")
        css.append("min-height:300px")
        #css.append("border-radius: 50%;")
        css.append("}")
        css.append(".floating-inside {")
        css.append("float: left;")
        css.append("background-color:#73EE21;")
        css.append("width: 100px;")
        css.append("height: 55px;")
        css.append("margin: 5px;")
        #css.append("display: inline-block;")
        css.append("min-height:100px")
        css.append("}")
        css.append(".floating-inside-clear {")
        css.append("float: left;")
        css.append("background-color:#73EE21;")
        css.append("width: 100px;")
        css.append("height: 55px;")
        css.append("margin: 10px;")
        css.append("display: grid;")
        css.append("min-height:100px")
        css.append("}")
        css.append(".floating-clear {")
        css.append("clear: left;")
        css.append("min-height:10px")
        css.append("}")
        return css
    def city(self):
        css = []
        css.append(".city {")
        css.append("background-color: white;")
        css.append("color: white;")
        css.append("padding: 10px;")
        css.append("font-family: verdana;")
        css.append("color: SlateBlue;")
        css.append("}")
        css.append(".on_normal_1{")
        css.append("float: left;")
        css.append("width: 900px;")
        css.append("background-color:powderblue;") 
        css.append("text-align: center;	")
        css.append("min-height:150px")
        css.append("}")
        css.append(".on_normal_2{")
        css.append("float: left;")
        #css.append("background-color:#55FF21;")
        css.append("background-color:#f8f8f8;")
        css.append("background-color:#C9F0DD;")
        css.append("text-align: center;	")
        css.append("width: 150px;")
        css.append("min-height:150px;")
        css.append("color:#0C3C26;")
        css.append("}")
        css.append(".on_normal_3{")
        css.append("clear: left;")
        css.append("background-color:lightgrey;")
        css.append("text-align: center;	")
        css.append("color: #ECECEC;")
        css.append("}")
        return css
    def style(self):
        css = []
        css.append("<style>")
        css.extend(self.city())
        css.extend(self.floating())
        css.extend(self.li())
        css.extend(self.table())
        css.append("</style>")
        return css
    def head(self):
        css = []	
        css.append("<head>") 
        css.extend(self.style())
        css.append("</head>")
        return css

class NaResponse(object):
    def go_home(response):
        css = NaCss().head()
        for one_css in css:
            response.write(one_css)
        response.write("<div class=""on_normal_2"">")
        response.write("Logo")
        response.write("</div>")
        response.write("<div class=""on_normal_1"">")
        response.write("<li class=""li-menu""><a href=""/"">Go back home</a> </li>")
        response.write("<li class=""li-menu""><a href=""/reading"">Reading</a> </li>")
        response.write("<li class=""li-menu""><a href=""/writing"">Writing</a> </li>")
        response.write("</div>")
        response.write("<div class=""on_normal_2"">")
        response.write("<li class=""li-menu""><a href=""/"">Book</a> </li>")
        response.write("<li class=""li-menu""><a href=""/reading"">Green</a> </li>")
        response.write("<li class=""li-menu""><a href=""/writing"">Grow</a> </li>")
        response.write("<table>")
        response.write("</table>")
        response.write("</div>")
        response.write("<div class=""on_normal_3"">")
        response.write("Read books then go home")
        response.write("</div>")
    def current_datetime(request):
        now = datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        # My first name is {{ first_name }}. My last name is {{ last_name }}.
        return html