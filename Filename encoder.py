import os
import json
from PIL import Image


# List all files in a directory using scandir()
basepath = 'run/'

def scanDir(path):
	
	splitPath = path.split("/")
	
	if len(splitPath) > 1:
		basepath = splitPath[len(splitPath) - 1]
	
	

	fi = []
	fo = []
	with os.scandir(path) as entries:
		for entry in entries:
					
				if entry.is_file():
					fi.append(entry.name)
					
				else:
					fo.append({str(entry.name) : scanDir(path+entry.name+"/")})
				
		#			arr[basepath].append(scanDir(path + entry.name + "/"))
	
#	print(fi)
		
#	arr[basepath]["folder"] = fo
	
	return {"files" : fi, "folder" : fo}


	#"src": "images/touch/homescreen72.png",
#    "sizes": "72x72",
#    "type": "image/png"

def eachImg(path, dummy, name):
	img = Image.open(path + "/" + name)
		
	width, height = img.size
		
	return {
		"sizes" : str(width) + "x" + str(height),
		"src" : dummy + "/" + name,
		"type" : "image/png"
	}


def getKey(obj):
	arr = []
	for i in obj:
		arr.append(i)
	return arr
	
x = scanDir(basepath)

test = getKey(x["folder"][0])[0]


a = x["folder"][0]

#print(a[test]["files"])
dummy = "App/_include/assets/img/homepage/"
arr = []
for index in x["folder"]:
	key = getKey(index)[0]
	src = basepath + key
	d = dummy + key
	for name in index[key]["files"]:
		imgObj = eachImg(src, d,  name)
		arr.append(imgObj)
		



j = json.dumps(arr)

f = open("json/ff.txt", "w+")
f.write(j)

print(arr)
