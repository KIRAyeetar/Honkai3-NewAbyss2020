from Plan_B.Main import player as ply
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
        self.cup_map_1 = {'1': +100, '2': +100, '3': +100, '4': +100, '5': +100, '6': +100, '7': +100, '8': +50, '9': +50,
                          '10': +50, '11': +47, '12': +50, '13': +0, '14': +0, '15': +0, '16': +0, '17': +0,
                          '18': +0, '19': +0, '20': 0}
        self.cup_map_2 = {'1': +150, '2': +150, '3': +150, '4': +150, '5': +150, '6': +100, '7': +100, '8': +100, '9': +0,
                          '10': +0, '11': +0, '12': +0, '13': -75, '14': -75, '15': -75, '16': -100, '17': -100,
                          '18': -100, '19': -100, '20': -100}
        self.cup_map_3 = {'1': +200, '2': +200, '3': +200, '4': +100, '5': +100, '6': +100, '7': +0, '8': +0, '9': +0,
                          '10': +0, '11': +0, '12': +0, '13': -75, '14': -75, '15': -75, '16': -150, '17': -150,
                          '18': -150, '19': -150, '20': -150}
        self.cup_map_4 = {'1': +100, '2': +100, '3': +100, '4': +0, '5': +0, '6': +0, '7': +0, '8': +0, '9': +0,
                          '10': +0, '11': -100, '12': -100, '13': -100, '14': -100, '15': -100, '16': -100, '17': -100,
                          '18': -100, '19': -100, '20': -100}
        self.cup_map_5 = {'1': +100, '2': +100, '3': +100, '4': +100, '5': +100, '6': -200, '7': -200, '8': -200, '9': -200,
                          '10': -200, '11': -200, '12': -200, '13': -200, '14': -200, '15': -200, '16': -200, '17': -200,
                          '18': -200, '19': -200, '20': -200}


        self.promote_info = [0, 100, 300, 500, 700, 900, 1200, 1500, 2000, float('inf')]
        self.crystal_info = [180, 190, 200, 220, 280, 340, 420, 500, 520]

    # 初始化深渊
    def init_abyss(self):
        # 原罪 1 am2
        abyss_member_2 = [ply.Player(2, cup=200, cup_virtual=180, player_id='2-' + str(i)) for i in
                          range(round(self.member_count / 415 * 65))]
        # 原罪 2 am3
        abyss_member_3 = [ply.Player(3, cup=300, cup_virtual=180, player_id='3-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        # 原罪 3 am4
        abyss_member_4 = [ply.Player(4, cup=500, cup_virtual=180, player_id='4-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        # 苦痛 1 am5
        abyss_member_5 = [ply.Player(5, cup=700, cup_virtual=180, player_id='5-' + str(i)) for i in
                          range(round(self.member_count / 415 * 70))]
        # 苦痛 2 am6
        abyss_member_6 = [ply.Player(6, cup=900, cup_virtual=180, player_id='6-' + str(i)) for i in
                          range(round(self.member_count / 415 * 84))]
        # 苦痛 3 am7
        abyss_member_7 = [ply.Player(7, cup=1200, cup_virtual=180, player_id='7-' + str(i)) for i in
                          range(round(self.member_count / 415 * 42))]
        # 红莲 am8
        abyss_member_8 = [ply.Player(8, cup=1500, cup_virtual=280, player_id='8-' + str(i)) for i in
                          range(round(self.member_count / 415 * 19))]
        # 寂灭 am9
        abyss_member_9 = [ply.Player(9, cup=2000, cup_virtual=280, player_id='9-' + str(i), flag_abyss_8=1) for i in
                          range(90)]
        self.all_abyss = [[], abyss_member_2, abyss_member_3, abyss_member_4, abyss_member_5, abyss_member_6, abyss_member_7,
                          abyss_member_8, abyss_member_9]

    # reset_abyss_helper()
    def reset_abyss_helper(self, level):
        tmp = pd.Series(self.all_abyss[level])
        tmp.apply(lambda a: a.reset())
        return list(tmp)

    # 赛季重置深渊，寂灭大于3000奖杯的，重置为3000
    def reset_abyss(self):
        self.all_abyss[8] = self.reset_abyss_helper(8)

    # 一轮深渊
    def fight(self, abyss_count, if_save_csv=0, save_path='../Data/csv/', save_name_sp=''):
        all_data = pd.DataFrame(columns=['id', 'score', 'fund_level', 'effort_level', 'abyss_count', 'abyss_level',
                                         'group', 'rank', 'ori_cup', 'fin_cup', 'info'])

        for abyss_index in range(len(self.all_abyss)):
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
            abyss_data['abyss_level'] = abyss_index+1

            # 先全部随机分20人为一组
            abyss_data = abyss_data.sample(frac=1)
            abyss_data = abyss_data.reset_index()
            abyss_data['group'] = abyss_data['index']//20

            # 根据分数，在group内部排序
            abyss_data['rank'] = abyss_data.groupby('group')['score'].rank(ascending=False, method='first').apply(lambda a: int(a))
            # score=0的直接排20
            tmp = abyss_data['id'].isin(abyss_data[abyss_data['score']==0]['id'])
            abyss_data['rank'] = (-tmp*abyss_data['rank']).replace(0, 20)

            # 根据排名更新奖杯;可以把奖杯更新信息的几个字典集合成一个大表更方便
            for rank in range(1, 21):
                # 禁忌深渊
                if abyss_index < 1: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_1[str(rank)]))
                # 原罪深渊
                elif abyss_index < 4: abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_2[str(rank)]))
                # 苦痛深渊
                elif abyss_index < 7:
                    abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_3[str(rank)]))
                # 红莲深渊
                elif abyss_index == 7:
                    abyss_data[abyss_data['rank'] == rank]['info'].apply(lambda a: a.cup_change(self.cup_map_4[str(rank)]))
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
            tmp.apply(lambda a: a.add_crystal(self.crystal_info[abyss_index]))
            # 第一次进红莲的判断
            if abyss_index == 7:
                tmp.apply(lambda a: a.is_first_abyss_8())
            self.all_abyss[abyss_index] = list(tmp)

        # 每24轮深渊赛季结算
        if abyss_count % 24 == 0:
            self.reset_abyss()

        # 选择是否保存此轮深渊的CSV
        # 重新做一次大表
        if if_save_csv == 1:
            all_data = pd.DataFrame(columns=['id', 'fund_level', 'effort_level', 'abyss_count', 'abyss_level', 'cup', 'crystal'])
            abyss_level = 0
            for abyss_index in range(len(self.all_abyss)):
                abyss_level += 1
                if len(self.all_abyss[abyss_index]) == 0:
                    continue
                abyss_data = pd.DataFrame(columns=['id', 'fund_level', 'effort_level', 'abyss_count', 'abyss_level', 'cup', 'crystal', 'info'])
                abyss_data['info'] = self.all_abyss[abyss_index]
                abyss_data['id'] = abyss_data['info'].apply(lambda a: a.id)
                abyss_data['fund_level'] = abyss_data['info'].apply(lambda a: a.fund_level)
                abyss_data['effort_level'] = abyss_data['info'].apply(lambda a: a.effort_level)
                abyss_data['abyss_count'] = abyss_count
                abyss_data['abyss_level'] = abyss_index + 1
                abyss_data['cup'] = abyss_data['info'].apply(lambda a: a.cup)
                abyss_data['crystal'] = abyss_data['info'].apply(lambda a: a.crystal)
                del abyss_data['info']
                all_data = all_data.append(abyss_data)

            all_data.to_csv(save_path+save_name_sp+str(abyss_count)+'.csv', index=None)

        return all_data




