#!/usr/bin/python3
'''module:
create tarball artifact of static files in local
'''

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''function:
    generates a .tgz archive from the contents of the web_static folder
    '''
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    archive_path = f'versions/web_static_{now}.tgz'
    print(f'Packing web_static to {archive_path}')
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    fab_stat = local(f'tar -cvzf {archive_path} web_static')
    if fab_stat.succeeded:
        size = os.path.getsize(archive_path)
        print(f'web_static packed: {archive_path} -> {size}Bytes')
        return archive_path
    else:
        return None
