class Edge:
    def __init__(self, source, destine, weight):
        self.weight = weight
        self.source = source
        self.destine = destine


class Graph:
    def __init__(self):
        self.vertices = set([])
        self.edges = set([])
        self.adjacents = {}

    def add_edge(self, edge):
        self.vertices.add(edge.source)
        self.vertices.add(edge.destine)
        if edge.source not in self.adjacents.keys():
            self.adjacents[edge.source] = set([])
        self.adjacents[edge.source].add(edge)
        self.edges.add(edge)
        # print("add edge from {} to {},weight{}".format(edge.source, edge.destine, edge.weight))

    def get_adjacents(self, vertex):
        # print("get the adjacent vertices of vertex {}".format(vertex))
        if vertex not in self.adjacents.keys():
            return set([])
        return self.adjacents[vertex]

    def vertex_number(self):
        return len(self.vertices)

    def edge_number(self):
        return len(self.edges)


class MinPQ:
    def __init__(self):
        self.queue = [(0, 0)]
        # print("create a min Priority Queue to record the distance")

    def is_empty(self):
        return len(self.queue) == 1

    def size(self):
        return len(self.queue) - 1

    def min(self):
        return self.queue[1]

    def insert(self, vertex, new_value):
        self.queue.append((vertex, new_value))
        self.swim(self.size())

    def del_min(self):
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        temp = self.queue.pop(-1)
        self.sink(1)
        return temp

    def swim(self, index):
        while index > 1 and self.queue[index // 2][1] > self.queue[index][1]:
            self.queue[index //
                       2], self.queue[index] = self.queue[index], self.queue[
                index // 2]
            index = index // 2

    def sink(self, index):
        while 2 * index <= self.size():
            next_level = 2 * index
            if next_level < self.size() and self.queue[next_level][
                1] > self.queue[next_level + 1][1]:
                next_level += 1
            if self.queue[index][1] <= self.queue[next_level][1]:
                return
            self.queue[index], self.queue[next_level] = self.queue[
                                                            next_level], self.queue[index]
            index = next_level

    def contains(self, vertex):
        for index in range(1, len(self.queue)):
            if self.queue[index][0] == vertex:
                return True
        return False

    def change_dist(self, vertex, new_dist):
        for index in range(1, len(self.queue)):
            if self.queue[index][0] == vertex:
                self.queue[index] = (vertex, new_dist)


class ShortestPath:
    def __init__(self, graph, start_point):
        self.dist_to = {}
        self.edge_to = {}
        for vertex in graph.vertices:
            self.dist_to[vertex] = float("inf")
        self.dist_to[start_point] = start_point
        self.start_point = start_point
        self.dist_queue = MinPQ()
        self.dist_queue.insert(start_point, self.dist_to[start_point])
        # print("insert the start point into the priority queue and initialize the distance")
        while not self.dist_queue.is_empty():
            vertex, _ = self.dist_queue.del_min()
            # print("grow the mini-distance tree by poping vertex {} from the queue".format(vertex))
            for edge in graph.get_adjacents(vertex):
                self.relax(edge)

    def relax(self, edge):
        # print("relax edge from {} to {}".format(edge.source, edge.destine))
        source = edge.source
        destine = edge.destine

        if self.dist_to[destine] > self.dist_to[source] + edge.weight:
            self.dist_to[destine] = self.dist_to[source] + edge.weight
            self.edge_to[destine] = edge
            if self.dist_queue.contains(destine):
                self.dist_queue.change_dist(destine, self.dist_to[destine])
            else:
                self.dist_queue.insert(destine, self.dist_to[destine])

    def dist_to(self, vertex):
        return self.dist_to[vertex]

    def path_to(self, vertex):
        lPath = [vertex]
        temp_vertex = vertex
        while temp_vertex != self.start_point:
            temp_vertex = self.edge_to[temp_vertex].source
            lPath.append(temp_vertex)
        lPath.reverse()
        return lPath


def Dijkstra(list_Grph,from_point,to_point):
    test = Graph()
    #Create an  graph 
    for item in list_Grph:
          test.add_edge(Edge(item[0], item[1],item[2]))
          # you will need to the next line of code if the graph is a disorderly 
          #test.add_edge(Edge(item[1], item[0],item[2]))
    path = ShortestPath(test, from_point)
    distPath = path.path_to(to_point)
    return distPath


def get_key(dict, value):
    list =  [k for k, v in dict.items() if v == value]
    a = list[0]
    return a

def Sum_money(graph,station_graph,disPath):
    sum_dis = 0
    while len(disPath) > 1:
        a = get_key(station_graph,disPath[0])
        # print(a)
        b = get_key(station_graph,disPath[1])
        # print(b)
        sum_dis += graph[a][b]
        disPath.pop(0)
    dis = sum_dis / 1000
    if 0 < dis < 6:
        money = 3
    elif dis > 6 and dis <= 12:
        money = 4
    elif dis > 12 and dis <= 22:
        money = 5
    elif dis > 22 and dis <= 32:
        money = 6
    elif dis > 32:
        dis -= 32
        dis = int(dis / 20) + 1
        money = 6 + dis
    elif dis == 0:
        money = ' '
    return money


def test():

    graph = {'pingguoyuan': {'gucheng': 2606},
        'gucheng': {'pingguoyuan': 2606, 'bajiaoyouleyuan': 1921},
        'bajiaoyouleyuan': {'gucheng': 1921, 'babaoshan': 1953},
        'babaoshan': {'bajiaoyouleyuan': 1953, 'yuquanlu': 1479},
        'yuquanlu': {'babaoshan': 1479, 'wukesong': 1810},
        'wukesong': {'yuquanlu': 1810, 'wanshoulu': 1778},
        'wanshoulu': {'wukesong': 1778, 'gongzhufen': 1313},
        'gongzhufen': {'wanshoulu': 1313, 'junshibowuguan': 1172, 'lianhuaqiao': 1016, 'xidiaoyutai': 2386},
        'junshibowuguan': {'gongzhufen': 1172, 'muxidi': 1166, 'baiduizi': 1912, 'beijingxizhan': 1398},
        'muxidi': {'junshibowuguan': 1166, 'nanlishilu': 1291},
        'nanlishilu': {'muxidi': 1291, 'fuxingmen': 424},
        'fuxingmen': {'nanlishilu': 424, 'xidan': 1590, 'fuchengmen': 1832, 'changchunjie': 1234},
        'xidan': {'fuxingmen': 1590, 'tiananmenxi': 1217, 'lingjinghutong': 1011, 'xuanwumen': 815},
        'tiananmenxi': {'xidan': 1217, 'tiananmendong': 925},
        'tiananmendong': {'tiananmenxi': 925, 'wangfujing': 852},
        'wangfujing': {'tiananmendong': 852, 'dongdan': 774},
        'dongdan': {'wangfujing': 774, 'jianguomen': 1230, 'dengshikou': 945, 'chongwenmen': 821},
        'jianguomen': {'dongdan': 1230, 'yong\'anli': 1377, 'beijingzhan': 945, 'zhaoyangmen': 1763},
        'yong\'anli': {'jianguomen': 1377, 'guomao': 790},
        'guomao': {'yong\'anli': 790, 'dawanglu': 1385, 'jintaixizhao': 835, 'shuangjing': 1759},
        'dawanglu': {'guomao': 1385, 'sihui': 1673, 'jiulongshan': 1780, 'hongmiao': 708},
        'sihui': {'dawanglu': 1673, 'sihuidong': 1715},
        'sihuidong': {'sihui': 1715, 'gaobeidian': 1375},
        'xizhimen': {'chegongzhuang': 909, 'jishuitan': 1899, 'dongwuyuan': 1441, 'xinjiekou': 1025, 'dazhongsi': 2839},
        'chegongzhuang': {'xizhimen': 909, 'fuchengmen': 960, 'chegongzhuangxi': 887, 'pinganli': 1443},
        'fuchengmen': {'chegongzhuang': 960, 'fuxingmen': 1832},
        'changchunjie': {'fuxingmen': 1234, 'xuanwumen': 929},
        'xuanwumen': {'changchunjie': 929, 'hepingmen': 851, 'xidan': 815, 'caishikou': 1152},
        'hepingmen': {'xuanwumen': 851, 'qianmen': 1171},
        'qianmen': {'hepingmen': 1171, 'chongwenmen': 1634},
        'chongwenmen': {'qianmen': 1634, 'beijingzhan': 1023, 'dongdan': 821, 'ciqikou': 876},
        'beijingzhan': {'chongwenmen': 1023, 'jianguomen': 945},
        'zhaoyangmen': {'jianguomen': 1763, 'dongsishitiao': 1027, 'dongsi': 1399, 'dongdaqiao': 1668},
        'dongsishitiao': {'zhaoyangmen': 1027, 'dongzhimen': 824},
        'dongzhimen': {'dongsishitiao': 824, 'yonghegong': 2228, 'liufang': 1769},
        'yonghegong': {'dongzhimen': 2228, 'andingmen': 794, 'hepinglibeijie': 1151, 'beixinqiao': 866},
        'andingmen': {'yonghegong': 794, 'guloudajie': 1237},
        'guloudajie': {'andingmen': 1237, 'jishuitan': 1766, 'andelibeijie': 1083, 'shenshahai': 1188},
        'jishuitan': {'guloudajie': 1766, 'xizhimen': 1899},
        'anheqiaobei': {'beigongmen': 1363},
        'beigongmen': {'anheqiaobei': 1363, 'xiyuan': 1251},
        'xiyuan': {'beigongmen': 1251, 'yuanmingyuan': 1672},
        'yuanmingyuan': {'xiyuan': 1672, 'beijingdaxuedongmen': 1295},
        'beijingdaxuedongmen': {'yuanmingyuan': 1295, 'zhongguancun': 887},
        'zhongguancun': {'beijingdaxuedongmen': 887, 'haidianhuangzhuang': 900},
        'haidianhuangzhuang': {'zhongguancun': 900, 'renmindaxue': 1063, 'suzhoujie': 950, 'zhichunli': 975},
        'renmindaxue': {'haidianhuangzhuang': 1063, 'weigongcun': 1051},
        'weigongcun': {'renmindaxue': 1051, 'guojiatushuguan': 1658},
        'guojiatushuguan': {'weigongcun': 1658, 'dongwuyuan': 1517, 'baishiqiaonan': 1096},
        'dongwuyuan': {'guojiatushuguan': 1517, 'xizhimen': 1441},
        'xinjiekou': {'xizhimen': 1025, 'pinganli': 1100},
        'pinganli': {'xinjiekou': 1100, 'xisi': 1100, 'chegongzhuang': 1443, 'beihaibei': 1321},
        'xisi': {'pinganli': 1100, 'lingjinghutong': 869},
        'lingjinghutong': {'xisi': 869, 'xidan': 1011},
        'caishikou': {'xuanwumen': 1152, 'taoranting': 1200, 'guanganmennei': 1374, 'hufangqiao': 885},
        'taoranting': {'caishikou': 1200, 'beijingnanzhan': 1643},
        'beijingnanzhan': {'taoranting': 1643, 'majiabao': 1480, 'taoranqiao': 887},
        'majiabao': {'beijingnanzhan': 1480, 'jiaomen west': 827},
        'jiaomen west': {'majiabao': 827, 'gongyixiqiao': 989, 'jiaomen east': 1254, 'caoqiao': 1688},
        'gongyixiqiao': {'jiaomen west': 989, 'xingong': 2798},
        'tiantongyuanbei': {'tiantongyuan': 939},
        'tiantongyuan': {'tiantongyuanbei': 939, 'tiantongyuannan': 965},
        'tiantongyuannan': {'tiantongyuan': 965, 'lishuiqiao': 1544},
        'lishuiqiao': {'tiantongyuannan': 1544, 'lishuiqiaonan': 1305, 'huoying': 4785, 'beiyuan': 2272},
        'lishuiqiaonan': {'lishuiqiao': 1305, 'beiyuanlubei': 1286},
        'beiyuanlubei': {'lishuiqiaonan': 1286, 'datunludong': 3000},
        'datunludong': {'beiyuanlubei': 3000, 'huixinxijiebeikou': 1838, 'anlilu': 938, 'guanzhuang': 1087},
        'huixinxijiebeikou': {'datunludong': 1838, 'huixinxijienankou': 1122},
        'huixinxijienankou': {'huixinxijiebeikou': 1122, 'hepingxiqiao': 1025, 'anzhenmen': 982, 'shaoyaoju': 1712},
        'hepingxiqiao': {'huixinxijienankou': 1025, 'hepinglibeijie': 1059},
        'hepinglibeijie': {'hepingxiqiao': 1059, 'yonghegong': 1151},
        'beixinqiao': {'yonghegong': 866, 'zhangzizhonglu': 791},
        'zhangzizhonglu': {'beixinqiao': 791, 'dongsi': 1016},
        'dongsi': {'zhangzizhonglu': 1016, 'dengshikou': 848, 'nanluoguxiang': 1937, 'zhaoyangmen': 1399},
        'dengshikou': {'dongsi': 848, 'dongdan': 945},
        'ciqikou': {'chongwenmen': 876, 'tiantandongmen': 1183, 'qiaowan': 1016, 'guangqumennei': 1138},
        'tiantandongmen': {'ciqikou': 1183, 'puhuangyu': 1900},
        'puhuangyu': {'tiantandongmen': 1900, 'liujiayao': 905, 'jingtai': 1025, 'fangzhuang': 1486},
        'liujiayao': {'puhuangyu': 905, 'songjiazhuang': 1670},
        'songjiazhuang': {'liujiayao': 1670, 'chengshousi': 1677, 'shiliuzhuang': 1269, 'xiaocun': 2631},
        'haidianwuluju': {'cishousi': 1508},
        'cishousi': {'haidianwuluju': 1508, 'huayuanqiao': 1431, 'xidiaoyutai': 1214, 'chedaogou': 1590},
        'huayuanqiao': {'cishousi': 1431, 'baishiqiaonan': 1166},
        'baishiqiaonan': {'huayuanqiao': 1166, 'chegongzhuangxi': 1664, 'guojiatushuguan': 1096, 'baiduizi': 943},
        'chegongzhuangxi': {'baishiqiaonan': 1664, 'chegongzhuang': 887},
        'beihaibei': {'pinganli': 1321, 'nanluoguxiang': 1349},
        'nanluoguxiang': {'beihaibei': 1349, 'dongsi': 1937, 'shenshahai': 902},
        'dongdaqiao': {'zhaoyangmen': 1668, 'hujialou': 845},
        'hujialou': {'dongdaqiao': 845, 'jintailu': 1450, 'tuanjiehu': 1149, 'jintaixizhao': 734},
        'jintailu': {'hujialou': 1450, 'shilibao': 2036, 'hongmiao': 894, 'zhaoyanggongyuan': 1085},
        'shilibao': {'jintailu': 2036, 'qingnianlu': 1282},
        'qingnianlu': {'shilibao': 1282, 'dalianpo': 3999},
        'dalianpo': {'qingnianlu': 3999, 'huangqu': 1238},
        'huangqu': {'dalianpo': 1238, 'changying': 1854},
        'changying': {'huangqu': 1854, 'caofang': 1405},
        'caofang': {'changying': 1405, 'wuzixueyuanlu': 2115},
        'wuzixueyuanlu': {'caofang': 2115, 'tongzhoubeiguan': 2557},
        'tongzhoubeiguan': {'wuzixueyuanlu': 2557, 'tongyunmen': 1468},
        'tongyunmen': {'tongzhoubeiguan': 1468, 'beiyunhexi': 1543},
        'beiyunhexi': {'tongyunmen': 1543, 'beiyunhedong': 1599},
        'beiyunhedong': {'beiyunhexi': 1599, 'haojiafu': 929},
        'haojiafu': {'beiyunhedong': 929, 'dongxiayuan': 1346},
        'dongxiayuan': {'haojiafu': 1346, 'lucheng': 1194},
        'lucheng': {'dongxiayuan': 1194},
        'beijingxizhan': {'wanzi': 935, 'junshibowuguan': 1398, 'liuliqiaodong': 1170},
        'wanzi': {'beijingxizhan': 935, 'daguanying': 734},
        'daguanying': {'wanzi': 734, 'guanganmennei': 1874},
        'guanganmennei': {'daguanying': 1874, 'caishikou': 1374},
        'hufangqiao': {'caishikou': 885, 'zhushikou': 1205},
        'zhushikou': {'hufangqiao': 1205, 'qiaowan': 869},
        'qiaowan': {'zhushikou': 869, 'ciqikou': 1016},
        'guangqumennei': {'ciqikou': 1138, 'guangqumenwai': 1332},
        'guangqumenwai': {'guangqumennei': 1332, 'shuangjing': 1241},
        'shuangjing': {'guangqumenwai': 1241, 'jiulongshan': 1311, 'guomao': 1759, 'jingsong': 1006},
        'jiulongshan': {'shuangjing': 1311, 'dajiaoting': 781, 'pingleyuan': 897, 'dawanglu': 1780},
        'dajiaoting': {'jiulongshan': 781, 'baiziwan': 865},
        'baiziwan': {'dajiaoting': 865, 'huagong': 903},
        'huagong': {'baiziwan': 903, 'nanlouzizhuang': 1464},
        'nanlouzizhuang': {'huagong': 1464, 'huanlegujingqu': 906},
        'huanlegujingqu': {'nanlouzizhuang': 906, 'fatou': 1679},
        'fatou': {'huanlegujingqu': 1679, 'shuanghe': 1304},
        'shuanghe': {'fatou': 1304, 'jiaohuachang': 1021},
        'jiaohuachang': {'shuanghe': 1021},
        'zhuxinzhuang': {'yuzhilu': 2318, 'gonghuacheng': 3799, 'shengmingkexueyuan': 2367},
        'yuzhilu': {'zhuxinzhuang': 2318, 'pingxifu': 1985},
        'pingxifu': {'yuzhilu': 1985, 'huilongguandongdajie': 2056},
        'huilongguandongdajie': {'pingxifu': 2056, 'huoying': 1114},
        'huoying': {'huilongguandongdajie': 1114, 'yuxin': 1894, 'huilongguan': 2110, 'lishuiqiao': 4785},
        'yuxin': {'huoying': 1894, 'xixiaokou': 1543},
        'xixiaokou': {'yuxin': 1543, 'yongtaizhuang': 1041},
        'yongtaizhuang': {'xixiaokou': 1041, 'lincuiqiao': 2553},
        'lincuiqiao': {'yongtaizhuang': 2553, 'senlingongyuannanmen': 2555},
        'senlingongyuannanmen': {'lincuiqiao': 2555, 'aolinpikegongyuan': 1016},
        'aolinpikegongyuan': {'senlingongyuannanmen': 1016, 'aotizhongxin': 1667, 'beishatan': 1999, 'anlilu': 1368},
        'aotizhongxin': {'aolinpikegongyuan': 1667, 'beitucheng': 900},
        'beitucheng': {'aotizhongxin': 900, 'anhuaqiao': 1018, 'jiandemen': 1100, 'anzhenmen': 1020},
        'anhuaqiao': {'beitucheng': 1018, 'andelibeijie': 1274},
        'andelibeijie': {'anhuaqiao': 1274, 'guloudajie': 1083},
        'shenshahai': {'guloudajie': 1188, 'nanluoguxiang': 902},
        'baiduizi': {'baishiqiaonan': 943, 'junshibowuguan': 1912},
        'liuliqiaodong': {'beijingxizhan': 1170, 'liuliqiao': 1309},
        'liuliqiao': {'liuliqiaodong': 1309, 'qilizhuang': 1778, 'xiju': 1584, 'lianhuaqiao': 2392},
        'qilizhuang': {'liuliqiao': 1778, 'fengtaidongdajie': 1325, 'dajing': 1579, 'xiju': 845},
        'fengtaidongdajie': {'qilizhuang': 1325, 'fengtainanlu': 1585},
        'fengtainanlu': {'fengtaidongdajie': 1585, 'keyilu': 980},
        'keyilu': {'fengtainanlu': 980, 'fengtaikejiyuan': 788},
        'fengtaikejiyuan': {'keyilu': 788, 'guogongzhuang': 1347},
        'guogongzhuang': {'fengtaikejiyuan': 1347, 'dabaotai': 1405},
        'bagou': {'suzhoujie': 1110, 'huoqiying': 1495},
        'suzhoujie': {'bagou': 1110, 'haidianhuangzhuang': 950},
        'zhichunli': {'haidianhuangzhuang': 975, 'zhichunlu': 1058},
        'zhichunlu': {'zhichunli': 1058, 'xitucheng': 1101, 'dazhongsi': 1206, 'wudaokou': 1829},
        'xitucheng': {'zhichunlu': 1101, 'mudanyuan': 1330},
        'mudanyuan': {'xitucheng': 1330, 'jiandemen': 973},
        'jiandemen': {'mudanyuan': 973, 'beitucheng': 1100},
        'anzhenmen': {'beitucheng': 1020, 'huixinxijienankou': 982},
        'shaoyaoju': {'huixinxijienankou': 1712, 'taiyanggong': 1003, 'wangjingxi': 2152, 'guangximen': 1110},
        'taiyanggong': {'shaoyaoju': 1003, 'sanyuanqiao': 1759},
        'sanyuanqiao': {'taiyanggong': 1759, 'liangmaqiao': 1506},
        'liangmaqiao': {'sanyuanqiao': 1506, 'nongyezhanlanguan': 914},
        'nongyezhanlanguan': {'liangmaqiao': 914, 'tuanjiehu': 853},
        'tuanjiehu': {'nongyezhanlanguan': 853, 'hujialou': 1149},
        'jintaixizhao': {'hujialou': 734, 'guomao': 835},
        'jingsong': {'shuangjing': 1006, 'panjiayuan': 1021},
        'panjiayuan': {'jingsong': 1021, 'shilihe': 1097},
        'shilihe': {'panjiayuan': 1097, 'fenzhongsi': 1804, 'fangzhuang': 1618, 'nanbalizhuang': 1147},
        'fenzhongsi': {'shilihe': 1804, 'chengshousi': 1058},
        'chengshousi': {'fenzhongsi': 1058, 'songjiazhuang': 1677},
        'shiliuzhuang': {'songjiazhuang': 1269, 'dahongmen': 1244},
        'dahongmen': {'shiliuzhuang': 1244, 'jiaomen east': 1130},
        'jiaomen east': {'dahongmen': 1130, 'jiaomen west': 1254},
        'caoqiao': {'jiaomen west': 1688, 'jijiamiao': 1547},
        'jijiamiao': {'caoqiao': 1547, 'shoujingmao': 1143},
        'shoujingmao': {'jijiamiao': 1143, 'fengtaizhan': 1717},
        'fengtaizhan': {'shoujingmao': 1717, 'niwa': 954},
        'niwa': {'fengtaizhan': 954, 'xiju': 749},
        'xiju': {'niwa': 749, 'liuliqiao': 1584, 'qilizhuang': 845},
        'lianhuaqiao': {'liuliqiao': 2392, 'gongzhufen': 1016},
        'xidiaoyutai': {'gongzhufen': 2386, 'cishousi': 1214},
        'chedaogou': {'cishousi': 1590, 'changchunqiao': 1205},
        'changchunqiao': {'chedaogou': 1205, 'huoqiying': 961},
        'huoqiying': {'changchunqiao': 961, 'bagou': 1495},
        'dazhongsi': {'xizhimen': 2839, 'zhichunlu': 1206},
        'wudaokou': {'zhichunlu': 1829, 'shangdi': 4866},
        'shangdi': {'wudaokou': 4866, 'xierqi': 2538},
        'xierqi': {'shangdi': 2538, 'longze': 3623, 'shengmingkexueyuan': 5440},
        'longze': {'xierqi': 3623, 'huilongguan': 1423},
        'huilongguan': {'longze': 1423, 'huoying': 2110},
        'beiyuan': {'lishuiqiao': 2272, 'wangjingxi': 6720},
        'wangjingxi': {'beiyuan': 6720, 'shaoyaoju': 2152, 'guanzhuang': 2071, 'wangjing': 1758},
        'guangximen': {'shaoyaoju': 1110, 'liufang': 1135},
        'liufang': {'guangximen': 1135, 'dongzhimen': 1769},
        'zhangguozhuang': {'yuanboyuan': 1345},
        'yuanboyuan': {'zhangguozhuang': 1345, 'dawayao': 4073},
        'dawayao': {'yuanboyuan': 4073, 'guozhuangzi': 1236},
        'guozhuangzi': {'dawayao': 1236, 'dajing': 2044},
        'dajing': {'guozhuangzi': 2044, 'qilizhuang': 1579},
        'taoranqiao': {'beijingnanzhan': 887, 'yongdingmenwai': 1063},
        'yongdingmenwai': {'taoranqiao': 1063, 'jingtai': 1119},
        'jingtai': {'yongdingmenwai': 1119, 'puhuangyu': 1025},
        'fangzhuang': {'puhuangyu': 1486, 'shilihe': 1618},
        'nanbalizhuang': {'shilihe': 1147, 'beigongdaximen': 1276},
        'beigongdaximen': {'nanbalizhuang': 1276, 'pingleyuan': 1128},
        'pingleyuan': {'beigongdaximen': 1128, 'jiulongshan': 897},
        'hongmiao': {'dawanglu': 708, 'jintailu': 894},
        'zhaoyanggongyuan': {'jintailu': 1085, 'zaoying': 1221},
        'zaoying': {'zhaoyanggongyuan': 1221, 'dongfengbeiqiao': 2173},
        'dongfengbeiqiao': {'zaoying': 2173, 'jiangtai': 1600},
        'jiangtai': {'dongfengbeiqiao': 1600, 'gaojiayuan': 1171},
        'gaojiayuan': {'jiangtai': 1171, 'wangjingnan': 676},
        'wangjingnan': {'gaojiayuan': 676, 'futong': 1168},
        'futong': {'wangjingnan': 1168, 'wangjing': 903},
        'wangjing': {'futong': 903, 'donghuqu': 1283, 'wangjingxi': 1758, 'wangjingdong': 1652},
        'donghuqu': {'wangjing': 1283, 'laiguangying': 1100},
        'laiguangying': {'donghuqu': 1100, 'shangezhuang': 1364},
        'shangezhuang': {'laiguangying': 1364},
        'qinghuadongluxikou': {'liudaokou': 1144},
        'liudaokou': {'qinghuadongluxikou': 1144, 'beishatan': 1337},
        'beishatan': {'liudaokou': 1337, 'aolinpikegongyuan': 1999},
        'anlilu': {'aolinpikegongyuan': 1368, 'datunludong': 938},
        'guanzhuang': {'datunludong': 1087, 'wangjingxi': 2071, 'shuangqiao': 1912, 'baliqiao': 1763},
        'wangjingdong': {'wangjing': 1652, 'cuigezhuang': 2295},
        'cuigezhuang': {'wangjingdong': 2295, 'maquanying': 2008},
        'maquanying': {'cuigezhuang': 2008, 'sunhe': 3309},
        'sunhe': {'maquanying': 3309, 'guozhan': 3386},
        'guozhan': {'sunhe': 3386, 'hualikan': 1615},
        'hualikan': {'guozhan': 1615, 'houshayu': 3354},
        'houshayu': {'hualikan': 3354, 'nanfaxin': 4576},
        'nanfaxin': {'houshayu': 4576, 'shimen': 2712},
        'shimen': {'nanfaxin': 2712, 'shunyi': 1331},
        'shunyi': {'shimen': 1331, 'fengbo': 2441},
        'fengbo': {'shunyi': 2441},
        'gaobeidian': {'sihuidong': 1375, 'chuanmeidaxue': 2002},
        'chuanmeidaxue': {'gaobeidian': 2002, 'shuangqiao': 1894},
        'shuangqiao': {'chuanmeidaxue': 1894, 'guanzhuang': 1912},
        'baliqiao': {'guanzhuang': 1763, 'tongzhoubeiyuan': 1700},
        'tongzhoubeiyuan': {'baliqiao': 1700, 'guoyuan': 1465},
        'guoyuan': {'tongzhoubeiyuan': 1465, 'jiukeshu': 990},
        'jiukeshu': {'guoyuan': 990, 'liyuan': 1225},
        'liyuan': {'jiukeshu': 1225, 'linheli': 1257},
        'linheli': {'liyuan': 1257, 'tuqiao': 776},
        'tuqiao': {'linheli': 776},
        'changpingxishankou': {'ming tombs': 1213},
        'ming tombs': {'changpingxishankou': 1213, 'changping': 3508},
        'changping': {'ming tombs': 3508, 'changpingdongguan': 2433},
        'changpingdongguan': {'changping': 2433, 'beishaowa': 1683},
        'beishaowa': {'changpingdongguan': 1683, 'nanshao': 1958},
        'nanshao': {'beishaowa': 1958, 'shahegaojiaoyuan': 5357},
        'shahegaojiaoyuan': {'nanshao': 5357, 'shahe': 1964},
        'shahe': {'shahegaojiaoyuan': 1964, 'gonghuacheng': 2025},
        'gonghuacheng': {'shahe': 2025, 'zhuxinzhuang': 3799},
        'shengmingkexueyuan': {'zhuxinzhuang': 2367, 'xierqi': 5440},
        'xiaocun': {'songjiazhuang': 2631, 'xiaohongmen': 1275},
        'xiaohongmen': {'xiaocun': 1275, 'jiugong': 2366},
        'jiugong': {'xiaohongmen': 2366, 'yizhuangqiao': 1982},
        'yizhuangqiao': {'jiugong': 1982, 'yizhuangwenhuayuan': 993},
        'yizhuangwenhuayuan': {'yizhuangqiao': 993, 'wanyuanjie': 1728},
        'wanyuanjie': {'yizhuangwenhuayuan': 1728, 'rongjingdongjie': 1090},
        'rongjingdongjie': {'wanyuanjie': 1090, 'rongchangdongjie': 1355},
        'rongchangdongjie': {'rongjingdongjie': 1355, 'tongjinanlu': 2337},
        'tongjinanlu': {'rongchangdongjie': 2337, 'jinghailu': 2301},
        'jinghailu': {'tongjinanlu': 2301, 'ciqunan': 2055},
        'ciqunan': {'jinghailu': 2055, 'ciqu': 1281},
        'ciqu': {'ciqunan': 1281},
        'xingong': {'gongyixiqiao': 2798, 'xihongmen': 5102},
        'xihongmen': {'xingong': 5102, 'gaomidianbei': 1810},
        'gaomidianbei': {'xihongmen': 1810, 'gaomidiannan': 1128},
        'gaomidiannan': {'gaomidianbei': 1128, 'zaoyuan': 1096},
        'zaoyuan': {'gaomidiannan': 1096, 'qingyuanlu': 1200},
        'qingyuanlu': {'zaoyuan': 1200, 'huangcunxidajie': 1214},
        'huangcunxidajie': {'qingyuanlu': 1214, 'huangcunhuochezhan': 987},
        'huangcunhuochezhan': {'huangcunxidajie': 987, 'yihezhuang': 2035},
        'yihezhuang': {'huangcunhuochezhan': 2035, 'shengwuyiyaojidi': 2918},
        'shengwuyiyaojidi': {'yihezhuang': 2918, 'tiangongyuan': 1811},
        'tiangongyuan': {'shengwuyiyaojidi': 1811},
        'dabaotai': {'guogongzhuang': 1405, 'daotian': 6466},
        'daotian': {'dabaotai': 6466, 'changyang': 4041},
        'changyang': {'daotian': 4041, 'libafang': 2150},
        'libafang': {'changyang': 2150, 'guangyangcheng': 1474},
        'guangyangcheng': {'libafang': 1474, 'liangxiangdaxuechengbei': 2003},
        'liangxiangdaxuechengbei': {'guangyangcheng': 2003, 'liangxiangdaxuecheng': 1188},
        'liangxiangdaxuecheng': {'liangxiangdaxuechengbei': 1188, 'liangxiangdaxuechengxi': 1738},
        'liangxiangdaxuechengxi': {'liangxiangdaxuecheng': 1738, 'liangxiangnanguan': 1332},
        'liangxiangnanguan': {'liangxiangdaxuechengxi': 1332, 'suzhuang': 1330},
        'suzhuang': {'liangxiangnanguan': 1330}
    }
    a = list(graph.keys())
    station_to_number = {}
    num = 0
    for i in a:
        num = num + 1
        station_to_number[i] = num
    station_graph = {}

    list_edge = []
    for i in graph.keys():
        edge = []
        for j,k in graph[i].items():
            edge.append(station_to_number[i])
            edge.append(station_to_number[j])
            edge.append(k)
            list_edge.append(edge[-3:])
    start_end = input()
    # print(start_end)
    for i in start_end:
        if i == ";":
            i == " "
    start_end_list = start_end.split(";")
    start = start_end_list[0]
    end = start_end_list[1]
    n = station_to_number
    start = station_to_number[start]
    end = station_to_number[end]

    path = Dijkstra(list_edge,start,end)
    print(Sum_money(graph,n,path))

test()
