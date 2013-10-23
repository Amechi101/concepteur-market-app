from django.template import Template, Context   #the Template class lives within django.template, use the Context class to pass information to the template

{# Comment #}  <-- # this is a comment for template system

{% Comment %}

# multi line comment for django template
 
{% endcomment %}


# {{ key }} You pass the information which is a key for the c = Context({'key': 'Infomation '}) just working simliar to a python dictonary


t = Template('My name is {{ name }}.') # use the {{to enter statements}}
c = Context({'name': "Amechi"})  # works like a regular python dictonary=, but just with the set of curly brackets in side the ()
t.render(c)  # you call the assignment with the render function to "fill" the template

# Its suppose to print --> u'My name is Stephane.'

#use this to save the raw text of your template and write a mulit line statement
raw_template = """<p>Dear {{ person_name }},</p>

<p>Thanks for placing an order from {{ company }}. It's scheduled to
 ship on {{ ship_date|date:"F j, Y" }}.</p>

{% if ordered_warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% else %}
<p>You didn't order a warranty, so you're on your own when
the products inevitably stop working.</p>
{% endif %}

<p>Sincerely,<br />{{ company }}</p>"""
t = Template(raw_template)  # create a object to pass 'raw_template' the Template class constructor
import datetime  #need a datetime module
c = Context({'person_name': 'John Smith',
     'company': 'Outdoor Equipment',
     'ship_date': datetime.date(2009, 4, 2),
     'ordered_warranty': False})
 t.render(c)

 u"""<p>Dear John Smith,</p>\n\n<p>Thanks for placing an order from Outdoor
Equipment. It's scheduled to\nship on April 2, 2009.</p>\n\n\n<p>You
didn't order a warranty, so you're on your own when\nthe products
inevitably stop working.</p>\n\n\n<p>Sincerely,<br />Outdoor Equipment
</p>"""

# content variable lookup using the dot character (.) traversing complex data strctures and access dictionary, and custom objects

from django.template import Template, Context
class Person(object):
     def __init__(self, first_name, last_name):  
         self.first_name, self.last_name = first_name, last_name  #use , to call the parameters arguments using self

t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.') #create a key for the context dict and pass the parameters from the Person class
c = Context({'person': Person('John', 'Smith')}) # create an instance of the class within the dictionary for Context
t.render(c)
u'Hello, John Smith.'


#########################################################
# built in tag and filters

{% if %} {% endif %}# This evaluates a variable and if it is True...it will display everything between the tags. But an empty string evaluates false

{% else %} is optional 


##########################################################
# this for testing multiple variables

and, or, not takes are allowed but cannot have and, or clause within the same tag

{% if athelete_list and coach_list %}
    both athletes and coaches are available.
{% endif %}

{% if not athlete_list %}
    There are no athletes.
{% endif %}

{% if athlete_list or coach_list %}
    There are some athletes or some coaches.
{% endif %}

{% if not athlete_list or coach_list %}
    There are no athletes or there are some coaches.
{% endif %}

{% if athlete_list and not coach_list %}
    There are some athletes and absolutely no coaches.
{% endif %}

##############################################
# This next section is for the for loop

{% for %} {% endfor %} #allows you to loop over each item in a sequence. For x in y, where y is the sequence to loop over and x is the name of the variable for a particular cycle loop



