from flask import Blueprint

ccppviews = Blueprint('ccppviews', __name__)

from . import ccpp_equipmentView, ccpp_turbine_auxiliaryView, ccpp_questionnaireView, ccpp_calculateView, ccpp_circulating_waterView, ccpp_chimney_calculateView, ccpp_turbineView, ccpp_select_gasView, ccpp_economicView, ccpp_biomassView, ccpp_form_schemes, ccpp_imgView
