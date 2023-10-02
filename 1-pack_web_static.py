#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    try:
        ourdate = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filenames = "versions/web_static_{}.tgz".format(ourdate)
        local("tar -cvzf {} web_static".format(filenames))
        return filenames
    except:
        return None
