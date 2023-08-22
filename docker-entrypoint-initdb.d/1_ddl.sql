-- 
-- データベース: `raspisens`
-- テーブルの構造 `sensorvalues`
--

DROP SCHEMA IF EXISTS raspi;
-- レコードを初期化したい場合、DROP SCHEMAをコメントアウトして、DROP DATABASEをアンコメント
-- DROP DATABASE IF EXISTS raspi;
CREATE DATABASE raspi CHARACTER SET utf8mb4;
use raspi;

CREATE TABLE raspi.sensorvalues(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `temp` float NOT NULL,
  `hum` float NOT NULL,
  `press` float NOT NULL,
  `machine` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=316;