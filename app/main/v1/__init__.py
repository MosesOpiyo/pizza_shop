from flask import Blueprint, blueprints
from flask_restful import Api

main = blueprints('main',__name__,url_prefix='/main')
api = Api(main,catch_all_404s=True)

from .models import models
from.views import views 