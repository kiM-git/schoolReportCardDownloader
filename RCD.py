"""
Report Card Downloader Version 2.0
No reverse engineering allowed.
"""
import chiper
import wget

def download(start, end, sYear, eYear,key):
	while start <= end:
		ls = key + "?details=%d&session=%d-%d" % (start,sYear,eYear)		
		link.append("http://" + ls)
		start += 1
	print(link)
	for i in link:
			print(i)
			file = wget.download(i)
			
if __name__ ==  "__main__" :
	
	start = input("Start Key: ")
	end = input("End Key: ")
	sYear = input("Starting Year:")
	eYear = input("Session End Year:")
	pin = int(input("Security Pin: "))
	pin -= 10000
	start = int(start)
	sYear = int(sYear)
	eYear = int(eYear)
	end = int(end)
	link = list()
	key = R"RV{w¦¡r © h­¯±¡£­´ª°©³t¶¿·¶º­± ´ÀÀÄÇ¶È»ºÍËÔ"
	lr = chiper.decrypt(key,pin)
	download(start, end, sYear, eYear, lr)

