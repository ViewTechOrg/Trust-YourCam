install:
	pkg update
	pkg upgrade
	apt-get install curl jq html2text cloudflared
	apt-get install boxes xh wget screen ruby neofetch
	apt-get install pv mpv python tmux bc
	pip install -r requirements.txt
	gem install lolcat
	@echo "[?] Paket berhasil di install"
	@echo "[?] tutor pakai ada di video resmi ViewTech Official"

build:
	@echo "[?] Menyiapkan Program"
	@sleep 1
	bash -c "export MOD='window';bash Server"

stop:
	@echo "[?] Shutdown Program"
	bash -c "export MOD='clear';bash Server"

update:
	bash -c "export MOD='update';bash Server"
help:
	@echo "make help"
	@echo "│"
	@echo "├───► make install"
	@echo "├───► make build"
	@echo "├───► make stop"
	@echo "└───► make update"
