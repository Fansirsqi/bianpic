import requests
import os
from lxml import etree
from multiprocessing.dummy import Pool
# url = 'https://pic.netbian.com/4kqiche/index.html'
for i in range(1,30):  #爬取1-29页的壁纸
    url = "https://pic.netbian.com/4kfengjing/index_"+str(i)+'.html'
    # 伪装浏览器头部
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    # get请求  获取text
    webPage = requests.get(url,headers = header)
    webPage.encoding='gbk'
    webPage = (webPage.text)

    html = etree.HTML(webPage)   # xpath解析
    href = html.xpath('//*[@id="main"]/div[3]/ul/li')

    urls = []   # 空列表存储数据
    for blank in href:   # 遍历
        src = 'https://pic.netbian.com'+blank.xpath('./a/img/@src')[0]  #图片地址
        title = blank.xpath('./a/b/text()')[0]   # 图片名称
        strc = title +'.jpg'   # 保存jpg格式
        # 拼接到字典中
        dic = {
            'name':strc,
            'url':src
        }
        urls.append(dic)    # 追加到列表中

    def get_src_data(dic):
        url = dic['url']
        stra = dic['name']
        print(stra,'正在下载...')
        data_src = requests.get(url,headers = header)
        # 下载图片内容
        if not os.path.exists('src_img'):  # 没有文件夹，则创建文件夹
            os.mkdir('src_img')
        with open('src_img/'+stra, mode="wb") as f:
            f.write(data_src.content)   # 写入信息二进制
            print(stra,'下载成功！')
    # 使用线程池对图片进行请求
    pool = Pool(20)
    pool.map(get_src_data,urls)
    pool.close()
    pool.join()
print("over!!!")