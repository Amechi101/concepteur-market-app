/* 
from myfiles import amechi

class SqlProblems (amechi.Author)

    When inputting the information within the django model based on the concepteur_market.sql document,
    ran into errors with tables messages & friends. 

    Specifically, since the foreign keys for friends both referenced users within the same table
    and for messages the recipient_id and sender_id both referenced users within the same table both came back with
    errors of conflicting entries within the command line prompt 

    So below I came up with a possible solution I am testing out within my django model: 
    */


create table friends (
  id1 bigint unsigned not null,
  primary key (id1),
  foreign key (id1) references users(id)
);

create table friendconnect (
  id2 bigint unsigned not null,
  primary key (id2),
  foreign key (id2) references users(id), /* duplicate connections(disregard): information flow: friendsconnect -> friends -> users */
  foreign key (id2) references friends(id1)
);

create table messages (
  id bigint unsigned not null auto_increment,
  sender_id bigint unsigned not null,
  sent_time timestamp,
  read_time timestamp,
  body text,
  primary key (id),
  foreign key (sender_id) references users(id)
);

create table messagesr (
  id bigint unsigned not null auto_increment,
  recipient_id bigint unsigned not null,
  sent_time timestamp,
  read_time timestamp,
  body text,
  primary key (id),
  foreign key (recipient_id) references users(id), /* duplicate connections(disregard): information flow: messager -> messages -> users */
  foreign key (recipient_id) references messages(id)
);


/* adding a address table & card table to my perosnal database. Need to make sense of a few things while creating the logic */

create table address (
  id bigint unsigned not null,
  address varchar(50),
  city varchar(50),
  state varchar(50),
  zip_code int(5),
  country varchar(30),
  isbilling boolean,
  primary key (id),
  foreign key (id) references users(id)
);

create table card (
 id bigint unsigned not null,
 cnumber bigint,
 ccv int(5),
 expire date,
 name_on_card varchar(30),
 primary key (id),
 foreign key (id) references users(id)
);




