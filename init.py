import os

if __name__ == "__main__":
	uid = os.getuid()
	with open("UID", "w") as f:
		f.write(str(uid))