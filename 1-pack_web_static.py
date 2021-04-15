#!/usr/bin/python3
""" Simple Module containing a do_pack function """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p versions")
    now = datetime.today()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                             now.month,
                                                             now.day,
                                                             now.hour,
                                                             now.minute,
                                                             now.second)
    try:
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None
