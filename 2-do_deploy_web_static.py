#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """to distributes an archive to the web servers"""
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
