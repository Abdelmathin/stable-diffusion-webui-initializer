import os
ROOT_DIR        = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)

cmd = (
'''
echo "Starting your application..."
cd  {0}/bed-story-front-end
make dev &

echo "Starting watcher..."
cd {0}/stable-diffusion-webui-initializer/outputs/
python3 -m http.server 3003 &

echo "Starting stable-diffusion-webui..."
cd {0}/stable-diffusion-webui-initializer/
make init
make webui &
echo "donne"
'''.format(ROOT_PARENT_DIR).strip())

os.system(cmd)