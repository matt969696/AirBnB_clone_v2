#!/usr/bin/python3
""" Simple Module containing a do_deploy function """
from datetime import datetime
from fabric.api import local, run, put, sudo, env
from os import path
env.hosts = ['34.75.232.143', '34.75.165.238']


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


def do_deploy(archive_path):
    """ distributes an archive to web servers"""
    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        dirpath = archive_path.split("/")[1].split(".")[0]
        sudo("mkdir -p /data/web_static/releases/{}/".format(dirpath))
        filepath = archive_path.split("/")[1]
        datapath = "/data/web_static/releases/{}".format(dirpath)
        sudo("tar -xvzf /tmp/{} -C {}".format(filepath, datapath))
        sudo("rm -rf /tmp/{}".format(filepath))
        sudo("mv {}/web_static/* {}".format(datapath, datapath))
        sudo("rm -rf {}/web_static".format(datapath))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(datapath))
        return True
    except:
        return False


def deploy():
    """ full creation and deployment"""
    filename = do_pack()
    if filename is None:
        return False
    return do_deploy(filename)
