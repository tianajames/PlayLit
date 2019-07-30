import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MoodPage(webapp2.RequestHandler): #Initial page
    def get(self):
        print ("I am here")
        welcome_template = the_jinja_env.get_template('moodpage.html')


    def post(self):
        welcome_template = the_jinja_env.get_template('moodpage.html')
        occasion_choice = self.request.get('Occasion')
        the_variable_dict = {"occasion":occasion_choice}
        self.response.write(welcome_template.render(the_variable_dict))

class WelcomePage(webapp2.RequestHandler):
    def get(self): #for a get request
            welcome_template = the_jinja_env.get_template('welcome.html')
            self.response.write(welcome_template.render())

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        welcome_template = the_jinja_env.get_template('main.html')
        self.response.write(welcome_template.render())

    def post(self):
        welcome_template = the_jinja_env.get_template('main.html')
        self.response.write(welcome_template.render())

class FinalPage(webapp2.RequestHandler):
    def get(self): #for a get request
        welcome_template = the_jinja_env.get_template('final.html')
        self.response.write(welcome_template.render())

    def post(self):
        welcome_template = the_jinja_env.get_template('final.html')
        self.response.write(welcome_template.render())


app = webapp2.WSGIApplication([
    ('/mood', MoodPage),
    ('/welcome', WelcomePage),
    ('/main', MainPage),
    ('/final', FinalPage)
], debug=True)
