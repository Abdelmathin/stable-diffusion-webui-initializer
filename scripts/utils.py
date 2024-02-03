import os

__CACHE__ = {}

def create_directory(dirname):
	os.system ("mkdir -p '" + str(dirname) + "'")

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
	path      = "."
	directory = __CACHE__.get("stable-diffusion-directory", None)
	if not directory:
		for i in range(10):
			path += "/.."
			for dirname in os.listdir(path):
				directory = path + "/" + dirname
				files = getlistdir(directory, str.lower)
				if ("launch.py" in files) and ("models" in files):
					models = getlistdir(directory + "/models", str.lower)
					if ("stable-diffusion" in models):
						__CACHE__["stable-diffusion-directory"] = directory
						return (directory)
	return (directory)

def join_path(*args):
	path = ""
	args = list(args)
	if not args:
		return ("")
	for i in args[:-1]:
		path += i + "/"
	path += args[-1]
	while ("//" in path):
		path = path.replace("//", "/")
	return (path)
