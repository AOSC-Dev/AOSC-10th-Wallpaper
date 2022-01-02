import os
import sys

filePath = "/Users/megabits/Desktop/Animation"
list = os.listdir(filePath)
startFile = int(sys.argv[1])
stopFile = int(sys.argv[2])
position = 0
for h in range(startFile, stopFile + 1):
        n = str(startFile) + ".png"
        if n not in list:
			print(position, "Not Found", n)
	startFile+=1
