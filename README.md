# iperf3pythontomysql
If like to graph iperf3 tests to mysql using python. mysql  Ver 14.14 Distrib 5.7.28 and Python 3.6.8

## why? 
My need at the time was that my WISP had constant issues and wanted to show the degrade in service during evenings. This now is used
on my fibre internet provider (actually my work) and if there is an issue I could pick this up, this is logged to mysql and then graphed by
grafana and alerted to a slack channel. If like to do the same can google TIG stack (telegraf,influx,grafana) and that should give you guides. 

## stuff used

https://github.com/thiezn/iperf3-python <br>
pip3 install mysqldb
