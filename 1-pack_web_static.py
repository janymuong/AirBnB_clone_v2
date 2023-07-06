#!/usr/bin/python3
'''module:
create tarball artifact of static files in local
'''

from fabric.api import local
import time
import os


def do_pack():
    '''
    A function that generaees a .tgx archive from the web_static folder
    '''
    if not os.path.exists('versions'):
        os.makedirs('versions')

    filename = time.strftime("%Y%m%d%H%M%S")
    artifact = "versions/web_static_{}.tgz".format(filename)
    try:
        local("tar -cvzf {} web_static".format(artifact))
        return artifact
    except Exception:
        return None
