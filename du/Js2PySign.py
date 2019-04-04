__all__ = ['sign']
# from https://github.com/XuCcc/DuTracker
# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['getSign', 't57', 't31', 't62'])
@Js
def PyJsHoisted_getSign_(n, e, t, this, arguments, var=var):
    var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'result', 'n', 'r', 'a', 't', 'e', 'o'])
    var.put('e', var.get('t62'))
    var.put('i', var.get('t31').get('utf8'))
    var.put('o', var.get('t57'))
    var.put('r', var.get('t31').get('bin'))
    @Js
    def PyJs_anonymous_21_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['d', 'C', 'b', 'p', 'm', 'B', 'h', 'g', 's', 'v', 'n', 't', 'l', 'f', 'c', 'A', 'u'])
        def PyJs_LONG_22_(var=var):
            return (var.put('n', (var.get('r').callprop('stringToBytes', var.get('n')) if (var.get('t') and PyJsStrictEq(Js('binary'),var.get('t').get('encoding'))) else var.get('i').callprop('stringToBytes', var.get('n')))) if (var.get('n').get('constructor')==var.get('String')) else (var.put('n', var.get('Array').get('prototype').get('slice').callprop('call', var.get('n'), Js(0.0))) if var.get('o')(var.get('n')) else (var.get('Array').callprop('isArray', var.get('n')) or var.put('n', var.get('n').callprop('toString')))))
        PyJs_LONG_22_()
        #for JS loop
        var.put('s', var.get('e').callprop('bytesToWords', var.get('n')))
        var.put('l', (Js(8.0)*var.get('n').get('length')))
        var.put('c', Js(1732584193.0))
        var.put('d', (-Js(271733879.0)))
        var.put('A', (-Js(1732584194.0)))
        var.put('p', Js(271733878.0))
        var.put('u', Js(0.0))
        while (var.get('u')<var.get('s').get('length')):
            try:
                var.get('s').put(var.get('u'), ((Js(16711935.0)&((var.get('s').get(var.get('u'))<<Js(8.0))|PyJsBshift(var.get('s').get(var.get('u')),Js(24.0))))|(Js(4278255360.0)&((var.get('s').get(var.get('u'))<<Js(24.0))|PyJsBshift(var.get('s').get(var.get('u')),Js(8.0))))))
            finally:
                    (var.put('u',Js(var.get('u').to_number())+Js(1))-Js(1))
        PyJsComma(var.get('s').put(PyJsBshift(var.get('l'),Js(5.0)), (Js(128.0)<<(var.get('l')%Js(32.0))), '|'),var.get('s').put((Js(14.0)+(PyJsBshift((var.get('l')+Js(64.0)),Js(9.0))<<Js(4.0))), var.get('l')))
        #for JS loop
        var.put('h', var.get('a').get('_ff'))
        var.put('f', var.get('a').get('_gg'))
        var.put('g', var.get('a').get('_hh'))
        var.put('m', var.get('a').get('_ii'))
        var.put('u', Js(0.0))
        while (var.get('u')<var.get('s').get('length')):
            try:
                var.put('C', var.get('c'))
                var.put('v', var.get('d'))
                var.put('b', var.get('A'))
                var.put('B', var.get('p'))
                def PyJs_LONG_23_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('c', var.get('h')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(0.0))), Js(7.0), (-Js(680876936.0)))),var.put('p', var.get('h')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(1.0))), Js(12.0), (-Js(389564586.0))))),var.put('A', var.get('h')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(2.0))), Js(17.0), Js(606105819.0)))),var.put('d', var.get('h')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))),var.put('c', var.get('h')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(4.0))), Js(7.0), (-Js(176418897.0))))),var.put('p', var.get('h')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(5.0))), Js(12.0), Js(1200080426.0)))),var.put('A', var.get('h')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))),var.put('d', var.get('h')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(7.0))), Js(22.0), (-Js(45705983.0))))),var.put('c', var.get('h')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(8.0))), Js(7.0), Js(1770035416.0)))),var.put('p', var.get('h')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))),var.put('A', var.get('h')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(10.0))), Js(17.0), (-Js(42063.0))))),var.put('d', var.get('h')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))),var.put('c', var.get('h')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(12.0))), Js(7.0), Js(1804603682.0)))),var.put('p', var.get('h')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(13.0))), Js(12.0), (-Js(40341101.0))))),var.put('A', var.get('h')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))),var.put('d', var.get('h')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(15.0))), Js(22.0), Js(1236535329.0)))),var.put('c', var.get('f')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(1.0))), Js(5.0), (-Js(165796510.0))))),var.put('p', var.get('f')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))),var.put('A', var.get('f')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(11.0))), Js(14.0), Js(643717713.0)))),var.put('d', var.get('f')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(0.0))), Js(20.0), (-Js(373897302.0))))),var.put('c', var.get('f')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(5.0))), Js(5.0), (-Js(701558691.0))))),var.put('p', var.get('f')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(10.0))), Js(9.0), Js(38016083.0)))),var.put('A', var.get('f')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(15.0))), Js(14.0), (-Js(660478335.0))))),var.put('d', var.get('f')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(4.0))), Js(20.0), (-Js(405537848.0))))),var.put('c', var.get('f')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(9.0))), Js(5.0), Js(568446438.0)))),var.put('p', var.get('f')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))),var.put('A', var.get('f')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(3.0))), Js(14.0), (-Js(187363961.0))))),var.put('d', var.get('f')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(8.0))), Js(20.0), Js(1163531501.0)))),var.put('c', var.get('f')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))),var.put('p', var.get('f')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(2.0))), Js(9.0), (-Js(51403784.0))))),var.put('A', var.get('f')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(7.0))), Js(14.0), Js(1735328473.0)))),var.put('d', var.get('f')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))),var.put('c', var.get('g')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(5.0))), Js(4.0), (-Js(378558.0))))),var.put('p', var.get('g')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))),var.put('A', var.get('g')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(11.0))), Js(16.0), Js(1839030562.0)))),var.put('d', var.get('g')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(14.0))), Js(23.0), (-Js(35309556.0))))),var.put('c', var.get('g')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))),var.put('p', var.get('g')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(4.0))), Js(11.0), Js(1272893353.0)))),var.put('A', var.get('g')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(7.0))), Js(16.0), (-Js(155497632.0))))),var.put('d', var.get('g')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))),var.put('c', var.get('g')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(13.0))), Js(4.0), Js(681279174.0)))),var.put('p', var.get('g')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(0.0))), Js(11.0), (-Js(358537222.0))))),var.put('A', var.get('g')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(3.0))), Js(16.0), (-Js(722521979.0))))),var.put('d', var.get('g')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(6.0))), Js(23.0), Js(76029189.0)))),var.put('c', var.get('g')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(9.0))), Js(4.0), (-Js(640364487.0))))),var.put('p', var.get('g')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(12.0))), Js(11.0), (-Js(421815835.0))))),var.put('A', var.get('g')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(15.0))), Js(16.0), Js(530742520.0)))),var.put('d', var.get('g')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(2.0))), Js(23.0), (-Js(995338651.0))))),var.put('c', var.get('m')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(0.0))), Js(6.0), (-Js(198630844.0))))),var.put('p', var.get('m')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(7.0))), Js(10.0), Js(1126891415.0)))),var.put('A', var.get('m')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))),var.put('d', var.get('m')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(5.0))), Js(21.0), (-Js(57434055.0))))),var.put('c', var.get('m')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(12.0))), Js(6.0), Js(1700485571.0)))),var.put('p', var.get('m')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))),var.put('A', var.get('m')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(10.0))), Js(15.0), (-Js(1051523.0))))),var.put('d', var.get('m')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))),var.put('c', var.get('m')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(8.0))), Js(6.0), Js(1873313359.0)))),var.put('p', var.get('m')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(15.0))), Js(10.0), (-Js(30611744.0))))),var.put('A', var.get('m')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))),var.put('d', var.get('m')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(13.0))), Js(21.0), Js(1309151649.0)))),var.put('c', var.get('m')(var.get('c'), var.get('d'), var.get('A'), var.get('p'), var.get('s').get((var.get('u')+Js(4.0))), Js(6.0), (-Js(145523070.0))))),var.put('p', var.get('m')(var.get('p'), var.get('c'), var.get('d'), var.get('A'), var.get('s').get((var.get('u')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))),var.put('A', var.get('m')(var.get('A'), var.get('p'), var.get('c'), var.get('d'), var.get('s').get((var.get('u')+Js(2.0))), Js(15.0), Js(718787259.0)))),var.put('d', var.get('m')(var.get('d'), var.get('A'), var.get('p'), var.get('c'), var.get('s').get((var.get('u')+Js(9.0))), Js(21.0), (-Js(343485551.0))))),var.put('c', PyJsBshift((var.get('c')+var.get('C')),Js(0.0)))),var.put('d', PyJsBshift((var.get('d')+var.get('v')),Js(0.0)))),var.put('A', PyJsBshift((var.get('A')+var.get('b')),Js(0.0)))),var.put('p', PyJsBshift((var.get('p')+var.get('B')),Js(0.0))))
                PyJs_LONG_23_()
            finally:
                    var.put('u', Js(16.0), '+')
        return var.get('e').callprop('endian', Js([var.get('c'), var.get('d'), var.get('A'), var.get('p')]))
    PyJs_anonymous_21_._set_name('anonymous')
    var.put('a', PyJs_anonymous_21_)
    @Js
    def PyJs_anonymous_24_(n, e, t, i, o, r, a, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 't':t, 'i':i, 'o':o, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'n', 's', 'r', 'a', 't', 'e', 'o'])
        var.put('s', (((var.get('n')+((var.get('e')&var.get('t'))|((~var.get('e'))&var.get('i'))))+PyJsBshift(var.get('o'),Js(0.0)))+var.get('a')))
        return (((var.get('s')<<var.get('r'))|PyJsBshift(var.get('s'),(Js(32.0)-var.get('r'))))+var.get('e'))
    PyJs_anonymous_24_._set_name('anonymous')
    @Js
    def PyJs_anonymous_25_(n, e, t, i, o, r, a, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 't':t, 'i':i, 'o':o, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'n', 's', 'r', 'a', 't', 'e', 'o'])
        var.put('s', (((var.get('n')+((var.get('e')&var.get('i'))|(var.get('t')&(~var.get('i')))))+PyJsBshift(var.get('o'),Js(0.0)))+var.get('a')))
        return (((var.get('s')<<var.get('r'))|PyJsBshift(var.get('s'),(Js(32.0)-var.get('r'))))+var.get('e'))
    PyJs_anonymous_25_._set_name('anonymous')
    @Js
    def PyJs_anonymous_26_(n, e, t, i, o, r, a, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 't':t, 'i':i, 'o':o, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'n', 's', 'r', 'a', 't', 'e', 'o'])
        var.put('s', (((var.get('n')+((var.get('e')^var.get('t'))^var.get('i')))+PyJsBshift(var.get('o'),Js(0.0)))+var.get('a')))
        return (((var.get('s')<<var.get('r'))|PyJsBshift(var.get('s'),(Js(32.0)-var.get('r'))))+var.get('e'))
    PyJs_anonymous_26_._set_name('anonymous')
    @Js
    def PyJs_anonymous_27_(n, e, t, i, o, r, a, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 't':t, 'i':i, 'o':o, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'n', 's', 'r', 'a', 't', 'e', 'o'])
        var.put('s', (((var.get('n')+(var.get('t')^(var.get('e')|(~var.get('i')))))+PyJsBshift(var.get('o'),Js(0.0)))+var.get('a')))
        return (((var.get('s')<<var.get('r'))|PyJsBshift(var.get('s'),(Js(32.0)-var.get('r'))))+var.get('e'))
    PyJs_anonymous_27_._set_name('anonymous')
    PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('a').put('_ff', PyJs_anonymous_24_),var.get('a').put('_gg', PyJs_anonymous_25_)),var.get('a').put('_hh', PyJs_anonymous_26_)),var.get('a').put('_ii', PyJs_anonymous_27_)),var.get('a').put('_blocksize', Js(16.0))),var.get('a').put('_digestsize', Js(16.0)))
    var.put('i', var.get('e').callprop('wordsToBytes', var.get('a')(var.get('n'), var.get('t'))))
    var.put('result', var.get('e').callprop('bytesToHex', var.get('i')))
    return var.get('result')
PyJsHoisted_getSign_.func_name = 'getSign'
var.put('getSign', PyJsHoisted_getSign_)
@Js
def PyJs_anonymous_1_(n, e, this, arguments, var=var):
    var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'n'])
    return ((var.get('n')<<var.get('e'))|PyJsBshift(var.get('n'),(Js(32.0)-var.get('e'))))
PyJs_anonymous_1_._set_name('anonymous')
@Js
def PyJs_anonymous_2_(n, e, this, arguments, var=var):
    var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'n'])
    return ((var.get('n')<<(Js(32.0)-var.get('e')))|PyJsBshift(var.get('n'),var.get('e')))
PyJs_anonymous_2_._set_name('anonymous')
@Js
def PyJs_anonymous_3_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e'])
    if (var.get('n').get('constructor')==var.get('Number')):
        return ((Js(16711935.0)&var.get('t62').callprop('rotl', var.get('n'), Js(8.0)))|(Js(4278255360.0)&var.get('t62').callprop('rotl', var.get('n'), Js(24.0))))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<var.get('n').get('length')):
        try:
            var.get('n').put(var.get('e'), var.get('t62').callprop('endian', var.get('n').get(var.get('e'))))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    return var.get('n')
PyJs_anonymous_3_._set_name('anonymous')
@Js
def PyJs_anonymous_4_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e'])
    #for JS loop
    var.put('e', Js([]))
    while (var.get('n')>Js(0.0)):
        try:
            var.get('e').callprop('push', var.get('Math').callprop('floor', (Js(256.0)*var.get('Math').callprop('random'))))
        finally:
                (var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1))
    return var.get('e')
PyJs_anonymous_4_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'i', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    var.put('i', Js(0.0))
    while (var.get('t')<var.get('n').get('length')):
        try:
            var.get('e').put(PyJsBshift(var.get('i'),Js(5.0)), (var.get('n').get(var.get('t'))<<(Js(24.0)-(var.get('i')%Js(32.0)))), '|')
        finally:
                PyJsComma((var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1)),var.put('i', Js(8.0), '+'))
    return var.get('e')
PyJs_anonymous_5_._set_name('anonymous')
@Js
def PyJs_anonymous_6_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    while (var.get('t')<(Js(32.0)*var.get('n').get('length'))):
        try:
            var.get('e').callprop('push', (PyJsBshift(var.get('n').get(PyJsBshift(var.get('t'),Js(5.0))),(Js(24.0)-(var.get('t')%Js(32.0))))&Js(255.0)))
        finally:
                var.put('t', Js(8.0), '+')
    return var.get('e')
PyJs_anonymous_6_._set_name('anonymous')
@Js
def PyJs_anonymous_7_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('n').get('length')):
        try:
            PyJsComma(var.get('e').callprop('push', PyJsBshift(var.get('n').get(var.get('t')),Js(4.0)).callprop('toString', Js(16.0))),var.get('e').callprop('push', (Js(15.0)&var.get('n').get(var.get('t'))).callprop('toString', Js(16.0))))
        finally:
                (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
    return var.get('e').callprop('join', Js(''))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_8_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('n').get('length')):
        try:
            var.get('e').callprop('push', var.get('parseInt')(var.get('n').callprop('substr', var.get('t'), Js(2.0)), Js(16.0)))
        finally:
                var.put('t', Js(2.0), '+')
    return var.get('e')
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'n', 'r', 't', 'o'])
    #for JS loop
    var.put('t', Js([]))
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('n').get('length')):
        try:
            #for JS loop
            var.put('o', (((var.get('n').get(var.get('i'))<<Js(16.0))|(var.get('n').get((var.get('i')+Js(1.0)))<<Js(8.0)))|var.get('n').get((var.get('i')+Js(2.0)))))
            var.put('r', Js(0.0))
            while (var.get('r')<Js(4.0)):
                try:
                    (var.get('t').callprop('push', var.get('e').callprop('charAt', (PyJsBshift(var.get('o'),(Js(6.0)*(Js(3.0)-var.get('r'))))&Js(63.0)))) if (((Js(8.0)*var.get('i'))+(Js(6.0)*var.get('r')))<=(Js(8.0)*var.get('n').get('length'))) else var.get('t').callprop('push', Js('=')))
                finally:
                        (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
        finally:
                var.put('i', Js(3.0), '+')
    return var.get('t').callprop('join', Js(''))
PyJs_anonymous_9_._set_name('anonymous')
@Js
def PyJs_anonymous_10_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'o', 't', 'i'])
    var.put('n', var.get('n').callprop('replace', JsRegExp('/[^A-Z0-9+\\/]/gi'), Js('')))
    #for JS loop
    var.put('t', Js([]))
    var.put('i', Js(0.0))
    var.put('o', Js(0.0))
    while (var.get('i')<var.get('n').get('length')):
        try:
            ((Js(0.0)!=var.get('o')) and var.get('t').callprop('push', (((var.get('e').callprop('indexOf', var.get('n').callprop('charAt', (var.get('i')-Js(1.0))))&(var.get('Math').callprop('pow', Js(2.0), (((-Js(2.0))*var.get('o'))+Js(8.0)))-Js(1.0)))<<(Js(2.0)*var.get('o')))|PyJsBshift(var.get('e').callprop('indexOf', var.get('n').callprop('charAt', var.get('i'))),(Js(6.0)-(Js(2.0)*var.get('o')))))))
        finally:
                var.put('o', (var.put('i',Js(var.get('i').to_number())+Js(1))%Js(4.0)))
    return var.get('t')
PyJs_anonymous_10_._set_name('anonymous')
PyJs_Object_0_ = Js({'rotl':PyJs_anonymous_1_,'rotr':PyJs_anonymous_2_,'endian':PyJs_anonymous_3_,'randomBytes':PyJs_anonymous_4_,'bytesToWords':PyJs_anonymous_5_,'wordsToBytes':PyJs_anonymous_6_,'bytesToHex':PyJs_anonymous_7_,'hexToBytes':PyJs_anonymous_8_,'bytesToBase64':PyJs_anonymous_9_,'base64ToBytes':PyJs_anonymous_10_})
var.put('t62', PyJs_Object_0_)
@Js
def PyJs_anonymous_13_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    return var.get('t31').get('bin').callprop('stringToBytes', var.get('unescape')(var.get('encodeURIComponent')(var.get('n'))))
PyJs_anonymous_13_._set_name('anonymous')
@Js
def PyJs_anonymous_14_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    return var.get('decodeURIComponent')(var.get('escape')(var.get('t').get('bin').callprop('bytesToString', var.get('n'))))
PyJs_anonymous_14_._set_name('anonymous')
PyJs_Object_12_ = Js({'stringToBytes':PyJs_anonymous_13_,'bytesToString':PyJs_anonymous_14_})
@Js
def PyJs_anonymous_16_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('n').get('length')):
        try:
            var.get('e').callprop('push', (Js(255.0)&var.get('n').callprop('charCodeAt', var.get('t'))))
        finally:
                (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
    return var.get('e')
PyJs_anonymous_16_._set_name('anonymous')
@Js
def PyJs_anonymous_17_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 't', 'e'])
    #for JS loop
    var.put('e', Js([]))
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('n').get('length')):
        try:
            var.get('e').callprop('push', var.get('String').callprop('fromCharCode', var.get('n').get(var.get('t'))))
        finally:
                (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
    return var.get('e').callprop('join', Js(''))
PyJs_anonymous_17_._set_name('anonymous')
PyJs_Object_15_ = Js({'stringToBytes':PyJs_anonymous_16_,'bytesToString':PyJs_anonymous_17_})
PyJs_Object_11_ = Js({'utf8':PyJs_Object_12_,'bin':PyJs_Object_15_})
var.put('t31', PyJs_Object_11_)
@Js
def PyJs_anonymous_19_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    return ((var.get('n').get('constructor').neg().neg() and (Js('function')==var.get('n').get('constructor').get('isBuffer').typeof())) and var.get('n').get('constructor').callprop('isBuffer', var.get('n')))
PyJs_anonymous_19_._set_name('anonymous')
@Js
def PyJs_anonymous_20_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    return (((Js('function')==var.get('n').get('readFloatLE').typeof()) and (Js('function')==var.get('n').get('slice').typeof())) and var.get('t')(var.get('n').callprop('slice', Js(0.0), Js(0.0))))
PyJs_anonymous_20_._set_name('anonymous')
PyJs_Object_18_ = Js({'t':PyJs_anonymous_19_,'i':PyJs_anonymous_20_})
var.put('t57', PyJs_Object_18_)
pass
pass


# Add lib to the module scope
sign = var.to_python()


if __name__ == '__main__':
    def get_product_info_url(productid):
        e = '048a9c4943398714b356a696503d2d36'
        string = f'productId{productid}sourceshareDetail{e}'
        result = sign.getSign(string)
        return f'http://m.poizon.com/mapi/product/detail?productId={productid}&' \
               f'source=shareDetail&' \
               f'sign={result}'
    result = get_product_info_url('18570')
    print(result)

    ss = sign.getSign('18570')
    print(ss)