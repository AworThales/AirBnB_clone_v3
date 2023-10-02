#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from datetime import datetime
from fabric.api import env, local, put, run
from os.path import exists, isdir
env.hosts = ['142.44.167.228', '144.217.246.195']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filenames = archive_path.split("/")[-1]
        no_ext = filenames.split(".")[0]
        path_url = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path_url, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filenames, path_url, no_ext))
        run('rm /tmp/{}'.format(filenames))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_url, no_ext))
        run('rm -rf {}{}/web_static'.format(path_url, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path_url, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
