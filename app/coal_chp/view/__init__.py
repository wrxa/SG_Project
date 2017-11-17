  

from flask import Blueprint

coalviews = Blueprint('coalviews', __name__)

from . import coalViews as coal_views