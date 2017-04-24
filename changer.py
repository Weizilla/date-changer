import os
import sys
from os.path import join
from os import stat, utime
from datetime import datetime, timedelta

td = timedelta(days=365, hours=13)

def change(root_dir):
    for root, dirs, files in os.walk(root_dir):
        pics = [join(root, name) for name in files if name.endswith("JPG")]
        for pic in pics:
            m_time = stat(pic).st_mtime
            new_m_time = calc_time(m_time)
            o = datetime.fromtimestamp(m_time)
            n = datetime.fromtimestamp(new_m_time)
            utime(pic, (new_m_time, new_m_time))
            print(f"p: {pic} new: {n} old: {o}")

def calc_time(old):
    old_time = datetime.fromtimestamp(old)
    new_time = old_time + td
    return new_time.timestamp()


if __name__ == "__main__":
    change(sys.argv[1])
