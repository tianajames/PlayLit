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
        self.response.write(results_template.render(the_variable_dict))

class MoodPage(webapp2.RequestHandler): #Initial page
    def get(self):
        welcome_template = the_jinja_env.get_template('moodpage.html')
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
    ('/', MoodPage),
    ('/artist', ArtistPage)
], debug=True)
