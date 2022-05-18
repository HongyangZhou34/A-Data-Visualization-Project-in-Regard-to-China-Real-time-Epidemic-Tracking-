
import requests
import time
import json
import csv


def get_tencent_data():
    """
    :return: 返回历史数据和当日详细数据
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)  # json字符串转字典
    data_all = json.loads(res['data'])

    history = {}  # 历史数据

    i = data_all["chinaTotal"]
    # 改变时间格式,不然插入数据库会报错，数据库是datetime类型
    ds = data_all["lastUpdateTime"].split(" ")[0]
    confirm = i["confirm"]
    suspect = i["suspect"]
    heal = i["heal"]
    dead = i["dead"]
    history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}

    i = data_all["chinaAdd"]
    ds = data_all["lastUpdateTime"].split(" ")[0]
    confirm = i["confirm"]
    suspect = i["suspect"]
    heal = i["heal"]
    dead = i["dead"]
    history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    details = []  # 当日详细数据
    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # list 25个国家
    data_province = data_country[0]["children"]  # 中国各省
    for pro_infos in data_province:
        province = pro_infos["name"]  # 省名
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details


def update_details():
    """
    更新 details 数据
    :return:
    """
    with open("details.csv", 'w', encoding='gbk', newline='') as fp:
        titles = ['time', 'provience', 'city', 'confirm', 'confirm_add', 'heal', 'dead']
        write = csv.writer(fp)
        write.writerow(titles)
        try:
            li = get_tencent_data()[1]  #  0 是历史数据字典,1 最新详细数据列表
            print(li)
            for item in li:

                write.writerow(item)
            print(f"{time.asctime()}更新最新数据完毕")

        except:
            print("更新失败")


def insert_history():
    """
        保存历史数据
    :return:
    """
    dic = get_tencent_data()[0]
    with open('history.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for k, v in dic.items():
                if k == row[0]:
                    print("{} 日的数据已更新".format(row[0]))
                    exit()
    with open("history.csv", 'a', encoding='utf8', newline='') as fp:
        try:
              # 0 是历史数据字典,1 最新详细数据列表
            for k, v in dic.items():
                data_list = []
                data_list.append(k)
                for name, data in v.items():
                    data_list.append(data)
            write = csv.writer(fp)
            write.writerow(data_list)
            print(f"{time.asctime()}更新最新数据完毕")
        except:
            print("更新失败")


if __name__ == "__main__":
    update_details()


