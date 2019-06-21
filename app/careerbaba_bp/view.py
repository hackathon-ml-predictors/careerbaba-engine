import pprint
import json
import requests
from flask import (
    Blueprint, render_template, current_app, request, redirect, session,
    url_for)
# from lib.engine import engine
# from lib.util import hook_on_product
# from urllib.parse import urlencode
import os

careerbaba_bp = Blueprint(' ', __name__, url_prefix='/careerbaba')


@careerbaba_bp.route('/')
def index():
    """

    """
    print ('asdasdasd')
    return ('Success',200)


@careerbaba_bp.route('/trian', methods=['POST'])
def trian():
    """
    1. render csv and save data in monogo DB
        1.1 data repair on over row level.
    2. call train method
    3. responce to cli or api!
    
    """
    return ('Success',200)


@careerbaba_bp.route('/recommandation', methods=['POST'])
def recommandation():
    """
    1. get data post
    2. 
    """
    return ('Success',200)
