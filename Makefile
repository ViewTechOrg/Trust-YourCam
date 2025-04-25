install:
	pkg update
	pkg upgrade
	apt-get install curl jq html2text xz-utils ncurses-utils nala
	apt-get install php cloudflared tree
	apt-get install boxes xh wget screen ruby neofetch
	apt-get install pv mpv python tmux bc
	pip install -r requirements.txt
	gem install lolcat
	@echo "[?] Paket berhasil di install"
	@echo "[?] tutor pakai ada di video resmi ViewTech Official"

clear:
	bash -c 'export MOD="clear";bash Server'
	tput reset
