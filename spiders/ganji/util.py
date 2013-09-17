#!/usr/bin/python2.7
#-*- coding=utf-8 -*-

# Copy Rights (c) Beijing TigerKnows Technology Co., Ltd.

__author__ = ['"wuyadong" <wuyadong@tigerknows.com>']

import datetime

from core.util import remove_white

_city2code = {
    u"北京": "110000",
    u"天津": "120000",
    u"石家庄": "130100",
    u"唐山": "130200",
    u"秦皇岛": "130300",
    u"邯郸": "130400",
    u"邢台": "130500",
    u"保定": "130600",
    u"张家口": "130700",
    u"承德": "130800",
    u"沧州": "130900",
    u"廊坊": "131000",
    u"衡水": "131100",
    u"太原": "140100",
    u"大同": "140200",
    u"阳泉": "140300",
    u"长治": "140400",
    u"晋城": "140500",
    u"朔州": "140600",
    u"晋中": "140700",
    u"运城": "140800",
    u"忻州": "140900",
    u"临汾": "141000",
    u"吕梁": "141100",
    u"呼和浩特": "150100",
    u"包头": "150200",
    u"乌海": "150300",
    u"赤峰": "150400",
    u"通辽": "150500",
    u"鄂尔多斯": "150600",
    u"呼伦贝尔": "150700",
    u"巴彦淖尔": "150800",
    u"乌兰察布": "150900",
    u"兴安": "152200",
    u"锡林郭勒": "152500",
    u"阿拉善": "152900",
    u"沈阳": "210100",
    u"大连": "210200",
    u"鞍山": "210300",
    u"抚顺": "210400",
    u"本溪": "210500",
    u"丹东": "210600",
    u"锦州": "210700",
    u"营口": "210800",
    u"阜新": "210900",
    u"辽阳": "211000",
    u"盘锦": "211100",
    u"铁岭": "211200",
    u"朝阳": "211300",
    u"葫芦岛": "211400",
    u"长春": "220100",
    u"吉林": "220200",
    u"四平": "220300",
    u"辽源": "220400",
    u"通化": "220500",
    u"白山": "220600",
    u"松原": "220700",
    u"白城": "220800",
    u"延边": "222400",
    u"哈尔滨": "230100",
    u"齐齐哈尔": "230200",
    u"鸡西": "230300",
    u"鹤岗": "230400",
    u"双鸭山": "230500",
    u"大庆": "230600",
    u"伊春": "230700",
    u"佳木斯": "230800",
    u"七台河": "230900",
    u"牡丹江": "231000",
    u"黑河": "231100",
    u"绥化": "231200",
    u"大兴安岭": "232700",
    u"上海": "310000",
    u"南京": "320100",
    u"无锡": "320200",
    u"徐州": "320300",
    u"常州": "320400",
    u"苏州": "320500",
    u"南通": "320600",
    u"连云港": "320700",
    u"淮安": "320800",
    u"盐城": "320900",
    u"扬州": "321000",
    u"镇江": "321100",
    u"泰州": "321200",
    u"宿迁": "321300",
    u"杭州": "330100",
    u"宁波": "330200",
    u"温州": "330300",
    u"嘉兴": "330400",
    u"湖州": "330500",
    u"绍兴": "330600",
    u"金华": "330700",
    u"衢州": "330800",
    u"舟山": "330900",
    u"台州": "331000",
    u"丽水": "331100",
    u"合肥": "340100",
    u"巢湖": "340181",
    u"芜湖": "340200",
    u"蚌埠": "340300",
    u"淮南": "340400",
    u"马鞍山": "340500",
    u"淮北": "340600",
    u"铜陵": "340700",
    u"安庆": "340800",
    u"黄山": "341000",
    u"滁州": "341100",
    u"阜阳": "341200",
    u"宿州": "341300",
    u"六安": "341500",
    u"亳州": "341600",
    u"池州": "341700",
    u"宣城": "341800",
    u"福州": "350100",
    u"厦门": "350200",
    u"莆田": "350300",
    u"三明": "350400",
    u"泉州": "350500",
    u"漳州": "350600",
    u"南平": "350700",
    u"龙岩": "350800",
    u"宁德": "350900",
    u"南昌": "360100",
    u"景德镇": "360200",
    u"萍乡": "360300",
    u"九江": "360400",
    u"新余": "360500",
    u"鹰潭": "360600",
    u"赣州": "360700",
    u"吉安": "360800",
    u"宜春": "360900",
    u"抚州": "361000",
    u"上饶": "361100",
    u"济南": "370100",
    u"青岛": "370200",
    u"淄博": "370300",
    u"枣庄": "370400",
    u"东营": "370500",
    u"烟台": "370600",
    u"潍坊": "370700",
    u"济宁": "370800",
    u"泰安": "370900",
    u"威海": "371000",
    u"日照": "371100",
    u"莱芜": "371200",
    u"临沂": "371300",
    u"德州": "371400",
    u"聊城": "371500",
    u"滨州": "371600",
    u"菏泽": "371700",
    u"郑州": "410100",
    u"开封": "410200",
    u"洛阳": "410300",
    u"平顶山": "410400",
    u"安阳": "410500",
    u"鹤壁": "410600",
    u"新乡": "410700",
    u"焦作": "410800",
    u"濮阳": "410900",
    u"许昌": "411000",
    u"漯河": "411100",
    u"三门峡": "411200",
    u"南阳": "411300",
    u"商丘": "411400",
    u"信阳": "411500",
    u"周口": "411600",
    u"驻马店": "411700",
    u"济源": "419001",
    u"武汉": "420100",
    u"黄石": "420200",
    u"十堰": "420300",
    u"宜昌": "420500",
    u"襄阳": "420600",
    u"鄂州": "420700",
    u"荆门": "420800",
    u"孝感": "420900",
    u"荆州": "421000",
    u"黄冈": "421100",
    u"咸宁": "421200",
    u"随州": "421300",
    u"恩施": "422800",
    u"仙桃": "429004",
    u"潜江": "429005",
    u"天门": "429006",
    u"神农架": "429021",
    u"长沙": "430100",
    u"株洲": "430200",
    u"湘潭": "430300",
    u"衡阳": "430400",
    u"邵阳": "430500",
    u"岳阳": "430600",
    u"常德": "430700",
    u"张家界": "430800",
    u"益阳": "430900",
    u"郴州": "431000",
    u"永州": "431100",
    u"怀化": "431200",
    u"娄底": "431300",
    u"湘西": "433100",
    u"广州": "440100",
    u"韶关": "440200",
    u"深圳": "440300",
    u"珠海": "440400",
    u"汕头": "440500",
    u"佛山": "440600",
    u"江门": "440700",
    u"湛江": "440800",
    u"茂名": "440900",
    u"肇庆": "441200",
    u"惠州": "441300",
    u"梅州": "441400",
    u"汕尾": "441500",
    u"河源": "441600",
    u"阳江": "441700",
    u"清远": "441800",
    u"东莞": "441900",
    u"中山": "442000",
    u"潮州": "445100",
    u"揭阳": "445200",
    u"云浮": "445300",
    u"南宁": "450100",
    u"柳州": "450200",
    u"桂林": "450300",
    u"梧州": "450400",
    u"北海": "450500",
    u"防城港": "450600",
    u"钦州": "450700",
    u"贵港": "450800",
    u"玉林": "450900",
    u"百色": "451000",
    u"贺州": "451100",
    u"河池": "451200",
    u"来宾": "451300",
    u"崇左": "451400",
    u"海口": "460100",
    u"三亚": "460200",
    u"五指山": "469001",
    u"琼海": "469002",
    u"儋州": "469003",
    u"文昌": "469005",
    u"万宁": "469006",
    u"东方": "469007",
    u"定安县": "469021",
    u"屯昌县": "469022",
    u"澄迈县": "469023",
    u"临高县": "469024",
    u"白沙": "469025",
    u"昌江": "469026",
    u"乐东": "469027",
    u"陵水": "469028",
    u"保亭": "469029",
    u"琼中": "469030",
    u"重庆": "500000",
    u"成都": "510100",
    u"自贡": "510300",
    u"攀枝花": "510400",
    u"泸州": "510500",
    u"德阳": "510600",
    u"绵阳": "510700",
    u"广元": "510800",
    u"遂宁": "510900",
    u"内江": "511000",
    u"乐山": "511100",
    u"南充": "511300",
    u"眉山": "511400",
    u"宜宾": "511500",
    u"广安": "511600",
    u"达州": "511700",
    u"雅安": "511800",
    u"巴中": "511900",
    u"资阳": "512000",
    u"阿坝": "513200",
    u"甘孜": "513300",
    u"凉山": "513400",
    u"贵阳": "520100",
    u"六盘水": "520200",
    u"遵义": "520300",
    u"安顺": "520400",
    u"铜仁": "522200",
    u"黔西南": "522300",
    u"毕节": "522400",
    u"黔东南": "522600",
    u"黔南": "522700",
    u"昆明": "530100",
    u"曲靖": "530300",
    u"玉溪": "530400",
    u"保山": "530500",
    u"昭通": "530600",
    u"丽江": "530700",
    u"普洱": "530800",
    u"临沧": "530900",
    u"楚雄": "532300",
    u"红河": "532500",
    u"文山": "532600",
    u"西双版纳": "532800",
    u"大理": "532900",
    u"德宏": "533100",
    u"怒江": "533300",
    u"迪庆": "533400",
    u"拉萨": "540100",
    u"昌都": "542100",
    u"山南": "542200",
    u"日喀则": "542300",
    u"那曲": "542400",
    u"阿里": "542500",
    u"林芝": "542600",
    u"西安": "610100",
    u"铜川": "610200",
    u"宝鸡": "610300",
    u"咸阳": "610400",
    u"渭南": "610500",
    u"延安": "610600",
    u"汉中": "610700",
    u"榆林": "610800",
    u"安康": "610900",
    u"商洛": "611000",
    u"兰州": "620100",
    u"嘉峪关": "620200",
    u"金昌": "620300",
    u"白银": "620400",
    u"天水": "620500",
    u"武威": "620600",
    u"张掖": "620700",
    u"平凉": "620800",
    u"酒泉": "620900",
    u"庆阳": "621000",
    u"定西": "621100",
    u"陇南": "621200",
    u"临夏": "622900",
    u"甘南": "623000",
    u"西宁": "630100",
    u"海东": "632100",
    u"海北": "632200",
    u"黄南": "632300",
    u"海南": "632500",
    u"果洛": "632600",
    u"玉树": "632700",
    u"海西": "632800",
    u"银川": "640100",
    u"石嘴山": "640200",
    u"吴忠": "640300",
    u"固原": "640400",
    u"中卫": "640500",
    u"乌鲁木齐": "650100",
    u"克拉玛依": "650200",
    u"吐鲁番": "652100",
    u"哈密": "652200",
    u"昌吉": "652300",
    u"博尔塔拉": "652700",
    u"巴音郭楞": "652800",
    u"阿克苏": "652900",
    u"克孜勒苏": "653000",
    u"喀什": "653100",
    u"和田": "653200",
    u"伊犁": "654000",
    u"塔城": "654200",
    u"阿勒泰": "654300",
    u"石河子": "659001",
    u"阿拉尔": "659002",
    u"图木舒克": "659003",
    u"五家渠": "659004"
}

_mt2tiger = {
    u"KTV": u"KTV",

    u"电影院": u"电影",

    u"国内游": u"酒店旅游",
    u"四星级/高档": u"酒店旅游",
    u"经济型/客栈": u"酒店旅游",
    u"一星级": u"酒店旅游",
    u"五星级/豪华": u"酒店旅游",
    u"三星级": u"酒店旅游",
    u"二星级": u"酒店旅游",

    u"美发": u"丽人",
    u"美甲/手护": u"丽人",
    u"SPA/美容/美体": u"丽人",
    u"脱毛/塑身/整容": u"丽人",
    u"化妆": u"丽人",
    u"其他丽人": u"丽人",
    u"婚纱摄影": u"丽人",
    u"个性写真": u"丽人",

    u"其他自助": u"美食",
    u"海鲜": u"美食",
    u"小吃": u"美食",
    u"快餐": u"美食",
    u"蛋糕": u"美食",
    u"咖啡厅/酒吧/茶室": u"美食",
    u"素食": u"美食",
    u"日本菜": u"美食",
    u"韩国菜": u"美食",
    u"东南亚菜": u"美食",
    u"江浙菜": u"美食",
    u"港式/粤菜": u"美食",
    u"其他中餐": u"美食",
    u"麻辣烫/串串香": u"美食",
    u"西餐": u"美食",
    u"川湘菜/湖北菜": u"美食",
    u"海鲜自助": u"美食",
    u"日料自助": u"美食",
    u"烤肉自助": u"美食",
    u"披萨自助": u"美食",
    u"综合类自助": u"美食",
    u"西北菜": u"美食",
    u"东北菜": u"美食",
    u"北京菜/鲁菜": u"美食",
    u"云贵菜": u"美食",
    u"干锅/烤鱼": u"美食",
    u"饮品/甜品/甜点": u"美食",
    u"披萨": u"美食",
    u"中亚菜/中东菜": u"美食",
    u"其他异国餐饮": u"美食",
    u"其他餐饮": u"美食",
    u"自助火锅": u"美食",
    u"清真菜": u"美食",
    u"中式烧烤/烤串": u"美食",
    u"客家/台湾": u"美食",
    u"汤/煲/砂锅/粥/炖菜": u"美食",
    u"创意菜/特色菜": u"美食",
    u"家常菜/农家菜/综合类": u"美食",
    u"火锅": u"美食",

    u"体检": u"生活服务",
    u"齿科": u"生活服务",
    u"艺术培训课程": u"生活服务",
    u"其他培训课程": "生活服务",
    u"儿童写真": u"生活服务",
    u"照片冲印/快印": u"生活服务",
    u"租车": u"生活服务",
    u"加油站": u"生活服务",
    u"汽车保养": u"生活服务",
    u"报刊杂志订阅": u"生活服务",
    u"充值服务": u"生活服务",
    u"宠物服务": u"生活服务",
    u"服装定制": u"生活服务",
    u"家政服务": u"生活服务",
    u"衣物/皮具洗护": u"生活服务",
    u"鲜花": u"生活服务",
    u"婚庆服务": u"生活服务",
    u"其他生活服务": u"生活服务",
    u"配镜服务": u"生活服务",
    u"母婴服务": u"生活服务",
    u"语言培训课程": u"生活服务",
    u"本地购物": u"生活服务",
    u"早教/儿童课程": u"生活服务",
    u"职业培训课程": u"生活服务",
    u"驾校": u"生活服务",
    u"网球/壁球": u"生活服务",
    u"武术": u"生活服务",
    u"其他文化艺术": u"生活服务",
    u"证件照": u"生活服务",
    u"其他摄影": u"生活服务",

    u"保健/按摩": u"休闲娱乐",
    u"桌面游戏": u"休闲娱乐",
    u"电玩/游戏币": "休闲娱乐",
    u"DIY(陶艺/巧克力/蛋糕/蜡烛)": u"休闲娱乐",
    u"真人CS": u"休闲娱乐",
    u"采摘/钓鱼/自助烧烤": u"休闲娱乐",
    u"动物园/海洋馆/植物园": u"休闲娱乐",
    u"主题公园/游乐园": u"休闲娱乐",
    u"儿童乐园": u"休闲娱乐",
    u"景点": u"休闲娱乐",
    u"水上乐园": u"休闲娱乐",
    u"温泉/洗浴/汗蒸": u"休闲娱乐",
    u"博物馆/美术馆/科技馆": u"休闲娱乐",
    u"展览": u"休闲娱乐",
    u"高空观景": u"休闲娱乐",
    u"单车游/巴士游/游船": u"休闲娱乐",
    u"演唱会": u"休闲娱乐",
    u"体育赛事": u"休闲娱乐",
    u"健身房": u"休闲娱乐",
    u"瑜伽/普拉提/健身操/形体": u"休闲娱乐",
    u"高尔夫": u"休闲娱乐",
    u"保龄球": u"休闲娱乐",
    u"台球": u"休闲娱乐",
    u"羽毛球/乒乓球": u"休闲娱乐",
    u"射箭/射击": u"休闲娱乐",
    u"赛车": u"休闲娱乐",
    u"骑马": u"休闲娱乐",
    u"攀登运动": u"休闲娱乐",
    u"游泳/水上运动": u"休闲娱乐",
    u"滑雪/滑冰": u"休闲娱乐",
    u"篮球/足球": u"休闲娱乐",
    u"其他运动": u"休闲娱乐",
    u"其他休闲娱乐": u"休闲娱乐",
    u"相声": u"休闲娱乐",
    u"其他剧目": u"休闲娱乐",
    u"足疗": u"休闲娱乐",
    u"儿童剧": u"休闲娱乐",
    u"话剧": u"休闲娱乐",
    u"歌舞剧": u"休闲娱乐",
    u"传统戏剧": u"休闲娱乐",
    u"音乐会": u"休闲娱乐",
    u"点播式电影": u"休闲娱乐",
    u"4D/5D电影": u"休闲娱乐",
    u"密室逃脱": u"休闲娱乐",
}


def get_city_code(city_pname):
    """获得对应城的code
        Args:
            city_pname: str,
        Returns:
            code: str, 如果不存在就返回None
    """
    if city_pname not in _city2code:
        return None
    else:
        return _city2code[city_pname]


def build_url(city_qname):
    """根据city_name构建对应的api host
        Args:
            city_qname: str, 城英文名
        Returns:
            url: str, host
    """
    return "%sxiaoqu" % city_qname


def extract_table(elem, text_splits):
    """解析table标签的内容
        Args:
            elem: Element, 节点元素
    """
    if elem is not None:
        tr_elems = elem.xpath("tr")
        for tr_elem in tr_elems:
            text_splits.append(u"-")
            for text in tr_elem.itertext():
                stripped_text = remove_white(text)
                if len(stripped_text) > 0:
                    text_splits.append(u" " + stripped_text)
            text_splits.append(u"N_line")


def extract_deal_menu_summary(elem, text_splits):
    if elem is not None:
        text_splits.append(u"-")
        for text in elem.itertext():
            stripped_text = remove_white(text)
            if len(stripped_text) > 0:
                text_splits.append(u" " + stripped_text)
        text_splits.append(u"N_line")


def extract_list(elem, text_splits):
    if elem is not None:
        for li_elem in elem:
            temps = []
            for text in li_elem.itertext():
                stripped_text = remove_white(text)
                if len(stripped_text) > 0:
                    temps.append(u" " + stripped_text)
            if len(temps) > 0:
                text_splits.append(u"-")
                text_splits.extend(temps)
                text_splits.append(u"N_line")


def item2dict(item):
    """讲item转换层dict
        Args:
            item:Item, item对象
        Returns:
            clone_dict:dict, 字典
    """
    clone_dict = {}
    for key, value in item.__dict__.items():
        if key == "start_time":
            clone_dict['start_time'] = datetime.datetime.fromtimestamp(
                float(value)).strftime("%Y-%m-%d %H:%M:%S")
        elif key == "end_time":
            clone_dict['end_time'] = datetime.datetime.fromtimestamp(
                float(value)).strftime("%Y-%m-%d %H:%M:%S")
        elif key == "deadline":
            clone_dict['deadline'] = datetime.datetime.fromtimestamp(
                float(value)).strftime("%Y-%m-%d %H:%M:%S")
        elif key == "pictures":
            clone_dict['pictures'] = [child_value
                                      if not isinstance(child_value, unicode)
                                      else child_value.encode("utf-8")
                                      for child_value in value]
        elif key == "place":
            temp_value = []
            for place_value in value:
                temp_dict = {}
                for child_key, child_value in place_value.items():
                    if isinstance(child_value, unicode):
                        child_value = child_value.encode("utf-8")
                    if isinstance(child_key, unicode):
                        child_key = child_key.encode("utf-8")
                    temp_dict[child_key] = child_value
                temp_value.append(temp_dict)
            clone_dict['place'] = temp_value
        else:
            clone_dict[key] = value if not isinstance(value, unicode) \
                else value.encode("utf-8")

    return clone_dict
