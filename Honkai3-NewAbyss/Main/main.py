import Plan_B.Main.abyss as ab
import pandas as pd
import os


def run():
    """自行设置保存模拟结果的目录；默认在'../Data/csv/m1/'文件夹中，没有请新建"""
    save_path = '../Data/csv/m1/'

    # 初始化深渊，设置初始人数
    abyss = ab.Abyss(member_count=200000)
    abyss.init_abyss()

    # 6星期，12轮深渊，1个版本；2个版本一个赛季

    data = pd.DataFrame()
    for abyss_count in range(1, 96+1):
        print('abyss_count: %d' % abyss_count)
        data = data.append(abyss.fight(abyss_count=abyss_count, if_save_csv=1, save_path=save_path, save_name_sp='new-'))
    data['ori_abyss_level'] = data['id'].apply(lambda a: int(a.split('-')[0]))
    data.to_csv(save_path + 'data_all.csv', index=None)


def ana():
    """在目录Analyze文件夹中进行数据分析"""
    pass


def get_file_list(file_path=''):
    file_list = os.listdir(file_path)
    return file_list


if __name__ == '__main__':
    run()

