import os
import sys
import subprocess
from utils import *

def get_public_ip():
	result = subprocess.run("curl ifconfig.me", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	return (result.stdout)

def get_local_ip():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.connect(("8.8.8.8", 80))
		public_ip = sock.getsockname()[0]
		return str(public_ip)
	except:
		pass
	return ("0.0.0.0")

if (__name__ == "__main__"):
	print ("YOUR PUBLIC IP: " + str(get_public_ip()))
	print ("YOUR LOCAL IP : " + str(get_local_ip()))
	args = " ".join(sys.argv[1:])
	cmd = (
'''
export COMMANDLINE_ARGS="--skip-torch-cuda-test --upcast-sampling --no-half-vae --use-cpu interrogate"
python3 "''' + get_stable_diffusion_webui_dir() + '''/launch.py" ''' + args
)
	cmd = cmd.strip()
	os.system(cmd)
