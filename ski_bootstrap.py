#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
cgitb.enable()


print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print(" <title>Glencoe Ski Resort</title>")
print("<meta charset='utf-8'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1'>")
print("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>")
print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>")
print("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>")
print("<style>")
#Remove the navbar's default margin-bottom and rounded borders 
print(".navbar {")
print(" margin-bottom: 0;")
print(" border-radius: 0;")
print(" }")
    
#Set height of the grid so .sidenav can be 100% (adjust as needed)
print(".row.content {height: 1363px}")
    
#Set pink background color and 100% height
print(".sidenav {")
print(" padding-top: 20px;")
print("background-color: rgba(243,244,246,0.5);")
print("height: 100%;")
print("}")

#set background photo
print('body {')
print('margin: 0;')
print('height: 1363px;')
print('background-image: url(https://www.visitscotland.com/cms-images/active/489308/cairngorms-ski-pass);')
print('background-size: 100% 100%;')
print('}')
    
#Set black background color, white text and some padding
print("footer {")
print("background-color: #555;")
print("color: white;")
print(" padding: 15px;")
print("}")
    
#On small screens, set height to 'auto' for sidenav and grid
print(" @media screen and (max-width: 767px) {")
print(" .sidenav {")
print(" height: auto;")
print("  padding: 15px;")
print("}")
print(" .row.content {height:auto;} ")
print(" }")
print("</style>")
print("</head>")
print("<body>")

print("<nav class='navbar navbar-inverse'>")
print("<div class='container-fluid'>")
print("<div class='navbar-header'>")
print("<button type='button' class='navbar-toggle' data-toggle='collapse' data-target='#myNavbar'>")
print("<span class='icon-bar'></span>")
print(" <span class='icon-bar'></span>")
print("<span class='icon-bar'></span>")                        
print("</button>")
#adds the edinburgh logo in top left
print("<a class='navbar-brand active' href='https://www.geos.ed.ac.uk/~s1712855/cgi-bin/ski_bootstrap.py'><img src='../logo2.png'style='width: 150px; height: 35px'></a>")				
print("</div>")


print("<div class='collapse navbar-collapse' id='myNavbar'>")
print(" <ul class='nav navbar-nav'>")
print(" <li class='active'><a href='https://www.geos.ed.ac.uk/~s1712855/cgi-bin/ski_bootstrap.py'>Home</a></li>")
print("<li><a href='https://www.ed.ac.uk/student-administration/timetabling/students/timetabling-systems/my-timetable'>Timetable</a></li>")
print("<li><a href='http://www.glencoemountain.co.uk/accommodation/'>Accomodation</a></li>")
print(" <li><a href='http://www.glencoemountain.co.uk/winter/'>Activity</a></li>")
print("</ul>")
print("<ul class='nav navbar-nav navbar-right'>")
print("<li><a href='#'><span class='glyphicon glyphicon-log-in'></span> Login</a></li>")
print("</ul>")
print("</div>")
print("</div>")
print("</nav>")
  
print("<div class='container-fluid text-center'>")    
print("<div class='row content'>")
print("<div class='col-sm-2 sidenav'>")
print(" <p><a href='#'>Link</a></p>")
print(" <p><a href='#'>Link</a></p>")
#create a button absolute linking to ski map
print('<div class="buttons"><button type="button" class="btn btn-warning btn-lg"><a href="https://www.geos.ed.ac.uk/~s1712855/cgi-bin/skimap.py"<p style="color: #336699;font-size:18px;">Ski Map</p></a></button></div>')
#create an empty line
print("&nbsp;")
#create a button absolute linking to reference
print('<div class="buttons"><button type="button" class="btn btn-warning btn-lg"><a href="https://www.geos.ed.ac.uk/~s1712855/cgi-bin/reference.py"<p style="color: #336699;font-size:18px;">Reference</p></a></button></div>')
print(" </div>")
print(" <div class='col-sm-8 text-left'>") 
#words
print("  <h1>Welcome to Glencoe Ski Resort</h1>")
print(" <p>Enchanted places and vibrant spaces for one and all.</p>")
print(" <p>Mountainous all-season highland resort with snow sports, walking and biking trails and archery.</p>")
#create an empty line
print("<hr>")
#words
print("<h3>A Map</h3>")
print("<p>map description</p>")
print("</div>")
print("<div class='col-sm-2 sidenav'>")
print("<div class='well'>")
print("<p>Opening Hours</p>")
print("<p>8:00-22:00</p>")
print("</div>")
print(" <div class='well'>")
print(" <p>How to contact us</p>")
print("<p>s1712855@sms.ed.ac.uk</p>")
print("</div>")
print(" </div>")
print("</div>")
print("</div>")

#create a footer
print("<footer class='container-fluid text-center'>")
#create a copyright label
print("<p>Copyright 2018 by Institute of Geography. All right reserved.</p>")
#tele number and adress
print("<p>Make a reservation:s1712855@sms.ed.ac.uk Address:9d Holyrood Road</p>")
print("</footer>")

print("</body>")
print("</html>")

