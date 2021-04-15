#!/usr/bin/python3
""" Simple Module containing a do_clean function """
import os
from fabric.api import *
env.hosts = ['34.75.232.143', '34.75.165.238']


def do_clean(number=0):
    """ Cleans old versions locally and on servers"""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    locarch = sorted(os.listdir("versions"))
    [locarch.pop() for i in range(number)]
    with lcd("versions"):
        for a in locarch:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        distarch = run("ls -tr").split()
        distarch = [a for a in distarch if "web_static_" in a]
        [distarch.pop() for i in range(number)]
        for a in distarch:
            run("rm -rf ./{}".format(a))
