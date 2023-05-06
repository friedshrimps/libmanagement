-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           5.7.33 - MySQL Community Server (GPL)
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Listage de la structure de la table db1. admin
CREATE TABLE IF NOT EXISTS `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Listage des données de la table db1.admin : ~2 rows (environ)
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` (`id`, `username`, `password`) VALUES
	(4, 'admin0', '$2b$12$EOpYcjswo1JAHWcsMRJwwuujKZcu99T2.Z/DxjukKtyMUY8WnIwMy');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;

-- Listage de la structure de la table db1. livres
CREATE TABLE IF NOT EXISTS `livres` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `titre` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` blob,
  `annee` int(11) DEFAULT NULL,
  `auteur` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Listage des données de la table db1.livres : ~8 rows (environ)
/*!40000 ALTER TABLE `livres` DISABLE KEYS */;
INSERT INTO `livres` (`id`, `titre`, `image`, `annee`, `auteur`) VALUES
	(1, 'book1', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B312E6A706567, 2021, 'aaaaaa'),
	(2, 'book2', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B322E6A706567, 2016, 'bbbbbb'),
	(3, 'book3', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B332E6A706567, 2007, 'cccccc'),
	(4, 'book4', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B342E6A706567, 2009, 'ddddd'),
	(5, 'book5', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B352E6A7067, 2001, 'eeeee'),
	(6, 'book6', _binary 0x433A2F6C617261676F6E322F7777772F7066612F626F6F6B362E6A7067, 2017, 'fffff');
/*!40000 ALTER TABLE `livres` ENABLE KEYS */;

-- Listage de la structure de la table db1. users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Listage des données de la table db1.users : ~8 rows (environ)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `username`, `password`) VALUES
	(1, 'aya', '$2b$12$VQM5tZR6/8hDyCAjbLHGCOBDttgFo2M.nGkWw4qhp9wjH0z1zfYOS');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
db1admindb1