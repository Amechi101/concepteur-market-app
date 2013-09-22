/*
 * Main database for Concepteur Market.
 *
 * @author Erik Strottmann
 */

create database concepteur_market;

use concepteur_market;

create table users (
  id bigint unsigned not null auto_increment,
  email varchar(254) unique not null,
  password varchar(255) not null,
  first_name varchar(255),
  last_name varchar(255),
  gender char(1),
  birthday date,
  reward_points_current int,
  reward_points_lifetime int,
  primary key (id)
);

/*
 * Stores only one entry for each friendship. That is, if users A and B are
 * friends, either (A, B) or (B, A) exists in this table, but not both.
 */
create table friends (
  id1 bigint unsigned not null,
  id2 bigint unsigned not null,
  primary key (id1, id2),
  foreign key (id1) references users(id),
  foreign key (id2) references users(id)
);

create table messages (
  id bigint unsigned not null auto_increment,
  sender_id bigint unsigned not null,
  recipient_id bigint unsigned not null,
  sent_time timestamp,
  read_time timestamp,
  body text,
  primary key (id),
  foreign key (sender_id) references users(id),
  foreign key (recipient_id) references users(id)
);

/*
 * Stores the user's customizations to her 3D model. These values are stored
 * in hexadecimal, stored in varchar (cf. string) columns.
 */
create table models (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the model's owner */
  hair_color varchar(255),
  hair_style varchar(255),
  skin_color varchar(255),
  eye_color varchar(255),
  lip_size varchar(255),
  primary key (id),
  foreign key (user_id) references users(id)
);

create table designers (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  description varchar(255),
  primary key (id)
);

/*
 * Represents a type of clothing, e.g. "shirt" or "shoes", increasing uniformity
 * in clothing table without introducing ambiguity.
 */
create table clothing_types (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (id)
);

create table clothing (
  id bigint unsigned not null auto_increment,
  designer_id bigint unsigned not null,
  title varchar(255),
  description varchar(255),
  clothing_type bigint unsigned, /* see table clothing_types */
  primary key (id),
  foreign key (designer_id) references designers(id),
  foreign key (clothing_type) references clothing_types(id)
);

/*
 * The color variations of a single item of clothing.
 */
create table clothing_colors (
  id bigint unsigned not null auto_increment,
  clothing_id bigint unsigned not null,
  color_name varchar(255),
  primary key (id)
);

create table clothing_likes (
  user_id bigint unsigned not null, /* the person who viewed the clothing */
  clothing_id bigint unsigned not null,
  liked boolean,
  primary key (user_id, clothing_id),
  foreign key (user_id) references users(id),
  foreign key (clothing_id) references clothing(id)
);

create table clothing_comments (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the comment's author */
  clothing_id bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (clothing_id) references clothing(id)
);

create table looks (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the look's owner */
  name varchar(255),
  time_posted timestamp,
  is_private boolean,
  primary key (id),
  foreign key (user_id) references users(id)
);

create table look_clothing (
  look_id bigint unsigned not null,
  clothing_id bigint unsigned not null,
  primary key (look_id, clothing_id),
  foreign key (look_id) references looks(id),
  foreign key (clothing_id) references clothing(id)
);

create table look_likes (
  user_id bigint unsigned not null, /* the person who viewed the look */
  look_id bigint unsigned not null,
  liked boolean,
  primary key (user_id, look_id),
  foreign key (user_id) references users(id),
  foreign key (look_id) references looks(id)
);

create table look_comments (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the comment's author */
  look_id bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (look_id) references looks(id)
);

create table moodboards (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the moodboard's owner */
  name varchar(255),
  time_posted timestamp,
  is_private boolean,
  primary key (id),
  foreign key (user_id) references users(id)
);

create table moodboard_clothing (
  moodboard_id bigint unsigned not null,
  clothing_id bigint unsigned not null,
  primary key (moodboard_id, clothing_id),
  foreign key (moodboard_id) references moodboards(id),
  foreign key (clothing_id) references clothing(id)
);

create table moodboard_likes (
  user_id bigint unsigned not null, /* the person who viewed the moodboard */
  moodboard_id bigint unsigned not null,
  liked boolean,
  primary key (user_id, moodboard_id),
  foreign key (user_id) references users(id),
  foreign key (moodboard_id) references moodboards(id)
);

create table moodboard_comments (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null, /* the comment's author */
  moodboard_id bigint unsigned not null,
  time_posted timestamp,
  body text,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (moodboard_id) references moodboards(id)
);

/*
 * Represents a type of clothing, e.g. "discount", increasing uniformity in
 * rewards table without introducing ambiguity.
 */
create table reward_types (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  primary key (id)
);

/*
 * Rewards that the user can purchase for reward points. These can be acquired
 * through the purchase of clothing, and might include rewards like
 * "$20 off your next purchase". Once purchased, a user's rewards are stored in
 * table user_rewards.
 */
create table rewards (
  id bigint unsigned not null auto_increment,
  name varchar(255),
  description varchar(255),
  point_cost int,
  is_available boolean,
  days_valid int,
  reward_type bigint unsigned, /* see table reward_types */
  discount_amount int, /* if any - some will be zero */
  primary key (id)
);

/*
 * The rewards a user has available to use in her "rewards pool".
 */
create table user_rewards (
  user_id bigint unsigned not null,
  reward_id bigint unsigned not null,
  is_valid boolean, /* false in cases such as after expiration */
  expiration date,
  primary key (user_id, reward_id),
  foreign key (user_id) references users(id),
  foreign key (reward_id) references rewards(id)
);

/*
 * An order placed by a user for one or more item of clothing.
 */
create table orders (
  id bigint unsigned not null auto_increment,
  user_id bigint unsigned not null,
  time_purchased timestamp,
  primary key (id),
  foreign key (user_id) references users(id)
);

/*
 * The items of clothing in an order.
 */
create table order_clothing (
  order_id bigint unsigned not null,
  clothing_id bigint unsigned not null,
  primary key (order_id, clothing_id),
  foreign key (order_id) references orders(id),
  foreign key (clothing_id) references clothing(id)
);