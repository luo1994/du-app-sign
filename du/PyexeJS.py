import execjs

def get_brand_list_url(brand_id, page):
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        sign = ctx.call('getSign', 'lastId{}recommendId{}048a9c4943398714b356a696503d2d36'.format(page, brand_id))
        url = 'https://m.poizon.com/mapi/product/recommendDetail?recommendId={}&lastId={}&sign={}'.format(brand_id, page,sign)
        return url

def get_product_url(product_id):
    with open('sign.js', 'r', encoding='utf-8')as f:
        all_ = f.read()
        ctx = execjs.compile(all_)
        sign = ctx.call('getSign', 'productId{}sourceshareDetail048a9c4943398714b356a696503d2d36'.format(product_id))
        product_url = 'https://m.poizon.com/mapi/product/detail?productId={}&source=shareDetail&sign={}'.format(product_id, sign)
        return product_url


if __name__ == '__main__':
    brand_list_url = get_brand_list_url(73, 2)
    product_url = get_product_url(18570)
    print(brand_list_url)
    print(product_url)


