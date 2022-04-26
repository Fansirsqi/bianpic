import requests
import re
import os
import color

# def list_how():

    # index_page = requests.get(url="https://pic.netbian.com/", headers=headers).content.decode('gbk')
    # t_list = re.findall(r'title=\"4K(.*?)图片', index_page, re.S)
    # index_page_2 = re.findall(r'<div class=\"nav-m clearfix tran\">.*?</div>', index_page, re.S)
    # for index_page_x in index_page_2:  # 获取壁纸分类链接
    #     u_list = re.findall(r'<a href=.*?href=\"/(.*?)/\" title=.*?</a>', index_page_x, re.S)
    #     print(u_list)
    #     # for i in u_list:
    #     #     print('https://pic.netbian.com/' + i + '/')  # 第二页则/index_2.html
    # print(t_list)
    #
    # # print(index_page)
    # # [print(i) for i in t_list]
    # # print('------------')


def down_img(se):
    i =howPageDown()
    url = 'https://pic.netbian.com'+se+i
    print(url)
    if i !='':
        p = re.findall('\d+',i)
        p= se+p[0]+'/'
        mkd(p)
    else:
        p = se +  '1/'
        mkd(p)
    page_text = requests.get(url=url, headers=headers).content.decode('gbk')
    link = re.findall(r'<li><a href=\"/tupian/(.*?)\" target=\"_blank\"><img src=', page_text, re.S)
    start_url = "https://pic.netbian.com/tupian/"
    for true_url in link:
        link_1 = start_url + true_url
        in_page = requests.get(url=link_1, headers=headers).content.decode('gbk')
        title = re.findall('class=\"photo-hd\"><h1>(.*?)</h1>', in_page)
        t_link = re.findall(r'id=\"img\"><img src=\"/(.*?).jpg', in_page)
        l_link = "https://pic.netbian.com/" + t_link[0] + '.jpg'
        img_data = requests.get(url=l_link, headers=headers).content
        path = '.'+p + title[0] + '.jpg'
        with open(path, 'wb') as img:
            img.write(img_data)
            print(title[0] + '  ---  完成！')
    print('\n\n===================\n\n')
    print('是否继续进行下载？')
    print('1.是 2.否')
    ifGoOn = int(input('请输入:\t'))
    if ifGoOn==2:
        exit()
    else:
        return se_a()

def select_a():
    print('    =======================================')
    print('''
        1.风景    4.动漫    7.动物    10.宗教
        2.美女    5.影视    8.人物    11.手机壁纸
        3.游戏    6.汽车    9.美食
        ''')
    print('    =======================================')
    how = int(input('请输入对应序号\n:'))
    print(how, type(how))
    if how == 1:
        print('选择了风景')
        href = '/4kfengjing/'
        down_img(href)
    elif how == 2:
        print('选择了美女')
        href = '/4kmeinv/'
    elif how == 3:
        print('选择了游戏')
        href = "/4kyouxi/"
    elif how == 4:
        print('选择了动漫')
        href = "/4kdongman/"
    elif how == 5:
        print('选择了影视')
        href = "/4kyingshi/"
    elif how == 6:
        print('选择了汽车')
        href = "/4kqiche/"
    elif how == 7:
        print('选择了动物')
        href = "/4kdongwu/"
    elif how == 8:
        print('选择了人物')
        href = "/4krenwu/"
    elif how == 9:
        print('选择了美食')
        href = "/4kmeishi/"
    elif how == 10:
        print('选择了宗教')
        href = "/4kzongjiao/"
    elif how == 11:
        print('选择了手机壁纸')
        href = "/shoujibizhi/"
    else:
        print('输入不符合要求')

def se_a():
    print('    =======================================')
    print('''
    1.风景    4.动漫    7.动物    10.宗教
    2.美女    5.影视    8.人物    11.手机壁纸
    3.游戏    6.汽车    9.美食
            ''')
    print('    =======================================')
    i = int(input('请输入对应序号\t:'))
    num = {
        1: '/4kfengjing/',
        2: '/4kmeinv/',
        3: "/4kyouxi/",
        4: "/4kdongman/",
        5: "/4kyingshi/",
        6: "/4kqiche/",
        7: "/4kdongwu/",
        8: "/4krenwu/",
        9: "/4kmeishi/",
        10: "/4kzongjiao/",
        11: "/shoujibizhi/"
    }
    lasturl = num.get(i,'输入有误')
    down_img(lasturl)
    return lasturl

def howPageDown():
    print('请问要下载第几页？')
    how_page = int(input("输入页码:\t"))
    if how_page == 1:
        print('下载该分类首页')
        return ''
    else:
        print('下载第' + str(how_page) + '页')
        i = 'index_'+str(how_page)+'.html'
        return i

def mkd(path):
    path='.'+path
    if not os.path.exists(path):
     os.makedirs(path)

if __name__ == '__main__':
    color.printBlueWhite()
    os.system('title 彼岸图网页图片下载 By 依旧归七')
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"}
    se_a()