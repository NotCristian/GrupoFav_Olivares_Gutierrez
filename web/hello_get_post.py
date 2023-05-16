#!/usr/bin/env python3

import cgi
import cgitb
import os


cgitb.enable()

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')


print("Content-Type: text/html; charset=utf-8")
print("Content-type:text/html\r\n")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<title>Hello - get CGI Program</title>")
print("</head>")
print("<body>")
print("<form action='/cgi-bin/hello_get.py' method='post'>")
#print("<form action='https://www.youtube.com/watch?v=dQw4w9WgXcQ' method='post'>")
print("<label class='form-label'>First Name: </label>")
print("<input class='form-control' type='text' name='first_name'><br />")
print("<label class='form-label'>Last Name: </label>")
print("<input class='form-control' type='text' name='last_name' id=''/>")
print("<input class='btn btn-primary' type='submit' value='Submit' />")
print("</form>")
print("</body>")
print("</html>")
