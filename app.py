from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

application = app = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

import json
from bson.json_util import dumps
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.zqvmomu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/team')
def team():
   return render_template('team.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    doc = {
        'name' : name_receive,
        'comment' : comment_receive,
        'password' : password_receive
    }
    db.fan.insert_one(doc)

    return jsonify({'msg': '저장완료'})

@app.route("/delete", methods=["POST"])
def delete_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)
    
    ori_pass = list(db.fan.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    print(password_receive)
    # return jsonify({'msg': '응답'})

    if ori_pass == password_receive:
        
        doc = {
            '_id' : obj_id
        }
        # print(doc)
        db.fan.delete_one(doc)
        return jsonify({'msg': '삭제완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})
    

@app.route("/edit", methods=["POST"])
def edit_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']


    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)

    ori_pass = list(db.fan.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    # return jsonify({'msg': '응답'})

    if ori_pass == password_receive:
        db.fan.update_one({'_id': obj_id}, {"$set":{'comment':comment_receive}})

        # doc = {
        #     '_id' : obj_id
        # }
        # print(doc)
        # db.fan.delete_one(doc)
        return jsonify({'msg': '수정완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})


    

@app.route("/guestbook", methods=["GET"])
# def guestbook_get():
#     all_fans = list(db.fan.find({}))
#     json_all_fans = json.dumps(str(all_fans), ensure_ascii=False)
#     return jsonify({'result': json_all_fans})

def guestbook_get():
    all_fans = list(db.fan.find({}))
    return jsonify({'result': dumps(all_fans)})




















@app.route("/comment/save", methods=["POST"])
def team_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    # json
    # params = request.get_json()
    # print(params['user_id'])


    doc = {
        'name' : name_receive,
        'comment' : comment_receive,
        'password' : password_receive
    }
    db.team.insert_one(doc)

    return jsonify({'msg': '저장완료'})

@app.route("/comment/delete", methods=["POST"])
def team_delete_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)
    # print(password_receive)
    ori_pass = list(db.team.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    # return jsonify({'msg': '응답'})
    print(ori_pass)

    if ori_pass == password_receive:
        
        doc = {
            '_id' : obj_id
        }
        # print(doc)
        db.team.delete_one(doc)
        return jsonify({'msg': '삭제완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})
    

@app.route("/comment/edit", methods=["POST"])
def team_edit_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']


    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)

    ori_pass = list(db.team.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    # return jsonify({'msg': '응답'})

    if ori_pass == password_receive:
        db.team.update_one({'_id': obj_id}, {"$set":{'comment':comment_receive}})

        # doc = {
        #     '_id' : obj_id
        # }
        # print(doc)
        # db.fan.delete_one(doc)
        return jsonify({'msg': '수정완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})


    

@app.route("/comment/get", methods=["GET"])
# def guestbook_get():
#     all_fans = list(db.fan.find({}))
#     json_all_fans = json.dumps(str(all_fans), ensure_ascii=False)
#     return jsonify({'result': json_all_fans})

def team_get():
    all_teams = list(db.team.find({}))
    # print(dumps(all_teams))
    return jsonify({'result': dumps(all_teams)})



@app.route("/data", methods=["GET"])
# def guestbook_get():
#     all_fans = list(db.fan.find({}))
#     json_all_fans = json.dumps(str(all_fans), ensure_ascii=False)
#     return jsonify({'result': json_all_fans})

def profile_get():
    all_profiles = list(db.profiles.find({},{'_id':False}))
    return jsonify({'result':all_profiles})




if __name__ == '__main__':
   app.run()
