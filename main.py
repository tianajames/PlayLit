import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ArtistPage(webapp2.RequestHandler): #Page that receives a post request with the value of moodchoose.
    def post(self):
        results_template = the_jinja_env.get_template('artistpage.html') #Selects an html file to be used as template
        mood_choice = self.request.get('moodchoose') #THE ACTUAL MAGIC
        the_variable_dict = {"mood":mood_choice}
        the_variable_dict = [""]
        self.response.write(results_template.render(the_variable_dict))

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

class ArtistPage(webapp2.RequestHandler):
    def get(self): #for a get request
        welcome_template = the_jinja_env.get_template('artistpage.html')
        self.response.write(welcome_template.render())

    def post(self):
        welcome_template = the_jinja_env.get_template('artistpage.html')
        mood_choice = self.request.get('moodchoose')
        the_variable_dict = {"mood":mood_choice}
        self.response.write(welcome_template.render(the_variable_dict))
class FinalPage(webapp2.RequestHandler):
    def get(self): #for a get request
        welcome_template = the_jinja_env.get_template('final.html')
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
    ('/mood', MoodPage),
    ('/artist', ArtistPage),
    ('/welcome', WelcomePage),
    ('/main', MainPage),
    ('/final', FinalPage)
], debug=True)
