import wget

start = input("Start Key: ")
end = input("End Key: ")
sYear = input("Starting Year:")
eYear = input("Session End Year:")
start = int(start)
sYear = int(sYear)
eYear = int(eYear)
end = int(end)
link = list()

while start <= end:
    lnk = 'http://edusecure.in/StMarysChandigarh/studentinfo/DownloadReportCard.aspx?details=%d&session=%d-%d' % (start,sYear,eYear)
    link.append(lnk)
    start += 1

for i in link:
    print(i)
    file = wget.download(i)
