import cgi
import webapp2
from google.appengine.api import rdbms
from google.appengine.ext.webapp.util import run_wsgi_app

_INSTANCE_NAME = 'concepteur-7823-m-002792:core' # the database instance id
_DATABASE_NAME = 'test' # the database name

class MainPage(webapp2.RequestHandler):
  def get(self):

    # The document that's loaded when the user enters the page. Note that the
    # form action is "/login", which causes a redirect to LoginPage when the
    # submit button is clicked.
    self.response.out.write("""
      <!DOCTYPE html>
      <html>
      <head>
        <title>Login test!</title>
      </head>
      <body>
        <form action="/login" method="post">
          <div>email: <input type="text" name="email"> <br /></div>
          <div>password: <input type="password" name="password"></div>
          <div><input type="submit" value="login"></div>
        </form>
      </body>
      </html>
      """)

class LoginPage(webapp2.RequestHandler):
  def post(self):
    # Get the data the user entered in the form 
    email = self.request.get("email")
    password = self.request.get("password")
    conn = rdbms.connect(instance=_INSTANCE_NAME, database=_DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users WHERE email=%s AND password=%s", (email, password))
    
    data = cursor.fetchall()

    if len(data) == 1:
      self.response.out.write("""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Login succeeded!</title>
        </head>
        <body>
          <p>You have logged in as
        """)
      self.response.out.write(data[0][1])
      self.response.out.write("""
        </p>
        </body>
        </html>
        """)
    else:
      self.response.out.write("""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Login failed!</title>
        </head>
        <body>
          <p>You have entered an incorrect username or password.</p>
        </body>
        </html>
        """)

    conn.close()

app = webapp2.WSGIApplication([('/', MainPage), ('/login', LoginPage)], debug=True)

def main():
  run_wsgi_app(app)

if __name__ == "__main__":
  main()

