-- 
-- データベース: `raspisens`
-- テーブルの構造 `sensorvalues`
-- 
CREATE TABLE `sensorvalues` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `temp` float NOT NULL,
  `hum` float NOT NULL,
  `press` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=316 ;