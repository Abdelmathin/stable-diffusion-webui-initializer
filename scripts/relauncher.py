import os
WORKSPACE_DIR = "/workspace"

cmd = (
'''

echo "Init stable-diffusion-webui..." && cd "''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/" && make init

echo "Starting your application..." && cd  ''' + WORKSPACE_DIR + '''/bed-story-front-end && make dev &

mkdir -p ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/outputs/
echo "Starting watcher..." && cd ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/outputs/ && python3 -m http.server 3003 &

echo "Starting stable-diffusion-webui..." && cd ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/ && make webui &

'''.strip())

os.system(cmd)
