import os
from utils import *

CVT_REPO_URL    = "https://github.com/Abdelmathin/civitai-models-downloader.git"
ROOT_DIR        = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)

commands = [
	"sudo apt-get update",
	"sudo apt-get install pip",
	'''cd "''' + ROOT_PARENT_DIR + '''" && git clone "''' + CVT_REPO_URL + '''"'''
]

if (__name__ == "__main__"):
	for cmd in commands:
		os.system (cmd)

	for [model_url, model_dir] in [
			['https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true', "/stable-diffusion-webui/models/Stable-diffusion/sd_xl_base_1.0.safetensors"]
		]:

		os.system ('cd "' + ROOT_PARENT_DIR + '/civitai-models-downloader" && python3 script.py "' + model_url + '" "' + model_dir + '"')
