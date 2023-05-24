import os
from itertools import combinations

import matplotlib.pyplot as plt
import pandas as pd

W_NORM = 0.05


def read_file(file_name, file_ext="xlsx"):
    df = pd.read_excel(file_name, header=0)
    
    return df

def read_csv(file_name,file_ext="csv"):
    df = pd.read_csv(file_name, header=0)
    
    return df


def all_info(df):
    V = df.shape[0]
    return V


result_1_param = {}
result_2_param = {}
# Define a function to execute SQL queries
""" def execute_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result """


def auth_chance_1_param(df, param, result_1_param):
    # Step 1: Extract the values of attribute j from the database
    def step_1(df, param):
        Q = df[param].nunique()
        
        return Q

    def step_2(df, param):
        Q_max = df[param].value_counts().max()
        
        return Q_max

    # Step 3 find chance of identification
    def step_3(df, param):
        Q = step_1(df, param)
        V = all_info(df)
        Wj = Q / V
        return Wj

    def step_4(df, param):
        Q_j = df[param].value_counts().to_dict()
        if isinstance(list(Q_j.keys())[0], pd.Timestamp):
            Q_j = {key.strftime("%d.%m.%Y"):Q_j[key] for key in Q_j}
        
        return Q_j

    Q_j = step_4(df, param)

    Wj = step_3(df, param)
    result_1_param[param] = Wj
    # graph_values(Q_j)
    return Q_j

    # Step 4 find same values for all attributes
    """ def auth_chance_2_param():
    #найти Q для каждого из параметров и перемножить
    # Найти диапазон с наибольшим количеством имен, начинающихся на какую-то букву(пока не ясно как ее выбирать)
    #Определить для этого диапазона Q(количество различных значений совокупности атрибута)
      y = np.linspace(0, 100, len(Q_j))
        x = Q_j.values()
        plt.plot(x, y)
        plt.plot(x, y, 'b-o')
        plt.plot(x, y , 'r-', lw=2)
        plt.show() 
    # """


def auth_chance_2_param(df, param1, param2, result_2_param):
    
    

    df[param1]=df[param1].astype(str)
    print(df[param1][0])
    first_letter = df[param1].str[0]

    # Подсчет уникальных значений
    count = first_letter.value_counts()

    # Сортировка результатов по убыванию количества
    sorted_count = count.sort_values(ascending=False)

    # Вывод буквы, которая встречается чаще всего
    most_common_letter = sorted_count.index[0]
    
    Q_1 = df[param1].nunique()
    Q_2 = df[param2].nunique()
    Q = Q_1 * Q_2
    
    V_1 = df[param1].str.startswith(most_common_letter).value_counts()[True]
    V_1 = df[param1].str.startswith(most_common_letter)
    values = [
        f"{df[param1][i]} {df[param2][i]}" for i, x in enumerate(V_1) if x == True
    ]
    
    unique_values = set(values)
    
    Q_j = {
        key: value
        for key, value in zip(
            unique_values, [values.count(item) for item in unique_values]
        )
    }

    x = list(Q_j.values())  # Количество повторов
    y = list(Q_j)  # Совокупность атрибутов
    """     
        plt.plot(x, y)
        plt.plot(x, y, "b-o")
        plt.plot(x, y, "r-", lw=2)
        plt.show()
    """
    Wj = len(unique_values) / len(values)
    
    result_2_param[f"{param1}, {param2}"] = Wj
    

    return (x, y)







""" 
def graph_chance(w_norm, Result):
    Result["W_norm"] = w_norm
    print(Result)
    plt.bar(Result.keys(), Result.values())
    # plt.hist(Result.keys(), Result.values(), bins=10)
    plt.show()
    return
"""
""" 
def main():
    for i in params:
        auth_chance_1_param(df, i, w_norm)

    graph_chance(w_norm, result_1_param)
    for i in combinations("0123", 2):
        auth_chance_2_param(df, params[int(i[0])], params[int(i[1])])
    graph_chance(w_norm, result_2_param)
"""

""" main() """
