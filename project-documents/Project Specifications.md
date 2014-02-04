Application Specification 
==========================
==========================
The application will be divide into three core parts: 

- **Users**: 

Where they will have their permissions and how they use the features to navigate throughout the site

- **Designer Admin Area**: 

This allows the designers to join the platform (upon being invited) and add information at their own time, while making any updates tothe product information they add for users to see.

- **Indieitude Admin Area**: 

This will be the master access for ourselves to govern the backend of the site, to approve user changes(see permissions in Users 
for more detail), Add our on content to the platform, using a similar methodology to the **designers** product upload and govern any other data in the site such as adding designers, deleting, and etc..



Users
======
This information is for the users presentation information(View). It is with this list we will create the Models(Logic behind the view) and Templates(The building structure of the View). This will follow the MVC format of thinking.

- **Login**:
User can Login via facebook or using an email/password combination 

- **Sign-Up**:
User can Sign-Up via facebook or using an email/password combination 

Critical UX Feature List
------------------------
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

Lets the user change Name, Username, email, Birthday, City, State, Country and Password

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
**Access Denied for Non-members**:
- Personal feed
- Settings
- Like Products
- Comment on Products
- Notifications 
- Alter information on products

**Access Granted for Non-members**:
- Viewing and Browsing product information

**Access Granted for Members**:
- All-Access(Everything a non-member cannot do)
- *Alter information on products (This permission is given to members achieving an influencer level of: Fashion Publisher)

Levels Below:

**Fashionista**

--> They have no editing power, (basic level you begin at)

**Fashion Publisher are allowed to Add**:

--> Adding Product Tags

--> Adding Product Links

--> Adding Boutiques

**Next level is (Fashion Editor), they are allowed to Delete/Add**:

--> Adding Product Tags

--> Adding Product Links

--> Adding Boutiques

**Final level is (Fashioneer), they are allowed to Delete/Add**:

--> Adding Product Tags

--> Adding Product Links

--> Adding Boutiques

--> Fiber Content

--> A, B (See Designer Admin Area: General Information)


Designers Admin Area
===================================
The Designers that would like to join the platform to added and maintain their own content, will have their own admin area to upload product information. Their will be two areas where designers will input information **General Information** and **Product Information**. The **General information area** will be a one-time save where the designers can update the information at anytime. The **Product Information area** will be the 'main' and critical component where the designers will upload the information onto the platform for user viewing, but will be able to update the information at anytime. SOme of the information however in **General Information** will be propagated to ease the redundancy of adding simple information over again in the **Product information area**, as well in the **Product Information area**.

- The #'s and single-letter code show what will sourced and shown to the users via on the product data from the designers input area **General Information** and **Product Information**.

Critical UX Feature List(General Information)
----------------------------------------
- **(9) Name**:

This information will be the name the designer goes by, and if the designer uses a different name for their label, a checkbox will be provided to allow the designer to
select which name appears for Users to see on the product information

- **Contact Information [internal info. For the Indieitude Team]**: 

This is Private information the designer provided if need we need to contact them. Information includes:

--> Phone # 

--> Address[Street # & Name, State, City, Zip Code] 

--> Email

- **(10) Boutiques or Shapes they sell at [if applicable]**:

Information need from them, would be Name of Boutique/Shop & State/City it is located in

- **(A) Specialties**: 

Whatever product the designer specializes in making, e.g. Accessories, Bags, Jeans

- **(B) Designer Store information [if applicable]**:

This is only if the designer owns a physical store, then we would need their address to advertise to users on the product information.


Critical UX Feature List(Product Information)
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

Standard sizes, and guidelines

- **(6) Novelty of Product [if applicable]**:

Helps shows if the product is ultra rare or one of a kind

--> Handmade

--> Limited Edition

--> One-Off-Item

- **(7) Product Tags [if applicable]**:

Refines the search for the users to find the product

- **(8) Made In NY [if applicable]**:

Shows if the product is made in NY

- **(11) Product links**:

lets the designer at links to sites their product is being sold on

- **(12) Product Image(s)**:

The designer adds product images to showcase the product


Indieitude Admin Area
===================================













