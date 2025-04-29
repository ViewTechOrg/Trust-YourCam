install:
	pkg update -y
	pkg upgrade -y
	pkg install curl jq html2text cloudflared bash -y
	pkg install boxes xh wget screen ruby neofetch figlet -y
	pkg install pv mpv python tmux bc php toilet tree -y
	pkg install ncurses-utils cowsay -y
	gem install lolcat
	pip install -r requirements.txt
	@echo "\033[1;32m[✓] Paket berhasil diinstall\033[0m"
	@echo "\033[1;34m[?] Tutor pakai ada di video resmi ViewTech Official\033[0m"
	@termux-open-url "https://youtu.be/KCg2qnYJEkk?si=k1BPmvKvctV7EJ_E"
build:
	@echo "\033[1;33m[?] Menyiapkan Program\033[0m"
	@sleep 1
	bash -c "export MOD='window';bash Server"

stop:
	@echo "\033[1;31m[?] Shutdown Program\033[0m"
	bash -c "export MOD='clear';bash Server"

update:
	bash -c "export MOD='update';bash Server"

define help
	@clear
	@cowsay -f eyes "Trust YourCam" | lolcat
	@echo
	@echo "\033[1;36mmake help\033[0m"
	@echo "│"
	@echo "├───► make install"
	@echo "├───► make build"
	@echo "├───► make stop"
	@echo "└───► make update"
endef

help:
	$(call help)
