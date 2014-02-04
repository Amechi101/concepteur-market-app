Application Specification 
==========================
==========================

Users
======
This information is for the users presentation information(View). It is with this list we will create the Models(Logic behind the view) and Templates(The buidling structure of the View). This will follow the MVC format of thinking.

- Login:
User can Login via facebook or using an email/password combination 

- Sign-Up:
User can Sign-Up via facebook or using an email/password combination 

Critical UX Feature List
------------------------
- All:
Aggregates the content in the designated content area, regardless of product specifications.

- What's New:
Aggregates the content in the designated content area, searching from the latest uploads from Designers & Indieitude Team, searching from Most Recent.

- Trending Now:
Aggregates the content in the designated content area, searching content that is either Liked and/or Commented the most in a given time frame, E.g. hour, day or week

- Collection:
Aggregates the content in the designated content area, allowing the user to filter through choices from categories e.g. Clothing, Accessories and etc

- Designers:
Aggregates the content in the designated content area, allowing the user to filter through different Designers within the platform, them another sub-level to filter through their specific choices within the selection.

- Location:
Aggregates the content in the designated content area, searching for content affiliated with designers merchandise in a particular area


Available for users after they Sign-up or Log-In
------------------------------------------------
- Personal Feed:
Aggregates the content in the designated content area, that the user liked on different products 

- Notifications:
Shows if the user has any new comments or announcements 

- Settings:
Lets the user change name, username, email, Birthday, City, State, Country and Password(if they did not sign-up with Facebook Log-In)


Non-Critical UX feature list
----------------------------
- About Us
- Terms
- Privacy Policy 
- Conditions
- Contact Us
- Social Media Links


Permissions 
------------
Access Denied for Non-members:
- Personal feed
- Settings
- Like Products
- Comment on Products
- Notifications 
- Alter information on products

Access Granted for Non-members:
-Viewing and Browsing product information

Access Granted for Members:
- All-Access(Everything a non-member cannot do)
- *Alter information on products (This permission is given to members achieving an influencer level of: Editor)


Designers
===================================
The Designers that would like to join the platform to added and maintain their own content, will have their own admin area to upload product information. Their will be two areas where designers will input information General Information and Product Information. The General information area will be a one-time save where the designers can update the information at anytime. The Product Information area will be the 'main' and critical component where the designers will upload the information onto the platform for user viewing, but will be able to update the information at anytime. SOme of the information however in General Information will be propagated to ease the redundancy of adding simple information over again in the Product information area, as well in the Product Information area.


Critical UX Feature List(General Information)
----------------------------------------
- (9) Name:
This information will be the name the designer goes by, and if the designer uses a different name for their label, a checkbox will be provided to allow the designer to
select which name appears for Users to see on the product information

- Contact Information [internal info. For the Indieitude Team]: 
This is Private information the designer provided if need we need to contact them. Information includes --> Phone # - Address[Street # & Name, State, City, Zip Code] - Email

- (10) Boutiques or Shapes they sell at [if applicable]:
Information need from them, would be Name of Boutique/Shop & State/City it is located in

- (A) Specialties: 
Whatever product the designer specializes in making, e.g. Accessories, Bags, Jeans

- (B) Designer Store information [if applicable]:
This is only if the designer owns a physical store, then we would need their address to advertise to users on the product information.


Critical UX Feature List(Product Information)
----------------------------------------



Database Architecture Best Practices  & Guidelines
==================================================
- Name case should be camel case e.g. hiThere
- Stray away from creating redundancy

Front-End Development Best Practices & Guidelines
=================================================








