from django.db import models

class Designer(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    label_name = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, null=True, blank=True)
    specialites = models.CharField(max_length=254,  null=True, blank=True)
    image = models.ImageField(upload_to='images/designers/main',max_length=100, null=True) #For the argument upload_to, will add to the static folder and generated image will be stored in suing that path specified

    #For Admin Purposes, to track and see which if still active by for administrative users only
    is_active = models.BooleanField(default=True)

    #Foreign Keys & other relationships
    product = models.ManyToManyField(Product)

    #Metadata
    class Meta:
    	 verbose_name = _("Designer Information")

    #Helps return something meaningful, to show within the admin interface for easy interaction
    def __unicode__(self):
    	return self.name


class Product(models.Model):
	name = models.CharField(max_length=254, blank=True, null=True)
	description = models.CharField(max_length=254, blank=True, null=True)    
	color_name = models.CharField(max_length=254, null=True, blank=True)
	size_types = models.CharField(max_length=7, null=True, blank=True)
	product_price = models.DecimalField(max_digits=9,decimal_places=2)
	old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00) #To show original price if, new price has been added
	product_tags = models.CharField(max_length=254, null=True, blank=True, help_text='Comma-delimited set of SEO keywords for product tag area')
	novelty = models.CharField(max_length=254, null=True, blank=True)
	product_website = models.URLField(max_length=200,  null=True, blank=True) #To show other sites to Users, where they can purchase the particular product
	image = models.ImageField(upload_to='images/products/main',max_length=100, null=True) #For the argument upload_to, will add to the static folder and generated image will be stored in suing that path specified
	slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')

	#This shows when each item was uploaded & by who, to the User 
	uploaded_by = models.CharField(max_length=254, blank=True, null=True)
	uploaded_at = models.DateTimeField(auto_now=True)

	#For Admin Purposes, to track and see which if still active by for administrative users only
	is_active = models.BooleanField(default=True)

	#Foreign Keys & other relationships
	categories = models.ManyToManyField(ProductCategory)
	boutiques = models.ManyToManyField(Boutique)

	#Metadata
    class Meta:
    	verbose_name = _("Product")
    	verbose_name_plural = _("Products")

	#Helps return something meaningful, to show within the admin interface for easy interaction
	def __unicode__(self):
		return self.name

class ProductCategory(models.Model):
   name = models.CharField(max_length=255L, blank=True, null=True)
   slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
   
   #For Admin Purposes, to track and see which if still active by for administrative users only
   is_active = models.BooleanField(default=True)

   #For Admin Purposes, to track when we add each product and each product was updated by administrative users
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   #Helps return something meaningful, to show within the admin interface for easy interaction
   def __unicode__(self):
      return self.name


class Boutique(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)    
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.IntergerField(max_length=5, null=True, blank=True)
    boutique_website = models.URLField(max_length=200,  null=True, blank=True)
    
    #For Admin Purposes, to track a product to see which is active by administrative users
    is_active = models.BooleanField(default=True)
   
    #Foreign Keys & other relationships
    designer = models.ManyToManyField(Designer)
   
   #Metadata
    class Meta:
    	verbose_name = _("Boutique Information")

   #Helps return something meaningful, to show within the admin interface for easy interaction
    def __unicode__(self):
    	return self.name

