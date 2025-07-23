PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(80) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
INSERT INTO user VALUES(1,'rodriguezvictor','strongjames@example.org');
INSERT INTO user VALUES(2,'mmorris','mathiskevin@example.org');
INSERT INTO user VALUES(3,'richardkennedy','marvinsmith@example.org');
INSERT INTO user VALUES(4,'kgarcia','schmidtjames@example.org');
INSERT INTO user VALUES(5,'ywatson','danielallen@example.com');
INSERT INTO user VALUES(6,'dparsons','nicolebates@example.org');
INSERT INTO user VALUES(7,'hamptonisaac','smithbrian@example.net');
INSERT INTO user VALUES(8,'jacksmith','danielharris@example.com');
INSERT INTO user VALUES(9,'gabriel29','leerichard@example.com');
INSERT INTO user VALUES(10,'martinezraymond','michael75@example.com');
INSERT INTO user VALUES(11,'stevensjustin','susan41@example.com');
INSERT INTO user VALUES(12,'peteranderson','jamesmoody@example.org');
INSERT INTO user VALUES(13,'joneskurt','mark11@example.net');
INSERT INTO user VALUES(14,'erikjames','plee@example.com');
INSERT INTO user VALUES(15,'andrewmack','tiffany05@example.org');
INSERT INTO user VALUES(16,'jessica39','pnichols@example.com');
INSERT INTO user VALUES(17,'maryterrell','melissa66@example.net');
INSERT INTO user VALUES(18,'christinebarajas','manuelsingh@example.net');
INSERT INTO user VALUES(19,'natalie69','jimmy48@example.com');
INSERT INTO user VALUES(20,'nealjames','staylor@example.com');
INSERT INTO user VALUES(21,'jacobmartinez','hunterwilson@example.com');
INSERT INTO user VALUES(22,'joshua11','steven09@example.org');
INSERT INTO user VALUES(23,'rebeccamiddleton','carlamcclain@example.org');
INSERT INTO user VALUES(24,'jacobcortez','sanchezherbert@example.org');
INSERT INTO user VALUES(25,'renee28','brownjessica@example.net');
INSERT INTO user VALUES(26,'oowen','nicolecain@example.net');
INSERT INTO user VALUES(27,'kelly51','imunoz@example.net');
INSERT INTO user VALUES(28,'luke31','thall@example.com');
INSERT INTO user VALUES(29,'moodybrian','julie84@example.com');
INSERT INTO user VALUES(30,'ronald21','dbarrera@example.com');
INSERT INTO user VALUES(31,'jvincent','grichardson@example.org');
INSERT INTO user VALUES(32,'dylan34','amber51@example.com');
INSERT INTO user VALUES(33,'joseph21','robertparks@example.com');
INSERT INTO user VALUES(34,'ocooper','sanchezstephen@example.org');
INSERT INTO user VALUES(35,'bestwilliam','victoria12@example.org');
INSERT INTO user VALUES(36,'jeffrey43','ellisnina@example.org');
INSERT INTO user VALUES(37,'amber04','joseph75@example.net');
INSERT INTO user VALUES(38,'millerkaren','gmiller@example.org');
INSERT INTO user VALUES(39,'connie32','colleenhowe@example.net');
INSERT INTO user VALUES(40,'karensweeney','adrian14@example.org');
INSERT INTO user VALUES(41,'tsimmons','amypaul@example.com');
INSERT INTO user VALUES(42,'rodriguezamanda','wgreen@example.net');
INSERT INTO user VALUES(43,'awebb','brandon61@example.net');
INSERT INTO user VALUES(44,'richard98','matthewolson@example.net');
INSERT INTO user VALUES(45,'vsmall','uvargas@example.org');
INSERT INTO user VALUES(46,'alin','timothypeters@example.com');
INSERT INTO user VALUES(47,'ccaldwell','christopher13@example.com');
INSERT INTO user VALUES(48,'joannaclark','allisonbennett@example.com');
INSERT INTO user VALUES(49,'vcunningham','smendoza@example.com');
INSERT INTO user VALUES(50,'paulchambers','johnnyanderson@example.net');
CREATE TABLE categories (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	parent_id INTEGER, 
	is_active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (slug), 
	FOREIGN KEY(parent_id) REFERENCES categories (id)
);
INSERT INTO categories VALUES(1,'Facebook','facebook','Facebook accounts and pages',NULL,1,'2025-07-23 07:18:48.731228');
INSERT INTO categories VALUES(2,'Instagram','instagram','Instagram accounts and followers',NULL,1,'2025-07-23 07:18:48.731336');
INSERT INTO categories VALUES(3,'Twitter','twitter','Twitter accounts and followers',NULL,1,'2025-07-23 07:18:48.731347');
INSERT INTO categories VALUES(4,'TikTok','tiktok','TikTok accounts and followers',NULL,1,'2025-07-23 07:18:48.731353');
INSERT INTO categories VALUES(5,'YouTube','youtube','YouTube channels and subscribers',NULL,1,'2025-07-23 07:18:48.731359');
INSERT INTO categories VALUES(6,'LinkedIn','linkedin','LinkedIn profiles and connections',NULL,1,'2025-07-23 07:18:48.731364');
INSERT INTO categories VALUES(7,'Telegram','telegram','Telegram channels and groups',NULL,1,'2025-07-23 07:18:48.731370');
INSERT INTO categories VALUES(8,'Discord','discord','Discord servers and members',NULL,1,'2025-07-23 07:18:48.731377');
INSERT INTO categories VALUES(9,'Reddit','reddit','Reddit accounts and karma',NULL,1,'2025-07-23 07:18:48.731383');
INSERT INTO categories VALUES(10,'Pinterest','pinterest','Pinterest accounts and boards',NULL,1,'2025-07-23 07:18:48.731389');
CREATE TABLE vendors (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	rating NUMERIC(3, 1), 
	total_sales INTEGER, 
	is_active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO vendors VALUES(1,'SocialBoost Pro',3.6000000000000000888,2295,1,'2024-09-16 09:17:19.634336');
INSERT INTO vendors VALUES(2,'DigitalGrowth',4.7999999999999998223,4492,1,'2024-04-01 02:36:47.509628');
INSERT INTO vendors VALUES(3,'AccountMaster',4.5999999999999996447,1466,1,'2025-06-09 22:51:31.188501');
INSERT INTO vendors VALUES(4,'SocialHub',4.5999999999999996447,3335,1,'2024-09-23 14:29:53.543839');
INSERT INTO vendors VALUES(5,'GrowthExperts',4,768,1,'2024-01-31 08:46:15.879401');
INSERT INTO vendors VALUES(6,'ViralBoost',4.4000000000000003552,946,1,'2024-02-14 09:27:29.521304');
INSERT INTO vendors VALUES(7,'SocialPower',4.5999999999999996447,1693,1,'2024-01-07 16:26:46.501949');
INSERT INTO vendors VALUES(8,'AccountFactory',4,3645,1,'2024-01-10 13:00:16.797703');
INSERT INTO vendors VALUES(9,'BoostMeUp',4.2000000000000001776,734,1,'2024-10-30 18:30:39.475248');
INSERT INTO vendors VALUES(10,'SocialKing',4.5999999999999996447,2852,1,'2024-06-22 09:01:30.803903');
INSERT INTO vendors VALUES(11,'DigitalBoost',4.5,1162,1,'2024-03-25 05:56:14.022353');
INSERT INTO vendors VALUES(12,'AccountPro',4.2999999999999998223,2454,1,'2025-06-28 03:06:02.347152');
INSERT INTO vendors VALUES(13,'SocialGenie',4.5999999999999996447,4064,1,'2024-06-21 22:35:12.888890');
INSERT INTO vendors VALUES(14,'GrowthMachine',4,1188,1,'2024-04-10 05:19:24.045301');
INSERT INTO vendors VALUES(15,'ViralExperts',4.9000000000000003552,2593,1,'2023-08-07 03:54:44.925228');
CREATE TABLE site_settings (
	id INTEGER NOT NULL, 
	"key" VARCHAR(100) NOT NULL, 
	value TEXT, 
	description TEXT, 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE ("key")
);
INSERT INTO site_settings VALUES(1,'site_name','AccsMarket','Website name','2025-07-23 07:18:48.785075','2025-07-23 07:18:48.785078');
INSERT INTO site_settings VALUES(2,'site_description','Buy or Sell Social Media Accounts','Website description','2025-07-23 07:18:48.785205','2025-07-23 07:18:48.785207');
INSERT INTO site_settings VALUES(3,'header_logo_url','/logo.png','Header logo URL','2025-07-23 07:18:48.785217','2025-07-23 07:18:48.785218');
INSERT INTO site_settings VALUES(4,'header_logo_alt','AccsMarket','Header logo alt text','2025-07-23 07:18:48.785224','2025-07-23 07:18:48.785225');
INSERT INTO site_settings VALUES(5,'search_enabled','true','Enable search functionality','2025-07-23 07:18:48.785230','2025-07-23 07:18:48.785231');
INSERT INTO site_settings VALUES(6,'search_placeholder','Search for accounts','Search input placeholder','2025-07-23 07:18:48.785237','2025-07-23 07:18:48.785238');
INSERT INTO site_settings VALUES(7,'navigation_menu','[{"label": "Home", "url": "/", "active": true}, {"label": "Categories", "url": "/categories", "active": true}, {"label": "Search", "url": "/search", "active": true}, {"label": "Become a Seller", "url": "/seller", "active": true}]','Navigation menu items','2025-07-23 07:18:48.785243','2025-07-23 07:18:48.785244');
CREATE TABLE pages (
	id INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	content TEXT, 
	is_active BOOLEAN, 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (slug)
);
INSERT INTO pages VALUES(1,'FAQ','faq','Frequently Asked Questions content here...',1,'2025-07-23 07:18:48.785573','2025-07-23 07:18:48.785575');
INSERT INTO pages VALUES(2,'Terms of Use','terms','Terms of Use content here...',1,'2025-07-23 07:18:48.785681','2025-07-23 07:18:48.785682');
INSERT INTO pages VALUES(3,'Privacy Policy','privacy','Privacy Policy content here...',1,'2025-07-23 07:18:48.785696','2025-07-23 07:18:48.785697');
INSERT INTO pages VALUES(4,'Contact Support','support','Contact Support information here...',1,'2025-07-23 07:18:48.785706','2025-07-23 07:18:48.785707');
INSERT INTO pages VALUES(5,'About Us','about','About Us content here...',1,'2025-07-23 07:18:48.785716','2025-07-23 07:18:48.785717');
CREATE TABLE footer_settings (
	id INTEGER NOT NULL, 
	company_name VARCHAR(100), 
	company_description TEXT, 
	logo_text VARCHAR(50), 
	logo_suffix VARCHAR(50), 
	social_link_1 VARCHAR(255), 
	social_link_1_icon VARCHAR(50), 
	social_link_2 VARCHAR(255), 
	social_link_2_icon VARCHAR(50), 
	social_link_3 VARCHAR(255), 
	social_link_3_icon VARCHAR(50), 
	quick_links TEXT, 
	support_links TEXT, 
	contact_email VARCHAR(100), 
	contact_website VARCHAR(100), 
	support_text VARCHAR(100), 
	security_text VARCHAR(100), 
	copyright_text VARCHAR(200), 
	payment_methods TEXT, 
	background_color VARCHAR(20), 
	text_color VARCHAR(20), 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO footer_settings VALUES(1,'ACCS market.com','Buy or Sell Social Media Accounts (PVA & Cheap). Your trusted marketplace for social media accounts.','ACCS','market.com','https://accsmarket.news','Globe','mailto:support@accsmarket.com','Mail','https://t.me/accsmarket','MessageCircle','[{"label": "Home", "url": "/"}, {"label": "Categories", "url": "/categories"}, {"label": "Search Accounts", "url": "/search"}, {"label": "Become a Seller", "url": "/seller"}]','[{"label": "FAQ", "url": "/faq"}, {"label": "Terms of Use", "url": "/terms"}, {"label": "Privacy Policy", "url": "/privacy"}, {"label": "Contact Support", "url": "/support"}]','support@accsmarket.com','accsmarket.news','24/7 Support Available','Secure Transactions','© 2024 AccsMarket. All rights reserved.','[{"name": "Bitcoin", "code": "BTC"}, {"name": "USDT", "code": "USDT"}, {"name": "Ethereum", "code": "ETH"}, {"name": "PayPal", "code": "PAYPAL"}]','#1a1a1a','#ffffff','2025-07-23 07:18:48.784550','2025-07-23 07:18:48.784553');
CREATE TABLE products (
	id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	name VARCHAR(500) NOT NULL, 
	description TEXT, 
	base_price FLOAT NOT NULL, 
	stock_quantity INTEGER, 
	rating FLOAT, 
	return_rate FLOAT, 
	delivery_time VARCHAR(50), 
	is_active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES categories (id)
);
INSERT INTO products VALUES(1,1,'Facebook Page with 90,366 Likes','High quality facebook account with real and active followers. Perfect for marketing and business growth.',75.640000000000000568,18,4.5999999999999996447,1.1000000000000000888,'24-48 hours',1,'2024-11-28 00:54:47.402416');
INSERT INTO products VALUES(2,1,'Facebook Page with 34,131 Likes','High quality facebook account with real and active followers. Perfect for marketing and business growth.',39.99000000000000199,3,4.2000000000000001776,1.0,'2-3 days',1,'2025-05-08 17:03:25.370048');
INSERT INTO products VALUES(3,1,'Facebook Page with 7,515 Likes','High quality facebook account with real and active followers. Perfect for marketing and business growth.',11.910000000000000141,8,4.4000000000000003552,1.6999999999999999555,'2-3 days',1,'2024-08-12 16:36:17.632888');
INSERT INTO products VALUES(4,1,'Facebook Account - 370,858 Friends','High quality facebook account with real and active followers. Perfect for marketing and business growth.',203.62999999999999544,5,4.2000000000000001776,0.5,'Instant',1,'2025-05-09 23:10:07.025178');
INSERT INTO products VALUES(5,1,'Facebook Account - 42,280 Friends','High quality facebook account with real and active followers. Perfect for marketing and business growth.',66.209999999999993745,20,4.2000000000000001776,1.8999999999999999111,'Instant',1,'2025-07-20 08:52:39.665541');
INSERT INTO products VALUES(6,1,'Facebook Account - 685,371 Friends','High quality facebook account with real and active followers. Perfect for marketing and business growth.',732.13999999999998637,11,4.5,0.69999999999999995559,'2-3 days',1,'2025-04-20 13:04:07.373408');
INSERT INTO products VALUES(7,1,'Facebook Group with 74,874 Members','High quality facebook account with real and active followers. Perfect for marketing and business growth.',47.350000000000001419,14,4.2000000000000001776,0.59999999999999997779,'24-48 hours',1,'2024-10-31 15:25:40.053210');
INSERT INTO products VALUES(8,1,'Facebook Group with 21,739 Members','High quality facebook account with real and active followers. Perfect for marketing and business growth.',13.900000000000000355,2,4.9000000000000003552,1.5,'1-24 hours',1,'2025-03-22 03:10:41.772805');
INSERT INTO products VALUES(9,1,'Facebook Group with 28,646 Members','High quality facebook account with real and active followers. Perfect for marketing and business growth.',34.170000000000001704,12,4.0999999999999996447,0.9000000000000000222,'Instant',1,'2024-08-10 13:38:22.390809');
INSERT INTO products VALUES(10,1,'Facebook Business Page - 71,584 Followers','High quality facebook account with real and active followers. Perfect for marketing and business growth.',124.53000000000000114,6,4.7000000000000001776,1.5,'2-3 days',1,'2025-03-31 19:06:35.621162');
INSERT INTO products VALUES(11,1,'Facebook Business Page - 576,009 Followers','High quality facebook account with real and active followers. Perfect for marketing and business growth.',339.99000000000000908,1,4.0999999999999996447,0.2000000000000000111,'24-48 hours',1,'2025-04-13 01:17:46.004541');
INSERT INTO products VALUES(12,1,'Facebook Business Page - 23,634 Followers','High quality facebook account with real and active followers. Perfect for marketing and business growth.',35.640000000000000568,6,4.9000000000000003552,1.1999999999999999555,'Instant',1,'2024-09-22 10:01:13.609997');
INSERT INTO products VALUES(13,2,'Instagram Account - 1,691 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',5.4500000000000001776,2,4.9000000000000003552,0.9000000000000000222,'1-24 hours',1,'2025-07-08 19:56:34.462624');
INSERT INTO products VALUES(14,2,'Instagram Account - 96,374 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',57.149999999999998578,8,4.2000000000000001776,1.3000000000000000444,'Instant',1,'2024-11-26 13:50:23.011267');
INSERT INTO products VALUES(15,2,'Instagram Account - 16,135 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',24.620000000000000993,5,4.7999999999999998223,1.5,'2-3 days',1,'2024-09-10 05:09:29.337444');
INSERT INTO products VALUES(16,2,'Instagram Business Account - 4,422 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',6.5400000000000000355,4,4.7999999999999998223,1.8999999999999999111,'1-24 hours',1,'2025-01-18 21:21:58.474979');
INSERT INTO products VALUES(17,2,'Instagram Business Account - 97,178 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',187.15000000000000568,11,4.9000000000000003552,0.2000000000000000111,'1-24 hours',1,'2024-09-25 10:38:49.928721');
INSERT INTO products VALUES(18,2,'Instagram Business Account - 8,687 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',7.2599999999999997868,19,4.5,1.3000000000000000444,'24-48 hours',1,'2025-04-14 23:33:12.812072');
INSERT INTO products VALUES(19,2,'Instagram Influencer Account - 166,910 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',88.219999999999998861,15,4.7000000000000001776,0.69999999999999995559,'1-24 hours',1,'2024-12-02 20:45:55.730226');
INSERT INTO products VALUES(20,2,'Instagram Influencer Account - 12,958 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',18.769999999999999573,5,4.7000000000000001776,1.1000000000000000888,'Instant',1,'2024-11-22 04:23:06.438195');
INSERT INTO products VALUES(21,2,'Instagram Influencer Account - 1,170 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',8.2200000000000006394,18,4.0,1.1999999999999999555,'1-24 hours',1,'2024-10-04 23:04:56.148279');
INSERT INTO products VALUES(22,2,'Instagram Theme Page - 414,955 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',543.85000000000002272,3,4.5,0.5,'Instant',1,'2025-05-23 22:29:08.602226');
INSERT INTO products VALUES(23,2,'Instagram Theme Page - 198,046 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',173.12000000000000454,18,4.0,0.2000000000000000111,'1-24 hours',1,'2025-05-27 22:29:54.905895');
INSERT INTO products VALUES(24,2,'Instagram Theme Page - 146,715 Followers','High quality instagram account with real and active followers. Perfect for marketing and business growth.',189.1699999999999875,20,4.7000000000000001776,1.3000000000000000444,'1-24 hours',1,'2025-01-17 01:43:04.135192');
INSERT INTO products VALUES(25,3,'Twitter Account - 2,628 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',8.5600000000000004973,1,4.2999999999999998223,1.1000000000000000888,'24-48 hours',1,'2024-11-27 10:59:28.171583');
INSERT INTO products VALUES(26,3,'Twitter Account - 1,118 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',5.0300000000000002486,1,4.7000000000000001776,1.8000000000000000444,'24-48 hours',1,'2025-07-02 22:45:40.027859');
INSERT INTO products VALUES(27,3,'Twitter Account - 2,619 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',12.939999999999999502,4,4.4000000000000003552,0.4000000000000000222,'Instant',1,'2024-09-01 13:14:47.933533');
INSERT INTO products VALUES(28,3,'Twitter Verified Account - 274,101 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',426.62000000000000455,2,4.2999999999999998223,1.5,'Instant',1,'2025-05-24 21:55:26.246849');
INSERT INTO products VALUES(29,3,'Twitter Verified Account - 9,061 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',12.77999999999999936,20,4.4000000000000003552,1.8000000000000000444,'Instant',1,'2025-01-29 12:28:41.281160');
INSERT INTO products VALUES(30,3,'Twitter Verified Account - 56,645 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',89.290000000000006256,14,4.5999999999999996447,0.2000000000000000111,'2-3 days',1,'2025-04-18 00:25:37.253053');
INSERT INTO products VALUES(31,3,'Twitter Business Account - 877,908 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',1076.7999999999999545,5,4.9000000000000003552,0.29999999999999998889,'24-48 hours',1,'2024-08-28 08:56:46.996244');
INSERT INTO products VALUES(32,3,'Twitter Business Account - 62,055 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',54.240000000000001987,12,4.5,0.69999999999999995559,'24-48 hours',1,'2025-01-28 12:50:22.492262');
INSERT INTO products VALUES(33,3,'Twitter Business Account - 2,870 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',8.5399999999999991473,14,4.7000000000000001776,1.3999999999999999111,'Instant',1,'2025-01-24 11:26:23.935358');
INSERT INTO products VALUES(34,3,'Twitter Influencer Account - 905,112 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',1578.1600000000000818,8,4.4000000000000003552,1.6000000000000000888,'Instant',1,'2025-05-18 08:01:20.644961');
INSERT INTO products VALUES(35,3,'Twitter Influencer Account - 77,665 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',108.76999999999999601,2,4.7000000000000001776,1.0,'Instant',1,'2025-01-26 02:31:50.612043');
INSERT INTO products VALUES(36,3,'Twitter Influencer Account - 105,071 Followers','High quality twitter account with real and active followers. Perfect for marketing and business growth.',147.19999999999998863,3,4.0999999999999996447,0.59999999999999997779,'Instant',1,'2025-05-23 06:50:35.380978');
INSERT INTO products VALUES(37,4,'TikTok Account - 9,742 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',16.760000000000001563,18,4.2000000000000001776,0.9000000000000000222,'1-24 hours',1,'2025-02-03 13:19:29.723724');
INSERT INTO products VALUES(38,4,'TikTok Account - 405,499 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',703.07000000000005003,1,4.7000000000000001776,1.6000000000000000888,'24-48 hours',1,'2025-01-09 17:09:38.322558');
INSERT INTO products VALUES(39,4,'TikTok Account - 464,925 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',558.37000000000000456,5,4.2999999999999998223,0.5,'1-24 hours',1,'2025-04-27 06:55:50.477002');
INSERT INTO products VALUES(40,4,'TikTok Creator Account - 54,296 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',31.789999999999999148,5,4.2000000000000001776,1.1999999999999999555,'Instant',1,'2025-07-06 11:22:18.049767');
INSERT INTO products VALUES(41,4,'TikTok Creator Account - 95,227 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',179.78999999999999204,3,4.0999999999999996447,0.4000000000000000222,'2-3 days',1,'2024-12-12 08:25:49.121048');
INSERT INTO products VALUES(42,4,'TikTok Creator Account - 581,674 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',364.97000000000002729,16,4.5,0.2000000000000000111,'2-3 days',1,'2025-07-16 16:09:54.562648');
INSERT INTO products VALUES(43,4,'TikTok Viral Account - 369,179 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',627.53999999999996364,18,4.5,0.29999999999999998889,'1-24 hours',1,'2024-11-21 00:29:39.911741');
INSERT INTO products VALUES(44,4,'TikTok Viral Account - 92,588 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',143.11000000000001363,1,4.2000000000000001776,0.69999999999999995559,'Instant',1,'2025-03-26 03:47:51.645871');
INSERT INTO products VALUES(45,4,'TikTok Viral Account - 205,942 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',123.87999999999999545,10,4.5,0.2000000000000000111,'24-48 hours',1,'2024-10-20 04:26:45.372016');
INSERT INTO products VALUES(46,4,'TikTok Business Account - 6,929 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',12.669999999999999928,16,4.7999999999999998223,1.3999999999999999111,'Instant',1,'2025-04-16 01:24:05.217144');
INSERT INTO products VALUES(47,4,'TikTok Business Account - 23,658 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',27.05000000000000071,20,4.4000000000000003552,1.1000000000000000888,'Instant',1,'2025-05-07 19:31:48.843659');
INSERT INTO products VALUES(48,4,'TikTok Business Account - 666,740 Followers','High quality tiktok account with real and active followers. Perfect for marketing and business growth.',864.25999999999999091,6,4.0,0.10000000000000000555,'1-24 hours',1,'2024-12-06 14:53:48.927607');
INSERT INTO products VALUES(49,5,'YouTube Channel - 416,324 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',276.12999999999999546,19,4.0,0.8000000000000000444,'1-24 hours',1,'2025-01-17 20:47:12.752517');
INSERT INTO products VALUES(50,5,'YouTube Channel - 419,476 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',313.47000000000002728,5,4.5999999999999996447,0.59999999999999997779,'1-24 hours',1,'2025-06-16 22:46:16.103470');
INSERT INTO products VALUES(51,5,'YouTube Channel - 631,694 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',417.75999999999999089,12,4.5,0.4000000000000000222,'24-48 hours',1,'2025-05-27 23:33:10.265330');
INSERT INTO products VALUES(52,5,'YouTube Gaming Channel - 15,996 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',14.580000000000000071,2,4.9000000000000003552,0.9000000000000000222,'Instant',1,'2025-04-28 14:35:30.124674');
INSERT INTO products VALUES(53,5,'YouTube Gaming Channel - 333,990 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',463.31000000000000225,6,4.0999999999999996447,0.8000000000000000444,'Instant',1,'2024-09-18 10:23:00.769940');
INSERT INTO products VALUES(54,5,'YouTube Gaming Channel - 230,714 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',440.43999999999999773,20,4.7999999999999998223,1.1999999999999999555,'2-3 days',1,'2025-01-08 17:21:00.323071');
INSERT INTO products VALUES(55,5,'YouTube Educational Channel - 50,940 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',64.689999999999997725,20,4.5999999999999996447,1.0,'Instant',1,'2025-06-15 10:28:10.430348');
INSERT INTO products VALUES(56,5,'YouTube Educational Channel - 134,294 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',231.00999999999999091,13,4.5999999999999996447,0.69999999999999995559,'24-48 hours',1,'2025-03-13 03:36:44.479634');
INSERT INTO products VALUES(57,5,'YouTube Educational Channel - 41,954 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',34.020000000000003125,16,4.7000000000000001776,1.3000000000000000444,'Instant',1,'2024-10-27 17:47:07.560742');
INSERT INTO products VALUES(58,5,'YouTube Music Channel - 6,244 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',9.5999999999999996447,19,4.5,1.6000000000000000888,'1-24 hours',1,'2025-03-29 04:19:22.294424');
INSERT INTO products VALUES(59,5,'YouTube Music Channel - 102,162 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',119.23000000000000398,19,5.0,1.0,'24-48 hours',1,'2025-05-28 12:01:55.438970');
INSERT INTO products VALUES(60,5,'YouTube Music Channel - 45,105 Subscribers','High quality youtube account with real and active followers. Perfect for marketing and business growth.',41.39999999999999858,20,4.5999999999999996447,0.10000000000000000555,'24-48 hours',1,'2024-08-07 07:42:43.405893');
INSERT INTO products VALUES(61,6,'LinkedIn Profile - 1,302 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',6.7800000000000002486,2,4.5,0.9000000000000000222,'1-24 hours',1,'2025-03-24 08:18:47.147598');
INSERT INTO products VALUES(62,6,'LinkedIn Profile - 784,229 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',1313.7300000000000181,17,4.2999999999999998223,1.6999999999999999555,'Instant',1,'2025-01-26 16:09:46.203555');
INSERT INTO products VALUES(63,6,'LinkedIn Profile - 5,256 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',9.4299999999999997157,11,4.9000000000000003552,1.8999999999999999111,'2-3 days',1,'2025-07-08 13:02:35.434532');
INSERT INTO products VALUES(64,6,'LinkedIn Business Page - 113,379 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',166.12999999999999544,1,4.7999999999999998223,0.9000000000000000222,'24-48 hours',1,'2025-04-20 15:39:00.766533');
INSERT INTO products VALUES(65,6,'LinkedIn Business Page - 3,501 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',6.1500000000000003552,1,5.0,0.4000000000000000222,'Instant',1,'2025-01-01 00:52:35.467618');
INSERT INTO products VALUES(66,6,'LinkedIn Business Page - 112,214 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',104.51000000000000511,11,4.4000000000000003552,0.69999999999999995559,'1-24 hours',1,'2025-02-13 14:15:43.711223');
INSERT INTO products VALUES(67,6,'LinkedIn Company Page - 1,793 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',12.689999999999999503,2,4.2999999999999998223,1.1999999999999999555,'Instant',1,'2024-10-26 13:56:16.570938');
INSERT INTO products VALUES(68,6,'LinkedIn Company Page - 54,072 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',68.499999999999999999,8,4.7999999999999998223,0.9000000000000000222,'1-24 hours',1,'2024-12-23 21:44:45.820710');
INSERT INTO products VALUES(69,6,'LinkedIn Company Page - 681,729 Followers','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',1083.0699999999999363,7,4.0999999999999996447,0.9000000000000000222,'1-24 hours',1,'2024-10-27 18:51:07.775131');
INSERT INTO products VALUES(70,6,'LinkedIn Personal Brand - 207,650 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',157.11000000000001363,4,4.2999999999999998223,1.8000000000000000444,'24-48 hours',1,'2025-06-10 22:29:44.066868');
INSERT INTO products VALUES(71,6,'LinkedIn Personal Brand - 2,207 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',8.3699999999999992184,13,4.5,0.2000000000000000111,'1-24 hours',1,'2025-03-16 21:04:41.470084');
INSERT INTO products VALUES(72,6,'LinkedIn Personal Brand - 42,804 Connections','High quality linkedin account with real and active followers. Perfect for marketing and business growth.',23.960000000000000852,12,4.2000000000000001776,2.0,'2-3 days',1,'2024-09-30 06:21:24.095163');
INSERT INTO products VALUES(73,7,'Telegram Channel - 904,408 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',1581.4000000000000909,12,4.0999999999999996447,1.1000000000000000888,'24-48 hours',1,'2025-02-03 14:06:25.225922');
INSERT INTO products VALUES(74,7,'Telegram Channel - 36,124 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',43.229999999999996875,5,4.2999999999999998223,0.4000000000000000222,'24-48 hours',1,'2024-11-08 06:44:13.115304');
INSERT INTO products VALUES(75,7,'Telegram Channel - 73,221 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',123.92000000000000171,8,4.9000000000000003552,0.9000000000000000222,'2-3 days',1,'2024-08-15 09:24:14.921670');
INSERT INTO products VALUES(76,7,'Telegram Group - 4,174 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',7.4100000000000001421,8,4.0999999999999996447,1.5,'1-24 hours',1,'2024-09-08 01:28:06.627636');
INSERT INTO products VALUES(77,7,'Telegram Group - 15,065 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',22.149999999999998578,9,4.5999999999999996447,1.8000000000000000444,'1-24 hours',1,'2024-12-01 15:35:41.157816');
INSERT INTO products VALUES(78,7,'Telegram Group - 21,483 Members','High quality telegram account with real and active followers. Perfect for marketing and business growth.',41.299999999999997156,14,4.4000000000000003552,0.2000000000000000111,'2-3 days',1,'2024-11-19 23:52:06.741390');
INSERT INTO products VALUES(79,7,'Telegram Bot - 759,009 Users','High quality telegram account with real and active followers. Perfect for marketing and business growth.',1320.6900000000000545,8,4.4000000000000003552,1.5,'2-3 days',1,'2024-10-04 19:02:02.157829');
INSERT INTO products VALUES(80,7,'Telegram Bot - 150,319 Users','High quality telegram account with real and active followers. Perfect for marketing and business growth.',263.57999999999998407,16,4.5,0.29999999999999998889,'2-3 days',1,'2025-02-20 16:44:01.614188');
INSERT INTO products VALUES(81,7,'Telegram Bot - 803,242 Users','High quality telegram account with real and active followers. Perfect for marketing and business growth.',1395.599999999999909,2,4.9000000000000003552,1.1999999999999999555,'2-3 days',1,'2024-10-03 18:31:48.743428');
INSERT INTO products VALUES(82,7,'Telegram News Channel - 107,450 Subscribers','High quality telegram account with real and active followers. Perfect for marketing and business growth.',138.78999999999999204,8,4.2999999999999998223,1.6999999999999999555,'1-24 hours',1,'2025-06-07 01:57:07.832314');
INSERT INTO products VALUES(83,7,'Telegram News Channel - 271,634 Subscribers','High quality telegram account with real and active followers. Perfect for marketing and business growth.',420.35000000000002275,12,4.9000000000000003552,0.29999999999999998889,'2-3 days',1,'2024-10-15 08:12:10.908701');
INSERT INTO products VALUES(84,7,'Telegram News Channel - 296,610 Subscribers','High quality telegram account with real and active followers. Perfect for marketing and business growth.',575.21000000000003637,3,4.7000000000000001776,2.0,'Instant',1,'2025-06-08 01:25:56.127405');
INSERT INTO products VALUES(85,8,'Discord Server - 105,717 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',197.2400000000000091,1,4.9000000000000003552,0.5,'Instant',1,'2024-08-15 11:12:59.243284');
INSERT INTO products VALUES(86,8,'Discord Server - 24,218 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',40.649999999999998578,9,4.0999999999999996447,2.0,'2-3 days',1,'2025-04-29 12:42:40.106252');
INSERT INTO products VALUES(87,8,'Discord Server - 178,649 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',199.59999999999999431,13,4.0999999999999996447,1.1000000000000000888,'2-3 days',1,'2025-05-28 15:52:30.362697');
INSERT INTO products VALUES(88,8,'Discord Gaming Server - 988,907 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',1849.6099999999998999,8,4.7000000000000001776,1.6999999999999999555,'2-3 days',1,'2025-07-06 11:05:31.238625');
INSERT INTO products VALUES(89,8,'Discord Gaming Server - 16,943 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',30.089999999999999858,19,4.5999999999999996447,1.1000000000000000888,'1-24 hours',1,'2025-05-16 11:11:28.801629');
INSERT INTO products VALUES(90,8,'Discord Gaming Server - 598,348 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',551.16999999999995909,19,4.2000000000000001776,0.69999999999999995559,'1-24 hours',1,'2024-08-16 16:58:45.274383');
INSERT INTO products VALUES(91,8,'Discord Community - 32,685 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',20.190000000000001278,8,4.7999999999999998223,0.8000000000000000444,'Instant',1,'2024-09-23 22:18:53.820771');
INSERT INTO products VALUES(92,8,'Discord Community - 309,528 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',177.71999999999999885,19,4.5,0.4000000000000000222,'Instant',1,'2025-04-03 07:33:51.363701');
INSERT INTO products VALUES(93,8,'Discord Community - 22,309 Members','High quality discord account with real and active followers. Perfect for marketing and business growth.',33.299999999999997158,9,4.0999999999999996447,0.5,'Instant',1,'2024-09-30 12:31:06.471749');
INSERT INTO products VALUES(94,8,'Discord Bot - 4,440 Servers','High quality discord account with real and active followers. Perfect for marketing and business growth.',6.7199999999999997513,3,4.7000000000000001776,0.69999999999999995559,'24-48 hours',1,'2025-05-07 06:00:23.727953');
INSERT INTO products VALUES(95,8,'Discord Bot - 832,602 Servers','High quality discord account with real and active followers. Perfect for marketing and business growth.',1009.2300000000000181,4,4.0,1.1000000000000000888,'Instant',1,'2025-03-01 00:01:55.885661');
INSERT INTO products VALUES(96,8,'Discord Bot - 6,382 Servers','High quality discord account with real and active followers. Perfect for marketing and business growth.',9.2599999999999997868,19,4.7999999999999998223,1.8999999999999999111,'24-48 hours',1,'2025-03-21 08:35:57.023186');
INSERT INTO products VALUES(97,9,'Reddit Account - 273,607 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',276.93999999999999771,6,4.2999999999999998223,0.29999999999999998889,'24-48 hours',1,'2025-04-06 13:25:06.373532');
INSERT INTO products VALUES(98,9,'Reddit Account - 7,686 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',10.900000000000000354,12,4.2000000000000001776,0.59999999999999997779,'24-48 hours',1,'2025-04-19 01:22:44.499358');
INSERT INTO products VALUES(99,9,'Reddit Account - 20,716 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',15.369999999999999218,4,4.2000000000000001776,0.9000000000000000222,'1-24 hours',1,'2025-03-27 18:27:29.614501');
INSERT INTO products VALUES(100,9,'Reddit Account - 146,559 Post Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',168.2599999999999909,11,4.0,1.0,'1-24 hours',1,'2024-10-23 20:45:37.018056');
INSERT INTO products VALUES(101,9,'Reddit Account - 286,833 Post Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',354.91000000000002502,10,4.0,1.6999999999999999555,'24-48 hours',1,'2025-01-05 00:34:59.452265');
INSERT INTO products VALUES(102,9,'Reddit Account - 7,908 Post Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',14.560000000000000497,13,4.9000000000000003552,0.5,'Instant',1,'2025-01-26 13:55:11.154300');
INSERT INTO products VALUES(103,9,'Reddit Account - 19,454 Comment Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',35.649999999999998578,18,4.9000000000000003552,1.6000000000000000888,'Instant',1,'2024-08-22 23:28:20.374182');
INSERT INTO products VALUES(104,9,'Reddit Account - 588,450 Comment Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',919.16999999999995903,8,5.0,1.6000000000000000888,'Instant',1,'2024-10-16 11:01:28.506378');
INSERT INTO products VALUES(105,9,'Reddit Account - 85,405 Comment Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',78.189999999999997724,4,4.9000000000000003552,1.1999999999999999555,'24-48 hours',1,'2024-08-24 01:10:40.891922');
INSERT INTO products VALUES(106,9,'Reddit Aged Account - 39,011 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',64.670000000000001706,17,4.4000000000000003552,0.4000000000000000222,'1-24 hours',1,'2025-07-09 15:00:49.029392');
INSERT INTO products VALUES(107,9,'Reddit Aged Account - 20,626 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',16.510000000000001563,20,4.9000000000000003552,2.0,'24-48 hours',1,'2025-03-31 15:38:59.834686');
INSERT INTO products VALUES(108,9,'Reddit Aged Account - 4,070 Karma','High quality reddit account with real and active followers. Perfect for marketing and business growth.',7.7900000000000000355,13,4.9000000000000003552,1.3000000000000000444,'2-3 days',1,'2025-06-30 23:53:51.009887');
INSERT INTO products VALUES(109,10,'Pinterest Account - 728,292 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',1331.6099999999998999,8,4.5,0.10000000000000000555,'2-3 days',1,'2024-10-06 11:36:27.865796');
INSERT INTO products VALUES(110,10,'Pinterest Account - 2,586 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',8.5099999999999997868,14,4.4000000000000003552,1.3999999999999999111,'2-3 days',1,'2025-01-22 08:33:57.714779');
INSERT INTO products VALUES(111,10,'Pinterest Account - 1,417 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',10.849999999999999644,6,4.5,0.5,'Instant',1,'2025-02-27 03:09:11.177299');
INSERT INTO products VALUES(112,10,'Pinterest Business Account - 4,610 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',5.4900000000000002131,5,4.7999999999999998223,0.9000000000000000222,'2-3 days',1,'2025-06-11 12:50:04.154439');
INSERT INTO products VALUES(113,10,'Pinterest Business Account - 40,256 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',53.420000000000001706,19,4.7999999999999998223,0.9000000000000000222,'Instant',1,'2024-10-09 23:40:13.876243');
INSERT INTO products VALUES(114,10,'Pinterest Business Account - 23,191 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',16.379999999999999005,2,4.5999999999999996447,0.2000000000000000111,'1-24 hours',1,'2025-06-22 12:24:34.126101');
INSERT INTO products VALUES(115,10,'Pinterest Board - 8,216 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',14.759999999999999786,9,4.5999999999999996447,1.6000000000000000888,'Instant',1,'2025-03-21 14:55:52.155961');
INSERT INTO products VALUES(116,10,'Pinterest Board - 37,134 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',52.070000000000000285,16,4.7000000000000001776,1.3000000000000000444,'1-24 hours',1,'2024-11-27 20:47:05.979856');
INSERT INTO products VALUES(117,10,'Pinterest Board - 80,810 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',157.13999999999998635,15,4.0999999999999996447,0.5,'2-3 days',1,'2024-12-26 08:52:57.068740');
INSERT INTO products VALUES(118,10,'Pinterest Niche Account - 7,136 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',8.25,4,4.9000000000000003552,1.3000000000000000444,'24-48 hours',1,'2025-05-16 05:40:31.579914');
INSERT INTO products VALUES(119,10,'Pinterest Niche Account - 7,073 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',5.7400000000000002131,11,4.9000000000000003552,0.69999999999999995559,'1-24 hours',1,'2024-11-23 05:35:51.516007');
INSERT INTO products VALUES(120,10,'Pinterest Niche Account - 45,873 Followers','High quality pinterest account with real and active followers. Perfect for marketing and business growth.',35.210000000000000852,11,4.7000000000000001776,1.6999999999999999555,'24-48 hours',1,'2025-06-29 04:03:58.676546');
CREATE TABLE product_vendors (
	id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	vendor_id INTEGER NOT NULL, 
	price NUMERIC(10, 3) NOT NULL, 
	stock INTEGER, 
	is_active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES products (id), 
	FOREIGN KEY(vendor_id) REFERENCES vendors (id)
);
INSERT INTO product_vendors VALUES(1,1,2,73.150000000000005686,4,1,'2025-07-23 07:14:40.241180');
INSERT INTO product_vendors VALUES(2,2,12,34.299999999999997157,4,1,'2025-07-23 07:16:08.748518');
INSERT INTO product_vendors VALUES(3,2,15,42.85999999999999943,1,1,'2025-07-23 07:12:57.160695');
INSERT INTO product_vendors VALUES(4,3,15,10.490000000000000212,1,1,'2025-07-23 07:15:39.281025');
INSERT INTO product_vendors VALUES(5,3,9,11.359999999999999431,6,1,'2025-07-23 07:16:16.155860');
INSERT INTO product_vendors VALUES(6,3,10,13.960000000000000852,2,1,'2025-07-23 07:15:45.493894');
INSERT INTO product_vendors VALUES(7,4,14,185.53999999999999204,10,1,'2025-07-23 07:13:41.381515');
INSERT INTO product_vendors VALUES(8,4,9,182.71000000000000795,5,1,'2025-07-23 07:18:01.731373');
INSERT INTO product_vendors VALUES(9,4,12,198.59999999999999431,4,1,'2025-07-23 07:15:34.498930');
INSERT INTO product_vendors VALUES(10,5,6,75.150000000000005684,6,1,'2025-07-23 07:17:01.504788');
INSERT INTO product_vendors VALUES(11,5,4,71.069999999999993178,9,1,'2025-07-23 07:15:43.115571');
INSERT INTO product_vendors VALUES(12,5,3,69.569999999999993177,6,1,'2025-07-23 07:18:09.405977');
INSERT INTO product_vendors VALUES(13,6,11,620.59000000000003184,2,1,'2025-07-23 07:18:34.892091');
INSERT INTO product_vendors VALUES(14,6,14,632.66999999999995905,8,1,'2025-07-23 07:14:38.134513');
INSERT INTO product_vendors VALUES(15,6,5,665.71000000000003639,7,1,'2025-07-23 07:13:04.189568');
INSERT INTO product_vendors VALUES(16,7,14,53.75,8,1,'2025-07-23 07:16:59.872421');
INSERT INTO product_vendors VALUES(17,7,2,56.61999999999999744,6,1,'2025-07-23 07:15:20.465696');
INSERT INTO product_vendors VALUES(18,7,3,53.799999999999997156,1,1,'2025-07-23 07:15:27.981606');
INSERT INTO product_vendors VALUES(19,8,11,16,1,1,'2025-07-23 07:12:57.137428');
INSERT INTO product_vendors VALUES(20,8,6,16.149999999999998578,9,1,'2025-07-23 07:15:06.047055');
INSERT INTO product_vendors VALUES(21,9,11,33.460000000000000852,9,1,'2025-07-23 07:13:21.786456');
INSERT INTO product_vendors VALUES(22,9,7,30.739999999999998436,2,1,'2025-07-23 07:12:56.121480');
INSERT INTO product_vendors VALUES(23,9,12,32.520000000000003127,10,1,'2025-07-23 07:15:46.364155');
INSERT INTO product_vendors VALUES(24,10,2,102.71999999999999886,10,1,'2025-07-23 07:18:10.865466');
INSERT INTO product_vendors VALUES(25,11,9,299.61000000000001363,10,1,'2025-07-23 07:18:21.958282');
INSERT INTO product_vendors VALUES(26,12,2,39.649999999999998578,5,1,'2025-07-23 07:13:57.597452');
INSERT INTO product_vendors VALUES(27,12,5,30.519999999999999572,5,1,'2025-07-23 07:17:15.982216');
INSERT INTO product_vendors VALUES(28,13,6,6.4299999999999997157,1,1,'2025-07-23 07:18:04.170689');
INSERT INTO product_vendors VALUES(29,13,12,6.3700000000000001065,7,1,'2025-07-23 07:18:25.176193');
INSERT INTO product_vendors VALUES(30,13,1,4.7800000000000002486,8,1,'2025-07-23 07:14:19.285671');
INSERT INTO product_vendors VALUES(31,14,4,57.369999999999997442,6,1,'2025-07-23 07:17:04.304523');
INSERT INTO product_vendors VALUES(32,15,9,21.019999999999999574,8,1,'2025-07-23 07:14:46.486755');
INSERT INTO product_vendors VALUES(33,15,7,21.410000000000000142,8,1,'2025-07-23 07:16:53.793550');
INSERT INTO product_vendors VALUES(34,16,9,6.4900000000000002131,3,1,'2025-07-23 07:15:08.075722');
INSERT INTO product_vendors VALUES(35,17,6,166,6,1,'2025-07-23 07:14:01.405159');
INSERT INTO product_vendors VALUES(36,17,14,155.84000000000000341,4,1,'2025-07-23 07:12:54.877853');
INSERT INTO product_vendors VALUES(37,17,11,160.5,4,1,'2025-07-23 07:13:21.270797');
INSERT INTO product_vendors VALUES(38,18,10,7.7099999999999999644,3,1,'2025-07-23 07:16:46.699247');
INSERT INTO product_vendors VALUES(39,19,6,95.62999999999999545,9,1,'2025-07-23 07:13:55.460279');
INSERT INTO product_vendors VALUES(40,20,10,19.620000000000000994,2,1,'2025-07-23 07:17:24.457200');
INSERT INTO product_vendors VALUES(41,21,15,9.7599999999999997868,10,1,'2025-07-23 07:17:06.204570');
INSERT INTO product_vendors VALUES(42,21,14,7.0499999999999998223,6,1,'2025-07-23 07:13:26.070590');
INSERT INTO product_vendors VALUES(43,22,1,532.41999999999995909,4,1,'2025-07-23 07:15:46.087508');
INSERT INTO product_vendors VALUES(44,22,15,511.80000000000001134,2,1,'2025-07-23 07:13:57.731939');
INSERT INTO product_vendors VALUES(45,23,13,207.28999999999999203,8,1,'2025-07-23 07:14:49.889297');
INSERT INTO product_vendors VALUES(46,24,14,217.28999999999999205,4,1,'2025-07-23 07:13:19.445596');
INSERT INTO product_vendors VALUES(47,24,4,202.77000000000001023,9,1,'2025-07-23 07:14:33.058654');
INSERT INTO product_vendors VALUES(48,25,1,8.0099999999999997868,6,1,'2025-07-23 07:17:06.993609');
INSERT INTO product_vendors VALUES(49,25,15,9.1500000000000003552,7,1,'2025-07-23 07:12:51.951825');
INSERT INTO product_vendors VALUES(50,26,8,5.3700000000000001065,1,1,'2025-07-23 07:15:48.736318');
INSERT INTO product_vendors VALUES(51,26,3,5.0099999999999997868,8,1,'2025-07-23 07:18:32.965118');
INSERT INTO product_vendors VALUES(52,26,11,4.9000000000000003552,8,1,'2025-07-23 07:18:13.290564');
INSERT INTO product_vendors VALUES(53,27,8,11.55000000000000071,5,1,'2025-07-23 07:18:32.059339');
INSERT INTO product_vendors VALUES(54,27,3,12.980000000000000426,4,1,'2025-07-23 07:13:50.424793');
INSERT INTO product_vendors VALUES(55,28,13,495.60000000000002272,7,1,'2025-07-23 07:17:16.021081');
INSERT INTO product_vendors VALUES(56,28,14,405.93000000000000683,5,1,'2025-07-23 07:13:43.095375');
INSERT INTO product_vendors VALUES(57,29,8,10.419999999999999928,2,1,'2025-07-23 07:14:13.418008');
INSERT INTO product_vendors VALUES(58,29,9,10.470000000000000639,2,1,'2025-07-23 07:13:01.146772');
INSERT INTO product_vendors VALUES(59,29,2,11.609999999999999431,2,1,'2025-07-23 07:13:17.436743');
INSERT INTO product_vendors VALUES(60,30,7,76.790000000000006251,6,1,'2025-07-23 07:16:26.869161');
INSERT INTO product_vendors VALUES(61,30,10,86,1,1,'2025-07-23 07:14:43.595995');
INSERT INTO product_vendors VALUES(62,30,3,88.140000000000000568,8,1,'2025-07-23 07:17:21.798378');
INSERT INTO product_vendors VALUES(63,31,9,909.76999999999998182,10,1,'2025-07-23 07:14:10.210690');
INSERT INTO product_vendors VALUES(64,32,15,44.280000000000001138,7,1,'2025-07-23 07:14:55.078907');
INSERT INTO product_vendors VALUES(65,32,5,63.560000000000002272,7,1,'2025-07-23 07:12:59.902426');
INSERT INTO product_vendors VALUES(66,32,6,48.630000000000002556,9,1,'2025-07-23 07:16:53.826901');
INSERT INTO product_vendors VALUES(67,33,12,10.160000000000000142,5,1,'2025-07-23 07:17:53.735809');
INSERT INTO product_vendors VALUES(68,33,5,9.1199999999999992184,3,1,'2025-07-23 07:18:00.694058');
INSERT INTO product_vendors VALUES(69,34,1,1418.4600000000000363,1,1,'2025-07-23 07:18:03.342200');
INSERT INTO product_vendors VALUES(70,35,7,88.689999999999997726,5,1,'2025-07-23 07:13:17.852545');
INSERT INTO product_vendors VALUES(71,35,9,92.890000000000000571,9,1,'2025-07-23 07:14:35.457183');
INSERT INTO product_vendors VALUES(72,36,9,155.22999999999998976,5,1,'2025-07-23 07:16:07.635366');
INSERT INTO product_vendors VALUES(73,36,5,165.62000000000000454,6,1,'2025-07-23 07:15:07.189259');
INSERT INTO product_vendors VALUES(74,36,13,138.49999999999999999,3,1,'2025-07-23 07:15:55.997309');
INSERT INTO product_vendors VALUES(75,37,10,18.379999999999999005,1,1,'2025-07-23 07:13:59.257955');
INSERT INTO product_vendors VALUES(76,38,10,653.79999999999995454,7,1,'2025-07-23 07:13:38.386081');
INSERT INTO product_vendors VALUES(77,39,9,636.62999999999999546,7,1,'2025-07-23 07:17:32.494673');
INSERT INTO product_vendors VALUES(78,40,15,33.079999999999998294,6,1,'2025-07-23 07:13:24.474779');
INSERT INTO product_vendors VALUES(79,40,6,29.120000000000000994,10,1,'2025-07-23 07:15:30.553482');
INSERT INTO product_vendors VALUES(80,41,11,212.21000000000000795,5,1,'2025-07-23 07:15:49.502479');
INSERT INTO product_vendors VALUES(81,41,9,194.97999999999998977,10,1,'2025-07-23 07:16:05.816581');
INSERT INTO product_vendors VALUES(82,41,7,147.65000000000000568,3,1,'2025-07-23 07:15:12.306296');
INSERT INTO product_vendors VALUES(83,42,10,312.7599999999999909,9,1,'2025-07-23 07:16:53.046866');
INSERT INTO product_vendors VALUES(84,42,11,335.68000000000000682,8,1,'2025-07-23 07:14:37.305101');
INSERT INTO product_vendors VALUES(85,42,8,413.43999999999999773,1,1,'2025-07-23 07:16:59.714236');
INSERT INTO product_vendors VALUES(86,43,12,581.74000000000000909,2,1,'2025-07-23 07:13:33.286806');
INSERT INTO product_vendors VALUES(87,43,13,680.82000000000005,1,1,'2025-07-23 07:18:20.900055');
INSERT INTO product_vendors VALUES(88,43,3,521.60000000000002274,5,1,'2025-07-23 07:12:52.627846');
INSERT INTO product_vendors VALUES(89,44,13,139.3400000000000034,4,1,'2025-07-23 07:12:58.936832');
INSERT INTO product_vendors VALUES(90,45,15,145.0099999999999909,10,1,'2025-07-23 07:16:40.192833');
INSERT INTO product_vendors VALUES(91,45,13,118.28000000000000114,2,1,'2025-07-23 07:15:26.136811');
INSERT INTO product_vendors VALUES(92,45,2,129.53000000000000113,1,1,'2025-07-23 07:18:17.725014');
INSERT INTO product_vendors VALUES(93,46,6,10.75,8,1,'2025-07-23 07:15:36.085662');
INSERT INTO product_vendors VALUES(94,46,1,13.490000000000000213,4,1,'2025-07-23 07:18:09.360501');
INSERT INTO product_vendors VALUES(95,47,11,25.839999999999999857,6,1,'2025-07-23 07:12:52.019477');
INSERT INTO product_vendors VALUES(96,47,3,30.05000000000000071,6,1,'2025-07-23 07:17:21.839596');
INSERT INTO product_vendors VALUES(97,47,13,30.379999999999999006,3,1,'2025-07-23 07:14:07.610401');
INSERT INTO product_vendors VALUES(98,48,3,749.14999999999997725,5,1,'2025-07-23 07:17:55.831212');
INSERT INTO product_vendors VALUES(99,49,10,221.52000000000001023,4,1,'2025-07-23 07:18:02.800152');
INSERT INTO product_vendors VALUES(100,49,3,253.65000000000000569,4,1,'2025-07-23 07:17:51.523148');
INSERT INTO product_vendors VALUES(101,50,13,259.410000000000025,8,1,'2025-07-23 07:18:43.869530');
INSERT INTO product_vendors VALUES(102,50,14,299.37000000000000454,10,1,'2025-07-23 07:14:01.711277');
INSERT INTO product_vendors VALUES(103,50,7,324.06999999999999318,1,1,'2025-07-23 07:15:20.126286');
INSERT INTO product_vendors VALUES(104,51,3,434.35000000000002274,2,1,'2025-07-23 07:14:36.554815');
INSERT INTO product_vendors VALUES(105,51,10,442.97000000000002727,6,1,'2025-07-23 07:15:43.477196');
INSERT INTO product_vendors VALUES(106,51,8,480.80000000000001135,7,1,'2025-07-23 07:18:18.178201');
INSERT INTO product_vendors VALUES(107,52,12,13.609999999999999431,3,1,'2025-07-23 07:15:28.695474');
INSERT INTO product_vendors VALUES(108,52,11,12.179999999999999715,8,1,'2025-07-23 07:15:34.836089');
INSERT INTO product_vendors VALUES(109,52,6,15.380000000000000782,5,1,'2025-07-23 07:17:23.908264');
INSERT INTO product_vendors VALUES(110,53,12,546,6,1,'2025-07-23 07:15:30.967169');
INSERT INTO product_vendors VALUES(111,54,4,419.42000000000001589,6,1,'2025-07-23 07:14:56.274243');
INSERT INTO product_vendors VALUES(112,54,3,440.95999999999997954,2,1,'2025-07-23 07:17:36.005807');
INSERT INTO product_vendors VALUES(113,54,10,422.42000000000001591,10,1,'2025-07-23 07:14:03.982164');
INSERT INTO product_vendors VALUES(114,55,8,74.090000000000003411,4,1,'2025-07-23 07:13:46.288357');
INSERT INTO product_vendors VALUES(115,55,7,69.099999999999994317,10,1,'2025-07-23 07:17:37.076329');
INSERT INTO product_vendors VALUES(116,56,9,217.11000000000001365,1,1,'2025-07-23 07:13:58.654814');
INSERT INTO product_vendors VALUES(117,56,14,272.13999999999998636,3,1,'2025-07-23 07:13:48.073222');
INSERT INTO product_vendors VALUES(118,56,10,231.7599999999999909,3,1,'2025-07-23 07:14:46.777133');
INSERT INTO product_vendors VALUES(119,57,15,29.120000000000000994,7,1,'2025-07-23 07:13:15.444650');
INSERT INTO product_vendors VALUES(120,57,8,35.640000000000000568,7,1,'2025-07-23 07:13:15.597778');
INSERT INTO product_vendors VALUES(121,57,5,40.670000000000001705,9,1,'2025-07-23 07:15:50.725164');
INSERT INTO product_vendors VALUES(122,58,15,8.0399999999999991473,9,1,'2025-07-23 07:13:14.949649');
INSERT INTO product_vendors VALUES(123,59,5,119.84999999999999431,7,1,'2025-07-23 07:18:41.857354');
INSERT INTO product_vendors VALUES(124,59,4,112.40000000000000567,9,1,'2025-07-23 07:13:55.999621');
INSERT INTO product_vendors VALUES(125,60,12,47.579999999999998292,5,1,'2025-07-23 07:15:10.038700');
INSERT INTO product_vendors VALUES(126,60,11,49.469999999999998861,7,1,'2025-07-23 07:14:20.633414');
INSERT INTO product_vendors VALUES(127,61,5,7.4699999999999997513,9,1,'2025-07-23 07:15:34.982043');
INSERT INTO product_vendors VALUES(128,62,1,1265.9800000000000181,2,1,'2025-07-23 07:15:54.361915');
INSERT INTO product_vendors VALUES(129,62,13,1325.1500000000000909,10,1,'2025-07-23 07:13:36.150846');
INSERT INTO product_vendors VALUES(130,63,13,7.580000000000000071,9,1,'2025-07-23 07:17:07.197010');
INSERT INTO product_vendors VALUES(131,64,14,173.68999999999999772,1,1,'2025-07-23 07:17:14.893951');
INSERT INTO product_vendors VALUES(132,64,9,138.5800000000000125,1,1,'2025-07-23 07:12:49.283020');
INSERT INTO product_vendors VALUES(133,65,2,5.2599999999999997868,2,1,'2025-07-23 07:13:39.255180');
INSERT INTO product_vendors VALUES(134,65,7,6.1600000000000001421,9,1,'2025-07-23 07:14:02.863082');
INSERT INTO product_vendors VALUES(135,66,7,105.98000000000000397,1,1,'2025-07-23 07:12:49.921216');
INSERT INTO product_vendors VALUES(136,66,13,91.620000000000004544,7,1,'2025-07-23 07:18:19.901996');
INSERT INTO product_vendors VALUES(137,66,8,122.81999999999999317,10,1,'2025-07-23 07:18:42.562413');
INSERT INTO product_vendors VALUES(138,67,15,15.099999999999999644,2,1,'2025-07-23 07:14:19.214453');
INSERT INTO product_vendors VALUES(139,68,5,70.760000000000005115,6,1,'2025-07-23 07:13:50.146235');
INSERT INTO product_vendors VALUES(140,68,4,69.840000000000003409,2,1,'2025-07-23 07:18:47.075364');
INSERT INTO product_vendors VALUES(141,69,3,904.91999999999995904,6,1,'2025-07-23 07:14:46.510298');
INSERT INTO product_vendors VALUES(142,69,12,952.90999999999996816,5,1,'2025-07-23 07:15:38.272078');
INSERT INTO product_vendors VALUES(143,69,13,1218.7100000000000364,9,1,'2025-07-23 07:16:26.010796');
INSERT INTO product_vendors VALUES(144,70,1,175.52000000000001023,7,1,'2025-07-23 07:17:47.587215');
INSERT INTO product_vendors VALUES(145,71,2,7.580000000000000071,8,1,'2025-07-23 07:15:50.959797');
INSERT INTO product_vendors VALUES(146,71,1,9.4499999999999992894,5,1,'2025-07-23 07:17:50.372816');
INSERT INTO product_vendors VALUES(147,71,10,8.5700000000000002842,3,1,'2025-07-23 07:14:25.563575');
INSERT INTO product_vendors VALUES(148,72,15,28.059999999999998721,4,1,'2025-07-23 07:13:48.285191');
INSERT INTO product_vendors VALUES(149,73,8,1615.4900000000000091,10,1,'2025-07-23 07:13:28.142335');
INSERT INTO product_vendors VALUES(150,73,6,1778.8299999999999272,1,1,'2025-07-23 07:16:18.078374');
INSERT INTO product_vendors VALUES(151,74,6,42.719999999999998863,3,1,'2025-07-23 07:17:31.417042');
INSERT INTO product_vendors VALUES(152,74,5,40.820000000000000285,8,1,'2025-07-23 07:16:39.852373');
INSERT INTO product_vendors VALUES(153,75,5,123.73999999999999488,7,1,'2025-07-23 07:15:41.620798');
INSERT INTO product_vendors VALUES(154,75,13,117.56999999999999317,8,1,'2025-07-23 07:18:15.050795');
INSERT INTO product_vendors VALUES(155,76,14,6.3799999999999998934,4,1,'2025-07-23 07:14:02.374047');
INSERT INTO product_vendors VALUES(156,76,15,7.3499999999999996447,4,1,'2025-07-23 07:16:41.219049');
INSERT INTO product_vendors VALUES(157,77,5,23.269999999999999573,9,1,'2025-07-23 07:16:19.414571');
INSERT INTO product_vendors VALUES(158,77,8,20.339999999999999857,5,1,'2025-07-23 07:15:26.395717');
INSERT INTO product_vendors VALUES(159,77,4,20.379999999999999006,10,1,'2025-07-23 07:14:41.279517');
INSERT INTO product_vendors VALUES(160,78,1,35.229999999999996873,9,1,'2025-07-23 07:18:13.283606');
INSERT INTO product_vendors VALUES(161,78,8,35.570000000000000285,3,1,'2025-07-23 07:13:51.954290');
INSERT INTO product_vendors VALUES(162,78,6,41.689999999999997727,1,1,'2025-07-23 07:13:33.086630');
INSERT INTO product_vendors VALUES(163,79,10,1271.380000000000109,1,1,'2025-07-23 07:14:40.505154');
INSERT INTO product_vendors VALUES(164,79,8,1545.7999999999999545,9,1,'2025-07-23 07:13:42.882275');
INSERT INTO product_vendors VALUES(165,79,3,1228.7999999999999544,9,1,'2025-07-23 07:13:46.275056');
INSERT INTO product_vendors VALUES(166,80,5,285.32999999999998407,7,1,'2025-07-23 07:14:32.108276');
INSERT INTO product_vendors VALUES(167,81,9,1394.0399999999999636,10,1,'2025-07-23 07:13:57.754869');
INSERT INTO product_vendors VALUES(168,81,7,1584.3299999999999272,5,1,'2025-07-23 07:15:20.361944');
INSERT INTO product_vendors VALUES(169,81,10,1499.2899999999999636,3,1,'2025-07-23 07:12:49.352357');
INSERT INTO product_vendors VALUES(170,82,3,117.07999999999999829,6,1,'2025-07-23 07:18:43.900389');
INSERT INTO product_vendors VALUES(171,82,2,138.81000000000000227,8,1,'2025-07-23 07:14:41.342356');
INSERT INTO product_vendors VALUES(172,82,11,125.06000000000000227,1,1,'2025-07-23 07:18:40.048972');
INSERT INTO product_vendors VALUES(173,83,14,410.93999999999999772,6,1,'2025-07-23 07:18:23.101115');
INSERT INTO product_vendors VALUES(174,83,7,403.20999999999997953,2,1,'2025-07-23 07:16:59.287201');
INSERT INTO product_vendors VALUES(175,83,4,472.54000000000002047,4,1,'2025-07-23 07:17:03.800936');
INSERT INTO product_vendors VALUES(176,84,6,492.73000000000001818,6,1,'2025-07-23 07:16:11.639391');
INSERT INTO product_vendors VALUES(177,85,7,211.97999999999998976,5,1,'2025-07-23 07:18:28.541837');
INSERT INTO product_vendors VALUES(178,86,15,36.380000000000002557,2,1,'2025-07-23 07:17:33.776871');
INSERT INTO product_vendors VALUES(179,86,9,36.369999999999997441,3,1,'2025-07-23 07:16:35.458484');
INSERT INTO product_vendors VALUES(180,86,6,35.170000000000001705,10,1,'2025-07-23 07:18:27.905788');
INSERT INTO product_vendors VALUES(181,87,4,237.72999999999998976,4,1,'2025-07-23 07:15:09.920463');
INSERT INTO product_vendors VALUES(182,87,15,184.93999999999999772,8,1,'2025-07-23 07:14:01.561912');
INSERT INTO product_vendors VALUES(183,87,12,176.09999999999999431,9,1,'2025-07-23 07:18:38.644652');
INSERT INTO product_vendors VALUES(184,88,5,2096.9600000000000363,9,1,'2025-07-23 07:16:33.282108');
INSERT INTO product_vendors VALUES(185,89,5,31.539999999999999147,10,1,'2025-07-23 07:12:50.638365');
INSERT INTO product_vendors VALUES(186,89,14,33.25999999999999801,5,1,'2025-07-23 07:18:19.590486');
INSERT INTO product_vendors VALUES(187,90,11,559.62000000000000454,8,1,'2025-07-23 07:15:23.965731');
INSERT INTO product_vendors VALUES(188,90,13,630.88999999999998634,2,1,'2025-07-23 07:15:24.948270');
INSERT INTO product_vendors VALUES(189,91,3,23.989999999999998437,7,1,'2025-07-23 07:18:09.152333');
INSERT INTO product_vendors VALUES(190,91,11,21.55000000000000071,5,1,'2025-07-23 07:14:24.845710');
INSERT INTO product_vendors VALUES(191,91,10,18.679999999999999715,7,1,'2025-07-23 07:18:00.280652');
INSERT INTO product_vendors VALUES(192,92,2,179.88999999999998636,9,1,'2025-07-23 07:18:16.226413');
INSERT INTO product_vendors VALUES(193,93,2,37.090000000000003411,4,1,'2025-07-23 07:13:54.266918');
INSERT INTO product_vendors VALUES(194,93,1,28.469999999999998862,7,1,'2025-07-23 07:13:58.054140');
INSERT INTO product_vendors VALUES(195,93,12,30.190000000000001278,10,1,'2025-07-23 07:16:06.330211');
INSERT INTO product_vendors VALUES(196,94,3,7.1399999999999996802,7,1,'2025-07-23 07:14:20.705544');
INSERT INTO product_vendors VALUES(197,94,8,5.9100000000000001421,5,1,'2025-07-23 07:12:57.905956');
INSERT INTO product_vendors VALUES(198,95,11,870.65999999999996814,2,1,'2025-07-23 07:16:02.980982');
INSERT INTO product_vendors VALUES(199,95,5,1135.6600000000000818,8,1,'2025-07-23 07:13:23.230573');
INSERT INTO product_vendors VALUES(200,95,4,1207.2999999999999545,4,1,'2025-07-23 07:14:14.277635');
INSERT INTO product_vendors VALUES(201,96,7,8.5999999999999996447,4,1,'2025-07-23 07:17:10.138543');
INSERT INTO product_vendors VALUES(202,96,5,7.5499999999999998223,8,1,'2025-07-23 07:18:20.746625');
INSERT INTO product_vendors VALUES(203,96,14,9.8699999999999992184,3,1,'2025-07-23 07:14:00.018959');
INSERT INTO product_vendors VALUES(204,97,8,261.73000000000001818,4,1,'2025-07-23 07:15:59.467288');
INSERT INTO product_vendors VALUES(205,98,4,10.640000000000000568,5,1,'2025-07-23 07:14:27.492854');
INSERT INTO product_vendors VALUES(206,98,14,12.960000000000000853,2,1,'2025-07-23 07:13:24.760515');
INSERT INTO product_vendors VALUES(207,99,10,18.410000000000000142,7,1,'2025-07-23 07:17:00.678579');
INSERT INTO product_vendors VALUES(208,99,13,14.150000000000000355,6,1,'2025-07-23 07:15:08.976639');
INSERT INTO product_vendors VALUES(209,100,3,157.74000000000000909,3,1,'2025-07-23 07:18:24.525056');
INSERT INTO product_vendors VALUES(210,100,11,175.87000000000000454,6,1,'2025-07-23 07:13:10.380116');
INSERT INTO product_vendors VALUES(211,100,6,186.46999999999999885,4,1,'2025-07-23 07:13:45.271996');
INSERT INTO product_vendors VALUES(212,101,3,310.64999999999997725,9,1,'2025-07-23 07:12:57.695311');
INSERT INTO product_vendors VALUES(213,101,6,318.49000000000000909,4,1,'2025-07-23 07:13:42.489823');
INSERT INTO product_vendors VALUES(214,102,14,14.710000000000000852,8,1,'2025-07-23 07:14:51.515790');
INSERT INTO product_vendors VALUES(215,102,13,13.849999999999999644,9,1,'2025-07-23 07:13:56.436027');
INSERT INTO product_vendors VALUES(216,102,3,17.019999999999999573,5,1,'2025-07-23 07:14:48.151020');
INSERT INTO product_vendors VALUES(217,103,13,41.479999999999996873,3,1,'2025-07-23 07:15:46.088344');
INSERT INTO product_vendors VALUES(218,103,7,41.869999999999997441,1,1,'2025-07-23 07:15:26.645128');
INSERT INTO product_vendors VALUES(219,104,12,1005.3500000000000227,8,1,'2025-07-23 07:17:45.804533');
INSERT INTO product_vendors VALUES(220,105,10,65.25,10,1,'2025-07-23 07:15:09.547568');
INSERT INTO product_vendors VALUES(221,106,12,69.469999999999998861,4,1,'2025-07-23 07:13:02.413170');
INSERT INTO product_vendors VALUES(222,106,9,61.770000000000003124,2,1,'2025-07-23 07:14:28.165183');
INSERT INTO product_vendors VALUES(223,106,1,54.729999999999996871,2,1,'2025-07-23 07:14:11.488838');
INSERT INTO product_vendors VALUES(224,107,4,13.849999999999999644,5,1,'2025-07-23 07:18:18.013072');
INSERT INTO product_vendors VALUES(225,107,1,15.820000000000000283,9,1,'2025-07-23 07:14:32.235457');
INSERT INTO product_vendors VALUES(226,108,10,6.5199999999999995736,10,1,'2025-07-23 07:16:11.178272');
INSERT INTO product_vendors VALUES(227,109,11,1260.3900000000001,1,1,'2025-07-23 07:15:32.462246');
INSERT INTO product_vendors VALUES(228,110,9,9.4499999999999992894,9,1,'2025-07-23 07:17:26.989145');
INSERT INTO product_vendors VALUES(229,110,8,7.2000000000000001776,8,1,'2025-07-23 07:14:46.389718');
INSERT INTO product_vendors VALUES(230,110,7,7.1900000000000003907,8,1,'2025-07-23 07:15:38.505281');
INSERT INTO product_vendors VALUES(231,111,12,9.6600000000000001421,8,1,'2025-07-23 07:16:15.782140');
INSERT INTO product_vendors VALUES(232,111,4,12.689999999999999503,6,1,'2025-07-23 07:16:23.281802');
INSERT INTO product_vendors VALUES(233,111,10,9.0700000000000002842,4,1,'2025-07-23 07:15:53.711161');
INSERT INTO product_vendors VALUES(234,112,7,6.4199999999999999289,5,1,'2025-07-23 07:15:30.128896');
INSERT INTO product_vendors VALUES(235,113,4,57.149999999999998578,6,1,'2025-07-23 07:17:15.142439');
INSERT INTO product_vendors VALUES(236,113,8,60.920000000000001706,3,1,'2025-07-23 07:12:54.977904');
INSERT INTO product_vendors VALUES(237,114,1,14.609999999999999431,2,1,'2025-07-23 07:18:38.969688');
INSERT INTO product_vendors VALUES(238,114,13,13.480000000000000425,1,1,'2025-07-23 07:13:36.969873');
INSERT INTO product_vendors VALUES(239,115,1,14.310000000000000497,1,1,'2025-07-23 07:15:04.233204');
INSERT INTO product_vendors VALUES(240,115,15,15.230000000000000426,8,1,'2025-07-23 07:13:29.880013');
INSERT INTO product_vendors VALUES(241,116,6,56.780000000000001138,3,1,'2025-07-23 07:17:21.530268');
INSERT INTO product_vendors VALUES(242,116,10,59.479999999999996875,6,1,'2025-07-23 07:12:49.241619');
INSERT INTO product_vendors VALUES(243,117,2,173.15000000000000568,2,1,'2025-07-23 07:15:45.915463');
INSERT INTO product_vendors VALUES(244,117,7,152.87999999999999545,2,1,'2025-07-23 07:13:23.047945');
INSERT INTO product_vendors VALUES(245,117,1,174.40999999999999658,1,1,'2025-07-23 07:18:39.432737');
INSERT INTO product_vendors VALUES(246,118,3,8.7300000000000004263,9,1,'2025-07-23 07:16:05.274350');
INSERT INTO product_vendors VALUES(247,118,9,8.3499999999999996447,3,1,'2025-07-23 07:13:05.540819');
INSERT INTO product_vendors VALUES(248,118,5,9.5999999999999996447,7,1,'2025-07-23 07:15:39.974313');
INSERT INTO product_vendors VALUES(249,119,2,6.4599999999999999644,7,1,'2025-07-23 07:12:59.422722');
INSERT INTO product_vendors VALUES(250,119,15,5.1200000000000001065,4,1,'2025-07-23 07:15:49.961597');
INSERT INTO product_vendors VALUES(251,119,12,5.2699999999999995736,7,1,'2025-07-23 07:13:10.279530');
INSERT INTO product_vendors VALUES(252,120,5,29.210000000000000852,3,1,'2025-07-23 07:17:43.210236');
INSERT INTO product_vendors VALUES(253,120,10,38.210000000000000851,4,1,'2025-07-23 07:15:24.716565');
CREATE TABLE orders (
	id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	vendor_id INTEGER NOT NULL, 
	customer_email VARCHAR(120) NOT NULL, 
	quantity INTEGER NOT NULL, 
	unit_price NUMERIC(10, 3) NOT NULL, 
	total_price NUMERIC(10, 3) NOT NULL, 
	payment_method VARCHAR(50) NOT NULL, 
	coupon_code VARCHAR(50), 
	subscribe_newsletter BOOLEAN, 
	status VARCHAR(20), 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES products (id), 
	FOREIGN KEY(vendor_id) REFERENCES vendors (id)
);
INSERT INTO orders VALUES(1,60,11,'sarawilson@example.net',1,49.469999999999998861,49.469999999999998861,'Bitcoin',NULL,0,'processing','2025-07-23 07:16:41.955101');
INSERT INTO orders VALUES(2,90,13,'johnsoncharles@example.net',1,630.88999999999998634,630.88999999999998634,'PayPal',NULL,1,'completed','2025-07-23 07:18:39.842638');
INSERT INTO orders VALUES(3,29,8,'kimberlysosa@example.org',4,10.419999999999999928,41.679999999999999714,'Credit Card',NULL,1,'processing','2025-07-23 07:17:20.768089');
INSERT INTO orders VALUES(4,91,3,'frank95@example.org',2,23.989999999999998437,47.979999999999996874,'USDT',NULL,1,'completed','2025-07-23 07:18:05.795078');
INSERT INTO orders VALUES(5,30,7,'catherine03@example.org',3,76.790000000000006251,230.37000000000000454,'Ethereum','LIKE',0,'pending','2025-07-23 07:16:51.849337');
INSERT INTO orders VALUES(6,106,12,'agreene@example.org',5,69.469999999999998861,347.35000000000002273,'USDT',NULL,1,'completed','2025-07-23 07:18:03.291533');
INSERT INTO orders VALUES(7,38,10,'smithholly@example.org',5,653.79999999999995454,3269,'Ethereum','MOVE',1,'processing','2025-07-23 07:16:24.961327');
INSERT INTO orders VALUES(8,96,7,'rharris@example.org',5,8.5999999999999996447,43,'USDT',NULL,1,'pending','2025-07-23 07:17:04.713241');
INSERT INTO orders VALUES(9,10,2,'kspears@example.com',4,102.71999999999999886,410.87999999999999544,'Bitcoin','DESPITE',1,'pending','2025-07-23 07:18:01.668207');
INSERT INTO orders VALUES(10,95,11,'kelly52@example.org',3,870.65999999999996814,2611.9800000000000181,'Credit Card','RECORD',0,'processing','2025-07-23 07:17:46.448573');
INSERT INTO orders VALUES(11,86,9,'howellryan@example.org',1,36.369999999999997441,36.369999999999997441,'Ethereum',NULL,1,'cancelled','2025-07-23 07:16:37.935017');
INSERT INTO orders VALUES(12,5,3,'riverakevin@example.com',1,69.569999999999993177,69.569999999999993177,'PayPal',NULL,1,'pending','2025-07-23 07:17:53.232603');
INSERT INTO orders VALUES(13,76,15,'masontracey@example.com',2,7.3499999999999996447,14.699999999999999289,'USDT',NULL,0,'processing','2025-07-23 07:15:53.035425');
INSERT INTO orders VALUES(14,66,13,'pittssherry@example.net',2,91.620000000000004544,183.24000000000000908,'Credit Card',NULL,0,'cancelled','2025-07-23 07:16:06.525971');
INSERT INTO orders VALUES(15,27,8,'millerearl@example.com',4,11.55000000000000071,46.200000000000002843,'Bitcoin',NULL,0,'completed','2025-07-23 07:16:15.708966');
INSERT INTO orders VALUES(16,65,7,'foxjermaine@example.com',1,6.1600000000000001421,6.1600000000000001421,'PayPal',NULL,0,'completed','2025-07-23 07:18:20.050524');
INSERT INTO orders VALUES(17,9,12,'psampson@example.net',3,32.520000000000003127,97.560000000000002273,'Credit Card','LET',0,'pending','2025-07-23 07:16:17.600087');
INSERT INTO orders VALUES(18,29,2,'jake39@example.net',1,11.609999999999999431,11.609999999999999431,'Credit Card',NULL,1,'processing','2025-07-23 07:16:50.220850');
INSERT INTO orders VALUES(19,111,12,'ingramcathy@example.com',5,9.6600000000000001421,48.299999999999997158,'Credit Card',NULL,0,'processing','2025-07-23 07:16:42.534583');
INSERT INTO orders VALUES(20,118,9,'justinjones@example.net',4,8.3499999999999996447,33.399999999999998578,'Bitcoin',NULL,1,'cancelled','2025-07-23 07:17:37.976427');
INSERT INTO orders VALUES(21,67,15,'christopher68@example.org',5,15.099999999999999644,75.500000000000000001,'PayPal',NULL,0,'processing','2025-07-23 07:17:42.661549');
INSERT INTO orders VALUES(22,69,13,'curtisjoseph@example.org',3,1218.7100000000000364,3656.1300000000001091,'Credit Card',NULL,1,'pending','2025-07-23 07:17:22.956975');
INSERT INTO orders VALUES(23,12,2,'russelldixon@example.net',2,39.649999999999998578,79.299999999999997157,'Bitcoin',NULL,0,'pending','2025-07-23 07:16:56.809558');
INSERT INTO orders VALUES(24,100,6,'bedwards@example.com',2,186.46999999999999885,372.93999999999999771,'Credit Card',NULL,1,'pending','2025-07-23 07:17:43.153829');
INSERT INTO orders VALUES(25,18,10,'jasmin62@example.org',1,7.7099999999999999644,7.7099999999999999644,'Ethereum',NULL,1,'completed','2025-07-23 07:18:33.568171');
INSERT INTO orders VALUES(26,60,11,'jaymartinez@example.org',3,49.469999999999998861,148.40999999999999658,'PayPal',NULL,0,'pending','2025-07-23 07:17:38.168835');
INSERT INTO orders VALUES(27,87,12,'xmiddleton@example.org',1,176.09999999999999431,176.09999999999999431,'USDT','AVOID',0,'processing','2025-07-23 07:18:40.886474');
INSERT INTO orders VALUES(28,7,3,'zbarr@example.org',5,53.799999999999997156,269,'Bitcoin',NULL,1,'cancelled','2025-07-23 07:16:07.704315');
INSERT INTO orders VALUES(29,114,13,'joshuaberry@example.com',3,13.480000000000000425,40.439999999999997727,'Ethereum',NULL,0,'cancelled','2025-07-23 07:16:26.697615');
INSERT INTO orders VALUES(30,41,7,'tammiemelton@example.org',2,147.65000000000000568,295.30000000000001136,'USDT',NULL,1,'processing','2025-07-23 07:16:52.087249');
INSERT INTO orders VALUES(31,87,12,'bowenphillip@example.com',4,176.09999999999999431,704.39999999999997727,'Ethereum','PROTECT',0,'completed','2025-07-23 07:16:42.092079');
INSERT INTO orders VALUES(32,28,14,'melinda33@example.org',3,405.93000000000000683,1217.7899999999999636,'USDT','MONTH',0,'pending','2025-07-23 07:17:01.665710');
INSERT INTO orders VALUES(33,57,5,'zcross@example.com',1,40.670000000000001705,40.670000000000001705,'Ethereum',NULL,0,'processing','2025-07-23 07:18:39.230886');
INSERT INTO orders VALUES(34,74,5,'larry53@example.com',1,40.820000000000000285,40.820000000000000285,'Bitcoin','FLOOR',1,'cancelled','2025-07-23 07:18:05.780177');
INSERT INTO orders VALUES(35,95,5,'heatherking@example.com',3,1135.6600000000000818,3406.9800000000000181,'Bitcoin',NULL,1,'processing','2025-07-23 07:17:43.738595');
INSERT INTO orders VALUES(36,57,8,'wspence@example.com',5,35.640000000000000568,178.19999999999998862,'Bitcoin','ANALYSIS',0,'pending','2025-07-23 07:17:23.602476');
INSERT INTO orders VALUES(37,80,5,'popemelissa@example.net',1,285.32999999999998407,285.32999999999998407,'Credit Card',NULL,1,'completed','2025-07-23 07:16:04.746948');
INSERT INTO orders VALUES(38,114,13,'yhernandez@example.net',2,13.480000000000000425,26.960000000000000851,'PayPal','GAS',1,'processing','2025-07-23 07:15:57.253139');
INSERT INTO orders VALUES(39,90,11,'emilychavez@example.net',1,559.62000000000000454,559.62000000000000454,'Credit Card',NULL,0,'cancelled','2025-07-23 07:17:42.469900');
INSERT INTO orders VALUES(40,67,15,'cmccoy@example.com',1,15.099999999999999644,15.099999999999999644,'Credit Card',NULL,0,'processing','2025-07-23 07:16:08.110544');
INSERT INTO orders VALUES(41,46,6,'robertsdenise@example.net',3,10.75,32.249999999999999999,'USDT',NULL,0,'cancelled','2025-07-23 07:17:04.651672');
INSERT INTO orders VALUES(42,111,10,'laurataylor@example.org',4,9.0700000000000002842,36.280000000000001136,'Ethereum',NULL,1,'pending','2025-07-23 07:17:39.426624');
INSERT INTO orders VALUES(43,65,2,'kowens@example.net',4,5.2599999999999997868,21.039999999999999147,'PayPal','LETTER',1,'cancelled','2025-07-23 07:16:28.749150');
INSERT INTO orders VALUES(44,54,4,'rchang@example.com',1,419.42000000000001589,419.42000000000001589,'Credit Card','FUTURE',1,'pending','2025-07-23 07:18:47.383029');
INSERT INTO orders VALUES(45,93,12,'david12@example.com',1,30.190000000000001278,30.190000000000001278,'Bitcoin',NULL,1,'processing','2025-07-23 07:18:04.857520');
INSERT INTO orders VALUES(46,62,1,'flee@example.com',1,1265.9800000000000181,1265.9800000000000181,'PayPal','LANGUAGE',1,'processing','2025-07-23 07:17:41.076752');
INSERT INTO orders VALUES(47,111,10,'dyeroscar@example.com',5,9.0700000000000002842,45.350000000000001421,'Ethereum','SIMILAR',1,'completed','2025-07-23 07:17:58.973752');
INSERT INTO orders VALUES(48,119,15,'owatson@example.com',2,5.1200000000000001065,10.240000000000000213,'Credit Card',NULL,0,'completed','2025-07-23 07:18:35.780122');
INSERT INTO orders VALUES(49,96,14,'sabrinahunter@example.org',4,9.8699999999999992184,39.479999999999996873,'USDT',NULL,0,'processing','2025-07-23 07:16:54.770869');
INSERT INTO orders VALUES(50,110,7,'jasonlee@example.org',4,7.1900000000000003907,28.760000000000001563,'Credit Card',NULL,1,'pending','2025-07-23 07:18:26.315032');
INSERT INTO orders VALUES(51,120,10,'pscott@example.org',4,38.210000000000000851,152.84000000000000341,'Bitcoin',NULL,0,'processing','2025-07-23 07:16:47.778541');
INSERT INTO orders VALUES(52,45,2,'bradley41@example.org',5,129.53000000000000113,647.64999999999997726,'Ethereum',NULL,0,'completed','2025-07-23 07:17:15.333531');
INSERT INTO orders VALUES(53,105,10,'john38@example.com',3,65.25,195.74999999999999999,'Bitcoin',NULL,0,'completed','2025-07-23 07:16:02.452156');
INSERT INTO orders VALUES(54,28,14,'zlynn@example.org',4,405.93000000000000683,1623.7200000000000273,'Bitcoin',NULL,0,'processing','2025-07-23 07:16:29.566820');
INSERT INTO orders VALUES(55,1,2,'garciamarc@example.net',1,73.150000000000005686,73.150000000000005686,'Ethereum',NULL,0,'pending','2025-07-23 07:17:29.985522');
INSERT INTO orders VALUES(56,24,14,'alexanderpaul@example.net',4,217.28999999999999205,869.1599999999999682,'PayPal','LOCAL',1,'pending','2025-07-23 07:16:35.724167');
INSERT INTO orders VALUES(57,13,12,'ericking@example.org',2,6.3700000000000001065,12.740000000000000213,'Ethereum',NULL,0,'processing','2025-07-23 07:15:49.583530');
INSERT INTO orders VALUES(58,28,14,'ppeterson@example.net',5,405.93000000000000683,2029.6500000000000909,'PayPal',NULL,0,'pending','2025-07-23 07:18:07.457482');
INSERT INTO orders VALUES(59,42,10,'timothy57@example.org',4,312.7599999999999909,1251.0399999999999635,'Bitcoin','DESIGN',1,'completed','2025-07-23 07:16:51.631980');
INSERT INTO orders VALUES(60,45,2,'diane95@example.org',4,129.53000000000000113,518.12000000000000454,'Ethereum',NULL,1,'processing','2025-07-23 07:16:51.844898');
INSERT INTO orders VALUES(61,31,9,'kathyharris@example.org',2,909.76999999999998182,1819.5399999999999636,'Ethereum',NULL,1,'pending','2025-07-23 07:18:12.043175');
INSERT INTO orders VALUES(62,35,9,'guerramorgan@example.net',5,92.890000000000000571,464.44999999999998863,'USDT','MORNING',1,'processing','2025-07-23 07:16:30.819290');
INSERT INTO orders VALUES(63,51,8,'marthale@example.net',3,480.80000000000001135,1442.4000000000000909,'USDT',NULL,0,'processing','2025-07-23 07:16:53.326168');
INSERT INTO orders VALUES(64,18,10,'wilkersonandrea@example.com',4,7.7099999999999999644,30.839999999999999857,'Credit Card','SECURITY',1,'processing','2025-07-23 07:17:28.430283');
INSERT INTO orders VALUES(65,90,13,'michelle01@example.org',1,630.88999999999998634,630.88999999999998634,'Credit Card',NULL,0,'completed','2025-07-23 07:16:37.188300');
INSERT INTO orders VALUES(66,65,2,'christopher24@example.com',3,5.2599999999999997868,15.77999999999999936,'Credit Card',NULL,1,'processing','2025-07-23 07:17:26.652889');
INSERT INTO orders VALUES(67,116,10,'connerkristina@example.org',2,59.479999999999996875,118.95999999999999374,'USDT',NULL,1,'processing','2025-07-23 07:16:05.442365');
INSERT INTO orders VALUES(68,116,6,'castrobryan@example.com',2,56.780000000000001138,113.56000000000000227,'Bitcoin',NULL,0,'processing','2025-07-23 07:18:19.985882');
INSERT INTO orders VALUES(69,116,10,'stephenreed@example.net',2,59.479999999999996875,118.95999999999999374,'Bitcoin','YET',0,'completed','2025-07-23 07:17:38.380441');
INSERT INTO orders VALUES(70,113,4,'mitchellgates@example.org',2,57.149999999999998578,114.29999999999999715,'Ethereum',NULL,0,'cancelled','2025-07-23 07:17:18.132496');
INSERT INTO orders VALUES(71,70,1,'wgallagher@example.net',1,175.52000000000001023,175.52000000000001023,'Credit Card',NULL,1,'completed','2025-07-23 07:18:44.994372');
INSERT INTO orders VALUES(72,116,10,'susanshepard@example.org',1,59.479999999999996875,59.479999999999996875,'Credit Card',NULL,0,'cancelled','2025-07-23 07:16:28.830510');
INSERT INTO orders VALUES(73,7,2,'brianasolis@example.com',1,56.61999999999999744,56.61999999999999744,'PayPal','PRODUCT',1,'pending','2025-07-23 07:16:36.971023');
INSERT INTO orders VALUES(74,53,12,'aliciamahoney@example.net',1,546,546,'Ethereum','WINDOW',1,'processing','2025-07-23 07:16:21.133666');
INSERT INTO orders VALUES(75,13,1,'davidmiller@example.com',1,4.7800000000000002486,4.7800000000000002486,'Bitcoin',NULL,0,'cancelled','2025-07-23 07:16:40.836859');
INSERT INTO orders VALUES(76,59,5,'ilewis@example.net',3,119.84999999999999431,359.55000000000001136,'Ethereum',NULL,0,'completed','2025-07-23 07:17:31.261685');
INSERT INTO orders VALUES(77,28,14,'thomasharmon@example.org',1,405.93000000000000683,405.93000000000000683,'Ethereum',NULL,1,'cancelled','2025-07-23 07:16:48.303936');
INSERT INTO orders VALUES(78,120,10,'angelapadilla@example.net',1,38.210000000000000851,38.210000000000000851,'Ethereum',NULL,0,'cancelled','2025-07-23 07:17:50.783893');
INSERT INTO orders VALUES(79,100,11,'susan58@example.net',1,175.87000000000000454,175.87000000000000454,'Credit Card',NULL,0,'processing','2025-07-23 07:18:02.237509');
INSERT INTO orders VALUES(80,114,13,'hayley60@example.net',5,13.480000000000000425,67.400000000000005683,'Credit Card','WORD',1,'cancelled','2025-07-23 07:17:08.515237');
INSERT INTO orders VALUES(81,60,12,'lisagonzalez@example.net',3,47.579999999999998292,142.74000000000000909,'USDT','MIGHT',1,'processing','2025-07-23 07:16:33.442008');
INSERT INTO orders VALUES(82,70,1,'krystallara@example.net',5,175.52000000000001023,877.60000000000002277,'Bitcoin',NULL,0,'cancelled','2025-07-23 07:18:29.004372');
INSERT INTO orders VALUES(83,114,1,'daniellebarker@example.com',5,14.609999999999999431,73.049999999999997157,'Ethereum',NULL,0,'completed','2025-07-23 07:17:43.716282');
INSERT INTO orders VALUES(84,68,4,'daniel65@example.org',5,69.840000000000003409,349.19999999999998862,'USDT',NULL,1,'pending','2025-07-23 07:16:28.945035');
INSERT INTO orders VALUES(85,11,9,'daltonsonya@example.org',2,299.61000000000001363,599.22000000000002727,'Credit Card',NULL,0,'pending','2025-07-23 07:17:50.670658');
INSERT INTO orders VALUES(86,43,12,'erica40@example.org',5,581.74000000000000909,2908.6999999999998182,'USDT','MAYBE',0,'processing','2025-07-23 07:18:32.154574');
INSERT INTO orders VALUES(87,90,11,'kennethburns@example.net',4,559.62000000000000454,2238.4800000000000181,'USDT',NULL,1,'completed','2025-07-23 07:17:49.315562');
INSERT INTO orders VALUES(88,46,1,'andrea18@example.net',2,13.490000000000000213,26.980000000000000427,'Ethereum','SHARE',1,'cancelled','2025-07-23 07:16:27.508171');
INSERT INTO orders VALUES(89,111,4,'jonesderrick@example.org',1,12.689999999999999503,12.689999999999999503,'Bitcoin','HOSPITAL',0,'completed','2025-07-23 07:16:02.597199');
INSERT INTO orders VALUES(90,86,9,'murphyelizabeth@example.com',5,36.369999999999997441,181.84999999999999432,'PayPal',NULL,1,'processing','2025-07-23 07:17:18.319427');
INSERT INTO orders VALUES(91,87,4,'jpatterson@example.com',2,237.72999999999998976,475.45999999999997952,'USDT',NULL,0,'cancelled','2025-07-23 07:16:58.017430');
INSERT INTO orders VALUES(92,51,10,'avilatoni@example.com',4,442.97000000000002727,1771.880000000000109,'Ethereum',NULL,0,'pending','2025-07-23 07:18:42.595958');
INSERT INTO orders VALUES(93,102,13,'xhall@example.net',4,13.849999999999999644,55.399999999999998577,'Bitcoin',NULL,0,'processing','2025-07-23 07:16:54.252968');
INSERT INTO orders VALUES(94,28,13,'woodpatricia@example.net',4,495.60000000000002272,1982.4000000000000909,'Credit Card',NULL,1,'processing','2025-07-23 07:16:51.515930');
INSERT INTO orders VALUES(95,4,14,'lukecurtis@example.org',2,185.53999999999999204,371.07999999999998408,'Ethereum',NULL,0,'processing','2025-07-23 07:16:49.205385');
INSERT INTO orders VALUES(96,94,8,'diazrobert@example.org',4,5.9100000000000001421,23.640000000000000568,'Bitcoin',NULL,1,'completed','2025-07-23 07:17:35.463437');
INSERT INTO orders VALUES(97,32,6,'paulcastro@example.org',5,48.630000000000002556,243.15000000000000569,'PayPal',NULL,1,'cancelled','2025-07-23 07:16:46.182519');
INSERT INTO orders VALUES(98,55,7,'michellejohnson@example.net',3,69.099999999999994317,207.30000000000001136,'Ethereum',NULL,1,'cancelled','2025-07-23 07:16:23.142201');
INSERT INTO orders VALUES(99,96,14,'megan62@example.com',4,9.8699999999999992184,39.479999999999996873,'USDT','EXIST',1,'completed','2025-07-23 07:16:13.557032');
INSERT INTO orders VALUES(100,43,12,'gordonbrian@example.org',3,581.74000000000000909,1745.2200000000000272,'Credit Card','LIGHT',1,'cancelled','2025-07-23 07:16:04.889663');
COMMIT;
