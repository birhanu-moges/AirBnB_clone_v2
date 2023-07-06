#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""
from os import path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["34.231.110.206", "3.239.57.196"]


def do_pack():
    """
    A function that generates an archive
    """
    date = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day,
        date.hour, date.minute, date.second
    )
    if not path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    cmd = "cd web_static && tar -cvzf ../{} . && cd -".format(archive)
    if local(cmd).succeeded:
        return archive
    return None
