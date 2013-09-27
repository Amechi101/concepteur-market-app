import webapp2

from models import Users
from google.appengine.ext import webapp


class P_InfoArea(webapp2.RequestHandler):
	def get(Users):
        Users.response.out.write("""
      <!DOCTYPE html>
      <html>
      <head>
        <title>Login test!</title>
      </head>
      <body>
        <form action="/users" method="post"> 
            <div>First Name: <input type="text" name="First Name"> Last Name: <input type="text" name="Last Name"></br></div>
            <div>Email: <input type="email" name="Email"></div>
            <div>Birthday: <input type="date" name="Birthdayr"></div>
            <div>Location: <input type="text" name="Location"></div>
            <div> New Password: <input type="password" name="password"> Re-Enter: <input type="password" name="password"</div>
            <div><input type="submit" value="login"></div>
        </form>
      </body>
      </html>
      """)

#where it will verify information certain information save
class send_to_server(webapp2.RequestHandler):
	def post(Users):
        email = Users.request.get("email") #validate email
            if email == invaild:
            	return ""
         
         password = User.request.get("password")

    # conn = rdbms.connect(instance=_INSTANCE_NAME, database=_DATABASE_NAME)
    # cursor = conn.cursor()
    # cursor.execute("SELECT email, password FROM users WHERE email=%s AND password=%s", (email, password))




