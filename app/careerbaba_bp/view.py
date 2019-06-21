import pprint
import json
import requests
import pandas as pd
import os

from flask import (
    Blueprint, render_template, current_app, request, redirect, session,
    url_for, jsonify)
# from lib.engine import engine
# from lib.util import hook_on_product
# from urllib.parse import urlencode
from .models import Students
from lib.engine import train


careerbaba_bp = Blueprint(' ', __name__, url_prefix='/careerbaba')


@careerbaba_bp.route('/')
def index():
    """

    """
    
    x = Students(name='jigness')
    x.save()

    AllStudents = Students.objects.all()
    return jsonify(AllStudents)
    # print ('asdasdasd')
    return ('Success',200)


@careerbaba_bp.route('/trian', methods=['POST'])
def trian():
    """
    1. render csv and save data in monogo DB
        1.1 data repair on over row level.
    2. call train method
    3. responce to cli or api!
    
    """
    csv_file = request.files.get("file")
    if not csv_file:
        return jsonify(errors="No file was uploaded. Please upload a file."), 422
    # sha_signature = sha1(csv_file.read()).hexdigest()
    # csv_file.seek(0)
    # merchant_exists = False
    # try:
    #     merchant = Merchant.objects.get(sha_signature=sha_signature)
    #     merchant_exists = True
    # except DoesNotExist:
    #     data = {
    #         "sha_signature": sha_signature,
    #         "token": "",
    #         "shop": {},
    #         "widgets": {"upsell": {}},
    #         "activated": False,
    #     }
    #     merchant, errors = MerchantSchema().load(data)
    for row in csv_file:
        try:
            x = Students(name=row)
            x.save()
        except IndexError as ex:
            print("ERROR: %s in file %s doesn't contain 5 colums" % (row, i))

    # data_df = pd.read_csv(csv_file)
    # print(data_df)
    #     merchant.save()
    return ('Success',200)


@careerbaba_bp.route('/recommandation', methods=['POST'])
def recommandation():
    """
    1. get data post
    2. 
    """
    return ('Success',200)


@careerbaba_bp.route('/testtrian', methods=['POST'])
def testtrian():
    csv_file = request.files.get("file")
    if not csv_file:
        return jsonify(errors="No file was uploaded. Please upload a file."), 422

    data_df = pd.read_csv(csv_file)
    train(data_df)
    return ('Success',200)