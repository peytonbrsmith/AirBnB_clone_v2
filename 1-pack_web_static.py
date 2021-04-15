#!/usr/bin/python3
"""compress web_static directory
into tgz archive
"""

from fabric.operations import local
import time


def do_pack():
    localtime = time.localtime(time.time())
    if int(localtime.tm_mon) < 10:
        curmonth = "0{}".format(localtime.tm_mon)
    else:
        curmonth = localtime.tm_mon
    curtime = "{}{}{}{}{}{}".format(localtime.tm_year,
                                    curmonth, localtime.tm_mday,
                                    localtime.tm_hour, localtime.tm_min,
                                    localtime.tm_sec)
    archivepath = "versions/web_static_{}.tgz".format(curtime)
    archive = local("tar -cvzf {} web_static".format(archivepath),
                    capture=True)
    print(archive)
    return archivepath