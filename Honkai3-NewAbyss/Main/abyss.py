from Main import player as ply
import pandas as pd

class Abyss(object):
    # round_count:深渊次数计数
    # member_count:总人数计数
    # abyss_member_N:第N层深渊的所有玩家对象
    def __init__(self, member_count=1000):
        self.round_count = 0
        self.member_count = member_count
        self.all_abyss = []
        # 正常奖杯变化表
        self.cup_map_1 = {'1': +100, '2': +95, '3': +89, '4': +84, '5': +79, '6': +74, '7': +68, '8': +63, '9': +58,
                          '10': +53, '11': +47, '12': +42, '13': +37, '14': +32, '15': +26, '16': +21, '17': +16,
                          '18': +11, '19': +5, '20': 0}
        self.cup_map_2 = {'1': +120, '2': +110, '3': +100, '4': +90, '5': +80, '6': +70, '7': +60, '8': +50, '9': +40,
                          '10': +30, '11': +20, '12': +10, '13': 0, '14': -10, '15': -20, '16': -30, '17': -40,
                          '18': -50, '19': -60, '20': -70}
        self.cup_map_3 = {'1': +160, '2': +143, '3': +126, '4': +109, '5': +93, '6': +76, '7': +59, '8': +42, '9': +25,
                          '10': +8, '11': -8, '12': -25, '13': -42, '14': -59, '15': -76, '16': -93, '17': -109,
                          '18': -126, '19': -143, '20': -160}
        self.cup_map_4 = {'1': +200, '2': +179, '3': +158, '4': +137, '5': +116, '6': +95, '7': +74, '8': +53, '9': +32,
                          '10': +11, '11': -11, '12': -32, '13': -53, '14': -74, '15': -95, '16': -116, '17': -137,
                          '18': -158, '19': -179, '20': -200}
        self.cup_map_5 = {'1': +200, '2': +179, '3': +158, '4': +137, '5': +116, '6': +95, '7': +74, '8': +53, '9': +32,
                          '10': +11, '11': -11, '12': -32, '13': -53, '14': -74, '15': -95, '16': -116, '17': -137,
                          '18': -158, '19': -179, '20': -200}
        # 1期奖杯变化表
        self.cup_map_3_1 = {'1': +160, '2': +160, '3': +160, '4': +160, '5': +160, '6': +160, '7': +160, '8': +160, '9': +145,
                            '10': +128, '11': +112, '12': +95, '13': +78, '14': +61, '15': +44, '16': +27, '17': +11,
                            '18': -6, '19': -23, '20': -40}
        self.cup_map_4_1 = {'1': +200, '2': +200, '3': +200, '4': +200, '5': +200, '6': +200, '7': +194, '8': +173, '9': +152,
                            '10': +131, '11': +109, '12': +88, '13': +67, '14': +46, '15': +25, '16': +4, '17': -17,
                            '18': -38, '19': -59, '20': -80}
        # 2-5期奖杯变化表
        self.cup_map_3_25 = {'1': +160, '2': +160, '3': +160, '4': +160, '5': +153, '6': +136, '7': +119, '8': +102, '9': +85,
                             '10': +68, '11': +52, '12': +35, '13': +18, '14': +1, '15': -16, '16': -33, '17': -49,
                             '18': -66, '19': -83, '20': -100}
        self.cup_map_4_25 = {'1': +200, '2': +200, '3': +200, '4': +197, '5': +176, '6': +155, '7': +134, '8': +113, '9': +92,
                             '10': +71, '11': +49, '12': +28, '13': +7, '14': -14, '15': -35, '16': -56, '17': -77,
                             '18': -98, '19': -119, '20': -140}

        self.promote_info = [0, 100, 200, 300, 500, 700, 900, 1200, 1500, 1800, 2200, 2600, 3200, float('inf')]
        self.crystal_info = [160, 170, 180, 190, 200, 220, 280, 340, 420, 460, 470, 480, 620]

    # 初始化深渊
    def init_abyss(self):
        # 禁忌 3
        abyss_member_3 = [ply.Player(3, cup=200, cup_virtual=180, player_id='3-' + str(i)) for i in
                          range(round(self.member_count / 415 * 65))]
        # 原罪 1 2 3
        abyss_member_4 = [ply.Player(4, cup=300, cup_virtual=180, player_id='4-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        abyss_member_5 = [ply.Player(5, cup=500, cup_virtual=180, player_id='5-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        abyss_member_6 = [ply.Player(6, cup=700, cup_virtual=180, player_id='6-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        # 苦痛 1 2 3
        abyss_member_7 = [ply.Player(7, cup=900, cup_virtual=180, player_id='7-' + str(i)) for i in
                          range(round(self.member_count / 415 * 84))]
        abyss_member_8 = [ply.Player(8, cup=1200, cup_virtual=180, player_id='8-' + str(i)) for i in
                          range(round(self.member_count / 415 * 42))]
        abyss_member_9 = [ply.Player(9, cup=1500, cup_virtual=180, player_id='9-' + str(i)) for i in
                          range(round(self.member_count / 415 * 19))]
        # 红莲1 2
        abyss_member_10 = [ply.Player(10, cup=1800, cup_virtual=280, player_id='10-' + str(i), flag_abyss_10=1) for i in range(80)]
        abyss_member_11 = [ply.Player(11, cup=2200, cup_virtual=280, player_id='11-' + str(i), flag_abyss_10=1) for i in range(10)]
        self.all_abyss = [[], [], abyss_member_3, abyss_member_4, abyss_member_5, abyss_member_6, abyss_member_7,
                          abyss_member_8, abyss_member_9, abyss_member_10, abyss_member_11, [], []]

    # reset_abyss_helper()
    def reset_abyss_helper(self, level, cup, cup_virtual, add_crystal, flag_abyss_10):
        tmp = pd.Series(self.all_abyss[level])
        tmp.apply(lambda a: a.reset(cup, cup_virtual, add_crystal, flag_abyss_10))
        return list(tmp)

    # 赛季重置深渊，集体掉级，重置奖杯，发水晶
    def reset_abyss(self):
        # 禁忌1 2 3
        abyss_member_1 = self.reset_abyss_helper(0, 0, 180, 300, 1)+self.reset_abyss_helper(1, 0, 180, 300, 1)+self.reset_abyss_helper(2, 0, 180, 300, 1)
        abyss_member_2 = self.reset_abyss_helper(3, 100, 180, 400, 1)
        abyss_member_3 = self.reset_abyss_helper(4, 200, 180, 400, 1)
        # 原罪 1 2 3
        abyss_member_4 = self.reset_abyss_helper(5, 300, 180, 400, 1)
        abyss_member_5 = self.reset_abyss_helper(6, 500, 180, 450, 1)
        abyss_member_6 = self.reset_abyss_helper(7, 700, 180, 450, 1)
        # 苦痛 1 2 3
        abyss_member_7 = self.reset_abyss_helper(8, 900, 180, 450, 1)
        abyss_member_8 = self.reset_abyss_helper(9, 1200, 180, 500, 1)
        abyss_member_9 = self.reset_abyss_helper(10, 1500, 180, 500, 1)
        # 红莲 1 2
        abyss_member_10 = self.reset_abyss_helper(11, 1800, 280, 500, 1)
        abyss_member_11 = self.reset_abyss_helper(12, 2200, 280, 500, 1)

        self.all_abyss = [abyss_member_1, abyss_member_2, abyss_member_3, abyss_member_4, abyss_member_5,
                          abyss_member_6, abyss_member_7, abyss_member_8, abyss_member_9, abyss_member_10,
                          abyss_member_11, [], []]

    # 一轮深渊
    def fight(self, abyss_count, if_save_csv=0, save_path='../Data/csv/', save_name_sp=''):
        all_data = pd.DataFrame(columns=['id', 'score', 'fund_level', 'effort_level', 'abyss_count', 'abyss_level',
                                         'group', 'rank', 'ori_cup', 'fin_cup', 'info'])
        abyss_level = 0
        for abyss_index in range(len(self.all_abyss)):
            abyss_level += 1
            # print('abyss_level: %d' % abyss_level)

            if len(self.all_abyss[abyss_index])== 0:
                continue
            abyss_data = pd.DataFrame(columns=['id', 'score', 'fund_level', 'effort_level', 'abyss_count', 'abyss_level',
                                               'group', 'rank', 'ori_cup', 'fin_cup', 'info'])
            abyss_data['info'] = self.all_abyss[abyss_index]

            # 基础信息迁移到一张大表
            abyss_data['id'] = abyss_data['info'].apply(lambda a: a.id)
            abyss_data['abyss_count'] = abyss_count
            abyss_data['score'] = abyss_data['info'].apply(lambda a: a.get_score_once())
            abyss_data['fund_level'] = abyss_data['info'].apply(lambda a: a.fund_level)
            abyss_data['effort_level'] = abyss_data['info'].apply(lambda a: a.effort_level)
            abyss_data['ori_cup'] = abyss_data['info'].apply(lambda a: a.cup)
            abyss_data['abyss_level'] = abyss_level

            # 先全部随机分20人为一组
            abyss_data = abyss_data.sample(frac=1)
            abyss_data = abyss_data.reset_index()
            abyss_data['group'] = abyss_data['index']//20

            # 根据分数，在group内部排序
            abyss_data['rank'] = abyss_data.groupby('group')['score'].rank(ascending=False, method='first').apply(lambda a: int(a))
            # score=0的直接排20
            tmp = abyss_data['id'].isin(abyss_data[abyss_data['score']==0]['id'])
            abyss_data['rank'] = (-tmp*abyss_data['rank']).replace(0, 20)
            # abyss_data['rank'] = [20 if list(abyss_data['score'])[i]==0 else list(abyss_data['rank'])[i] for i in range(len(abyss_data))]

            # 根据排名更新奖杯;可以把奖杯更新信息的几个字典集合成一个大表更方便
            for rank in range(1, 21):
                # 禁忌深渊
                if abyss_index <= 3: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_1[str(rank)]))
                # 原罪深渊
                elif abyss_index <= 6: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_2[str(rank)]))

                # # 改版前苦痛深渊
                # elif abyss_index <= 9:
                #     abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3[str(rank)]))
                # # 改版前红莲深渊
                # elif abyss_index <= 12:
                #     abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4[str(rank)]))

                # 苦痛深渊
                elif abyss_index <= 9:
                    # 第1期
                    if abyss_count % 24 <= 1: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3_1[str(rank)]))
                    # 第2-5期
                    elif abyss_count % 24 <= 5: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3_25[str(rank)]))
                    # 正常情况
                    else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3[str(rank)]))
                # 红莲深渊
                elif abyss_index <= 12:
                    # 第1期
                    if abyss_count % 24 <= 1: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4_1[str(rank)]))
                    # 第2-5期
                    elif abyss_count % 24 <= 5: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4_25[str(rank)]))
                    # 正常情况
                    else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4[str(rank)]))
                # 寂灭
                else: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_5[str(rank)]))

            del abyss_data['index']
            all_data = all_data.append(abyss_data)

        #  每4轮开始前氪金等级有概率提升；每12轮开始前氪金等级集体贬值；每12轮结束时单人扣杯场次计数清零
        if (abyss_count+1) % 4 == 0:
            all_data['info'].apply(lambda a: a.add_fund_level())
        if (abyss_count+1) % 12 == 0:
            all_data['info'].apply(lambda a: a.red_fund_level())
        if abyss_count % 12 == 0:
            all_data['info'].apply(lambda a: a.zero_fail())

        # 战斗结束，根据奖杯发水晶，重新分配深渊;第一次进入红莲的虚拟奖杯+100
        all_data['fin_cup'] = all_data['info'].apply(lambda a: a.cup)
        for abyss_index in range(len(self.all_abyss)):
            tmp = all_data[(all_data['fin_cup']>=self.promote_info[abyss_index]) & (all_data['fin_cup']<self.promote_info[abyss_index+1])]['info']
            tmp.apply(lambda a: a.update_crystal(self.crystal_info[abyss_index]))
            # 第一次进红莲的判断
            if abyss_index == 10:
                tmp.apply(lambda a: a.is_first_abyss_10())
            self.all_abyss[abyss_index] = list(tmp)

        # 每24轮深渊赛季结算
        if abyss_count % 24 == 0:
            self.reset_abyss()

        # 选择是否保存此轮深渊的CSV
        if if_save_csv==1:
            all_data['fin_crystal'] = all_data['info'].apply(lambda a: a.crystal)
            del all_data['info']
            all_data.to_csv(save_path+save_name_sp+str(abyss_count)+'.csv', index=None)

        return all_data




