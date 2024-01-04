PYTHON	=	python3

webui:
	@${PYTHON} scripts/main.py --port 3001 --listen --api

no-webui:
	@${PYTHON} scripts/main.py --nowebui --port 3001 --listen --api

init:
	@${PYTHON} scripts/init.py
