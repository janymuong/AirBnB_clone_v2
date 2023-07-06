#!/usr/bin/python3
'''module:
create tarball artifact of static files in local
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''do_pack fabric:
    generates a .tgz archive from the contents of the web_static folder
    '''

    now = datetime.now().strftime('%Y%m%d%H%M%S')

    artifact = f'versions/web_static_{now}.tgz'
    local('mkdir -p versions')
    fab_stat = local(f'tar -czvf {artifact} web_static')
    return artifact if fab_stat.succeeded else None
