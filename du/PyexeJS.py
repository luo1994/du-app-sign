import execjs
import requests

headers = {
    'Host': "app.poizon.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI "
                  "MiniProgramEnv/Windows WindowsWechat",
    'appid': "wxapp",
    'appversion': "4.4.0",
    'content-type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "gzip, deflate",
    'Accept': "*/*",
}


def get_recensales_list_url(lastId, productId):
    # 最近购买接口
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        sign = ctx.call('getSign',
                        'lastId{}limit20productId{}sourceAppapp19bc545a393a25177083d4a748807cc0'.format(lastId,
                                                                                                        productId))
        recensales_list_url = 'https://app.poizon.com/api/v1/h5/product/fire/recentSoldList?' \
                              'productId={}&lastId={}&limit=20&sourceApp=app&sign={}'.format(productId, lastId, sign)
        return recensales_list_url


def get_search_by_keywords_url(page, sortMode, sortType):
    # 关键词搜索商品接口
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        # 53489
        sign = ctx.call('getSign',
                        'limit20page{}sortMode{}sortType{}titleajunionId19bc545a393a25177083d4a748807cc0'.format(page,
                                                                                                                 sortMode,
                                                                                                                 sortType))
        search_by_keywords_url = 'https://app.poizon.com/api/v1/h5/product/fire/search/list?title=aj&page={}&sortType={}&sortMode={}&' \
                                 'limit=20&unionId=&sign={}'.format(page, sortType, sortMode, sign)
        return search_by_keywords_url


def get_brand_list_url(lastId, tabId):
    # 商品品类列表接口
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        sign = ctx.call('getSign',
                        'lastId{}limit20tabId{}19bc545a393a25177083d4a748807cc0'.format(lastId, tabId))
        brand_list_url = 'https://app.poizon.com/api/v1/h5/index/fire/shoppingTab?' \
                         'tabId={}&limit=20&lastId={}&sign={}'.format(tabId, lastId, sign)
        return brand_list_url


def get_product_detail_url(productId):
    # 商品详情接口
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        sign = ctx.call('getSign',
                        'productId{}productSourceNamewx19bc545a393a25177083d4a748807cc0'.format(productId))
        product_detail_url = 'https://app.poizon.com/api/v1/h5/index/fire/flow/product/detail?' \
                             'productId={}&productSourceName=wx&sign={}'.format(productId, sign)
        return product_detail_url


recensales_list_url = get_recensales_list_url(0, 40755)
search_by_keywords_url = get_search_by_keywords_url(0, 1, 0)
brand_list_url = get_brand_list_url(1, 4)
product_detail_url = get_product_detail_url(53489)
recensales_list_response = requests.get(url=recensales_list_url, headers=headers)
search_by_keywords_response = requests.get(url=search_by_keywords_url, headers=headers)
brand_list_response = requests.get(url=brand_list_url, headers=headers)
product_detail_response = requests.get(url=product_detail_url, headers=headers)
print(recensales_list_response.text)
print(search_by_keywords_response.text)
print(brand_list_response.text)
print(product_detail_response.text)
