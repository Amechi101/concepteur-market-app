from bs4 import BeautifulSoup
import requests
import re
from website_methods import WebsiteMethodScan

# This file is intended to be the base structure for the algorithm design.

# The problem we intend to solve is getting the raw data from the site "scraping" and return images when the user searchs for a keyword.
# We would get the links from the individual store pages then call each of those pages and scrape those pages,
# Which means getting a subset of information, for internal purposes. 


class SearchBase:
	"""
	Base class representing a instance of the product search
	"""

	def __init__(self):
		"""
		Initialize Beautiful Soup
		"""
		pass


	def keyword_search(self, Categories=True):
		"""
		Method for searching keyword values in the array for lookup
		"""

		# 1.
		#  Find the Keywords for a particular product by looking up the reference in a dictionary lookup, by indexing the within the dict for said category, for 
		#  example when a user selects one of the pre-shown categories on or site, i.e. "Tops", the search engine scraps through the website and makes an
		#  API call to our dictionary to see any words that match within our dictionary using regEx Pattern or other methods.
		# 
		# 2.
		#  And if any new words related to the search from a product arises creates a new [list] filled with the new words and that becomes a new 'Tier' 
		#  populated in an [list] for the particular category 'key' in our dictionary. But if a word has a near match of a pattern to a already existing 'Tier's
		#  [list] of words, it appends() the word into that [list] of the category and the array becomes Nth size bigger.
		#  
		#######
		# Further Explanation:
		# A word such as "Tops" is a category 'key', and has access to a dictionary of a 'Tier' of words in a [list].
		# The Tiers will be in order from 1, 2, 3,... n+1 order to show the importance of the word lookups. So intuitively the first 'Tier' will have the most 
		# common use case words and for each search and any new 'Tier' added
		


		# Global dictionary !important 
		indietude_dictionary = { 
			'Tops': {
				'Tier 1': ["Shirts", "Short-Sleeve", "Button-Down"],
				'Tier 2':[],
				'Tier 3':[]
			},
			'Bottoms': {
				'Tier 1':[""],
				'Tier 2':[""],
				'Tier 3':[""],
			},
			'Dresses': {
				'Tier 1':[""],
				'Tier 2':[""],
				'Tier 3':[""],
			},
			'Shoes': {
				'Tier 1':[""],
				'Tier 2':[""],
				'Tier 3':[""],
			}, 
			'Accessories': {
				'Tier 1':[""],
				'Tier 2':[""],
				'Tier 3':[""],
			}
		}

		for key in Categories.keys():
			for website in website_methods:
				# scan the site(s) using the keywords in our dict
				for product_mapping:
					if product is not in db.sql():
						# then insert into database all product information by calling beautiful soup methods and mapping the item to our own representation
						# from the predefined sites using the regEx pattern method!
						return updated keyword into indietude_dictionary.appened() 
					elif keyword is not in the dictionary:
						# add keyword to particular category 'key' inside the proper Tier 'key' 
						# and match to see if the word is similar to Tier's words 
						if words are not similar:
							# then create a new Tier 'key' with the current searches words in a new[list] within the proper categories 'key' dictionary area
					else:
						# Else dump API call and cancel the lookup
						return no value and proceed to showing product listed items on site

		
	def RegEx(self, pattern):
		"""
		Global Method for pattern matching for keyword search, and product mapping for the stated item
		"""

		# This is an example of defining regEx Pattern methods
		pattern = "(^T|Bo|Dre$)"



	def keyword_save(self, store):
		"""
		Method for storing keyword values in an array for a particular category
		"""
		pass

	

	def product_mapping(self, product_title, designer_name, price, boutique_affliation, images, site_link, product_object):
		"""
	 	Method for mapping the information we want from the site after the initial scrapping


	 	*The obj is just a representation of the data, inside a tuple
		"""
		
		self.product_title = product_title 
		self.designer_name = designer_name 
		self.price_new = price
		self.boutique_affliation = boutique_affliation #This data will be for internal usage purposes
		self.site_link = site_link #This data will be for internal usage purposes
		self.images = images
		self.product_object = product_object

		product_object = ( product_title, designer_name, price, boutique_affliation, site_link, images )


class BeautifulSoup( SearchBase ):
	"""
     Class for beautiful soup library, this is suppose to add a layer of abstraction and 
		use the methods of the beautiful soup layer within our own class structure and methods
	"""
	def __init__(self):
		super(SearchBase, self).__init__()
		self.arg = arg
		



###############################
###################################################################
################################################################################################
##################################################################################################################
# Additional Notes:
# driver method that originally collects all the product data 

#1. go to each site and collect all the products, or all the products based off of a certain search result 

#	this would have the same methods of keyword search (or full-site search and beautiful soup for abstraction), and return an product object

#2. search different keywords and see if the product comes up on that keyword search and then add the link in the database between the product and the keywords

# or can combine the two. As you go through the list of keywords just check to see if the product is already in the database or not

#afterwards, go through keywords and match product information with searches

#regular expressions to match different patterns
#refining beyond websites searches...
#for ASOS, anything that doesn't say ASOS is a designer item and not from ASOS
#checking each of the listings and pattern matching titles to see what we want

#get the entire html. run pattern matching, and then use beautiful soup to get it

#saving the image file in the database

