import os
import sys

def getlistdir(dirname, callback = None):
	files = []
	try:
		for basename in os.listdir(dirname):
			if callback:
				files.append(callback(basename))
			else:
				files.append(basename)
	except:
		pass
	return (files)

def get_stable_diffusion_webui_dir():
	path = "."
	for i in range(10):
		path += "/.."
		for dirname in os.listdir(path):
			directory = path + "/" + dirname
			files = getlistdir(directory, str.lower)
			if ("launch.py" in files) and ("models" in files):
				models = getlistdir(directory + "/models", str.lower)
				if ("stable-diffusion" in models):
					return (directory)
	return (None)

if (__name__ == "__main__"):
	args = " ".join(sys.argv[1:])
	cmd = (
'''
export COMMANDLINE_ARGS="--skip-torch-cuda-test --upcast-sampling --no-half-vae --use-cpu interrogate"
python3 "''' + get_stable_diffusion_webui_dir() + '''/launch.py" ''' + args
)
	cmd = cmd.strip()
	os.system(cmd)
