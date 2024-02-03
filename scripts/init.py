import os
import utils
import config
import requests

ST_REPO_URL        = "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"
CVT_REPO_URL       = "https://github.com/Abdelmathin/civitai-models-downloader.git"
INSTANTID_REPO_URL = "https://github.com/InstantID/InstantID.git"
ROOT_DIR           = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT_PARENT_DIR    = os.path.dirname(ROOT_DIR)
ST_DIR             = ROOT_PARENT_DIR + "/stable-diffusion-webui"
CVT_DIR            = ROOT_PARENT_DIR + "/civitai-models-downloader"
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

def change_output_image_prefix(default = "img"):
	filename = ST_DIR + "/modules/images.py"
	content  = ""
	for line in open(filename):
		magic_key = '''if basename == '' else f"{basename}-{basecount + i:04}"'''
		if magic_key in line:
			_line = line.strip().replace(" ", "")
			if _line.startswith("fn="):
				tabs = line[:line.index("fn")]
				line = tabs + 'fn = ' + "os.environ.get('OUTPUT_IMAGE_PREFIX', '" + default + "')" + ' #' + magic_key + "\n"
		content += line
	with open(filename, "w") as fp:
		fp.write(content)

def change_outputs_dirname():
	filename = ST_DIR + "/modules/images.py"
	content  = ""
	for line in open(filename):
		magic_key = '''dirname = namegen.apply(opts.directories_filename_pattern'''
		if magic_key in line:
			_line = line.strip().replace(" ", "")
			if _line.startswith("dirname="):
				tabs = line[:line.index("dirname")]
				line = tabs + 'dirname = ' + "os.environ.get('DIRECTORIES_FILENAME_PATTERN', '')" + ' # ' + magic_key + "\n"
		content += line
	with open(filename, "w") as fp:
		fp.write(content)

def change_relauncher():
	content = open(ROOT_DIR + "/scripts/relauncher.py").read()
	with open(ST_DIR + "/relauncher.py", "w") as fp:
		fp.write(content)

def clone_instant_id():
	stable_diffusion_directory = utils.get_stable_diffusion_webui_dir()
	instantid_directory        = utils.join_path(stable_diffusion_directory, "InstantID")
	instantid_clone_command    = "git clone '{0}' '{1}'".format(INSTANTID_REPO_URL, instantid_directory)
	instantid_models_directory = utils.join_path(instantid_directory, "models")
	os.system(instantid_clone_command)
	utils.create_directory(instantid_models_directory)
	antelopev2_content = requests.get("https://drive.usercontent.google.com/download?id=18wEUfMNohBJ4K3Ly5wpTejPfDzp-8fI8&export=download&authuser=0&confirm=t&uuid=a77d00b9-9fc5-46d6-98c0-cf1e24d366d4&at=APZUnTVwBOWdw7amPPudnhJc6LOk%3A1706999007535").content
	antelopev2_zip     = utils.join_path(instantid_models_directory, "antelopev2.zip")
	with open(antelopev2_zip, "wb") as fp:
		fp.write(antelopev2_content)
	os.system ("cd '" + str(instantid_models_directory) + "' && unzip antelopev2.zip")

clone_instant_id()

exit()

if (__name__ == "__main__"):
	change_relauncher()
	for cmd in commands:
		os.system (cmd)
	for model_path, model_url in models.items():
		model_file = ST_DIR + "/models/" + model_path
		if not os.path.exists(model_file):
			os.system ('cd "' + CVT_DIR + '" && python3 script.py "' + model_url + '" "' + model_file + '"')
	change_output_image_prefix()
	change_outputs_dirname()
