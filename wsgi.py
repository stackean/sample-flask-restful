#!/usr/bin/python
import sys
# working directory
sys.path.insert(0,"/var/www/webroot/ROOT/")
# write app name after from. for example if it is hello.py then write hello
from app import app as application
