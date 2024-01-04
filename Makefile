PYTHON	=	python3

start:
	@cd ../stable-diffusion-webui
	@${PYTHON} relauncher.py &

webui:
	@${PYTHON} scripts/main.py --port 3001 --listen --api

no-webui:
	@${PYTHON} scripts/main.py --nowebui --port 3001 --listen --api

init:
	@${PYTHON} scripts/init.py


