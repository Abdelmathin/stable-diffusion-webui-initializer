import os
ST_REPO_URL     = "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"
CVT_REPO_URL    = "https://github.com/Abdelmathin/civitai-models-downloader.git"
ROOT_DIR        = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)

commands = [
	'''cd "''' + ROOT_PARENT_DIR + '''" && git clone "''' + ST_REPO_URL + '''"''',
	'''cd "''' + ROOT_PARENT_DIR + '''" && git clone "''' + CVT_REPO_URL + '''"'''
]

if (__name__ == "__main__"):
	for cmd in commands:
		os.system (cmd)
