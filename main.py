import webapp2
import jinja2
import os
import test2
import random
import json
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MoodPage(webapp2.RequestHandler): #Initial page
    def get(self):
        print ("I am here")
        welcome_template = the_jinja_env.get_template('moodpage.html')
        occasion_choice = self.request.get('main')
        the_variable_dict = {"occasion":occasion_choice}
        self.response.write(welcome_template.render(the_variable_dict))


    def post(self):
        welcome_template = the_jinja_env.get_template('moodpage.html')
        occasion_choice = self.request.get('main')
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
        mood_choice = self.request.get('mood')


        search = test2.get_search(mood_choice)
        search = json.loads(search)
        search = random.choice(search['playlists']['items'])
        playlist_name = search['name']

        playlist_id = "https://open.spotify.com/embed/user/spotify/playlist/" + search['id']
        # tracks = test2.get_tracks(search['id'])
        # tracks = json.loads(tracks)
        # list = []
        # while tracks:
        #     for i, playlist in enumerate(tracks['items']):
        #         list.append("%4d %s" % (i + 1 + tracks['offset'], playlist['track']['name']))
        #         if i == len(tracks['items'])-1:
        #             tracks =False
        # print(list)
        tracks = test2.get_tracks(search['id'])
        tracks = json.loads(tracks)
        list = []
        while tracks:
            for i, playlist in enumerate(tracks['items']):
                list.append("%4d %s" % (i + 1 + tracks['offset'], playlist['track']['name']))
                if i == len(tracks['items'])-1:
                    tracks =False
        print(list)

        the_variable_dict = {
        "Mood":mood_choice,
        "tracks":list,

        "playlist_name": playlist_name,
        "playlist_id":playlist_id,
        "playlist_name": playlist_name

        }

        self.response.write(welcome_template.render(the_variable_dict))
    def post(self):
        welcome_template = the_jinja_env.get_template('final.html')
        mood_choice = self.request.get('mood')


        search = test2.get_search(mood_choice)
        search = json.loads(search)
        search = random.choice(search['playlists']['items'])
        playlist_name = search['name']
        playlist_id = "https://open.spotify.com/embed/user/spotify/playlist/" + search['id']

end("%4d %s" % (i + 1 + tracks['offset'], playlist['track']['name']))


app = webapp2.WSGIApplication([
    ('/mood', MoodPage),
    ('/welcome', WelcomePage),
    ('/main', MainPage),
    ('/final', FinalPage)
], debug=True)
