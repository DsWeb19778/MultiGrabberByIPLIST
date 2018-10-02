def main():
	# facebook.com/name.path
	import requests
	import os
	import time
	from time import sleep
	import platform
	system = platform.system()
	if (system == "Windows"):
		os.system("cls")
		color = "a"
		os.system("color "+color)
	else:
		os.system("clear")
		os.system("color "+color)
	print("==>> Coded By DsWeb19778")
	print("==>> Contact [Facebook.com/name.path]")
	iplist = raw_input("==>> Enter List IP :>>> ")
	openlist = open(iplist,"r")
	readme = openlist.readlines()
	print("==>> IPS you have : "+str(len(readme)))
	for ips in readme:
		exploit = "http://api.hackertarget.com/reverseiplookup/?q="+str(ips)
		conn = requests.get(exploit)
		sleep(3) # server respond 
		readrzlt = conn.content 
		file_name = "mysites.txt" # FIle Name you can change it
		file_mod = "a+"
		hacksite = open(file_name,file_mod)
		hacksite.write(readrzlt)
		print("[+] Grabbing From : "+str(ips))
		print("[+] Save IN ["+file_name+"]")
		print(readrzlt)
		hacksite.close()




if __name__ == '__main__':
		main()	
