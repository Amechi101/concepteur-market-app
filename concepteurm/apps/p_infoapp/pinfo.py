from users.model import Users
from cards.model import Cards
from address.model import Address

def get_users(self):
    if users.information.appear.write("""
                    <!DOCTYPE html>
            <html>
            <head>
                <title>Personal Info</title>
            </head>
            <body>
                <div>
                    <form action="/users" method="post"> 
                        <div class ="">
                 <h1>General Information</h1>
                    <div> First Name <input type="text" name="First Name"> Last Name: <input type="text" name="Last Name"></br></div>
                    <div> Email <input type="email" name="Email"></div>
                    <div> Birthday <input type="date" name="Birthday"></div>
                    <div> City <input type="text" name="City"></div>
                    <div> State <input type="text" name="State"></div>
                    <div> Country <input type="text" name="Country"></div>
                    <div> New Password <input type="password" name="password"> Re-Enter <input type="password" name="password"></div>
                    <div><input type="submit" value="Save"></div>
                </div>
                <div>
                 <h1>Payment Method</h1>
                    <div>Credit Card <input type="number" name="Credit Card"> 
                    <div> Name on Card <input type="text" name="Credit Card"></div>
                    <div> Date <input type="date" name="Date"></div>
                    <div><input type="submit" value="Save"></div>
                </div>
                <div>
                 <h1>Shipping Information</h1>
                    <div> Address <input type="text" name="Address"> 
                    <div> City <input type="text" name="City"></div>
                    <div> State <input type="text" name="State"></div>
                    <div> Zip Code <input type="number" name="Zip Code"> 
                    <div> Country <input type="text" name="Country"></div>
                    <div><input type="submit" value="Save"></div>
                </div>
                <div>
                 <h1>Billing Information</h1>
                    <div> Address <input type="text" name="Address"> 
                    <div> City <input type="text" name="City"></div>
                    <div> State <input type="text" name="State"></div>
                    <div> Zip Code <input type="number" name="Zip Code"> 
                    <div> Country <input type="text" name="Country"></div>
                    <div><input type="submit" value="Save"></div>
                </div>
            </form>  
        </div>
        </body>
      </html>
      """)
    
    if len(data) == 0:
        users.response.out.write()
            pass

 
































































# import cgi
# import webapp2
# from google.appengine.api import rdbms
# from google.appengine.ext.webapp.util import run_wsgi_app
# from models import Users
# from models import Address
# from models import Card


# class PersonalInfo(webapp2.RequestHandler):
#     def get(self):
#         self.response.out.write("""
      #       <!DOCTYPE html>
      #       <html>
      #       <head>
      #           <title>Personal Info</title>
      #       </head>
      #       <body>
      #           <div>
      #               <form action="/users" method="post"> 
      #                   <div class ="">
      #            <h1>General Information</h1>
      #               <div> First Name <input type="text" name="First Name"> Last Name: <input type="text" name="Last Name"></br></div>
      #               <div> Email <input type="email" name="Email"></div>
      #               <div> Birthday <input type="date" name="Birthday"></div>
      #               <div> City <input type="text" name="City"></div>
      #               <div> State <input type="text" name="State"></div>
      #               <div> Country <input type="text" name="Country"></div>
      #               <div> New Password <input type="password" name="password"> Re-Enter <input type="password" name="password"></div>
      #               <div><input type="submit" value="Save"></div>
      #           </div>
      #           <div>
      #            <h1>Payment Method</h1>
      #               <div>Credit Card <input type="number" name="Credit Card"> 
      #               <div> Name on Card <input type="text" name="Credit Card"></div>
      #               <div> Date <input type="date" name="Date"></div>
      #               <div><input type="submit" value="Save"></div>
      #           </div>
      #           <div>
      #            <h1>Shipping Information</h1>
      #               <div> Address <input type="text" name="Address"> 
      #               <div> City <input type="text" name="City"></div>
      #               <div> State <input type="text" name="State"></div>
      #               <div> Zip Code <input type="number" name="Zip Code"> 
      #               <div> Country <input type="text" name="Country"></div>
      #               <div><input type="submit" value="Save"></div>
      #           </div>
      #           <div>
      #            <h1>Billing Information</h1>
      #               <div> Address <input type="text" name="Address"> 
      #               <div> City <input type="text" name="City"></div>
      #               <div> State <input type="text" name="State"></div>
      #               <div> Zip Code <input type="number" name="Zip Code"> 
      #               <div> Country <input type="text" name="Country"></div>
      #               <div><input type="submit" value="Save"></div>
      #           </div>
      #       </form>  
      #   </div>
      #   </body>
      # </html>
      # """)


# class PersonalInfoPage(webapp2.RequestHandler):
#   def post(self):
#     # Get the data the user entered in the form 
#     email = self.request.get("email")
#     password = self.request.get("password")
    

#     conn = rdbms.connect(instance=_INSTANCE_NAME, database=_DATABASE_NAME)
#     cursor = conn.cursor()
#     cursor.execute("SELECT email, password FROM users WHERE email=%s AND password=%s", (email, password))
    
#     data = cursor.fetchall()





# if list(data) == 1











# class P_InfoArea(webapp2.RequestHandler):
# 	def get(Users):
#         Users.response.out.write("""
#       <!DOCTYPE html>
#       <html>
#       <head>
#         <title>Login test!</title>
#       </head>
#       <body>
#         <form action="/users" method="post"> 
#             <div>First Name: <input type="text" name="First Name"> Last Name: <input type="text" name="Last Name"></br></div>
#             <div>Email: <input type="email" name="Email"></div>
#             <div>Birthday: <input type="date" name="Birthdayr"></div>
#             <div>Location: <input type="text" name="Location"></div>
#             <div> New Password: <input type="password" name="password"> Re-Enter: <input type="password" name="password"</div>
#             <div><input type="submit" value="login"></div>
#         </form>
#       </body>
#       </html>
#       """)

# #where it will verify information certain information save
# class send_to_server(webapp2.RequestHandler):
# 	def post(Users):
#         email = Users.request.get("email") #validate email
#             if email == invaild:
#             	return ""
         
#          password = User.request.get("password")

#     # conn = rdbms.connect(instance=_INSTANCE_NAME, database=_DATABASE_NAME)
#     # cursor = conn.cursor()
#     # cursor.execute("SELECT email, password FROM users WHERE email=%s AND password=%s", (email, password))




