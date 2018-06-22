from flask import Blueprint

biomassviews = Blueprint('biomassviews', __name__)

from . import viewsBiomass
