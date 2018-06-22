from flask import Blueprint

gpg_view = Blueprint('gpg_view', __name__)

from . import gpg_views