import os
import time

WORKSPACE_DIR = "/workspace"

launch_string = (
'''

rm -rf /sd-models
rm -rf /cn-models
rm -rf /stable-diffusion-webui

echo "Init stable-diffusion-webui..." && cd "''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/" && make init

echo "Starting your application..." && cd  ''' + WORKSPACE_DIR + '''/bed-story-front-end && make dev &

mkdir -p ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/outputs/
echo "Starting watcher..." && cd ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/outputs/ && python3 -m http.server 3003 &

echo "Starting stable-diffusion-webui..." && cd ''' + WORKSPACE_DIR + '''/stable-diffusion-webui-initializer/ && make webui

'''.strip())

def relaunch_process(launch_counter=0):
	while True:
		print("- -" * 20)
		print("Relauncher: Launching...")
		if launch_counter > 0:
			print("\tRelaunch count: " + str(launch_counter))
		try:
			os.system(launch_string)
		except Exception as err:
			print("An error occurred: ", err)
		finally:
			print(">>>>>>>>>>>>>>>>>>>>>> Relauncher: Process is ending. Relaunching in 2s... <<<<<<<<<<<<<<<<<<<<<")
			launch_counter += 1
			time.sleep(2)

if __name__ == "__main__":
    relaunch_process()
