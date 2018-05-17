import os


def getProcessStatus(processes):
	for process in processes:
		command = os.popen("ps axu | grep " + process['name'] + " | grep -v grep | awk {'print $2;'}")
		line = command.read()
		command.close()
		if line:
			process['status'] = "Running"
			process['pid'] = line.translate(None,"\n',N('on\e) ")
		if line == "":
			process['status'] = "Stopped"
			process['pid'] = "N/A"
	return processes