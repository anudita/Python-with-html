#!/bin/python

import cgi
import commands

print "Content-type: text/html\n\n"
data=cgi.FieldStorage()

namenode=data.getvalue('nnode')
datanode1=data.getvalue('dnode1')
datanode2=data.getvalue('dnode2')
datanode3=data.getvalue('dnode3')

print namenode, datanode1, datanode2, datanode3
if namenode == 'nnode':
	commands.getoutput('sudo virsh destroy namenode')
if datanode1 == 'dnode1':
	commands.getoutput('sudo virsh destroy datanode1')
if datanode2 == 'dnode2':
	commands.getoutput('sudo virsh destroy datanode2')
if datanode3 == 'dnode3':
	commands.getoutput('sudo virsh destroy datanode3')
