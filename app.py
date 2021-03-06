""" Create by Ken at 2020 Feb 11 """
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from connection import Connection
import json
import traceback

app = Flask(__name__)
CORS(app)

con = Connection("localhost", "root", "abc13579", "QuanLyCayTrongVatNuoi")


####### Phong ban
@app.route("/phong-ban", methods=["GET"])
def phongban():
    print(request.method)
    return jsonify(con.phongban(action="GET"))


@app.route("/phong-ban", methods=["POST"])
def phongbanPOST():
    content = request.data
    r_dict = json.loads(content.decode('utf-8'))
    return jsonify(con.phongban(action=request.method, data=r_dict))


@app.route("/phong-ban", methods=["PUT"])
def phongbanPUT():
    content = request.data
    r_dict = json.loads(content.decode('utf-8'))
    return jsonify(con.phongban(action=request.method, data=r_dict))


@app.route("/phong-ban", methods=["DELETE"])
def phongbanDELETE():
    content = request.data
    r_dict = json.loads(content.decode('utf-8'))
    return jsonify(con.phongban(action=request.method, data=r_dict))


### nhan viên
@app.route("/nhan-vien", methods=["GET"])
def nv():
    print(request.method)
    return jsonify(con.nhanvien(action=request.method))


@app.route("/nhan-vien", methods=["POST"])
def nvPOST():
    content = request.data
    r_dict = json.loads(content.decode('utf-8'))
    return jsonify(con.nhanvien(action=request.method, data=r_dict))


# vat_nuoi
@app.route("/hang-hoa-vat-nuoi", methods=["GET"])
def get_all_vat_nuoi():
    try:
        return jsonify(con.vat_nuoi(action="GET"))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-vat-nuoi", methods=["POST"])
def add_vat_nuoi():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.vat_nuoi(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-vat-nuoi", methods=["PUT"])
def update_vat_nuoi():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.vat_nuoi(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-vat-nuoi", methods=["DELETE"])
def delete_vat_nuoi():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.vat_nuoi(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


# cay_trong
@app.route("/hang-hoa-cay-trong", methods=["GET"])
def get_all_cay_trong():
    try:
        return jsonify(con.cay_trong(action="GET"))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-cay-trong", methods=["POST"])
def add_cay_trong():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.cay_trong(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-cay-trong", methods=["PUT"])
def update_cay_trong():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.cay_trong(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


@app.route("/hang-hoa-cay-trong", methods=["DELETE"])
def delete_cay_trong():
    try:
        content = request.data
        r_dict = json.loads(content.decode('utf-8'))
        return jsonify(con.cay_trong(action=request.method, data=r_dict))
    except:
        print(traceback.format_exc())
        return 'Internal server error', 500


app.run(host="0.0.0.0", port=8080)
