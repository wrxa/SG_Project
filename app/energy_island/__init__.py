from flask import Blueprint

energy_island = Blueprint('energy_island', __name__)

from . import views
