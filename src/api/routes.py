"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import math
import random
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
#from models import Person

api = Blueprint('api', __name__)


@api.route('/excuse', methods=['GET'])
def handle_excuse():

    who = ["My dog ", "My grandma ", "His turtle ", "My bird "]
    did = [" ate ", " lost ", " crashed ", " broke "]
    what = [" my lunch ", " my keys ", " my car ", " my head "]
    when = [
        " just when I was about to leave.",
        " right before you called.",
        " when I was finishing class.",
        " during my lunch.",
        " while I was praying."
    ]

    excuse = who[math.floor(random.randint(0, len(who)-1))] + did[math.floor(random.randint(0, len(did)-1))] + what[math.floor(random.randint(0, len(what)-1))] + when[math.floor(random.randint(0, len(when)-1))]
    response_body = {
        "excuse": excuse
    }

    return jsonify(response_body), 200