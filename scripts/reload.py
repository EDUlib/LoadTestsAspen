#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import os
import re
import codecs
import sys
import unicodedata
from datetime import datetime

#
# Files to be used
#

NEWUSERSFILE = "/home/ubuntu/toto.txt"

#
# Open the users file
#

newusers = codecs.open(NEWUSERSFILE, "w+", "utf-8")

#
# connecting to the MySQL database
# DO NOT FORGET TO CHANGE THE ADDRESS OF THE DATABASE WHEN NEEDED (localhost or backend IP)
#

#db = MySQLdb.connect(host="10.0.1.212", user="edxapp001", passwd="password", db="edxapp", use_unicode=True, charset="utf8")
#cursor = db.cursor()
#cursor.execute("set names 'utf8'")

#
# creating user in edX
#
start = 1000
end = 5000
#edx_course = "edX/Open_DemoX/edx_demo_course"
#newpassword = "pbkdf2_sha256$10000$OFkE9agOumMK$XUCT1ez+k3iC8bAC4ig3W+00yoenrUeEduYdzvrHSqs="
password = "user0500"
firstname = "user"
lastname = ""

while start < end:

   username = 'user'+str(start)
   email = username+'@fake.com'
   lastname = str(start)


   #command = "cd /edx/app/edxapp/edx-platform ; sudo -u www-data /edx/bin/python.edxapp ./manage.py lms --settings aws create_user --name=\"%s\" --email='%s' --username=\"%s\" --course='%s'" % (username, email, username, edx_course)

   #try:
   #   result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
   #   start += 1 
   #except subprocess.CalledProcessError as grepexc:
   #   print "error code", grepexc.returncode, grepexc.output
   #   start += 1 
   #   continue

   start += 2

   #cursor.execute("UPDATE auth_user SET password=%s WHERE username=%s", (newpassword, username));

   newusers.write(username+','+password+'\n')

   #db.commit()

#
# closing the newusers file
#

newusers.close()
