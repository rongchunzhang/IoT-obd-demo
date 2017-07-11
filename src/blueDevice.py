##import subprocess
##
##subprocess.call("rfcomm", "release rfcomm0")
##
##subprocess.call("rfcomm connect rfcomm0 00:1D:A5:00:10:4A 1")
import os
os.system("sudo rfcomm release rfcomm0")
os.system("sudo rfcomm connect rfcomm0 00:1D:A5:00:10:4A 1")
