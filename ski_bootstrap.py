#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
cgitb.enable()
import resorts from .Geomlists.resorts as resorts

class webpage():
    def printer(self,name)
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
        print(".row.content {height: 450px}")
        
        #Set pink background color and 100% height
        print(".sidenav {")
        print(" padding-top: 20px;")
        print("background-color: rgba(254,67,101,0.5);")
        print("height: 100%;")
        print("}")
        
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
        print("<a class='navbar-brand' href='#'>Logo</a>")
        print("</div>")
        print("<div class='collapse navbar-collapse' id='myNavbar'>")
        print(" <ul class='nav navbar-nav'>")
        print(" <li class='active'><a href='#'>Home</a></li>")
        print("<li><a href='#'>About</a></li>")
        print("<li><a href='#'>Projects</a></li>")
        print(" <li><a href='#'>Contact</a></li>")
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
        print(" <ul>”)
        
        #Access Oracle from Python and make a database connection
        conn = cx_Oracle.connect("student/train@geosgen")
              #prepare and execute a query and display the results using a simple loop which returns each row in turn
        c = conn.cursor()
        c.execute("SELECT RESORT_NAME FROM RESORTS")
        for row in c:
        	print(" <p><a href='https://www.kfc.co.uk/'>", row(0), "</a></p>")
        conn.close()
        print ('<table>')
        for i in       
    
    
        print(" <p><a href='#'>Link</a></p>")“”“
     
          
          
          
          
          
        print(" </div>")
        print(" <div class='col-sm-8 text-left'>") 
        print("  <h1>Welcome</h1>")
        print(" <p>The resort is situated in an area of outstanding natural beauty on Rannoch Moor and offers stunning views of the iconic Buachaille Etive Mor. The onsite campsite boasts a large camping area, hook-ups and microlodges. In summer the centre offers chairlift rides, mountain biking (Downhill and XC), tubing, hill-walking, climbing,  photography and great home cooked &hellip.</p>")
        print("<hr>")
        print("<h3>Test</h3>")
        print(" <p>Lorem ipsum...</p>")
        print("</div>")
        print("<div class='col-sm-2 sidenav'>")
        print("<div class='well'>")
        print("<p>ADS</p>")
        print("</div>")
        print(" <div class='well'>")
        print(" <p>ADS</p>")
        print("</div>")
        print(" </div>")
        print("</div>")
        print("</div>")
    
        print("<footer class='container-fluid text-center'>")
        print("<p>Copyright 2018 by Institute of Geography. All right reserved.</p>")
        print("</footer>")
        
        print("</body>")    
        print("</html>")

