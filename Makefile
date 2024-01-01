PYTHON	=	python3

webui:
	@${PYTHON} scripts/main.py --port 3002 --listen --api

no-webui:
	@${PYTHON} scripts/main.py --nowebui --port 3003 --listen --api

init:
	@${PYTHON} scripts/init.py
