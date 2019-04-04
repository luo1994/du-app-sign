"""
    python 位左移问题

    参考: https://blog.csdn.net/pzqingchong/article/details/77991187
     from https://github.com/onetwo1/du-app
"""

import os
import execjs
import requests
from urllib.parse import quote, unquote


# url = "https://m.poizon.com/mapi/product/recommendDetail?recommendId=73&lastId=&sign=555e33ce226ab7acbf4b006d00378f63"
url = "https://m.poizon.com/mapi/product/recommendDetail?recommendId=73&lastId=&sign={}"

"""编译的 js 左移函数"""
exec_js_func = execjs.compile("function get_num(expression){return eval(expression)}")


def call_exec_js(expression):
    """res = fun.call("get_num", 128, 408)"""
    return exec_js_func.call("get_num", expression)


def exec_shell_command(command):
    """
        python 左移问题解决, 使用 shell 脚本, 但是注意 shell 执行结果是不带符号的.....
        为了简单,只用来处理左移, 比如 exec_shell_command("echo $[128 << 408]")
    """
    result = os.popen(command).read().strip()
    print(result)
    return int(result)


def get_sign_string(params: dict):
    """
        ::param {recommendId: "73", lastId: ""}
    """
    sign_string = ''
    sort_params = {k: params[k] for k in sorted(params.keys())}
    for k, v in sort_params.items():
        sign_string += k + v
    sign_string += "048a9c4943398714b356a696503d2d36"
    return sign_string


def rotl(e, n):
    return e << n | e >> 32 - n


def endian(e):
    if isinstance(e, int):
        return 16711935 & rotl(e, 8) | 4278255360 & rotl(e, 24)
    for n in range(len(e)):
        e[n] = endian(e[n])
    return e


def bytesToWords(e):
    n = [0 for i in range(len(e))]
    r = 0
    for t in range(len(e)):
        n[r >> 5] |= (e[t] << 24 - r % 32)
        r += 8
    n = [i for i in n if i != 0]
    return n


def bytesToHex(e):
    n = []

    for t in range(len(e)):
        n.append(hex(e[t] >> 4)[-1])
        n.append(hex(15 & e[t])[-1])
    return "".join(n)


def wordsToBytes(e):
    n = []
    for t in range(0, 32*len(e), 8):
        n.append(e[t >> 5] >> 24 - t % 32 & 255)
    return n


def utf8_StringToBytes(e):
    return bin_StringToBytes(unquote(quote(e)))


def bin_StringToBytes(e: str):
    n = []
    for t in range(len(e)):
        n.append(255 & ord(e[t]))
    return n


def bin_bytesToString(e: list):
    n = []
    for t in range(len(e)):
        n.append(chr(e[t]))
    return "".join(n)


class A(object):

    @staticmethod
    def ff(e, n, t, r, o, i, a):
        s = e + (n & t | ~n & r) + (o >> 0) + a
        # command = f"echo $[({s} << {i} | {s} >> 32 - {i}) + {n}]"
        return call_exec_js(f"({s} << {i} | {s} >>> 32 - {i}) + {n}")
        # return (call_exec_js(s, i) | s >> 32 - i) + n
        # return execjs.eval(f"({s} << {i} | {s} >> 32 - {i}) + {n}")

    @staticmethod
    def gg(e, n, t, r, o, i, a):
        s = e + (n & r | t & ~r) + (o >> 0) + a
        return call_exec_js(f"({s} << {i} | {s} >>> 32 - {i}) + {n}")

    @staticmethod
    def hh(e, n, t, r, o, i, a):
        s = e + (n ^ t ^ r) + (o >> 0) + a
        return call_exec_js(f"({s} << {i} | {s} >>> 32 - {i}) + {n}")

    @staticmethod
    def ii(e, n, t, r, o, i, a):
        s = e + (t ^ (n | ~r)) + (o >> 0) + a
        return call_exec_js(f"({s} << {i} | {s} >>> 32 - {i}) + {n}")


def func(e):
    e = utf8_StringToBytes(e)
    s = bytesToWords(e)
    c = 8 * len(e)
    u = 1732584193
    l = -271733879
    d = -1732584194
    f = 271733878
    for p in range(len(s)):
        s[p] = 16711935 & (s[p] << 8 | s[p] >> 24) | 4278255360 & (s[p] << 24 | s[p] >> 8)
    # s[c >> 5] |= execjs.eval(f"128 << {c} % 32")
    s[c >> 5] |= call_exec_js(f"128 << {c} % 32")
    s.append(0)
    s.append(c)
    a = A()
    h = a.ff
    m = a.gg
    v = a.hh
    g = a.ii
    for p in range(len(s)):
        _A = u
        y = l
        b = d
        _C = f
        u = h(u, l, d, f, s[p + 0], 7, -680876936)
        f = h(f, u, l, d, s[p + 1], 12, -389564586)
        d = h(d, f, u, l, s[p + 2], 17, 606105819)
        l = h(l, d, f, u, s[p + 3], 22, -1044525330)
        u = h(u, l, d, f, s[p + 4], 7, -176418897)
        f = h(f, u, l, d, s[p + 5], 12, 1200080426)
        d = h(d, f, u, l, s[p + 6], 17, -1473231341)
        l = h(l, d, f, u, s[p + 7], 22, -45705983)
        u = h(u, l, d, f, s[p + 8], 7, 1770035416)
        f = h(f, u, l, d, s[p + 9], 12, -1958414417)
        d = h(d, f, u, l, s[p + 10], 17, -42063)
        l = h(l, d, f, u, s[p + 11], 22, -1990404162)
        u = h(u, l, d, f, s[p + 12], 7, 1804603682)
        f = h(f, u, l, d, s[p + 13], 12, -40341101)
        d = h(d, f, u, l, s[p + 14], 17, -1502002290)
        l = h(l, d, f, u, 0, 22, 1236535329)
        u = m(u, l, d, f, s[p + 1], 5, -165796510)
        f = m(f, u, l, d, s[p + 6], 9, -1069501632)
        d = m(d, f, u, l, s[p + 11], 14, 643717713)
        l = m(l, d, f, u, s[p + 0], 20, -373897302)
        u = m(u, l, d, f, s[p + 5], 5, -701558691)
        f = m(f, u, l, d, s[p + 10], 9, 38016083)
        d = m(d, f, u, l, 0, 14, -660478335)
        l = m(l, d, f, u, s[p + 4], 20, -405537848)
        u = m(u, l, d, f, s[p + 9], 5, 568446438)
        f = m(f, u, l, d, s[p + 14], 9, -1019803690)
        d = m(d, f, u, l, s[p + 3], 14, -187363961)
        l = m(l, d, f, u, s[p + 8], 20, 1163531501)
        u = m(u, l, d, f, s[p + 13], 5, -1444681467)
        f = m(f, u, l, d, s[p + 2], 9, -51403784)
        d = m(d, f, u, l, s[p + 7], 14, 1735328473)
        l = m(l, d, f, u, s[p + 12], 20, -1926607734)
        u = v(u, l, d, f, s[p + 5], 4, -378558)
        f = v(f, u, l, d, s[p + 8], 11, -2022574463)
        d = v(d, f, u, l, s[p + 11], 16, 1839030562)
        l = v(l, d, f, u, s[p + 14], 23, -35309556)
        u = v(u, l, d, f, s[p + 1], 4, -1530992060)
        f = v(f, u, l, d, s[p + 4], 11, 1272893353)
        d = v(d, f, u, l, s[p + 7], 16, -155497632)
        l = v(l, d, f, u, s[p + 10], 23, -1094730640)
        u = v(u, l, d, f, s[p + 13], 4, 681279174)
        f = v(f, u, l, d, s[p + 0], 11, -358537222)
        d = v(d, f, u, l, s[p + 3], 16, -722521979)
        l = v(l, d, f, u, s[p + 6], 23, 76029189)
        u = v(u, l, d, f, s[p + 9], 4, -640364487)
        f = v(f, u, l, d, s[p + 12], 11, -421815835)
        d = v(d, f, u, l, 0, 16, 530742520)
        l = v(l, d, f, u, s[p + 2], 23, -995338651)
        u = g(u, l, d, f, s[p + 0], 6, -198630844)
        f = g(f, u, l, d, s[p + 7], 10, 1126891415)
        d = g(d, f, u, l, s[p + 14], 15, -1416354905)
        l = g(l, d, f, u, s[p + 5], 21, -57434055)
        u = g(u, l, d, f, s[p + 12], 6, 1700485571)
        f = g(f, u, l, d, s[p + 3], 10, -1894986606)
        d = g(d, f, u, l, s[p + 10], 15, -1051523)
        l = g(l, d, f, u, s[p + 1], 21, -2054922799)
        u = g(u, l, d, f, s[p + 8], 6, 1873313359)
        f = g(f, u, l, d, 0, 10, -30611744)
        d = g(d, f, u, l, s[p + 6], 15, -1560198380)
        l = g(l, d, f, u, s[p + 13], 21, 1309151649)
        u = g(u, l, d, f, s[p + 4], 6, -145523070)
        f = g(f, u, l, d, s[p + 11], 10, -1120210379)
        d = g(d, f, u, l, s[p + 2], 15, 718787259)
        l = g(l, d, f, u, s[p + 9], 21, -343485551)
        u = call_exec_js(f"{u} + {_A} >>> 0")
        l = call_exec_js(f"{l} + {y} >>> 0")
        d = call_exec_js(f"{d} + {b} >>> 0")
        f = call_exec_js(f"{f} + {_C} >>> 0")
        p += 16
        break
    r = wordsToBytes(endian([u, l, d, f]))
    return bytesToHex(r)


if __name__ == '__main__':
    si = get_sign_string({"recommendId": "73", "lastId": ""})
    sign = func(si)
    res = requests.get(url.format(sign))
    print(res.status_code)
