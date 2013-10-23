from django.db import models
# from django.db import connection
# from concepteurm.server import conn  #this imports the db connection for mysql inside this module, so request to and from the db is possible 


# To store the user choices (when they create their model )
# new user
# post the information

class Models(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users')
    hair_color = models.IntegerField(null=True, blank=True)
    hair_style = models.IntegerField(null=True, blank=True)
    skin_color = models.IntegerField(null=True, blank=True)
    eye_color = models.IntegerField(null=True, blank=True)
    lip_size = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'models'

    def __unicode__(self):
        return '%s %s %s %s %s %s %s' % (self.user, self.hair_color, self.hair_style, self.skin_color, self.eye_color, self.lip_size)

user_selection = {'hair_color':[4444] ,'hair_style':[7575] ,'skin_color':[8585] ,'eye_color':[8484] , 'lip_size':[5555] }

    def selected_style(self, choices):
        for choices in user_selection:
            user_selection['hair_color'] = 'selected_style'

        
        


    






