import json

from flask import Blueprint, render_template

with open('pets.json', encoding='utf-8') as fh:
    pets = json.load(fh)

bp = Blueprint('pet', __name__, url_prefix='/pets')


@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)


@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)
