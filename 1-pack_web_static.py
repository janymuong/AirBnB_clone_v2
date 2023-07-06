#!/usr/bin/python3
'''module:
create tarball artifact of static files in local
'''

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''do_pack fabric:
    generates a .tgz archive from the contents of the web_static folder
    '''

    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    artifact = 'versions/web_static_{}.tgz'.format(now)
    local('mkdir -p versions')
    fab_stat = local('tar -czvf {} web_static'.format(artifact))
    if fab_stat.succeeded:
        size = os.path.getsize(artifact)
        print('web_static packed: {} -> {}Bytes'.format(artifact, size))
        return artifact
    else:
        return None
