# coding=UTF-8（等号换为”:“也可以）
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
import sys

# 胜平负 让球  半全场 总进球 比分 这个顺序
listSer = ("3", "1", "0", "3", "1", "0",
           "3-3", "3-1", "3-0",
           "1-3", "1-1", "1-0",
           "0-3", "0-1", "0-0",
           "0", "1", "2", "3", "4", "5", "6", "7",
           "1:0", "2:0", "2:1", "3:0", "3:1",
           "3:2", "4:0", "4:1", "4:2", "5:0",
           "5:1", "5:2", "胜其它",
           "0:0", "1:1", "2:2", "3:3", "平其它",

           "0:1", "0:2", "1:2", "0:3", "1:3",
           "2:3", "0:4", "1:4", "2:4", "0:5",
           "1:5", "2:5", "负其它")

listText = ("主胜", "平", "客胜", "主胜", "平", "客胜",
            "胜胜", "胜平", "胜负",
            "平胜", "平平", "平负",
            "负胜", "负平", "负负",
            "0", "1", "2", "3", "4", "5", "6", "7+",
            "1:0", "2:0", "2:1", "3:0", "3:1",
            "3:2", "4:0", "4:1", "4:2", "5:0",
            "5:1", "5:2", "胜其它",
            "0:0", "1:1", "2:2", "3:3", "平其它",

            "0:1", "0:2", "1:2", "0:3", "1:3",
            "2:3", "0:4", "1:4", "2:4", "0:5",
            "1:5", "2:5", "负其它"
            )
listOdd = (
    "1.58",
    "3.50",
    "4.15",
    "2.78",
    "3.45",
    "1.97",
    "2.25",
    "17.00",
    "40.00",
    "3.80",
    "5.30",
    "10.00",
    "24.00",
    "17.00",
    "7.50",
    "10.00",
    "4.10",
    "3.25",
    "3.50",
    "5.50",
    "10.00",
    "17.00",
    "28.00",
    "6.00",
    "7.00",
    "6.50",
    "12.00",
    "12.50",
    "22.00",
    "25.00",
    "27.00",
    "50.00",
    "60.00",
    "70.00",
    "120.00",
    "50.00",
    "10.00",
    "6.50",
    "15.00",
    "70.00",
    "400.00",
    "10.00",
    "21.00",
    "11.50",
    "60.00",
    "40.00",
    "40.00",
    "200.00",
    "120.00",
    "150.00",
    "600.00",
    "400.00",
    "500.00",
    "150.00",
    "1.58",
    "1.97",
    "1.58",
    "3.50",
    "4.15"
)

SEL_zhusheng = 0
SEL_ping = 1
SEL_kesheng = 2
SEL_rangsheng = 3
SEL_rangping = 4
SEL_rangfu = 5
SEL_33 = 6
SEL_31 = 7
SEL_30 = 8
SEL_13 = 9
SEL_11 = 10
SEL_10 = 11
SEL_03 = 12
SEL_01 = 13
SEL_00 = 14
SEL_0 = 15
SEL_1 = 16
SEL_2 = 17
SEL_3 = 18
SEL_4 = 19
SEL_5 = 20
SEL_6 = 21
SEL_7 = 22
SEL_1_0 = 23
SEL_2_0 = 24
SEL_2_1 = 25
SEL_3_0 = 26
SEL_3_1 = 27
SEL_3_2 = 28
SEL_4_0 = 29
SEL_4_1 = 30
SEL_4_2 = 31
SEL_5_0 = 32
SEL_5_1 = 33
SEL_5_2 = 34
SEL_4_3 = 35
SEL_0_0 = 36
SEL_1_1 = 37
SEL_2_2 = 38
SEL_3_3 = 39
SEL_4_4 = 40
SEL_0_1 = 41
SEL_0_2 = 42
SEL_1_2 = 43
SEL_0_3 = 44
SEL_1_3 = 45
SEL_2_3 = 46
SEL_0_4 = 47
SEL_1_4 = 48
SEL_2_4 = 49
SEL_0_5 = 50
SEL_1_5 = 51
SEL_2_5 = 52
SEL_3_4 = 53

PLAYWAY_SPF = 0  # 胜平负
PLAYWAY_RQSPF = 1  # 让球胜平负
PLAYWAY_BIFEN = 2  # 比分
PLAYWAY_BANQUAN = 3  # 半全场
PLAYWAY_JINQIU = 4  # 总进球

VAR_50 = 1  # 可能
VAR_100 = 0  # 一定发生
VAR_0 = 2  # 不可能


class IPlayRelationship(object):
    def setRangQiu(self, ranqiu):
        self.ranqiu = ranqiu

    def getRelationship(self, firstIndex, secondIndex):
        return VAR_50

    def getRangqiu(self):
        return self.ranqiu;


# /***
#  * 进球索引转胜平负索引
#  * @param jinqiuIndex
#  * @return
#  */
def jinqiuIndex2SpfIndexs(jinqiuIndex):
    # //0球只有平
    if (jinqiuIndex == 0):
        return [1]
    # 偶数球，7+ 胜平负都有
    if (jinqiuIndex % 2 == 0 or jinqiuIndex == 7):
        return [0, 1, 2]
    # 奇数球 胜负
    return [0, 2]


# //胜平负进球
class SpfJinqiuRelationship(IPlayRelationship):
    def getRelationship(self, spfIndex, jqIndex):
        indexs = jinqiuIndex2SpfIndexs(jqIndex)
        if (isArrayContainValue(indexs, spfIndex)):
            return VAR_50
        return VAR_0


# /***
#     * 半全场的索引转成胜平负的索引
#     * @param banquanIndex
#     * @return 半场结果，全场结果
#     */
def banquanIndex2SpfIndex(banquanIndex):
    return [banquanIndex / 3, banquanIndex % 3]


class SpfBanquanRelationship(IPlayRelationship):
    def getRelationship(self, firstId, secondId):
        if banquanIndex2SpfIndex(secondId)[1] == firstId:
            return VAR_50
        return VAR_0


class SpfRqspfRelationship(IPlayRelationship):
    def getRelationship(self, firstId, secondId):
        indexs = rqspfIndex2SpfIndexs(secondId, self.getRangqiu())
        if (isArrayContainValue(indexs, firstId)):
            return VAR_50
        return VAR_0

    # /***
    #  * 让球胜平负玩法转成胜平负玩法索引
    #  * @param rqspfIndex 让球胜平负的索引
    #  * @param rangqiu 让球数
    #  * @return 胜平负玩法索引数据
    #  */


def rqspfIndex2SpfIndexs(rqspfIndex, rangqiu):
    if (rangqiu == 1):  # 主+1
        if (rqspfIndex == 0):
            return {0, 1}  # 让胜->胜平
        else:
            return {2}  # 让平/让负->负
    elif (rangqiu >= 2):  # {#主+2以上
        if (rqspfIndex == 0):
            return {0, 1, 2}  # 让胜->胜平负
        else:
            return {2}  # 让平/让负->负
    elif (rangqiu == -1):  # {主-1
        if (rqspfIndex == 0 or rqspfIndex == 1):
            return {0}  # 让胜/让平->胜
        else:
            return {0, 1}  # 让负->平负
    elif (rangqiu <= -2):  # {主-2以上
        if (rqspfIndex == 0 or rqspfIndex == 1):
            return {0}  # 让胜/让平->胜
        else:
            return {0, 1, 2}  # 让负->胜平负
    else:
        return {}


def isArrayContainValue(arr, value):
    for d in arr:
        if (d == value):
            return True
    return False


def plays2Key(key1, key2):
    return key1 * 10 + key2


class ScoreInfo(object):
    def __init__(self, home, away, isOther=False):
        self.home = home
        self.away = away
        self.isOther = isOther

    def getJinqiuCha(self):
        return self.home - self.away

    def getJinqiu(self):
        return self.home + self.away

    def getSpfIndex(self):
        cha = self.home - self.away
        if (cha > 0):
            return 0
        if (cha == 0):
            return 1
        return 2

    def getHome(self):
        return self.home

    def getAway(self):
        return self.away


listScores = (ScoreInfo(1, 0),
              ScoreInfo(2, 0),
              ScoreInfo(2, 1),
              ScoreInfo(3, 0),
              ScoreInfo(3, 1),
              ScoreInfo(3, 2),
              ScoreInfo(4, 0),
              ScoreInfo(4, 1),
              ScoreInfo(4, 2),
              ScoreInfo(5, 0),
              ScoreInfo(5, 1),
              ScoreInfo(5, 2),
              ScoreInfo(4, 3, True),
              ScoreInfo(0, 0),
              ScoreInfo(1, 1),
              ScoreInfo(2, 2),
              ScoreInfo(3, 3),
              ScoreInfo(4, 4, True),
              ScoreInfo(0, 1),
              ScoreInfo(0, 2),
              ScoreInfo(1, 2),
              ScoreInfo(0, 3),
              ScoreInfo(1, 3),
              ScoreInfo(2, 3),
              ScoreInfo(0, 4),
              ScoreInfo(1, 4),
              ScoreInfo(2, 4),
              ScoreInfo(0, 5),
              ScoreInfo(1, 5),
              ScoreInfo(2, 5),
              ScoreInfo(3, 4, True))


class SpfBifenRelationship(IPlayRelationship):
    def getRelationship(self, firstId, secondId):
        info = listScores[secondId]
        if (info.getSpfIndex() == firstId):
            return VAR_50
        return VAR_0


class RqspfBanquanRelationship(IPlayRelationship):
    def getRelationship(self, firstId, secondId):
        indexs = rqspfIndex2SpfIndexs(firstId, self.getRangqiu())
        spfIndex = banquanIndex2SpfIndex(secondId)
        if isArrayContainValue(indexs, spfIndex[1]):
            return VAR_50
        return VAR_0


class RqspfJinqiuRelationship(IPlayRelationship):
    def icontains(self, arrs, arrs2):
        for aa in arrs:
            for bb in arrs2:
                if (aa == bb):
                    return True

    def getRelationship(self, firstId, secondId):
        datas = rqspfIndex2SpfIndexs(firstId, self.getRangqiu())
        datas2 = jinqiuIndex2SpfIndexs(secondId)
        if (self.icontains(datas, datas2)):
            return VAR_50
        return VAR_0


class RqspfBifenRelationship(IPlayRelationship):
    def getRelationship(self, firstId, secondId):
        scoreInfo = listScores[secondId]
        value = scoreInfo.getJinqiuCha()
        # // 胜其它
        # 负其它(平其它, 同普通方式)
        if (scoreInfo.isOther and value != 0):
            if (value == 1):  # 胜其它  差值是 [1~+)
                if (firstId == 0):  # 胜其它选 让胜,是可能发生的
                    return VAR_50
                elif firstId == 1:  # 胜其它选让平
                    if (self.getRangqiu() <= -1):  # //[1+rangqiu,+无穷+rangqiu)  让球的值是-1到-无穷
                        return VAR_50
                    return VAR_0  # //让平不可能了
                elif firstId == 2:  # //胜其它选让负
                    if (self.getRangqiu() <= -2):
                        return VAR_50
                    return VAR_0  # // 让负不可能了
            elif value == -1:  # 差值是[-1,-无穷)
                if firstId == 0:
                    if (self.getRangqiu() >= 2):
                        return VAR_50
                    return VAR_0  # // 让胜不可能了
                elif firstId == 1:  # 负其它选让平
                    if (self.getRangqiu() >= 1):  # 大于等于1
                        return VAR_50
                    return VAR_0  # // 让平不可能了
                elif firstId == 2:  # 负其它选让负, 是可能发生的
                    return VAR_50
        mChaBall = value + self.getRangqiu()
        # // 让胜
        if (mChaBall > 0):
            if firstId == 0:
                return VAR_50
            return VAR_0  # 让球胜
        # // 让平
        if (mChaBall == 0):
            if firstId == 1:
                return VAR_50
            return VAR_0  # 让球平
            # // 让负
        if (mChaBall < 0):
            if firstId == 2:
                return VAR_50
            return VAR_0
        return VAR_0


class BanquanJinqiuRelationship(SpfJinqiuRelationship):
    def getRelationship(self, banquanIndex, jinqiuIndex):
        spfIndexs = banquanIndex2SpfIndex(banquanIndex)

        # 总进球为0时,只是能平平
        if jinqiuIndex == 0:
            if (spfIndexs[0] == 1 and spfIndexs[1] == 1):
                return VAR_50
            return VAR_0

        var = super(BanquanJinqiuRelationship, self).getRelationship(spfIndexs[1], jinqiuIndex)
        # 胜负，负胜，总进球大于等于3
        if abs(spfIndexs[0] - spfIndexs[1]) == 2 and var == VAR_50:
            if jinqiuIndex < 3:
                return VAR_0
        return var


class BanquanBifenRelationship(IPlayRelationship):
    def getRelationship(self, banquanIndex, scoreIndex):
        spfIndexs = banquanIndex2SpfIndex(banquanIndex)
        halfResult = spfIndexs[0]  # //0--胜 1--平 2--负
        endResult = spfIndexs[1]  # //0--胜 1--平 2--负
        info = listScores[scoreIndex]
        if (info.getSpfIndex() == endResult):
            if (endResult == 0):  # 胜   客队没有得分，与胜胜或平胜相容
                if (info.getAway() == 0 and (halfResult == 0 or halfResult == 1)):
                    return VAR_50
                if (info.getAway() != 0):
                    return VAR_50
            elif endResult == 1:  # 平
                # // 0:0只可能与  平平相容
                if (info.getHome() == 0 and halfResult == 1):
                    return VAR_50
                # // 非0:0和胜平 / 负平 / 平平相容
                if (info.getAway() != 0):
                    return VAR_50
            elif endResult == 2:  # 负
                # // 主队没有得分，与负负 / 平负相容
                if (info.getHome() == 0 and (halfResult == 1 or halfResult == 2)):
                    return VAR_50
                # // 主队得分, 与负负 / 平负 / 胜负相容
                if (info.getHome() != 0):
                    return VAR_50

        return VAR_0


class JinqiuBifenRelationship(IPlayRelationship):
    def getRelationship(self, ballIndex, bfIndex):
        info = listScores[bfIndex]
        allBall = info.getJinqiu()
        # //0球和0-0的比分
        if (ballIndex == 0 and allBall == 0):
            return VAR_100
        # 其它比分总进球为7
        if (info.isOther):
            if ballIndex == 7:
                return VAR_50
            return VAR_0
        if (ballIndex == allBall):
            return VAR_50
        return VAR_0


# 胜平负 让球  半全场 总进球 比分 这个顺序
hashMap = {plays2Key(PLAYWAY_SPF, PLAYWAY_RQSPF): SpfRqspfRelationship(),
           plays2Key(PLAYWAY_SPF, PLAYWAY_BANQUAN): SpfBanquanRelationship(),
           plays2Key(PLAYWAY_SPF, PLAYWAY_JINQIU): SpfJinqiuRelationship(),
           plays2Key(PLAYWAY_SPF, PLAYWAY_BIFEN): SpfBifenRelationship(),
           plays2Key(PLAYWAY_RQSPF, PLAYWAY_BANQUAN): RqspfBanquanRelationship(),
           plays2Key(PLAYWAY_RQSPF, PLAYWAY_JINQIU): RqspfJinqiuRelationship(),
           plays2Key(PLAYWAY_RQSPF, PLAYWAY_BIFEN): RqspfBifenRelationship(),
           plays2Key(PLAYWAY_BANQUAN, PLAYWAY_JINQIU): BanquanJinqiuRelationship(),
           plays2Key(PLAYWAY_BIFEN, PLAYWAY_BANQUAN): BanquanBifenRelationship(),
           plays2Key(PLAYWAY_BIFEN, PLAYWAY_JINQIU): JinqiuBifenRelationship()
           }


def index2PlayId(index):
    if index <= 2:
        return PLAYWAY_SPF
    if index <= 5:
        return PLAYWAY_RQSPF
    if index <= 14:
        return PLAYWAY_BANQUAN
    if index <= 22:
        return PLAYWAY_JINQIU
    if index <= 53:
        return PLAYWAY_BIFEN

    # /***
    #  * 获取玩法的数组索引,这里的索引与选择对话框是一一对应的
    #  * @param playWay
    #  * @return
    #  */


def getPlayRangeIndex(playWay):
    dict = {
        PLAYWAY_SPF: [0, 2],  # 胜平负 0-2
        PLAYWAY_RQSPF: [3, 5],  # 让球胜平负3-5
        PLAYWAY_BANQUAN: [6, 14],  # 半全场 6-14
        PLAYWAY_JINQIU: [15, 22],  # 总进球15-22
        PLAYWAY_BIFEN: [23, 53]  # 比分23-53
    }
    return dict[playWay]


def playWay2Text(playWay):
    dict = {
        PLAYWAY_SPF: "胜平负",  # 胜平负 0-2
        PLAYWAY_RQSPF: "让球胜平负",  # 让球胜平负3-5
        PLAYWAY_BANQUAN: "半全场",  # 半全场 6-14
        PLAYWAY_JINQIU: "总进球",  # 总进球15-22
        PLAYWAY_BIFEN: "比分"  # 比分23-53
    }
    return dict[playWay]


def playIndex2PlayText(playIndex):
    playWay = index2PlayId(playIndex)
    return playWay2Text(playWay)


def var2Text(var):
    # if VAR_0==var:
    #     return "不可能发生的----"
    # if VAR_50==var:
    #     return "有可能发生的"
    # if VAR_100==var:
    #     return "%100 一定发生的"
    # return "NONE "
    dict = {
        VAR_50: "* 有可能发生",
        VAR_100: "一定发生",
        VAR_0: "不可能发生"
    }
    return dict[var]


# 玩法转换成文字
def playIndex2Text(playIndex):
    return '%s(%s)' % (playIndex2PlayText(playIndex), listText[playIndex])


def getRelationship(playIndex1, playIndex2, rangqiu):
    playWay1 = index2PlayId(playIndex1)
    playWay2 = index2PlayId(playIndex2)
    # // 玩法相同
    if (playWay1 == playWay2):
        # print "玩法相同", var2Text(VAR_0)
        # print "-----------"
        return VAR_0
    print "比较玩法", playIndex2Text(playIndex1), playIndex2Text(playIndex2), "让球数", rangqiu
    # // 得到玩法的第一个索引
    playIndex1 = playIndex1 - getPlayRangeIndex(playWay1)[0]
    playIndex2 = playIndex2 - getPlayRangeIndex(playWay2)[0]
    key = plays2Key(min(playWay1, playWay2), max(playWay1, playWay2))
    relationship = hashMap[key]
    relationship.setRangQiu(rangqiu)

    print"策略类", relationship.__class__
    print "玩法", playWay1, playWay2, "索引", playIndex1, playIndex2

    result = relationship.getRelationship(playIndex1, playIndex2)
    print var2Text(result)
    print "--------------------------------------------"
    return result


class FBallItem(object):
    def __init__(self, selArray, rangqiu, oddArray=listOdd):
        # 排序
        selArray.sort()
        self.selArray = selArray
        self.rangqiu = rangqiu
        self.oddArray = oddArray
        pass


class Pair:
    def __init__(self, a, b, value=VAR_0):
        minVar = min(a, b)
        maxVar = max(a, b)
        # //排序由小到大
        self.a = minVar
        self.b = maxVar
        self.value = value

    def __str__(self):
        return "%d,%d" % (self.a, self.b);

    def isMaxRate(self):
        return self.value == VAR_50 or self.value == VAR_100

    def isMinRate(self):
        return self.value == VAR_100

    def equals(self, obj):
        return self.a == obj.a and self.b == obj.b


class GroupOne(object):
    def __init__(self, fballItem):
        self.fballItem = fballItem
        self.hashSet = set()

    def __str__(self):
        var = ""
        for index in self.hashSet:
            var += playIndex2Text(index)
        return var

    def getAllRate(self):
        total = 0
        for integer in self.hashSet:
            total += float(self.fballItem.oddArray[integer])
        return total

    def containsValue(self, value):
        return self.hashSet.__contains__(value)

    def add(self, pair):
        self.hashSet.add(pair.a)
        self.hashSet.add(pair.b)

    def addOne(self, a):
        self.hashSet.add(a)

    def isFinishMergin(self, pair, listParis):
        if self.hashSet.__len__() == 0:
            return False
        # 都添加了，所以不需要合并
        isContainA = self.hashSet.__contains__(pair.a)
        isContainB = self.hashSet.__contains__(pair.b)

        if (isContainA and isContainB):
            return True

        # 判断传递关系
        if isContainB:
            for integer in self.hashSet:
                if self.containsItem(Pair(pair.a, integer), listParis) == False:
                    return False
            self.add(pair)
            return True
        if isContainA:
            for integer in self.hashSet:
                if self.containsItem(Pair(pair.b, integer), listParis) == False:
                    return False
            self.add(pair)
            return True
        return False

    def containsItem(self, pair, pairs):
        for i in pairs:
            if (i.equals(pair)):
                return True
        return False


class Groups:
    def __init__(self, fballItem):
        self.fballItem = fballItem
        self.listGroups = []
        pass

    def __str__(self):
        var = ""
        for one in self.listGroups:
            var += one.__str__() + "|"
        return var

    def containsValue(self, value):
        for ttaa in self.listGroups:
            if (ttaa.containsValue(value)):
                return True
        return False

    def addAll2Group(self, pairList):
        for pair in pairList:
            self.add2Group(pair, pairList)

    def addNewGroupPair(self, pair):
        one = GroupOne(self.fballItem)
        one.add(pair)
        self.listGroups.append(one)

    def addNewGroup(self, value):
        one = GroupOne(self.fballItem)
        one.addOne(value)
        self.listGroups.append(one)

    def addOthers(self, values):
        for value in values:
            if self.containsValue(value) == False:
                self.addNewGroup(value)

    def add2Group(self, pair, pairLists):
        for one in self.listGroups:
            if (one.isFinishMergin(pair, pairLists)):
                return
        self.addNewGroupPair(pair)


class CombinationUtil:
    def __init__(self, total, choose):
        self.total = total
        self.listResult = []
        self.choose = choose

    def startCalc(self):
        array = []
        for i in range(self.total):
            array.append(i)
        hadChoosenArr = []
        self.lottery(array, 0, self.total - 1, self.choose, hadChoosenArr)

    def getReslut(self):
        return self.listResult

    def lottery(self, array, startIndex, endIndex, needBalls, hadChoosenArr):
        if needBalls == 0:
            self.addResult(hadChoosenArr);
            return
        maxIndex = (endIndex - needBalls + 1);
        for i in range(startIndex, maxIndex + 1):
            hadChoosenArr.append(array[i]);
            self.lottery(array, (i + 1), endIndex, (needBalls - 1), hadChoosenArr)
            hadChoosenArr.remove(array[i]);

    def addResult(self, hadChoosenArr):
        arr = []
        for i in hadChoosenArr:
            arr.append(i)
        self.listResult.append(arr)
        pass


combinationCache = {}


# total选 choose
def getCombinationList(total, choose):
    key = total, choose
    var = combinationCache.keys().__contains__(key)
    if var:
        return combinationCache[key]
    else:
        var = CombinationUtil(total, choose)
        var.startCalc()
        reslut = var.getReslut()
        combinationCache[key] = reslut
        return reslut
    pass


class RewardHelp:
    def __init__(self, fballItem):
        self.fballItem = fballItem;
        self.minGroups = Groups(fballItem)
        self.maxGroups = Groups(fballItem)
        self.maxRate = sys.float_info.min
        self.minRate = sys.float_info.max
        pass

    def buildGroups(self):
        selArr = self.fballItem.selArray
        if selArr.__len__() == 1:
            self.minGroups.addNewGroup(selArr[0])
            self.maxGroups.addNewGroup(selArr[0])
            return
        list = getCombinationList(selArr.__len__(), 2)
        listMaxPairs = []
        listMinPairs = []
        for arr in list:  # arr的长度是2
            index1 = selArr[arr[0]]
            index2 = selArr[arr[1]]
            relations = getRelationship(index1, index2, self.fballItem.rangqiu)
            var = Pair(index1, index2, relations)
            if var.isMaxRate():
                listMaxPairs.append(var)
            if var.isMinRate():
                listMinPairs.append(var)
        self.maxGroups.addAll2Group(listMaxPairs)
        self.minGroups.addAll2Group(listMinPairs)

        self.maxGroups.addOthers(selArr)
        self.minGroups.addOthers(selArr)

        print "分组 maxGroup", self.maxGroups
        print "分组 minGroup", self.minGroups

    def buildRateDatas(self):
        self.buildGroups();
        selArr = self.fballItem.selArray
        if selArr.__len__() == 1:  # {//长度为1表示最小值是它，最大值也是它
            self.maxRate = self.minRate = selArr[0];
            print "maxRate = minRate = ", self.maxRate
            return;

        # //计算最小分组赔率,最大分组赔率
        for one in self.maxGroups.listGroups:
            self.maxRate = max(one.getAllRate(), self.maxRate);
        for one in self.minGroups.listGroups:
            self.minRate = min(one.getAllRate(), self.minRate);
        print "maxRate ", self.maxRate
        print "minRate ", self.minRate


def getRangeReturns(listFballItems, passWayItems):
    rewordLists = []
    for item in listFballItems:
        var = RewardHelp(item)
        var.buildRateDatas()
        rewordLists.append(var)
    dbMin = sys.float_info.max
    dbMax = 0

    for item in passWayItems:
        list = getCombinationList(listFballItems.__len__(), item)
        print "组合为:",list
        for arr in list:
            minVar = 1
            maxVar = 1
            for index in arr:
                helpItem = rewordLists[index]
                minVar *= helpItem.minRate
                maxVar *= helpItem.maxRate
            dbMax += maxVar
            dbMin = min(dbMin, minVar)
    return (dbMin * 2, dbMax * 2)


if __name__ == "__main__":
    # 过关方式
    # passWays = [1, 2, 3, 4, 5, 6]
    #
    # 测试关系
    # getRelationship(SEL_30, SEL_2, 1)
    # getRelationship(SEL_rangfu, SEL_4_2, 1)

    # list= getCombinationList(54,2)
    # for arr in list:
    #     if(arr[0]>SEL_rangfu):
    #         break
    #     getRelationship(arr[0], arr[1], 1)

    #
    # sett = {1, 2, 1}

    # print getCombinationList(4, 4)
    import time
    vartime=time.time();
    #
    # listFballItems = [
    #     FBallItem([SEL_zhusheng, SEL_3, SEL_3_0, SEL_2_5, SEL_0_5, SEL_30, SEL_03], 1),
    #     FBallItem([SEL_0, SEL_0_0], 1)
    # ]
    listFballItems = [
        FBallItem([SEL_zhusheng, SEL_rangfu], 1),
        FBallItem([SEL_zhusheng, SEL_rangfu], 1),
        FBallItem([SEL_zhusheng, SEL_rangfu], 1)
    ]

    #
    print getRangeReturns(listFballItems, [2])

    print time.time()-vartime;
