import os

f = open("/etc/rc.local/RoboGUI.sh", "wr+")

f.write("python /home/student/RoboGUI/host.py &")

os.chmod("RoboGUI.sh", 0o755)
