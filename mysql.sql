create database <whatever like to call it> ;

"""
CREATE TABLE `iperf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime DEFAULT NULL,
  `server` text,
  `ip` text,
  `sent_bytes` BIGINT,
  `bps` double DEFAULT NULL,
  `Mbps` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
"""
