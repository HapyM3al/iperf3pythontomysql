# iperf3pythontomysql
If like to graph iperf3 tests to mysql using python. mysql  Ver 14.14 Distrib 5.7.28 and Python 3.6.8 on ubuntu 18.02 LTS

I know this can be optomized a little, it was a rush and honestly works perfect for me. 

## why? 
My need at the time was that my WISP had constant issues and wanted to show the degrade in service during evenings. This now is used on my fibre internet provider (actually my work) and if there is an issue I could pick this up, this is logged to mysql and then graphed by grafana and alerted to a slack channel. If like to do the same can google TIG stack (telegraf,influx,grafana) and that should give you guides. 

We had internal work iperf server in remote location about 1500km from me so that helps as well testing transit and so on. Doing this on own LAN doesnt make sense to me, use a public or your own remote iperf server, give it a A record and should work if nothing firewall related etc blocks it. 

## stuff used

https://github.com/thiezn/iperf3-python <br>
pip3 install mysqldb

## sql file

this assumes did the mysql install, should work with mariadb as well. Then did usual secure install process and so on. You need to make a database then a table. You can name it whatever like to that is up to you to decide just need to be referenced.

## cron
mine rus every 20min. use cronguru if you want to adjust to whatever like. 

 ``` */20 * * * * /usr/bin/python3 /dir/to/file/pyiperf3.py```
 
 ## grafana 
 
 here is select I do on grafana:
 ```
 SELECT
  datetime AS "time",
  bps
FROM iperf
WHERE
  $__timeFilter(datetime) 
 (optional if your wan changes and does other things) and ip = 'ipaddresshere'
ORDER BY datetime
```

here is example how mine looking: https://imgur.com/a/Q5WQ8vN 
