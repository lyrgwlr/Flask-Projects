from flask import Blueprint

handler = Blueprint('handler',__name__)

from app.handler import handler