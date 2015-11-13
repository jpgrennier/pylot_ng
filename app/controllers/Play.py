"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from datetime import datetime
import random

class Play(Controller):
    def __init__(self, action):
        super(Play, self).__init__(action)
       
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        try:
            session['gold']
        except:
            session['gold'] = 0

        try:
            session['activities']
        except:
            session['activities'] = []

        return self.load_view('index.html')

    def process_money(self):

        if request.form['where'] == 'farm':
            session['gold'] = random.randrange(10,21)
        elif request.form['where'] == 'cave':
            session['gold'] = random.randrange(5,11)
        elif request.form['where'] == 'house':
            session['gold'] = random.randrange(2,6)
        elif request.form['where'] == 'casino':
            session['gold'] = random.randrange(-50,51)

        activity = ''
        
        time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        if session['gold'] >= 0:
            activity += 'Earned ' + str(session['gold']) + ' gold from the ' + str(request.form['where']) + '!' + '(' + str(time) + ')'
        else:
            activity += 'Entered Casino and lost ' + str(session['gold']) + ' gold... Ouch.' + '(' + str(time) + ')' 
        
        session['gold'] += session['gold']
        session['activities'].insert(0, activity)
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')

        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        
