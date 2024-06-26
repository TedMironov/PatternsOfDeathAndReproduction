"""
Routes and views for the bottle application.
"""

from bottle import route, view, request
from datetime import datetime
from game_of_life_handler import snapshot, get_snapshot
from snapshot_repo import InMemorySnapshotRepository, JsonSnapshotRepository, SnapshotRepository

snapshotRepo: SnapshotRepository = JsonSnapshotRepository()

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='О нас',
        message='',
        year=datetime.now().year
    )

@route('/game_of_life')
@view('game_of_life')
def game_of_life():
    """Renders the game of life page."""
    return dict(
        title='Игра жизнь',
        year=datetime.now().year,
        snapshots=snapshotRepo.all_snapshot_names()
    )


@route('/infect')
@view('infect')
def infect():
    """Renders the game of life page."""
    return dict(
        title='infect',
        year=datetime.now().year
    )

@route('/underwater_world')
@view('underwater_world')
def underwater():
    """Renders the game of life page."""
    return dict(
        title='underwater world',
        year=datetime.now().year
    )

@route('/snapshot/add', method='POST')
def save_snapshot():
    return snapshot(dict(request.json), snapshotRepo)

@route('/snapshots/<name>')
def snapshot_get(name: str):
    return get_snapshot(name, snapshotRepo)
