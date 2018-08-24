import os, re
ips = ['127.0.0.1','192.168.0.11','10.3.1.19','192.168.0.13']

for ip in ips:
	cmd = "ping -c4 " + ip
	r = '\n'.join(os.popen(cmd).readlines())

	m = re.search ("time \\dms", r)
	print m.group(0)

	if re.search ("64 bytes from", r):
	  print "ativo"
	else:
	  print "inativo"