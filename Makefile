PYTHON	=	python3

webui:
	@${PYTHON} scripts/main.py --port 80 --listen

no-webui:
	@${PYTHON} scripts/main.py --nowebui --port 80 --listen
