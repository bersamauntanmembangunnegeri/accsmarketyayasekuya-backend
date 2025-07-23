PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
INSERT INTO categories VALUES(1,'Facebook Accounts','facebook-accounts','High-quality Facebook accounts for various purposes',NULL,1,'2025-07-23 11:05:36.163343');
INSERT INTO categories VALUES(2,'Instagram Accounts','instagram-accounts','Premium Instagram accounts with various features',NULL,1,'2025-07-23 11:05:36.163347');
INSERT INTO categories VALUES(3,'Facebook Softregs','facebook-softregs','Facebook accounts registered with software',1,1,'2025-07-23 11:05:36.167943');
INSERT INTO categories VALUES(4,'Facebook With friends','facebook-with-friends','Facebook accounts with existing friends',1,1,'2025-07-23 11:05:36.167946');
INSERT INTO categories VALUES(5,'Instagram Softreg','instagram-softreg','Instagram accounts registered with software',2,1,'2025-07-23 11:05:36.167947');
INSERT INTO categories VALUES(6,'Instagram Aged','instagram-aged','Aged Instagram accounts',2,1,'2025-07-23 11:05:36.167947');
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
INSERT INTO footer_settings VALUES(1,'ACCS market.com','Buy or Sell Social Media Accounts (PVA & Cheap). Your trusted marketplace for social media accounts.','ACCS','market.com','#','Globe','#','Mail','#','MessageCircle','[{"label": "Home", "url": "#"}, {"label": "Categories", "url": "#"}, {"label": "Search Accounts", "url": "#"}, {"label": "Become a Seller", "url": "#"}]','[{"label": "FAQ", "url": "#"}, {"label": "Terms of Use", "url": "#"}, {"label": "Privacy Policy", "url": "#"}, {"label": "Contact Support", "url": "#"}]','support@accsmarket.com','accsmarket.news','24/7 Support Available','Secure Transactions','© 2024 AccsMarket.com. All rights reserved.','["BTC", "USDT", "ETH", "PayPal"]','bg-gray-800','text-white','2025-07-23 11:08:38.790200','2025-07-23 11:08:38.790204');
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
INSERT INTO products VALUES(1,3,'FB Accounts | Verified by e-mail, there is no email in the set. Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.','High quality Facebook accounts verified by email',0.27800000000000002486,345,4.5999999999999996447,2.1000000000000000888,'48h',1,'2025-07-23 11:05:36.172477');
INSERT INTO products VALUES(2,3,'FB Accounts | Verified by email (email not included). Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.','Facebook soft registered accounts from USA',0.29599999999999998534,1648,4.7999999999999998223,2.7000000000000001776,'48h',1,'2025-07-23 11:05:36.172479');
INSERT INTO products VALUES(3,4,'FB Accounts | The number of subscribers is 50+. Verified by e-mail, there is no email in the set. Male and female. The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Token are included in the package. Accounts are registered in Bangladesh IP.','Facebook accounts with 50+ subscribers',0.99899999999999999911,27,4.5999999999999996447,0.69999999999999995559,'48h',1,'2025-07-23 11:05:36.172479');
INSERT INTO products VALUES(4,5,'IG Accounts | Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.','Instagram soft registered accounts from USA',0.182999999999999996,99,4.9000000000000003552,1.6000000000000000888,'48h',1,'2025-07-23 11:05:36.172480');
INSERT INTO products VALUES(5,6,'IG Accounts | Aged accounts 2019-2021. Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.','Aged Instagram accounts from USA',0.6989999999999999547,524,4.9000000000000003552,2.0,'48h',1,'2025-07-23 11:05:36.172480');
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
COMMIT;
