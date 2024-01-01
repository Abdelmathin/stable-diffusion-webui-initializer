import os
ST_REPO_URL     = "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"
CVT_REPO_URL    = "https://github.com/Abdelmathin/civitai-models-downloader.git"
ROOT_DIR        = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)
ST_DIR          = ROOT_PARENT_DIR + "/stable-diffusion-webui"
CVT_DIR         = ROOT_PARENT_DIR + "/civitai-models-downloader"
commands = [
	"sudo apt-get update",
	"sudo apt-get install pip",
	'''cd "''' + ROOT_PARENT_DIR + '''" && git clone "''' + ST_REPO_URL + '''"''',
	'''cd "''' + ROOT_PARENT_DIR + '''" && git clone "''' + CVT_REPO_URL + '''"'''
]

models = {
	"Stable-diffusion/sd_xl_base_1.0.safetensors"     : "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true",
	"Lora/picture-books-children-cartoon.safetensors" : "https://civitai.com/api/download/models/198105"
}

if (__name__ == "__main__"):
	for cmd in commands:
		os.system (cmd)
	for model_path, model_url in models.items():
		model_file = ST_DIR + "/models/" + model_path
		if not os.path.exists(model_file):
			os.system ('cd "' + CVT_DIR + '" && python3 script.py "' + model_url + '" "' + model_file + '"')
