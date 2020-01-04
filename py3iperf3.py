#!/usr/bin/env python3

import iperf3
import socket
import datetime
from requests import get
import MySQLdb as mdb
import sys

client = iperf3.Client()
client.duration = 20
client.server_hostname = 'hostname/ip' 
client.port = portnumber
client.protocol = 'protocol(udp or tcp)'
client.num_streams = 10
client.reverse = True
client.version = 3

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M:%S")
ip = get('http://myip.dnsomatic.com').text

result = client.run()

server = 'hostname/ip' #samesame as client.server_hostname, this can be improved. 
sent_bytes = (result.sent_bytes)
bps = (result.sent_bps)
Mbps = (result.sent_Mbps)
con = mdb.connect('localhost', 'root','password', 'database'); #you have to change stuff here - ip,username,password,database. You can make another user with right permissions. 
cur = con.cursor()
sql = ("INSERT INTO iperf (datetime,server,ip,sent_bytes,bps,Mbps) VALUES ('{}','{}','{}','{}','{}','{}')".format(date,server,ip,sent_bytes,bps,Mbps))
cur.execute(sql)
con.commit()
con.close()
