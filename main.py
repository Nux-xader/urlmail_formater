import sys, os

clr = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	print("""
 █░█ █▀█ █░░ █▀▄▀█ ▄▀█ █ █░░
 █▄█ █▀▄ █▄▄ █░▀░█ █▀█ █ █▄▄ V1.0.0

 █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █▀▀ █▀█
 █▀░ █▄█ █▀▄ █░▀░█ █▀█ ░█░ ██▄ █▀▄

 Coder by : https://github.com/Nux-xader
 Contact  : https://wa.me/6281251389915
 ___________________________________________________________________""")


def preperate():
	while True:
		try:
			path = str(input(" File : "))
			file = open(path, "r").read().split("\n")
			break
		except:
			print(f" [!] File {path} not found")

	while True:
		saveto = str(input(" Save result to : "))
		if saveto.split(".")[-1] != "txt": saveto+=".txt"
		try:
			open(saveto, "r").read()
			print(f" File {saveto} already exists")
		except:
			break

	return file, saveto


def email():
	data, saveto = preperate()


def url():
	datas, saveto = preperate()
	for data in datas:
		if "|" in data:
			node = data.split("|")
			data = data.replace(node[0], "").replace(node[-1], "")
		else:
			node = data.split("//")[-1].split("/")
			data = data.replace(node[0], "").replace(node[-1], "").replace("/", "|")
		open(saveto, "a").write(data)


def main():
	while True:
		clr()
		banner()
		print("""
 [1] Url
 [2] Email
 [0] Exit
 """)
		while True:
			choice = str(input(" Choice menu : "))
			if choice == "1":
				url()
				break

			elif choice == "2":
				email()
				break

			elif choice == "0":
				print("\n [+] Program finished")
				sys.exit()

			else:
				print(" [!] Invalid choice")


if __name__ == '__main__':
	main()