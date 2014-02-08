/* 
Database table for Indieitude

@Authors:

Amechi Egbe
Yeshwant Dasari 
August Tan

*/


/**************** User tables ********************/

create table users (
  users_id bigint unsigned not null auto_increment,
  email varchar(255) unique not null,
  password varchar(255) not null,
  user_points int not null auto_increment,
  user_title varchar(255) auto_increment,
  user_name varchar(255),
  first_name varchar(255),
  last_name varchar(255),
  birthday date,
  city varchar(50),
  state varchar(2),
  primary key (users_id)
);



/************** Product tables  *****************/


--Product Information

create table product (
  product_id bigint unsigned not null auto_increment,
  product_name varchar(255),
  product_desc text,
  color_name varchar(255),
  size_types varchar(7),
  fiber_context text,
  product_price unsigned float,
  product_tags varchar(255),
  made_in_ny boolean,
  novelty_of_item varchar(255),
  primary key (product_id)
  foreign key (product_img_id) references product_img(id),
  foreign key (designer_id) references designer_id,
  foreign key (product_types) references product_types
);


/*
 * Represents a type of products, e.g. "shirt", accessories or "shoes", increasing uniformity
 * in product table without introducing ambiguity.
 */
create table product_types (
  product_types_id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (product_types_id)
);


--Product Images

create table product_images (
  product_img_id bigint unsigned not null auto_increment,
  product_img mediumblob,
  product_id bigint unsigned not null,
  designer_id bigint unsigned not null,
  primary key (product_img_id),
  foreign key (product_id) references product(id),
  foreign key (designer_id) references designer(id)
);

--Tables for users likes/comments on the product

create table product_likes (
  user_id bigint unsigned not null, /* the person who liked the product */
  product_id bigint unsigned not null,
  liked boolean,
  primary key (user_id, product_id),
  foreign key (user_id) references users(id),
  foreign key (product_id) references product(id)
);

create table product_comments (
  user_id bigint unsigned not null, /* the comment's author */
  product_id bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (user_id, time_posted),
  foreign key (user_id) references users(id),
  foreign key (product_id) references product(id)
);

/*********** Designer tables  *****************/


--Designer information
create table designer (
designer_id bigint unsigned not null auto_increment,
designer_name varchar(255),
designer_labelname varchar(255), 
designer_phone_number unsigned int,
designer_email varchar(255),
designer_address text,
designer_state varchar(2),
designer_city varchar(50),
designer_zipcode unsigned int,
designer_specialities boolean,
foreign key (product_id) references product(id)
foreign key (boutiques_id) references boutiques(id)
);


create table boutiques (
boutiques_id bigint unsigned not null auto_increment,
boutique_image mediumblob,
boutique_name varchar(255),
boutique_address text,
boutique_city varchar(50),
boutique_state varchar(2),
boutique_zipcode unsigned int,
foreign key (designer_id) references designer(id),
foreign key (product_id) references product(id)
);




