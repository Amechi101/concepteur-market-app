Application Specification 
==========================
==========================
The application will be divide into three core parts: 

- **User Area**: 

Where they will have their permissions and how they use the features to navigate throughout the site

- **Designer Admin Area**: 

This allows the designers to join the platform (**upon being invited and gaining access**) and add information at their own time, while making any updates to the product information they add for users to see.

- **Indieitude Admin Area**: 

This will be the master admin for ourselves to govern the backend of the site, to approve user changes (**see permissions in Users for more detail**), Add our own content(product pictures and information) to the platform, using the same upload procudure as the **designers** product upload and govern any other data in the site such as adding designers, deleting users, and etc..


Users (use case)
======
This information is for the users. 

It is with this list we will create in Django the Models (**Logic behind the view and database layer**) , View (**the portion that selects which data to display and how to display it, is handled by views and templates**) and Controller (**the portion that delegates to a view depending on user input, is handled by the framework itself by following your URLconf and calling the appropriate Python function for the given URL**). This will follow the MVC format.

Login/Signup Requirements
------------------------

- **Login**:
Users can Login via facebook or entering an email/password combination

- **Sign-Up**:
Users can Sign-Up via facebook or entering an email/password combination 

Critical User Feature List
------------------------

Menu options for Users to select product items available to all users who are non-members or members:

- **All**:

Aggregates the content in the designated content area, regardless of product specifications.

- **What's New**:

Aggregates the content in the designated content area, searching from the latest uploads from Designers & Indieitude Team, searching from Most Recent.

- **Trending Now**:

Aggregates the content in the designated content area, searching content that is either Liked and/or Commented the most in a given time frame, E.g. hour, day or week 

- **Collection**:

Aggregates the content in the designated content area, allowing the user to filter through choices from categories e.g. Clothing, Accessories and etc

- **Designers**:

Aggregates the content in the designated content area, allowing the user to filter through different Designers within the platform, them another sub-level to filter through their specific choices within the selection.

- **Location**:

Aggregates the content in the designated content area, searching for content affiliated with designers merchandise in a particular area


Available for users after they Sign-up or Log-In
------------------------------------------------
- **Personal Feed**:

Aggregates the content in the designated content area, that the user liked on different products 

- **Notifications**:

Shows if the user has any new comments or announcements 

- **Settings**:

Lets the user change Name, Username, Email, Birthday, City, State, Profile Picture and Password

Non-Critical user feature list
----------------------------
- About Us
- Terms
- Privacy Policy 
- Conditions
- Contact Us
- Designer Stories
- Social Media Links


Permissions 
------------
**Access Denied for Non-members**:
- Personal feed
- Settings
- Liking Products
- Commenting on Products
- Notifications 
- Altering information on products

**Access Granted for Non-members**:
- Viewing and Browsing product information 

**Access Granted for Members**:
- All-Access(Everything a non-member cannot do)
- *Alter information on products (This permission is given to members achieving an influencer level of: Fashion Editor)

Levels Below:

**Fashionista** Default level

--> They have no editing power, (basic level everyone begins at)

**Fashion Editor is allowed to Add**:

--> Adding Product Tags

--> Adding Product Links

--> Adding Boutiques


Designers Admin Area (use case)
===================================
The Designers that would like to join the platform to add and maintain their own content, will have their own admin area to upload product information. Their will be two areas where designers will input information **General Information** and **Product Information**. The **General information area** will be where the designers can update basic information at anytime. The **Product Information area** will be the **main** and critical component where the designers will upload the information onto the platform for users viewing, but will be able to update the already uploaded information at anytime. Some of the information however in **General Information** will be propagated to ease the redundancy of adding simple information over again in the **Product information area**, as well in the **Product Information area**.

The #'s and single-letter code show what will sourced from the database storing from the  **General Information** and **Product Information** and shown to the users on the product, some of which users can adjust. 

**General Information** and **Product Information** will show all the necessary sections for designers to input information


Login/Signup Requirements
----------------------------

- **Login**:
Designers can Login using email/password combination 

- **Invited**:
Designers can get invited by signup with email, name and phone# 


Critical Designer Feature List (General Information)
----------------------------------------
- **(9) Name**:

This information will be the name the designer goes by, and if the designer uses a different name for their label, a checkbox will be provided to allow the designer to select which name appears for Users to see on the product information

- **Contact Information [internal info. For the Indieitude Team]**: 

This is Private information the designer provides if need we need to contact them. Information includes:

--> Phone# 

--> Email

- **(10) Boutiques or Shops they sell at [if applicable]**:

Information needed from them, would be Name of Boutique/Shop & State/City Boutique/Shop is located in

- **(A) Specialties**: 

Whatever the designer specializes in making, e.g. Accessories, Bags, Jeans

- **(B) Designer Store information [if applicable]**:

This is only if the designer owns a physical store, then we would need their address to advertise to users on the product information.


Critical Designer Feature List (Product Information)
----------------------------------------
- **(1) Product Name**:

What the name of the product is e.g. Blazer Shirt, Valdenas Green Dress

- **(2) Product Description**:

This is a detailed description of the product describing it with a short synopsis.

- **(3) Fiber Content**:

What the product is made up of, and given the percentages. e.g. Nylon, Silk

- **(4) Available colors**:

Colors the designer has available for the product

- **(5) Fit Sizes**

Sizes the product is available in

- **(6) Novelty of Product [if applicable]**:

Helps shows if the product is ultra rare or one of a kind, E.g.:

--> Handmade

--> Limited Edition

--> One-Off-Item

--> Etc..

- **(7) Product Tags [if applicable]**:

Refines the search for the users to filter the product and helps for SEO

- **(8) Made In NY [if applicable]**:

Shows if the product is made in NY

- **(11) Product links**:

lets the designer at links to sites their product is being sold on

- **(12) Product Image(s)**:

The designer adds product images to showcase the product

- **(13) Designer Video (optional)**:

The designer adds a 90sec video introducing themselves and story behind their product/themselves 

Permissions 
------------
**Access Denied for Non-Designers not on the platform**:
- Cannot login to the Designer Admin Area

**Access Granted for Non-Designers not on the platform**:
- Same as Users(Non-members) **see Access Granted for Non-members(User) in permissions for more detail**
- **Can request to get invited by signing up via a desginated designer signup on homepage

**Access Granted for Designers Invited on the platform**:
- Add Product information that will be displayed to the user
- Delete Product Information already uploaded
- Edit Product information alreay uploaded



Indieitude Admin Area
===================================













