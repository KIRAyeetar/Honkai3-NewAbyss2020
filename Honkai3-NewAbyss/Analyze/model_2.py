import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    data = pd.read_csv('../Data/csv/m2/data_all.csv')
    data_1 = data[data['abyss_count']==1]
    data_24 = data[data['abyss_count']==24]
    data_48 = data[data['abyss_count']==48]
    data_72 = data[data['abyss_count']==72]
    data_96 = data[data['abyss_count']==96]
    data_list = [data_1, data_24, data_48, data_72, data_96]


    # 文字分析
    '''
                                            老   新24期  新48期  新72期  新96期
    原 苦痛保级人员占比20%, 平均每期水晶收益   260    336    324     319    316
    原 红莲升降人员占比10%, 平均每期水晶收益   340    415    389     377    371
    原 红莲保级人员占比4.5%, 平均每期水晶收益  420    474    454     441    431
    原 无限升降人员80人, 平均每期水晶收益      480    537    530     512    493
    原 无限保级人员10人, 平均每期水晶收益      600    595    588     556    529
    '''
    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 7]
        print(np.mean(data_tmp['fin_crystal']/max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 8]
        print(np.mean(data_tmp['fin_crystal'] / max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 9]
        print(np.mean(data_tmp['fin_crystal'] / max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 10]
        print(np.mean(data_tmp['fin_crystal'] / max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 11]
        print(np.mean(data_tmp['fin_crystal'] / max(data_tmp['abyss_count'])))


    '''
                老    新1期   新24期  新48期  新72期  新96期
    原罪人数占比 33%    50%     30%     33%    34%    34%
    苦痛人数占比 33%    33%     62%     61%    60%    59%
    红莲人数占比 10%    ~~~     8 %     5 %    4 %    4 %
    '''
    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 4) | (data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6)]
        print(len(data_tmp)*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 7) | (data_i['abyss_level'] == 8) | (data_i['abyss_level'] == 9)]
        print(len(data_tmp)*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 10) | (data_i['abyss_level'] == 11) | (data_i['abyss_level'] == 12)]
        print(len(data_tmp)*1./len(data_i))

    '''
                   新1期     新24期    新48期      新72期      新96期
       奖杯总数  141206425 231877648  218865491  214733235   212015879
    原罪奖杯总数  54675446  41724497   46626703   47305868    45508073
    苦痛奖杯总数  78910196  155497381  151798984  149427346   148323718
    红莲奖杯总数   175337   33707406   19998693   17578166    17272507
    '''
    print(sum(data_1['fin_cup']), sum(data_24['fin_cup']), sum(data_48['fin_cup']), sum(data_72['fin_cup']), sum(data_96['fin_cup']))


    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 4) | (data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6)]
        print(sum(data_tmp['fin_cup']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 7) | (data_i['abyss_level'] == 8) | (data_i['abyss_level'] == 9)]
        print(sum(data_tmp['fin_cup']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 10) | (data_i['abyss_level'] == 11) | (data_i['abyss_level'] == 12)]
        print(sum(data_tmp['fin_cup']))


    '''
                 新1期   新24期   新48期   新72期    新96期
       平均凹度  0.700    0.717   0.734    0.749    0.763
    原罪平均凹度  0.689   0.515   0.501    0.477    0.468
    苦痛平均凹度  0.802   0.780   0.835    0.882    0.928
    红莲平均凹度  0.838   0.976   1.072    1.153    1.192
    '''
    print(np.mean(data_1['effort_level']), np.mean(data_24['effort_level']), np.mean(data_48['effort_level']),
          np.mean(data_72['effort_level']), np.mean(data_96['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 4) | (data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6)]
        print(np.mean(data_tmp['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 7) | (data_i['abyss_level'] == 8) | (data_i['abyss_level'] == 9)]
        print(np.mean(data_tmp['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 10) | (data_i['abyss_level'] == 11) | (data_i['abyss_level'] == 12)]
        print(np.mean(data_tmp['effort_level']))


    '''
                     新1期   新24期   新48期   新72期   新96期
      总不打人数占比   30%     30%      30%     30%      30%
    原罪不打人数占比   15%     14%      16%     18%      18%
    苦痛不打人数占比   7 %     15%      13%     11%      10%
    红莲不打人数占比   ~~~    0.01%    0.06%   0.05%    0.05%
    '''
    for data_i in data_list:
        data_tmp = data_i
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 4) | (data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6)]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 7) | (data_i['abyss_level'] == 8) | (data_i['abyss_level'] == 9)]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 10) | (data_i['abyss_level'] == 11) | (data_i['abyss_level'] == 12)]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    # 画点图
    graph(data)


def graph(data, if_save=0, save_path=''):
    # 原 苦痛/红莲升降/红莲保级 人员 随深渊次数的 平均水晶收益
    crystal_kt = []
    crystal_kt2hl = []
    crystal_hl = []
    for abyss_count in range(1, max(data['abyss_count'])+1):
        data_i = data[data['abyss_count']==abyss_count]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 7)]
        crystal_kt += [np.mean(data_tmp['fin_crystal'] / abyss_count)]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 8)]
        crystal_kt2hl += [np.mean(data_tmp['fin_crystal'] / abyss_count)]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 9)]
        crystal_hl += [np.mean(data_tmp['fin_crystal'] / abyss_count)]

    data_graph = pd.DataFrame(data={'abyss_count': range(1, max(data['abyss_count'])+1), 'crystal_kt': crystal_kt,
                                    'crystal_kt2hl': crystal_kt2hl, 'crystal_hl': crystal_hl})
    print(data_graph)
    data_graph = data_graph.set_index('abyss_count')
    data_graph.plot.line()
    plt.xticks(np.arange(0, max(data['abyss_count']) + 1, 4), np.arange(0, max(data['abyss_count']) + 1, 4))
    plt.savefig('../Data/graph/m2/原深渊等级人员水晶收益.jpg')
    # plt.show()

    # 原 苦痛/红莲升降/红莲保级 人员 随深渊次数的 深渊等级变化
    abyss_level_kt = []
    abyss_level_kt2hl = []
    abyss_level_hl = []
    for abyss_count in range(1, max(data['abyss_count'])+1):
        data_i = data[data['abyss_count']==abyss_count]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 7)]
        abyss_level_kt += [np.mean(data_tmp['abyss_level'])]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 8)]
        abyss_level_kt2hl += [np.mean(data_tmp['abyss_level'])]

        data_tmp = data_i[(data_i['ori_abyss_level'] == 9)]
        abyss_level_hl += [np.mean(data_tmp['abyss_level'])]

    data_graph = pd.DataFrame(data={'abyss_count': range(1, max(data['abyss_count'])+1), 'abyss_level_kt': abyss_level_kt,
                                    'abyss_level_kt2hl': abyss_level_kt2hl, 'abyss_level_hl': abyss_level_hl})
    print(data_graph)
    data_graph = data_graph.set_index('abyss_count')
    data_graph.plot.line()
    plt.savefig('../Data/graph/m2/原深渊等级人员在新深渊等级变化.jpg')
    # plt.show()

    # 新 原罪/苦痛/红莲 人数 随深渊次数的变化
    hum_count_yz = []
    hum_count_kt = []
    hum_count_hl = []
    for abyss_count in range(1, max(data['abyss_count'])+1):
        data_i = data[data['abyss_count']==abyss_count]

        data_tmp = data_i[(data_i['abyss_level'] == 4) | (data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6)]
        hum_count_yz += [len(data_tmp)]

        data_tmp = data_i[(data_i['abyss_level'] == 7) | (data_i['abyss_level'] == 8) | (data_i['abyss_level'] == 9)]
        hum_count_kt += [len(data_tmp)]

        data_tmp = data_i[(data_i['abyss_level'] == 10) | (data_i['abyss_level'] == 11) | (data_i['abyss_level'] == 12)]
        hum_count_hl += [len(data_tmp)]

    data_graph = pd.DataFrame(data={'abyss_count': range(1, max(data['abyss_count'])+1), 'hum_count_yz': hum_count_yz,
                                    'hum_count_kt': hum_count_kt, 'hum_count_hl': hum_count_hl})
    print(data_graph)
    data_graph = data_graph.set_index('abyss_count')
    data_graph.plot.line()
    plt.xticks(np.arange(0, max(data['abyss_count'])+1, 4), np.arange(0, max(data['abyss_count'])+1, 4))
    plt.savefig('../Data/graph/m2/新深渊各等级人员数量变化.jpg')
    # plt.show()

    return


def get_file_list(file_path=''):
    file_list = os.listdir(file_path)
    return file_list


if __name__ == '__main__':
    run()


"""  Player核心机制源代码  """
'''
    # 计算每次的凹分水平；凹分水平=0.4至1.6内十分位随机数，5%概率为0；最小为0，最大为2; 低于0.1视为不打
    # 引入败者越咸机制，凹分水平=凹分水平-上次凹分水*abs(氪金水平-14.5)*0.035，概率为(扣杯场次/12)；扣杯场次一个版本12轮深渊清零一次
    # 引入胜者越肝机制，凹分水平=凹分水平+上次凹分水平*氪金水平*0.035，概率为(加杯场次/12)；加杯场次一个版本12轮深渊清零一次
    # 引入越底层越容易不打机制，(0~氪金水平)随机数 小于 (0~3)随机数 时，effort_level直接为0
    def update_effort_level(self):
        # 越底层越不打机制
        if random.uniform(0, 3)>random.uniform(0, self.fund_level):
            self.effort_level = 0
            return

        # 胜者越肝机制/败者越咸机制, 再引入(0.8~1.2)的随机波动
        add_effort_num = self.effort_level * random.uniform(0.8, 1.2) * self.fund_level * 0.035
        red_effort_num = self.effort_level * random.uniform(0.8, 1.2) * abs(self.fund_level-14.5) * 0.035

        self.effort_level = random.randint(4, 16)/10.
        if random.uniform(0, 1)<=(self.fail_count_in_version/12.):
            self.effort_level -= red_effort_num
        if random.uniform(0, 1)<=(self.win_count_in_version/12.):
            self.effort_level += add_effort_num

        if self.effort_level<0.1:
            self.effort_level = 0
        if self.effort_level > 2:
            self.effort_level = 2

    # 每4轮深渊结束(一次池子的时间)，都有(6.5*氪金水平+12)的概率，氪金提升自己的氪金水平1级，最高[13.5]
    def add_fund_level(self):
        if random.uniform(0, 100) < (self.fund_level*6.5+6):
            self.fund_level += 0.5
        if self.fund_level > 13.5:
            self.fund_level = 13.5

    # 每一个版本结束(6周，12轮深渊，1个版本)，装备会被淘汰，全体氪金水平下降0.5级，最低为0；计数由外部判断
    def red_fund_level(self):
        self.fund_level -= 0.5
        if self.fund_level < 0:
            self.fund_level = 0
'''

"""  采用了第一赛季前5期新奖杯的机制  """
'''
    # 苦痛深渊
    elif abyss_index <= 9:
        # 第1期
        if abyss_count <= 1: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3_1[str(rank)]))
        # 第2-5期
        elif abyss_count <= 5: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3_25[str(rank)]))
        # 正常情况
        else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3[str(rank)]))
    # 红莲深渊
    elif abyss_index <= 12:
        # 第1期
        if abyss_count <= 1: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4_1[str(rank)]))
        # 第2-5期
        elif abyss_count <= 5: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4_25[str(rank)]))
        # 正常情况
        else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4[str(rank)]))
    # 寂灭
    else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_5[str(rank)]))
'''