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

    dt_now = datetime.utcnow()

    artifact = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(dt_now.year,
                                                             dt_now.month,
                                                             dt_now.day,
                                                             dt_now.hour,
                                                             dt_now.minute,
                                                             dt_now.second)
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    fab_stat = local(f'tar -czvf {artifact} web_static')
    if fab_stat.succeeded:
        size = os.path.getsize(artifact)
        print(f'web_static packed: {artifact} -> {size}Bytes')
        return artifact
    else:
        return None
