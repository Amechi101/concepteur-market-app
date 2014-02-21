/* 
Database table for Indieitude

@Authors:

Amechi Egbe
Yeshwant Dasari 
August Tan

*/

/**************** User tables ********************/

create table Users (
  uid bigint unsigned not null auto_increment,
  email varchar(255) unique not null,
  password varchar(255) not null,
  u_points int not null,
  u_title varchar(255),
  user_name varchar(255),
  f_name varchar(255),
  l_name varchar(255),
  birthday date,
  city varchar(50),
  state varchar(2),
  primary key (uid)
);


/************** Product tables  *****************/


--Product Information

create table Product (
  pid bigint unsigned not null auto_increment,
  pro_name varchar(255),
  pro_desc text,
  color_name varchar(255),
  size_types varchar(7),
  fiber_context text,
  pro_price unsigned decimal(6,2) not null, /* better practice to use decimals to store in the database */
  pro_tags varchar(255),
  made_ny boolean,
  novelty varchar(255),
  primary key (product_id),
  foreign key (pro_img_id) references product_images(pro_img_id),
  foreign key (d_id) references designer(did)
);


/*
 * Represents a type of products, e.g. "shirt", accessories or "shoes", increasing uniformity
 * in product table without introducing ambiguity.
 */

create table Product_types (
  pro_types_id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (pro_types_id)
);


--Product Images

create table Product_images (
  pro_img_id bigint unsigned not null auto_increment,
  pro_img_filename varchar(255), /* changed from data type mediumblob --> filename as the images will be stored in the server instead for a lighter database */
  pid bigint unsigned not null,
  did bigint unsigned not null,
  primary key (pro_img_id),
  foreign key (pid) references product (pid),
  foreign key (did) references designer (did)
);

--Tables for users likes/comments on the product

create table Product_likes (
  uid bigint unsigned not null, /* the person who liked the product */
  pid bigint unsigned not null,
  liked boolean,
  primary key (uid, pid),
  foreign key (uid) references users(uid),
  foreign key (pid) references product(pid)
);


create table Product_Comments (
  uid bigint unsigned not null, /* the comment's author */
  pid bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (uid, time_posted),
  foreign key (uid) references users(uid),
  foreign key (pid) references product(pid)
);


/*********** Designer tables  *****************/


--Designer information
create table Designer (
  did bigint unsigned not null auto_increment,
  d_name varchar(255),
  d_labelname varchar(255), 
  d_phone_number unsigned int,
  d_email varchar(255),
  d_address text,
  d_state varchar(2),
  d_city varchar(50),
  d_zipcode unsigned int,
  d_specialities boolean,
  foreign key (pid) references product(pid),
  foreign key (bid) references boutiques(bid)
);


create table Boutiques (
  bid bigint unsigned not null auto_increment,
  b_image_filename varchar(255), /* changed from data type mediumblob --> filename as the images will be stored in the server instead for a lighter database */
  b_name varchar(255),
  b_address text,
  b_city varchar(50),
  b_state varchar(2),
  b_zipcode unsigned int,
  foreign key (did) references designer(did),
  foreign key (pid) references product(pid)
);

-- Table created from the many to many relationship between Product and Boutique

Create table Pro_bou (
  pid bigint unsigned not null,
  bid bigint unsigned not null
);



/************ Relational Scheme for Database **********************/

Users (
  uid, 
  email, 
  password, 
  u_points, 
  u_title, 
  username, 
  f_name, 
  l_name, 
  birthday, 
  city, 
  state
)
    Primary Key: uid

Designer (
   did, 
   d_name, 
   d_labelname, 
   d_phone,
   d_email, 
   d_address, 
   d_state, 
   d_city, 
   d_zipcode, 
   d_specialist
)
    Primary key: did

Product (
  pid, 
  pro_name,
  pro_desc, 
  color_name, 
  fiber_context, 
  pro_price, 
  pro_tags,              
  made_in_NY, 
  novelity_of_items
)
  Primary Key: pid

Product_types (
  pro_types_id, 
  name
)
Primary Key: pro_types_id

Product_images (
  pro_img_id, 
  pro_img, 
  pid, 
  did
)
Primary key: pro_img_id
Foreign key: pid referencing product.pid 
              did referencing designer.did

Boutiques (
  bid, 
  b_img, 
  b_name, 
  b_address, 
  b_city, 
  b_state, 
  b_zipcode
)
  Primary key: bid

Pro_likes (
  uid, 
  pid, 
  liked
)
Primary key: uid, pid
Foreign key: uid referencing users.uid
             pid referencing product.pid



comments (
  uid, 
  pid, 
  time_posted, 
  body
)
Primary key: uid,  time_posted
Foreign key: uid referencing users.uid
             pid referencing product.pid

pro_bou (
  pid, 
  bid
)    
  Primary key: pid, bid
  Foreign key: pid referencing product.pid
               Bid referencing boutique.bid





