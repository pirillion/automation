import os
import subprocess
import time
import signal

SIGINT = 9
command = "ssh -v -p 22 localhost"
process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
time.sleep(3)
print("pid = ")
print(process.pid)
print("return code = ")
print(process.returncode)
os.kill(process.pid, signal.SIGINT)
print("data = ")
data = process.communicate()[0]
print(data)

