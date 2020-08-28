import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    data = pd.read_csv('../Data/csv/m1/data_all.csv')
    data_1 = data[data['abyss_count']==1]
    data_24 = data[data['abyss_count']==24]
    data_48 = data[data['abyss_count']==48]
    data_72 = data[data['abyss_count']==72]
    data_96 = data[data['abyss_count']==96]
    data_list = [data_1, data_24, data_48, data_72, data_96]


    # 文字分析
    '''
                                            老   新24期  新48期  新72期  新96期
    原 苦痛保级人员占比20%, 平均每期水晶收益   260    353    354     353    352
    原 红莲升降人员占比10%, 平均每期水晶收益   340    438    436     433    430
    原 红莲保级人员占比4.5%, 平均每期水晶收益  420    492    488     485    483
    原 无限相关人员总共90人, 平均每期水晶收益   540    509    507     506    505
    '''
    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 6]
        print(np.mean(data_tmp['crystal']/max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 7]
        print(np.mean(data_tmp['crystal'] / max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 8]
        print(np.mean(data_tmp['crystal'] / max(data_tmp['abyss_count'])))

    for data_i in data_list:
        data_tmp = data_i[data_i['ori_abyss_level'] == 9]
        print(np.mean(data_tmp['crystal'] / max(data_tmp['abyss_count'])))

    '''
             新1期      新24期    新48期   新72期    新96期
    原罪人数  98795     76097     70490    64801    59479
    苦痛人数  94458     81633     78638    76007    73442
    红莲人数  9157      17169     16480    16081    16276
    寂灭人数  90         634       678      759      633
    '''
    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 2) | (data_i['abyss_level'] == 3) | (data_i['abyss_level'] == 4)]
        print(len(data_tmp))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6) | (data_i['abyss_level'] == 7)]
        print(len(data_tmp))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==8]
        print(len(data_tmp))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==9]
        print(len(data_tmp))


    '''
                老    新1期   新24期  新48期  新72期  新96期
    原罪人数占比 33%    48%     37%     34%    32%    29%
    苦痛人数占比 33%    46%     40%     38%    37%    36%
    红莲人数占比 10%    4 %     8 %     8 %    8 %    8 %
    寂灭人数占比 ~~~    0.3%    0.3%    0.3%   0.3%   0.3%
    '''
    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 2) | (data_i['abyss_level'] == 3) | (data_i['abyss_level'] == 4)]
        print(len(data_tmp)*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6) | (data_i['abyss_level'] == 7)]
        print(len(data_tmp)*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==8]
        print(len(data_tmp)*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==9]
        print(len(data_tmp)*1./len(data_i))

    '''
                   新1期     新24期      新48期      新72期     新96期
       奖杯总数  140757750  145776309  140281050  135724439   131753790
    原罪奖杯总数  38113750  30925775    28613613   26670718   24827157
    苦痛奖杯总数  88588600  84798797   82189675    79689972    77075675
    红莲奖杯总数   13872900  27921375  26887375    26292125    26742775
    寂灭奖杯总数   182500    1300550    1396125    1559225     1301125
    '''
    print(sum(data_1['cup']), sum(data_24['cup']), sum(data_48['cup']), sum(data_72['cup']), sum(data_96['cup']))


    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 2) | (data_i['abyss_level'] == 3) | (data_i['abyss_level'] == 4)]
        print(sum(data_tmp['cup']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6) | (data_i['abyss_level'] == 7)]
        print(sum(data_tmp['cup']))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==8]
        print(sum(data_tmp['cup']))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==9]
        print(sum(data_tmp['cup']))

    '''
                 新1期   新24期   新48期   新72期    新96期
       平均凹度  0.620    0.611   0.603    0.597    0.597
    禁忌平均凹度  0       0.006   0.0016   0.0009   0.0005   
    原罪平均凹度  0.487   0.489   0.510    0.522    0.541
    苦痛平均凹度  0.740   0.822   0.849    0.884    0.925
    红莲平均凹度  0.811   1.064   1.115    1.166    1.206
    '''
    print(np.mean(data_1['effort_level']), np.mean(data_24['effort_level']), np.mean(data_48['effort_level']),
          np.mean(data_72['effort_level']), np.mean(data_96['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level'] == 1]
        print(np.mean(data_tmp['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 2) | (data_i['abyss_level'] == 3) | (data_i['abyss_level'] == 4)]
        print(np.mean(data_tmp['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6) | (data_i['abyss_level'] == 7)]
        print(np.mean(data_tmp['effort_level']))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level'] == 8]
        print(np.mean(data_tmp['effort_level']))


    '''
                     新1期   新24期   新48期   新72期   新96期
      总不打人数占比   38%     39%      41%     42%      44%
    原罪不打人数占比   24%     18%      16%     14%      12%
    苦痛不打人数占比   12%     7 %      6 %     5 %      5 %
    红莲不打人数占比   ~~~     0.9%     0.7%    0.6%     0.6%
    '''
    for data_i in data_list:
        data_tmp = data_i
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 2) | (data_i['abyss_level'] == 3) | (data_i['abyss_level'] == 4)]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[(data_i['abyss_level'] == 5) | (data_i['abyss_level'] == 6) | (data_i['abyss_level'] == 7)]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    for data_i in data_list:
        data_tmp = data_i[data_i['abyss_level']==8]
        print(len(data_tmp[data_tmp['effort_level']==0])*1./len(data_i))

    return


def get_file_list(file_path=''):
    file_list = os.listdir(file_path)
    return file_list


if __name__ == '__main__':
    run()


"""  Player核心修改机制源代码  """
'''
    # 计算每次的凹分水平；凹分水平=0.4至1.6内十分位随机数，5%概率为0；最小为0，最大为2; 低于0.1视为不打
    # 引入败者越咸机制，凹分水平=凹分水平-上次凹分水*abs(氪金水平-9.5)*0.035，概率为(扣杯场次/12)；扣杯场次一个版本12轮深渊清零一次
    # 引入胜者越肝机制，凹分水平=凹分水平+上次凹分水平*氪金水平*0.035，概率为(加杯场次/12)；加杯场次一个版本12轮深渊清零一次
    # 引入越底层越容易不打机制，(0~氪金水平)随机数 小于 (0~n)随机数 时，effort_level直接为0；n默认为3,约40%的人不打; 范围[0, 9.5]
    def update_effort_level(self, give_up_level=3):
        # 越底层越不打机制, (0~n)是不打的等级，默认为3
        n = give_up_level
        if random.uniform(0, n)>random.uniform(0, self.fund_level):
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
'''
