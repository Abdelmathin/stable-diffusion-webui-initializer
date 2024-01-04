echo "**** syncing venv to workspace, please wait. This could take a while on first startup! ****"
rsync --remove-source-files -rlptDu --ignore-existing /venv/ /workspace/venv/

cd /workspace/stable-diffusion-webui-initializer/
make init
make webui &

# rm -rf /stable-diffusion-webui
# ln -s /sd-models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
# ln -s /cn-models/* /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/

cd /workspace/stable-diffusion-webui-initializer/outputs/
python3 -m http.server 3003 &
#
#
cd  /workspace/bed-story-front-end
make dev &


# echo "**** syncing venv to workspace, please wait. This could take a while on first startup! ****"
# rsync --remove-source-files -rlptDu --ignore-existing /venv/ /workspace/venv/

# echo "**** syncing stable diffusion to workspace, please wait ****"
# rsync --remove-source-files -rlptDu --ignore-existing /stable-diffusion-webui/ /workspace/stable-diffusion-webui/
# ln -s /sd-models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
# ln -s /cn-models/* /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/

# if [[ $RUNPOD_STOP_AUTO ]]
# then
#     echo "Skipping auto-start of webui"
# else
#     echo "Started webui through relauncher script"
#     cd /workspace/stable-diffusion-webui
#     python relauncher.py &
# fi
