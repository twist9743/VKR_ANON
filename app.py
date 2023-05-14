import hashlib
import os
import random
from itertools import combinations, groupby
from operator import itemgetter

from flask import (Flask, make_response, redirect, render_template, request,
                   session, url_for)

from fundament import (W_NORM, auth_chance_1_param, auth_chance_2_param,
                       read_file)

app = Flask(__name__)

app.config.update(SECRET_KEY="osd(99092=36&462134kjKDhuIS_d23")


def get_key(param_dict, value):
    for k, Wj_min in param_dict.items():
        if Wj_min == value:
            return k



@app.route("/", methods=["GET", "POST"])
def home():
    res = make_response(render_template("home.html"))
    if request.cookies.get("session", None) == None:
        res.set_cookie(
            "session",
            hashlib.sha256(str(int(random.random() * 10)).encode()).hexdigest(),
        )
    return res


@app.route("/api/upload_file", methods=["POST"])
def api_upload():
    if request.cookies.get("session", None):
        session = request.cookies.get("session", None)
        file = request.files["file"]
        file_path = "user_files/" + session + "." + file.filename.split(".")[-1]
        file.save(file_path)
        if not os.path.isfile(file_path):
            return {"error": True, "message": "Ошибка сохранения файла."}
    else:
        return {
            "error": True,
            "message": "Не создана сессия. Перезайдите на главную страницу перед получением результатов.",
        }
    return {"error": False}

@app.route("/results", methods=["GET"])
def results():
    if request.cookies.get("session", None) == None:
        return redirect(url_for("home.html"))
     
    session = request.cookies.get("session")
    
    if os.path.isfile("user_files/" + session + ".xlsx"):
        df, params = read_file("user_files/" + session + ".xlsx", "xlsx")
    elif os.path.isfile("user_files/" + session + ".csv"):
        df, params = read_file("user_files/" + session + ".csv", "csv")
        
    result_1_param = {}
    result_2_param = {}

    Q_j_list = []
    for i in params:
        Q_j_list.append(auth_chance_1_param(df, i, result_1_param))
   
    xy_list = []
    for i in combinations(params.to_list(), 2):
        xy_list.append(
            auth_chance_2_param(df, i[0], i[1], result_2_param)
        )

    
    result_dict=dict()
    for key in result_1_param.keys():
        row={}
        keys = list(k for k in result_2_param.keys() if key in k.split(', '))
        for k in keys:
            table_key = k.split(', ')
            table_key.remove(key)
            row.update({table_key[0]:result_2_param[k]})
        row.update({key:result_1_param[key]})
        result_dict.update({key:row})
    print(result_dict)
    
    bot_table=dict()
    min_wj=list()
    result = list()
    regExp = "[,']"
    for i in range(0,len(result_1_param)):
        if list(result_1_param.values())[i]<0.05:
            min_wj.append(list(result_1_param.values())[i])
        else:
            bot_table[list(result_1_param.keys())[i]]=list(result_1_param.values())[i]
    
    for i in range(0,len(min_wj)):    
        min_params_list = get_key(result_1_param, min_wj[i]).split(sep=",")
    keys = list(result_2_param.keys())   
    params_list = list()
    for i in range(len(keys)):
        for j in range(0, i):
            params_list.append(keys[i].split(sep=","))
    new_params_list = [el for el, _ in groupby(params_list)]
            
    for i in range(len(new_params_list)):
        if str(new_params_list[i]).translate(
                {ord(i): None for i in regExp}
            ).find(str(min_params_list).translate(
                {ord(i): None for i in regExp}
            ))!=-1:
            result.append(list(new_params_list[i]))
    
    final_result = dict()
    for i in range(len(result_2_param)):
        for j in range(len(result)):
            regExp = "[,']"
            check_result = str(list(result_2_param.keys())[i]).translate(
                {ord(i): None for i in regExp}
            )

           
            test_str = str((result[j])).translate({ord(i): None for i in regExp})
            test_str = " ".join(test_str.split())
           
            if check_result == test_str:
                
                final_result[list(result_2_param.keys())[i]] = list(
                    result_2_param.values()
                )[i]
    bot_final= bot_table | final_result
    bot_final_sorted = dict(sorted(bot_final.items(), key=itemgetter(1), reverse=True))
    
    
  

    
    return render_template("results.html", params=params,result_dict=result_dict, bot_final_sorted=bot_final_sorted)


@app.route("/full_results", methods=["GET"])
def full_results():
    if request.cookies.get("session", None) == None:
        return redirect(url_for("home.html"))

    session = request.cookies.get("session")

    if os.path.isfile("user_files/" + session + ".xlsx"):
        df, params = read_file("user_files/" + session + ".xlsx", "xlsx")
    elif os.path.isfile("user_files/" + session + ".csv"):
        df, params = read_file("user_files/" + session + ".csv", "csv")

    result_1_param = {}
    result_2_param = {}

    Q_j_list = []
    for i in params:
        Q_j_list.append(auth_chance_1_param(df, i, result_1_param))
   
    xy_list = []
    for i in combinations(params.to_list(), 2):
        xy_list.append(
            auth_chance_2_param(df, i[0], i[1], result_2_param)
        )

    return render_template(
        "full_results.html",
        data={
            "Q_j_list": Q_j_list,
            "xy_list": xy_list,
            "result_1_param": result_1_param,
            "result_2_param": result_2_param,
        },
    )


if __name__ == "__main__":
    app.run(debug=True)
