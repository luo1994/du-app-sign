var t62 = {
    rotl: function (n, e) {
        return n << e | n >>> 32 - e
    },
    rotr: function (n, e) {
        return n << 32 - e | n >>> e
    },
    endian: function (n) {
        if (n.constructor == Number)
            return 16711935 & t62.rotl(n, 8) | 4278255360 & t62.rotl(n, 24);
        for (var e = 0; e < n.length; e++)
            n[e] = t62.endian(n[e]);
        return n
    },
    randomBytes: function (n) {
        for (var e = []; n > 0; n--)
            e.push(Math.floor(256 * Math.random()));
        return e
    },
    bytesToWords: function (n) {
        for (var e = [], t = 0, i = 0; t < n.length; t++,
            i += 8)
            e[i >>> 5] |= n[t] << 24 - i % 32;
        return e
    },
    wordsToBytes: function (n) {
        for (var e = [], t = 0; t < 32 * n.length; t += 8)
            e.push(n[t >>> 5] >>> 24 - t % 32 & 255);
        return e
    },
    bytesToHex: function (n) {
        for (var e = [], t = 0; t < n.length; t++)
            e.push((n[t] >>> 4).toString(16)),
                e.push((15 & n[t]).toString(16));
        return e.join("")
    },
    hexToBytes: function (n) {
        for (var e = [], t = 0; t < n.length; t += 2)
            e.push(parseInt(n.substr(t, 2), 16));
        return e
    },
    bytesToBase64: function (n) {
        for (var t = [], i = 0; i < n.length; i += 3)
            for (var o = n[i] << 16 | n[i + 1] << 8 | n[i + 2], r = 0; r < 4; r++)
                8 * i + 6 * r <= 8 * n.length ? t.push(e.charAt(o >>> 6 * (3 - r) & 63)) : t.push("=");
        return t.join("")
    },
    base64ToBytes: function (n) {
        n = n.replace(/[^A-Z0-9+\/]/gi, "");
        for (var t = [], i = 0, o = 0; i < n.length; o = ++i % 4)
            0 != o && t.push((e.indexOf(n.charAt(i - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | e.indexOf(n.charAt(i)) >>> 6 - 2 * o);
        return t
    }
};
var t31 = {
    utf8: {
        stringToBytes: function (n) {
            return t31.bin.stringToBytes(unescape(encodeURIComponent(n)))
        },
        bytesToString: function (n) {
            return decodeURIComponent(escape(t.bin.bytesToString(n)))
        }
    },
    bin: {
        stringToBytes: function (n) {
            for (var e = [], t = 0; t < n.length; t++)
                e.push(255 & n.charCodeAt(t));
            return e
        },
        bytesToString: function (n) {
            for (var e = [], t = 0; t < n.length; t++)
                e.push(String.fromCharCode(n[t]));
            return e.join("")
        }
    }
};
var t57 = {
    t: function (n) {
        return !!n.constructor && "function" == typeof n.constructor.isBuffer && n.constructor.isBuffer(n)
    },
    i: function (n) {
        return "function" == typeof n.readFloatLE && "function" == typeof n.slice && t(n.slice(0, 0))
    }

    /*!
* Determine if an object is a Buffer
*
* @author   Feross Aboukhadijeh <https://feross.org>
* @license  MIT
*/
};


function getSign(n, e, t) {
    var e = t62
        , i = t31.utf8
        , o = t57
        , r = t31.bin
        , a = function (n, t) {
        n.constructor == String ? n = t && "binary" === t.encoding ? r.stringToBytes(n) : i.stringToBytes(n) : o(n) ? n = Array.prototype.slice.call(n, 0) : Array.isArray(n) || (n = n.toString());
        for (var s = e.bytesToWords(n), l = 8 * n.length, c = 1732584193, d = -271733879, A = -1732584194, p = 271733878, u = 0; u < s.length; u++)
            s[u] = 16711935 & (s[u] << 8 | s[u] >>> 24) | 4278255360 & (s[u] << 24 | s[u] >>> 8);
        s[l >>> 5] |= 128 << l % 32,
            s[14 + (l + 64 >>> 9 << 4)] = l;
        for (var h = a._ff, f = a._gg, g = a._hh, m = a._ii, u = 0; u < s.length; u += 16) {
            var C = c
                , v = d
                , b = A
                , B = p;
            c = h(c, d, A, p, s[u + 0], 7, -680876936),
                p = h(p, c, d, A, s[u + 1], 12, -389564586),
                A = h(A, p, c, d, s[u + 2], 17, 606105819),
                d = h(d, A, p, c, s[u + 3], 22, -1044525330),
                c = h(c, d, A, p, s[u + 4], 7, -176418897),
                p = h(p, c, d, A, s[u + 5], 12, 1200080426),
                A = h(A, p, c, d, s[u + 6], 17, -1473231341),
                d = h(d, A, p, c, s[u + 7], 22, -45705983),
                c = h(c, d, A, p, s[u + 8], 7, 1770035416),
                p = h(p, c, d, A, s[u + 9], 12, -1958414417),
                A = h(A, p, c, d, s[u + 10], 17, -42063),
                d = h(d, A, p, c, s[u + 11], 22, -1990404162),
                c = h(c, d, A, p, s[u + 12], 7, 1804603682),
                p = h(p, c, d, A, s[u + 13], 12, -40341101),
                A = h(A, p, c, d, s[u + 14], 17, -1502002290),
                d = h(d, A, p, c, s[u + 15], 22, 1236535329),
                c = f(c, d, A, p, s[u + 1], 5, -165796510),
                p = f(p, c, d, A, s[u + 6], 9, -1069501632),
                A = f(A, p, c, d, s[u + 11], 14, 643717713),
                d = f(d, A, p, c, s[u + 0], 20, -373897302),
                c = f(c, d, A, p, s[u + 5], 5, -701558691),
                p = f(p, c, d, A, s[u + 10], 9, 38016083),
                A = f(A, p, c, d, s[u + 15], 14, -660478335),
                d = f(d, A, p, c, s[u + 4], 20, -405537848),
                c = f(c, d, A, p, s[u + 9], 5, 568446438),
                p = f(p, c, d, A, s[u + 14], 9, -1019803690),
                A = f(A, p, c, d, s[u + 3], 14, -187363961),
                d = f(d, A, p, c, s[u + 8], 20, 1163531501),
                c = f(c, d, A, p, s[u + 13], 5, -1444681467),
                p = f(p, c, d, A, s[u + 2], 9, -51403784),
                A = f(A, p, c, d, s[u + 7], 14, 1735328473),
                d = f(d, A, p, c, s[u + 12], 20, -1926607734),
                c = g(c, d, A, p, s[u + 5], 4, -378558),
                p = g(p, c, d, A, s[u + 8], 11, -2022574463),
                A = g(A, p, c, d, s[u + 11], 16, 1839030562),
                d = g(d, A, p, c, s[u + 14], 23, -35309556),
                c = g(c, d, A, p, s[u + 1], 4, -1530992060),
                p = g(p, c, d, A, s[u + 4], 11, 1272893353),
                A = g(A, p, c, d, s[u + 7], 16, -155497632),
                d = g(d, A, p, c, s[u + 10], 23, -1094730640),
                c = g(c, d, A, p, s[u + 13], 4, 681279174),
                p = g(p, c, d, A, s[u + 0], 11, -358537222),
                A = g(A, p, c, d, s[u + 3], 16, -722521979),
                d = g(d, A, p, c, s[u + 6], 23, 76029189),
                c = g(c, d, A, p, s[u + 9], 4, -640364487),
                p = g(p, c, d, A, s[u + 12], 11, -421815835),
                A = g(A, p, c, d, s[u + 15], 16, 530742520),
                d = g(d, A, p, c, s[u + 2], 23, -995338651),
                c = m(c, d, A, p, s[u + 0], 6, -198630844),
                p = m(p, c, d, A, s[u + 7], 10, 1126891415),
                A = m(A, p, c, d, s[u + 14], 15, -1416354905),
                d = m(d, A, p, c, s[u + 5], 21, -57434055),
                c = m(c, d, A, p, s[u + 12], 6, 1700485571),
                p = m(p, c, d, A, s[u + 3], 10, -1894986606),
                A = m(A, p, c, d, s[u + 10], 15, -1051523),
                d = m(d, A, p, c, s[u + 1], 21, -2054922799),
                c = m(c, d, A, p, s[u + 8], 6, 1873313359),
                p = m(p, c, d, A, s[u + 15], 10, -30611744),
                A = m(A, p, c, d, s[u + 6], 15, -1560198380),
                d = m(d, A, p, c, s[u + 13], 21, 1309151649),
                c = m(c, d, A, p, s[u + 4], 6, -145523070),
                p = m(p, c, d, A, s[u + 11], 10, -1120210379),
                A = m(A, p, c, d, s[u + 2], 15, 718787259),
                d = m(d, A, p, c, s[u + 9], 21, -343485551),
                c = c + C >>> 0,
                d = d + v >>> 0,
                A = A + b >>> 0,
                p = p + B >>> 0
        }
        return e.endian([c, d, A, p])
    };
    a._ff = function (n, e, t, i, o, r, a) {
        var s = n + (e & t | ~e & i) + (o >>> 0) + a;
        return (s << r | s >>> 32 - r) + e
    }
        ,
        a._gg = function (n, e, t, i, o, r, a) {
            var s = n + (e & i | t & ~i) + (o >>> 0) + a;
            return (s << r | s >>> 32 - r) + e
        }
        ,
        a._hh = function (n, e, t, i, o, r, a) {
            var s = n + (e ^ t ^ i) + (o >>> 0) + a;
            return (s << r | s >>> 32 - r) + e
        }
        ,
        a._ii = function (n, e, t, i, o, r, a) {
            var s = n + (t ^ (e | ~i)) + (o >>> 0) + a;
            return (s << r | s >>> 32 - r) + e
        }
        ,
        a._blocksize = 16,
        a._digestsize = 16;
    var i = e.wordsToBytes(a(n, t));
    var result = e.bytesToHex(i);
    return result
}

