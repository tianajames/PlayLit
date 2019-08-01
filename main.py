import webapp2
import jinja2
import os
import test2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MoodPage(webapp2.RequestHandler): #Initial page
    def get(self):
        print ("I am here")
        mood_template = the_jinja_env.get_template('moodpage.html')


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
        results_template = the_jinja_env.get_template('results.html')
        self.response.write(results_template.render())

    def post(self):
        results_template = the_jinja_env.get_template('results.html')
        occasion = self.request.get("Occasion")
        
        input_variables = {
            "occasion1":occasion,
            # "songs":list1,
            # "name":artist
        }

        self.response.write(results_template.render(input_variables))


app = webapp2.WSGIApplication([
    ('/mood', MoodPage),
    ('/welcome', WelcomePage),
    ('/main', MainPage),
    ('/final', FinalPage)
], debug=True)
