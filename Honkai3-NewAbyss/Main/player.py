import random

class Player(object):
    # fund_level:氪金水平，0-13个等级按第一次分配的深渊对应，按后续规则有变化
    # effort_level:凹分水平，每次深渊随机在0-2之间波动，0表示放弃不打
    # fail_count_in_version:每个版本的掉杯次数
    # fail_count_in_version:每个版本的加杯次数
    # cup:奖杯数
    # cup_virtual:虚拟奖杯数
    def __init__(self, fund_level, cup=0, cup_virtual=0, player_id='None', flag_abyss_10=0):
        self.fund_level = fund_level
        self.cup = cup
        self.cup_virtual = cup_virtual
        self.id = player_id
        self.effort_level = 1
        self.fail_count_in_version = 0
        self.win_count_in_version = 0
        self.crystal = 0
        # 是否进过红莲
        self.flag_abyss_10 = 0


    # 计算每次的凹分水平；凹分水平=0.4至1.6内十分位随机数，5%概率为0；最小为0，最大为2; 低于0.1视为不打
    # 引入败者越咸机制，凹分水平=凹分水平-上次凹分水*abs(氪金水平-14.5)*0.035，概率为(扣杯场次/12)；扣杯场次一个版本12轮深渊清零一次
    # 引入胜者越肝机制，凹分水平=凹分水平+上次凹分水平*氪金水平*0.035，概率为(加杯场次/12)；加杯场次一个版本12轮深渊清零一次
    # 引入越底层越容易不打机制，(0~氪金水平)随机数 小于 (0~n)随机数 时，effort_level直接为0；n默认为3,约30%的人不打; 范围[0, 13.5]
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

    # 分数=氪金水平+凹分水平，越高排名越前;凹分水平为0时表示不打
    def get_score_once(self):
        self.update_effort_level()
        if self.effort_level == 0:
            return 0
        else:
            return self.fund_level + self.effort_level

    # 奖杯变化; 记录失败
    def cup_change(self, num):
        # 如果是扣奖杯
        if num<0:
            self.fail_count_in_version += 1
            # 如果虚拟奖杯不够用
            if num+self.cup_virtual<0:
                self.cup_virtual = 0
                self.cup += self.cup_virtual+num
                if self.cup<0:
                    self.cup = 0
            # 如果够用
            else:
                self.cup_virtual += num
        else:
            self.win_count_in_version += 1
            self.cup += num

    # 水晶收益增加;
    def update_crystal(self, num):
        self.crystal += num

    # 第一次进入红莲的虚拟奖杯判断
    def is_first_abyss_10(self):
        if self.flag_abyss_10 == 0:
            self.cup_virtual += 100
            self.flag_abyss_10 =1

    # 一版本内的加扣杯场次清零
    def zero_fail(self):
        self.fail_count_in_version = 0
        self.win_count_in_version = 0

    # 赛季重置
    def reset(self, cup, cup_virtual, add_crystal, flag_abyss_10):
        self.cup = cup
        self.cup_virtual = cup_virtual
        self.update_crystal(add_crystal)
        self.flag_abyss_10 = flag_abyss_10




