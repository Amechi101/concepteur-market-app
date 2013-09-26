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