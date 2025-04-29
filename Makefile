install:
	pkg update
	pkg upgrade
	apt-get install curl jq html2text cloudflared bash
	apt-get install boxes xh wget screen ruby neofetch figlet
	apt-get install pv mpv python tmux bc php toilet tree
	pkg install ncurses-utils
	pip install -r requirements.txt
	gem install lolcat
	@echo "\033[1;32m[?] Paket berhasil di install\033[0m"
	@echo "\033[1;34m[?] Tutor pakai ada di video resmi ViewTech Official\033[0m"

build:
	@echo "\033[1;33m[?] Menyiapkan Program\033[0m"
	@sleep 1
	bash -c "export MOD='window';bash Server"

stop:
	@echo "\033[1;31m[?] Shutdown Program\033[0m"
	bash -c "export MOD='clear';bash Server"

update:
	bash -c "export MOD='update';bash Server"

help:
        clear
	@echo "\033[1;36mmake help\033[0m"
	@echo "│"
	@echo "├───► make install"
	@echo "├───► make build"
	@echo "├───► make stop"
	@echo "└───► make update"
