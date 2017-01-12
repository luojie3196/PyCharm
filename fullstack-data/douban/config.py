#!/usr/bin/python
# -*- coding:utf-8 -*-

# mysql info config
HOST = "localhost"
USER = "root"
password = "93560"
db = "db_int"
port = 3306
charset = "utf8"

# douban table info
'''
CREATE TABLE `douban` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `movie_id` int(4) NOT NULL DEFAULT '0',
  `rate` float(3,1) NOT NULL DEFAULT '0.0',
  `url` varchar(128) NOT NULL DEFAULT '',
  `cover` varchar(255) NOT NULL DEFAULT '',
  `director` text NOT NULL,
  `scriptwriter` text NOT NULL,
  `protagonist` text NOT NULL,
  `type` varchar(128) NOT NULL DEFAULT '',
  `region` text NOT NULL,
  `language` varchar(255) NOT NULL DEFAULT '',
  `release_time` text NOT NULL,
  `numbers` varchar(30) NOT NULL DEFAULT '',
  `run_time` varchar(128) NOT NULL DEFAULT '',
  `other_title` varchar(255) NOT NULL DEFAULT '',
  `imdb_link` varchar(128) NOT NULL DEFAULT '',
  `website` varchar(128) NOT NULL DEFAULT '',
  `comment_num` int(4) NOT NULL DEFAULT '0',
  `summary` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IND` (`rate`)
) ENGINE=MyISAM AUTO_INCREMENT=50160 DEFAULT CHARSET=utf8;
'''