"""Route declaration."""
from flask import current_app as app
from flask import render_template
from flask import Flask,Markup,url_for,redirect,make_response,request,jsonify
from .parseresult import getbuilddate



@app.route('/<int:sessionid>',methods=['GET'])
def home(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        nav = [
        {"name": "Summary", "url": url_for('getsummarydir', sessionid=sessionid)},
        {"name": "All", "url": url_for('getalldir', sessionid=sessionid)},
        {"name": "Success", "url": url_for('getsuccessdir', sessionid=sessionid)},
        {"name": "Failed", "url":  url_for('getfaileddir', sessionid=sessionid)},
        {"name": "Unreachable", "url":  url_for('getunreachdir', sessionid=sessionid)},
        {"name": "Pending", "url":  url_for('getpendingdir', sessionid=sessionid)}
        ]

        return render_template(
          "home.html",
          nav=nav,
          title="RUSE",
          description="Root Update Status Environment for session {}".format(sessionid),
        )

@app.route('/summary/<int:sessionid>',methods=['GET'])
def getsummarydir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['Summary']), 200, headers)

@app.route('/all/<int:sessionid>',methods=['GET'])
def getalldir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['All hosts info']), 200, headers)

@app.route('/success/<int:sessionid>',methods=['GET'])
def getsuccessdir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['success hosts info']), 200, headers)

@app.route('/failed/<int:sessionid>',methods=['GET'])
def getfaileddir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['failed hosts info']), 200, headers)

@app.route('/unreachable/<int:sessionid>',methods=['GET'])
def getunreachdir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['unreachable hosts info']), 200, headers)

@app.route('/pending/<int:sessionid>',methods=['GET'])
def getpendingdir(sessionid):
    if request.method != 'GET':
        return make_response("Wrong Format", 400)
    tdir = getbuilddate(sessionid)
    if not len(tdir.keys()):
        return Markup('<h1> Nothing to process</h1>')
    else:
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(tdir['Pending hosts info']), 200, headers)

