# -*- coding: UTF-8 -*-
from ping3 import ping

pingtest_name = ['京东商城', '苏宁电器', '国美', '淘宝', '天猫', '亚马逊', '聚划算', '爱淘宝', '网易考拉', '网易严选', '阿里云', '优酷', '爱奇艺', '腾讯视频', '芒果TV', '乐视视频', '搜狐视频', '哔哩哔哩', '土豆网', 'CCTV', '斗鱼直播', '虎牙直播', 'YY直播', '企鹅电竞', '企鹅直播', '直播吧', '花椒直播', '战旗直播', '龙珠直播', '凤凰网', '环球网', '澎湃新闻', '腾讯新闻', '新浪新闻', '搜狐新闻', '网易新闻', '观察者', '军事头条', '中华网军事', '铁血军事', '腾讯军事', '人民网军事', '米尔网', '新浪军事', '环球军事', '凤凰军事', '东方财富', '新浪财经', '和讯财经', '第一财经', '财新网', '中国经济网', '网易财经', '证券之星', '雪球财经', '新浪微博', '知乎', '豆瓣', '百度贴吧', 'LOFTER', '水木社区', '天涯社区', '猫扑网', 'Dribbble', 'Iconfont', 'Easyicon', '花瓣网', '摄图网', '包图网', '网易云音乐', 'QQ音乐', '酷狗音乐', '荔枝FM', '蜻蜓FM', '酷我音乐', '虾米音乐', '喜马拉雅', '豆瓣FM', '携程网', '飞猪旅行', '马蜂窝', '途牛', '穷游网', '驴妈妈', '同程网', '去哪儿', 'NBA', 'CCTV5', '网易体育', '直播吧', '懂球帝', '虎扑体育', '新浪体育', '腾讯体育', '搜狐体育', '汽车之家', '太平洋汽车', '易车网', '人人车', '优信二手车', '瓜子二手车', '爱卡汽车', '车辆违章查询', '汽车用品', '哔哩哔哩', 'M站', '腾讯动漫', '网易漫画', '半次元', '有妖气', '中关村在线', '太平洋电脑', 'Engadget中国', 'IT之家', 'ZEALER', '数字尾巴', 'Chiphell', '苏宁数码', '京东数码', '开源中国', 'Segmentfault', 'v2ex', 'CSDN', '博客园', '开发者头条', '掘金', '智联招聘', '拉勾网', 'BOSS直聘', '前程无忧', '猎聘网', '100offer', '内推网']
pingtest_address = ['jd.com', 'suning.com', 'gome.com.cn', 'taobao.com', 'tmall.com', 'amazon.cn', 's.click.taobao.com', 'ai.taobao.com', 'kaola.com', 'you.163.com', 'aliyun.com', 'youku.com', 'iqiyi.com', 'v.qq.com', 'mgtv.com', 'le.com', 'tv.sohu.com', 'bilibili.com', 'tudou.com', 'tv.cctv.com', 'douyu.com', 'huya.com', 'yy.com', 'egame.qq.com', 'live.qq.com', 'zhibo8.cc', 'huajiao.com', 'zhanqi.tv', 'longzhu.com', 'ifeng.com', 'huanqiu.com', 'thepaper.cn', 'news.qq.com', 'news.sina.com.cn', 'news.sohu.com', 'news.163.com', 'guancha.cn', 'mil.eastday.com', 'military.china.com', 'tiexue.net', 'new.qq.com', 'military.people.com.cn', 'miercn.com', 'mil.news.sina.com.cn', 'mil.huanqiu.com', 'news.ifeng.com', 'eastmoney.com', 'finance.sina.com.cn', 'hexun.com', 'yicai.com', 'caixin.com', 'ce.cn', 'money.163.com', 'stockstar.com', 'xueqiu.com', 'weibo.com', 'zhihu.com', 'douban.com', 'tieba.baidu.com', 'lofter.com', 'newsmth.net', 'focus.tianya.cn', 'mop.com', 'dribbble.com', 'iconfont.cn', 'easyicon.net', 'huaban.com', '699pic.com', 'ibaotu.com', 'music.163.com', 'y.qq.com', 'kugou.com', 'lizhi.fm', 'qingting.fm', 'kuwo.cn', 'xiami.com', 'ximalaya.com', 'douban.fm', 'ctrip.com', 'fliggy.com', 'mafengwo.cn', 'tuniu.com', 'qyer.com', 'lvmama.com', 'ly.com', 'qunar.com', 'china.nba.com', 'sports.cctv.com', 'sports.163.com', 'zhibo8.cc', 'dongqiudi.com', 'hupu.com', 'sports.sina.com.cn', 'sports.qq.com', 'sports.sohu.com', 'autohome.com.cn', 'pcauto.com.cn', 'yiche.com', 'renrenche.com', 'xin.com', 'guazi.com', 'xcar.com.cn', 'nkg.122.gov.cn', 'che.jd.com', 'bilibili.com', 'missevan.com', 'ac.qq.com', 'manhua.163.com', 'bcy.net', 'u17.com', 'zol.com.cn', 'pconline.com.cn', 'cn.engadget.com', 'ithome.com', 'zealer.com', 'dgtle.com', 'chiphell.com', 'suning.com', 'shuma.jd.com', 'oschina.net', 'segmentfault.com', 'v2ex.com', 'csdn.net', 'cnblogs.com', 'toutiao.io', 'juejin.im', 'zhaopin.com', 'lagou.com', 'zhipin.com', '51job.com', 'liepin.com', 'cn.100offer.com', 'neitui.me']
time_delay=[]
name_address={}
def ping_host(ip):
    """
    获取节点的延迟的作用
    :param node:
    :return:
    """
    ip_address = ip
    response = ping(ip_address, unit='ms')

    return response


# with open('net_address.txt', 'r') as f:
#     for line in f:
#         total = 0
#         times_avg = 0
#         print(line.replace('\n',''))
#         for i in range(0, 5):
#             try:
#                 line.strip()
#                 delay = ping_host(line.replace('\n',''))
#                 total = delay + total
#                 times_avg = times_avg + 1
#             except TypeError:
#                 pass
#         try:
#             time_delay.append(str(round(total/times_avg, 2)))
#             name_address[line.replace('\n','')]=str(round(total/times_avg, 2))
#             print(str(round(total/times_avg, 2)))
#         except ZeroDivisionError:
#             time_delay.append('-1')
#             name_address[line.replace('\n','')]='-1'


for address in pingtest_address:
    total = 0
    times_avg = 0
    print(address.replace('\n',''))
    for i in range(0, 5):
        try:
            address.strip()
            delay = ping_host(address.replace('\n',''))
            total = delay + total
            times_avg = times_avg + 1
        except TypeError:
            pass
    try:
        time_delay.append(str(round(total/times_avg, 2)))
        name_address[address.replace('\n','')]=str(round(total/times_avg, 2))
        print(str(round(total/times_avg, 2)))
    except ZeroDivisionError:
        time_delay.append('-1')
        name_address[address.replace('\n','')]='-1'


print(time_delay)



def gen_markdown_table_2d(head_name, rows_name, cols_name, data):
    """
    Params:
        head_name: {str} 表头名， 如"count\比例"
        rows_name, cols_name: {list[str]} 项目名， 如 1,2,3
        data: {ndarray(H, W)}

    Returns:
        table: {str}
    """
    ELEMENT = " {} |"

    H, W = data.shape
    LINE = "|" + ELEMENT * W

    lines = []

    ## 表头部分
    lines += ["| {} | {} |".format(head_name, ' | '.join(cols_name))]

    ## 分割线
    SPLIT = "{}:"
    line = "| {} |".format(SPLIT.format('-'*len(head_name)))
    for i in range(W):
        line = "{} {} |".format(line, SPLIT.format('-'*len(cols_name[i])))
    lines += [line]

    ## 数据部分
    for i in range(H):
        d = list(map(str, list(data[i])))
        lines += ["| {} | {} |".format(rows_name[i], ' | '.join(d))]

    table = '\n'.join(lines)
    return table
