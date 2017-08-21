import string
from linecache import getline
i = 0
rserver = []
ipAddress = []
serverfarm = []
searchfile = open("lb.text", "r")
for line in searchfile:
	if "rserver host " in line:
		ip = next(searchfile)
		ipAddress.append(ip.replace("  ip address ", ""))
		lrserver = line
		rserver.append(lrserver.replace("rserver host ", ""))
		i += 1
	if "serverfarm host " in line:
		lserverfarm = line
		serverfarm.append(lserverfarm.replace("serverfarm host ", ""))
		
searchfile.close()
print (rserver[114])
print (ipAddress[114])
print (serverfarm[5])

