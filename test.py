#!/usr/bin/python
import re
import subprocess

#used as a quick way to handle shell commands
def getFromShell_raw(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.readlines()

def getFromShell(command):
    result = getFromShell_raw(command)
    for i in range(len(result)):
        result[i] = result[i].strip() # strip out white space
    return result

def get_sd_list():
    print "checking devices"
    devices = []
    for d in getFromShell('udisks --enumerate-device-files'):
        if re.match('^/dev/sd..$',d):
#            devices.append(Mass_storage_device(device_file=d))
            print d
    return devices

get_sd_list()
