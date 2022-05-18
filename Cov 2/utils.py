import time
import pandas as pd


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{}")
    return time_str.format("年","月","日")


def get_c1_data():
    """
    :return: 返回大屏div id=c1 的数据
    """
    df = pd.read_csv("history.csv", encoding='gbk')
    data = []
    for i in range(4):
        data.append(str(df.iloc[df.shape[0]-1][i+1]))
    return data


def get_c2_data():
    """
    :return:  返回各省数据
    """
    data = []
    df = pd.read_csv("details.csv", encoding='gbk')
    df_1 = df.groupby(df['provience']).sum()
    name_list = df_1.index.tolist()
    num_list = df_1['confirm'].tolist()
    for i in range(len(df_1)):
        data_list = []
        data_list.append(name_list[i])
        data_list.append(num_list[i])
        data.append(data_list)
    return data


def get_l1_data():
    data = []
    day_list = []
    confirm_list =[]
    dead_list = []
    heal_list = []
    suspect_list = []
    df = pd.read_csv("history.csv", encoding='gbk')
    for i in range(df.shape[0]):
        confirm_list.append(str(df.iloc[i]['confirm']))
        day_list.append(str(df.iloc[i]['ds'][5:]))
        dead_list.append(str(df.iloc[i]['dead']))
        heal_list.append(str(df.iloc[i]['heal']))
        if df.iloc[i]['suspect'] < 0:
            suspect_list.append('0')
    data.append(confirm_list)
    data.append(day_list)
    data.append(dead_list)
    data.append(heal_list)
    data.append(suspect_list)
    return data


def get_l2_data():
    data = []
    day_list = []
    confirm_add_list = []
    suspect_add_list = []
    df = pd.read_csv("history.csv", encoding='gbk')
    for i in range(df.shape[0]):
        confirm_add_list.append(str(df.iloc[i]['confirm_add']))
        day_list.append(str(df.iloc[i]['ds'][5:]))
        suspect_add_list.append(str(df.iloc[i]['suspect_add']))
    data.append(confirm_add_list)
    data.append(day_list)
    data.append(suspect_add_list)
    return data


def get_r1_data():
    """
    :return:  返回非湖北地区城市确诊人数前5名
    """
    data = []
    df = pd.read_csv("details.csv", encoding='gbk')
    df = df.sort_values(by=['confirm'], ascending=False).head(5)
    data.append(df['confirm'].tolist())
    data.append(df['city'].tolist())
    return data


if __name__ == "__main__":
    get_c2_data()