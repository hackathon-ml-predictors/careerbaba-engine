import pprint
import json
import requests
import pandas as pd
import os
import numpy as np

from flask import (
    Blueprint, render_template, current_app, request, redirect, session,
    url_for, jsonify)
# from lib.engine import engine
# from lib.util import hook_on_product
# from urllib.parse import urlencode
from .models import Students
from lib.engine import train, get_recommanded_job


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


@careerbaba_bp.route('/recommandation', methods=['POST','GET'])
def recommandation():
    """
    1. get data post
    2. get_recommanded_job
    """
    PostData = []
    jsonPostData = []
    content = request.get_json(silent=True)
    last = ''
    for row in content:
        # print(row['value'])
        # data = {row['name']:row['value']}
        if last != row['name']:
            PostData.append(row['value'])
            last = row['name']

    jsonPostData.append(PostData)
    print(len(PostData))
    jsonPostData = np.array(jsonPostData)
    print(jsonPostData)

    # return ('Success',200)
    

    # jsonPostData = [[76, 87, 60, 84, 89, 73, 62, 88, 69, 7, 1, 1, 2, 5, 0, 1, 0, 6, 1,
    #     1, 0, 1, 0, 7, 5, 0, 7, 0, 0, 23, 0, 1, 0, 0, 1, 1, 1, 1]]

#     jsonPostData = np.array([[84,72,88,62,66,63,78,94,60,12,2,1,6,6,'yes','no','no','r programming','cloud computing','no','yes','poor','excellent','parallel computing','developer','higherstudies','BPA','no','no','Romance','salary','no','stubborn','Technical','salary','smart worker','no','no'
# ]])
    # print(jsonPostData)
    # return ('Success',200)

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder

    labelencoder = LabelEncoder()

    for i in range(14,38):
        jsonPostData[:,i] = labelencoder.fit_transform(jsonPostData[:,i])

    print((jsonPostData))
    job = get_recommanded_job(jsonPostData)
    
    return (str(job),200)
    # return ('Success',200)


@careerbaba_bp.route('/testtrian', methods=['POST'])
def testtrian():
    csv_file = request.files.get("file")
    if not csv_file:
        return jsonify(errors="No file was uploaded. Please upload a file."), 422

    data_df = pd.read_csv(csv_file)
    train(data_df)
    return ('Success',200)