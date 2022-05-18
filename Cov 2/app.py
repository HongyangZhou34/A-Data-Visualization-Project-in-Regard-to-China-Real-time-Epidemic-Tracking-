from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    return jsonify({"day":data[1],"confirm": data[0], "suspect": data[4], "heal": data[3], "dead": data[2]})

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    return jsonify({"day": data[1], "confirm_add": data[0], "suspect_add": data[2]})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    return jsonify({"city": data[1], "confirm": data[0]})


@app.route("/time2")
def get_time():
    return utils.get_time()

@app.route('/ajax',methods=["get","post"])
def hello_world4():
    name = request.values.get("name")
    score =  request.values.get("score")
    print(f"name:{name},score:{score}")
    return '10000'

@app.route('/tem')
def hello_world3():
    return render_template("index.html")

@app.route('/login')
def hello_world2():
    name =  request.values.get("name")
    pwd =  request.values.get("pwd")
    return f'name={name},pwd={pwd}'

@app.route("/abc")
def hello_world1():
    id = request.values.get("id")
    return f"""
    <form action="/login">
        账号：<input name="name" value="{id}"><br>
        密码：<input name="pwd">
        <input type="submit">
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True)
