"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/game_of_life')
@view('game_of_life')
def game_of_life():
    """Renders the game of life page."""
    return dict(
        title='Game of life',
        year=datetime.now().year
    )


@route('/infect')
@view('infect')
def infect():
    """Renders the game of life page."""
    return dict(
        title='infect',
        year=datetime.now().year
    )