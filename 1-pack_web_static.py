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

    now = datetime.utcnow()
    artifact_name = 'web_static_' + now.strftime('%Y%m%d%H%M%S') + '.tgz'
    artifact_path = 'versions/' + artifact_name

    if not os.path.exists('versions'):
        local('mkdir -p versions')

    result = local('tar -cvzf {} web_static'.format(artifact_path))
    if result.failed:
        return None

    size = os.path.getsize(artifact_path)
    print('web_static packed: {} -> {}Bytes'.format(artifact_path, size))
    return artifact_path
