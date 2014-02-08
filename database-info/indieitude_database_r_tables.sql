/* 
Database table for Indieitude

@Authors:

Amechi Egbe

*/


/**************** User tables ********************/


create table users (
  id bigint unsigned not null auto_increment,
  email varchar(254) unique not null,
  password varchar(255) not null,
  user_points int not null auto_increment,
  user_title varchar(255) auto_increment,
  user_name varchar(255),
  first_name varchar(255),
  last_name varchar(255),
  birthday date,
  city varchar(50),
  state varchar(50),
  country varchar(30),
  primary key (id)
);




/************** Product tables  *****************/


--Product Information

create table product (
  id bigint unsigned not null auto_increment,
  product_name
  product_description
  fiber_types
  product_types
  made_in_ny
  novelty_of_item boolean,
  foreign key (product_images_id) references product_images(id),



);

/*
 * Represents a type of products, e.g. "shirt", accessories or "shoes", increasing uniformity
 * in product table without introducing ambiguity.
 */
create table product_types (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (id)
);

/*
 * Represents a type of fibers, e.g. "Nylon", accessories or "Cotton", increasing uniformity
 * in product table without introducing ambiguity.
 */
create table fiber_types (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (id)
);

/*
 * The color variations of a single item of a particular product, needing a color variation.
 */
create table product_colors (
  id bigint unsigned not null auto_increment,
  product_id bigint unsigned not null,
  color_name varchar(255),
  primary key (id)
);


--Product Images

create table product_images (
  product_id bigint unsigned not null,
  designer_id bigint unsigned not null,
  primary key (product_id, designer_id),
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
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the comment's author */
  product_id bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (product_id) references product(id)
);

/*********** Designer tables  *****************/


--Designer information
create table designer (


);




