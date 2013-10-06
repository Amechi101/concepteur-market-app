class Address(models.Model):
    id = models.ForeignKey('Users', primary_key=True, db_column='id')
    address = models.CharField(max_length=50L, blank=True)
    city = models.CharField(max_length=50L, blank=True)
    state = models.CharField(max_length=50L, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=30L, blank=True)
    isbilling = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'address'


class Card(models.Model):
    id = models.ForeignKey('Users', primary_key=True, db_column='id')
    cnumber = models.BigIntegerField(null=True, blank=True)
    ccv = models.IntegerField(null=True, blank=True)
    expire = models.DateField(null=True, blank=True)
    name_on_card = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'card'

class Clothing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    designer = models.ForeignKey('Designers')
    title = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    clothing_type = models.ForeignKey('ClothingTypes', null=True, db_column='clothing_type', blank=True)
    class Meta:
        db_table = 'clothing'

class ClothingColors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clothing_id = models.BigIntegerField()
    color_name = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'clothing_colors'

class ClothingComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    clothing = models.ForeignKey(Clothing)
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    class Meta:
        db_table = 'clothing_comments'

class ClothingLikes(models.Model):
    user = models.ForeignKey('Users')
    clothing = models.ForeignKey(Clothing)
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'clothing_likes'

class ClothingTypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'clothing_types'

class ConcepteurappClothing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    designer = models.ForeignKey('ConcepteurappDesigners')
    title = models.CharField(max_length=255L)
    description = models.CharField(max_length=255L)
    clothing_type = models.ForeignKey('ConcepteurappClothingtypes', null=True, db_column='clothing_type', blank=True)
    class Meta:
        db_table = 'concepteurapp_clothing'

class ConcepteurappClothingcolors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clothing_id = models.BigIntegerField()
    color_name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'concepteurapp_clothingcolors'

class ConcepteurappClothingcomments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    clothing = models.ForeignKey(ConcepteurappClothing)
    time_posted = models.DateTimeField()
    body = models.TextField()
    class Meta:
        db_table = 'concepteurapp_clothingcomments'

class ConcepteurappClothinglikes(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    clothing = models.ForeignKey(ConcepteurappClothing)
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_clothinglikes'

class ConcepteurappClothingtypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'concepteurapp_clothingtypes'

class ConcepteurappDesigners(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    description = models.CharField(max_length=255L)
    class Meta:
        db_table = 'concepteurapp_designers'

class ConcepteurappFriendconnect(models.Model):
    id2 = models.ForeignKey('ConcepteurappFriends', primary_key=True, db_column='id2')
    class Meta:
        db_table = 'concepteurapp_friendconnect'

class ConcepteurappFriends(models.Model):
    id1 = models.ForeignKey('ConcepteurappUsers', primary_key=True, db_column='id1')
    class Meta:
        db_table = 'concepteurapp_friends'

class ConcepteurappLookclothing(models.Model):
    id = models.IntegerField(primary_key=True)
    look = models.ForeignKey('ConcepteurappLooks')
    clothing = models.ForeignKey(ConcepteurappClothing)
    class Meta:
        db_table = 'concepteurapp_lookclothing'

class ConcepteurappLookcomments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    look = models.ForeignKey('ConcepteurappLooks')
    time_posted = models.DateTimeField()
    body = models.TextField()
    class Meta:
        db_table = 'concepteurapp_lookcomments'

class ConcepteurappLooklikes(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    look = models.ForeignKey('ConcepteurappLooks')
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_looklikes'

class ConcepteurappLooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    name = models.CharField(max_length=255L)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_looks'

class ConcepteurappMessages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sender = models.ForeignKey('ConcepteurappUsers')
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField()
    class Meta:
        db_table = 'concepteurapp_messages'

class ConcepteurappMessagesr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    recipient = models.ForeignKey(ConcepteurappMessages)
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField()
    class Meta:
        db_table = 'concepteurapp_messagesr'

class ConcepteurappModels(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    hair_color = models.CharField(max_length=255L)
    hair_style = models.CharField(max_length=255L)
    skin_color = models.CharField(max_length=255L)
    eye_color = models.CharField(max_length=255L)
    lip_size = models.CharField(max_length=255L)
    class Meta:
        db_table = 'concepteurapp_models'

class ConcepteurappMoodboardclothing(models.Model):
    id = models.IntegerField(primary_key=True)
    moodboard = models.ForeignKey('ConcepteurappMoodboards')
    clothing = models.ForeignKey(ConcepteurappClothing)
    class Meta:
        db_table = 'concepteurapp_moodboardclothing'

class ConcepteurappMoodboardcomments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    moodboard = models.ForeignKey('ConcepteurappMoodboards')
    time_posted = models.DateTimeField()
    body = models.TextField()
    class Meta:
        db_table = 'concepteurapp_moodboardcomments'

class ConcepteurappMoodboardlikes(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    moodboard = models.ForeignKey('ConcepteurappMoodboards')
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_moodboardlikes'

class ConcepteurappMoodboards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    name = models.CharField(max_length=255L)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_moodboards'

class ConcepteurappOrderclothing(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('ConcepteurappOrders')
    clothing = models.ForeignKey(ConcepteurappClothing)
    class Meta:
        db_table = 'concepteurapp_orderclothing'

class ConcepteurappOrders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    time_purchased = models.DateTimeField()
    class Meta:
        db_table = 'concepteurapp_orders'

class ConcepteurappRewards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    description = models.CharField(max_length=255L)
    point_cost = models.IntegerField(null=True, blank=True)
    is_available = models.IntegerField(null=True, blank=True)
    days_valid = models.IntegerField(null=True, blank=True)
    reward_type = models.BigIntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_rewards'

class ConcepteurappRewardtypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'concepteurapp_rewardtypes'

class ConcepteurappUserrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('ConcepteurappUsers')
    reward = models.ForeignKey(ConcepteurappRewards)
    is_valid = models.IntegerField(null=True, blank=True)
    expiration = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_userrewards'

class ConcepteurappUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=254L, unique=True)
    password = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L)
    last_name = models.CharField(max_length=255L)
    gender = models.CharField(max_length=1L)
    birthday = models.DateField(null=True, blank=True)
    reward_points_current = models.IntegerField(null=True, blank=True)
    reward_points_lifetime = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'concepteurapp_users'

class Designers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'designers'

class Friendconnect(models.Model):
    id2 = models.ForeignKey('Friends', primary_key=True, db_column='id2')
    class Meta:
        db_table = 'friendconnect'

class Friends(models.Model):
    id1 = models.ForeignKey('Users', primary_key=True, db_column='id1')
    class Meta:
        db_table = 'friends'

class LookClothing(models.Model):
    look = models.ForeignKey('Looks')
    clothing = models.ForeignKey(Clothing)
    class Meta:
        db_table = 'look_clothing'

class LookComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    look = models.ForeignKey('Looks')
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    class Meta:
        db_table = 'look_comments'

class LookLikes(models.Model):
    user = models.ForeignKey('Users')
    look = models.ForeignKey('Looks')
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'look_likes'

class Looks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    name = models.CharField(max_length=255L, blank=True)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'looks'

class Messages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sender = models.ForeignKey('Users')
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField(blank=True)
    class Meta:
        db_table = 'messages'

class Messagesr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    recipient = models.ForeignKey(Messages)
    sent_time = models.DateTimeField()
    read_time = models.DateTimeField()
    body = models.TextField(blank=True)
    class Meta:
        db_table = 'messagesr'

class Models(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    hair_color = models.CharField(max_length=255L, blank=True)
    hair_style = models.CharField(max_length=255L, blank=True)
    skin_color = models.CharField(max_length=255L, blank=True)
    eye_color = models.CharField(max_length=255L, blank=True)
    lip_size = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'models'

class MoodboardClothing(models.Model):
    moodboard = models.ForeignKey('Moodboards')
    clothing = models.ForeignKey(Clothing)
    class Meta:
        db_table = 'moodboard_clothing'

class MoodboardComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    moodboard = models.ForeignKey('Moodboards')
    time_posted = models.DateTimeField()
    body = models.TextField(blank=True)
    class Meta:
        db_table = 'moodboard_comments'

class MoodboardLikes(models.Model):
    user = models.ForeignKey('Users')
    moodboard = models.ForeignKey('Moodboards')
    liked = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'moodboard_likes'

class Moodboards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    name = models.CharField(max_length=255L, blank=True)
    time_posted = models.DateTimeField()
    is_private = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'moodboards'

class OrderClothing(models.Model):
    order = models.ForeignKey('Orders')
    clothing = models.ForeignKey(Clothing)
    class Meta:
        db_table = 'order_clothing'

class Orders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    time_purchased = models.DateTimeField()
    class Meta:
        db_table = 'orders'

class RewardTypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'reward_types'

class Rewards(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    point_cost = models.IntegerField(null=True, blank=True)
    is_available = models.IntegerField(null=True, blank=True)
    days_valid = models.IntegerField(null=True, blank=True)
    reward_type = models.BigIntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'rewards'

class UserRewards(models.Model):
    user = models.ForeignKey('Users')
    reward = models.ForeignKey(Rewards)
    is_valid = models.IntegerField(null=True, blank=True)
    expiration = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'user_rewards'

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
    class Meta:
        db_table = 'users'



# Django stuff.....

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'



class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'
