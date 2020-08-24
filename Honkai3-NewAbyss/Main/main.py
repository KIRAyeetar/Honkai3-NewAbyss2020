import Main.abyss as ab
import pandas as pd
import numpy as np
import os

def run():
    save_path = '../Data/csv/m5/'

    # 初始化深渊，设置初始人数
    abyss = ab.Abyss(member_count=200000)
    abyss.init_abyss()

    # 6星期，12轮深渊，1个版本；2个版本一个赛季
    # 开打
    data = pd.DataFrame()

    for abyss_count in range(1, 96+1):
        print('abyss_count: %d' % abyss_count)
        data = data.append(abyss.fight(abyss_count=abyss_count, if_save_csv=1, save_path=save_path, save_name_sp='new-'))
    data['ori_abyss_level'] = data['id'].apply(lambda a: int(a.split('-')[0]))
    data.to_csv(save_path + 'data_all.csv', index=None)


def ana():
    data = pd.read_csv('../Data/csv/data_all.csv')
    data['ori_abyss_level'] = data['id'].apply(lambda a: int(a.split('-')[0]))
    data_1 = data[data['abyss_count']==1]
    data_24 = data[data['abyss_count']==24]
    data_48 = data[data['abyss_count']==48]

    # data_tmp = data[(data['abyss_level']==10) | (data['abyss_level']==11) | (data['abyss_level']==12)]
    # print(len(data_tmp))
    # data_tmp = data[(data['ori_abyss_level'] == 9) | (data['ori_abyss_level'] == 8)]
    # print(len(data_tmp))
    #
    # print(sum(data['fund_level']))
    #
    # print(np.mean(data['effort_level']))


def get_file_list(file_path=''):
    file_list = os.listdir(file_path)
    return file_list


if __name__ == '__main__':
    run()

