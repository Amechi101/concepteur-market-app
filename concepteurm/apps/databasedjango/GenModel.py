class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=254L, unique=True)
    password = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L, blank=True)
    last_name = models.CharField(max_length=255L, blank=True)
    gender = models.CharField(max_length=1L, blank=True)
    birthday = models.DateField(null=True, blank=True)
    reward_points_current = models.IntegerField(null=True, blank=True)
    reward_points_lifetime = models.IntegerField(null=True, blank=True)


class Clothing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    designer = models.ForeignKey('Designers')
    title = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    clothing_type = models.ForeignKey('ClothingTypes', null=True, db_column='clothing_type', blank=True)


class ClothingColors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clothing_id = models.BigIntegerField()
    color_name = models.CharField(max_length=255L, blank=True)
    

class ClothingComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    clothing = models.ForeignKey(Clothing)
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    

class ClothingLikes(models.Model):
    user = models.ForeignKey('Users')
    clothing = models.ForeignKey(Clothing)
    liked = models.IntegerField(null=True, blank=True)
    
class ClothingTypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
   

class Designers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
  

class Friendconnect(models.Model):
    id2 = models.ForeignKey('Friends', primary_key=True, db_column='id2')


class Friends(models.Model):
    id1 = models.ForeignKey('Users', primary_key=True, db_column='id1')

    
class LookClothing(models.Model):
    look = models.ForeignKey('Looks')
    clothing = models.ForeignKey(Clothing)
    

class LookComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    look = models.ForeignKey('Looks')
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    

class LookLikes(models.Model):
    user = models.ForeignKey('Users')
    look = models.ForeignKey('Looks')
    liked = models.IntegerField(null=True, blank=True)
   

class Looks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    name = models.CharField(max_length=255L, blank=True)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    
class Messages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sender = models.ForeignKey('Users')
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField(blank=True)

class Messagesr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    recipient = models.ForeignKey(Messages)
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField(blank=True)
  

class Models(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    hair_color = models.CharField(max_length=255L, blank=True)
    hair_style = models.CharField(max_length=255L, blank=True)
    skin_color = models.CharField(max_length=255L, blank=True)
    eye_color = models.CharField(max_length=255L, blank=True)
    lip_size = models.CharField(max_length=255L, blank=True)
    

class MoodboardClothing(models.Model):
    moodboard = models.ForeignKey('Moodboards')
    clothing = models.ForeignKey(Clothing)
   

class MoodboardComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    moodboard = models.ForeignKey('Moodboards')
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    

class MoodboardLikes(models.Model):
    user = models.ForeignKey('Users')
    moodboard = models.ForeignKey('Moodboards')
    liked = models.IntegerField(null=True, blank=True)
  

class Moodboards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    name = models.CharField(max_length=255L, blank=True)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    

class OrderClothing(models.Model):
    order = models.ForeignKey('Orders')
    clothing = models.ForeignKey(Clothing)
   

class Orders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    time_purchased = models.DateTimeField()
    

class RewardTypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
   

class Rewards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    point_cost = models.IntegerField(null=True, blank=True)
    is_available = models.IntegerField(null=True, blank=True)
    days_valid = models.IntegerField(null=True, blank=True)
    reward_type = models.BigIntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    

class UserRewards(models.Model):
    user = models.ForeignKey('Users')
    reward = models.ForeignKey(Rewards)
    is_valid = models.IntegerField(null=True, blank=True)
    expiration = models.DateField(null=True, blank=True)
    



    