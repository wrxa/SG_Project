# -*- coding: utf-8 -*-
import ctypes
from platform import *
import math

cdll_names = {'Linux': 'libseuif97.so',
              'Windows': 'libseuif97.dll'}

osplat = system()
if (osplat == 'Linux'):
    flib = ctypes.cdll.LoadLibrary(cdll_names[osplat])
    prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int)
elif (osplat == 'Windows'):
    flib = ctypes.windll.LoadLibrary(cdll_names[osplat])
    prototype = ctypes.WINFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int)


# 饱和区压强计算
def psat_t(t):
    '''
    饱和区已知t(°C)求p(bar)
    '''
    t = t + 273.15
    if t <= 647.096 and t > 273.15:
        psat_t = (__p4_T(t)) * 10
        return psat_t
    return -1


def psat_s(s):
    '''
    饱和区已知s(kJ/(kg K))求p(bar)
    '''
    if s > -0.0001545495919 and s < 9.155759395:
        psat_s = __p4_s(s) * 10
        return psat_s
    return -1


# 饱和区温度计算
def tsat_p(p):
    '''
    饱和区已知p(bar)求t(°C)
    '''
    p = p / 10.000
    if p >= 0.000611657 and p <= 22.06395 + 0.001:
        tsat_p = __t4_P(p) - 273.15
        return tsat_p
    return -1


def tsat_s(s):
    '''
    饱和区已知s(kJ/(kg K))求t(°C)
    '''
    if s > -0.0001545495919 and s < 9.155759395:
        tsat_s = __t4_P(__p4_s(s)) - 273.15
        return tsat_s
    return -1


# 已知 (p,t)
def pt(p, t, pid):
    f = prototype(("seupt", flib),)
    result = f(p, t, pid)
    return result


def pt2h(p, t):
    f = prototype(("seupt", flib),)
    result = f(p, t, 4)
    return result


def pt2s(p, t):
    f = prototype(("seupt", flib),)
    result = f(p, t, 5)
    return result


def pt2v(p, t):
    f = prototype(("seupt", flib),)
    result = f(p, t, 3)
    return result


def pt2x(p, t):
    f = prototype(("seupt", flib),)
    result = f(p, t, 15)
    return result


# 已知 (p,h)
def ph(p, h, pid):
    f = prototype(("seuph", flib),)
    result = f(p, h, pid)
    return result


def ph2s(p, h):
    f = prototype(("seuph", flib),)
    result = f(p, h, 5)
    return result


def ph2v(p, h):
    f = prototype(("seuph", flib),)
    result = f(p, h, 3)
    return result


def ph2t(p, h):
    f = prototype(("seuph", flib),)
    result = f(p, h, 1)
    return result


def ph2x(p, h):
    f = prototype(("seuph", flib),)
    result = f(p, h, 15)
    return result


# 已知 (p,s)
def ps(p, s, pid):
    f = prototype(("seups", flib),)
    result = f(p, s, pid)
    return result


def ps2t(p, s):
    f = prototype(("seups", flib),)
    result = f(p, s, 1)
    return result


def ps2h(p, s):
    f = prototype(("seups", flib),)
    result = f(p, s, 4)
    return result


def ps2v(p, s):
    f = prototype(("seups", flib),)
    result = f(p, s, 3)
    return result


def ps2x(p, s):
    f = prototype(("seups", flib),)
    result = f(p, s, 15)
    return result


# 已知 (h,s)
def hs(h, s, pid):
    f = prototype(("seuhs", flib),)
    result = f(h, s, pid)
    return result


def hs2t(h, s):
    f = prototype(("seuhs", flib),)
    result = f(h, s, 1)
    return result


def hs2p(h, s):
    f = prototype(("seuhs", flib),)
    result = f(h, s, 0)
    return result


def hs2v(h, s):
    f = prototype(("seuhs", flib),)
    result = f(h, s, 3)
    return result


def hs2x(h, s):
    f = prototype(("seuhs", flib),)
    result = f(h, s, 15)
    return result


# 已知 (t,h)
def th(t, h, pid):
    f = prototype(("seuth", flib),)
    result = f(t, h, pid)
    return result


# 已知 (t,s)
def ts(t, s, pid):
    f = prototype(("seuts", flib),)
    result = f(t, s, pid)
    return result


def ts2p(t, s):
    f = prototype(("seuts", flib),)
    result = f(t, s, 0)
    return result


def ts2v(t, s):
    f = prototype(("seuts", flib),)
    result = f(t, s, 3)
    return result


def ts2h(t, s):
    f = prototype(("seuts", flib),)
    result = f(t, s, 4)
    return result


def ts2x(t, s):
    f = prototype(("seuts", flib),)
    result = f(t, s, 15)
    return result


# 已知 (p,x)
def px(p, x, pid):
    f = prototype(("seupx", flib),)
    result = f(p, x, pid)
    return result


def px2t(p, x):
    f = prototype(("seupx", flib),)
    result = f(p, x, 1)
    return result


def px2h(p, x):
    f = prototype(("seupx", flib),)
    result = f(p, x, 4)
    return result


def px2s(p, x):
    f = prototype(("seupx", flib),)
    result = f(p, x, 5)
    return result


def px2v(p, x):
    f = prototype(("seupx", flib),)
    result = f(p, x, 3)
    return result


# 已知 (t,x)
def tx(t, x, pid):
    f = prototype(("seutx", flib),)
    result = f(t, x, pid)
    return result


def tx2p(t, x):
    f = prototype(("seutx", flib),)
    result = f(t, x, 0)
    return result


def tx2v(t, x):
    f = prototype(("seutx", flib),)
    result = f(t, x, 3)
    return result


def tx2h(t, x):
    f = prototype(("seutx", flib),)
    result = f(t, x, 4)
    return result


def tx2s(t, x):
    f = prototype(("seutx", flib),)
    result = f(t, x, 5)
    return result


# ---------- processing ------------
def ishd(p1, t1, p2):
    f = flib.seuishd
    f.argtypes = [c_double, c_double, c_double]
    f.restype = c_double
    result = f(p1, t1, p2)
    return result


def ief(p1, t1, p2, t2):
    f = flib.seuief
    f.argtypes = [c_double, c_double, c_double, c_double]
    f.restype = c_double
    result = f(p1, t1, p2, t2)
    return result


def __p4_T(T):
    '''
    饱和区压强计算
    辅助方法
    '''
    teta = T - 0.23855557567849 / (T - 650.17534844798)
    a = teta ** 2 + 1167.0521452767 * teta - 724213.16703206
    B = -17.073846940092 * teta ** 2 + 12020.82470247 * teta - 3232555.0322333
    C = 14.91510861353 * teta ** 2 - 4823.2657361591 * teta + 405113.40542057
    p4_T = (2 * C / (-B + math.sqrt((B * B - 4 * a * C)))) ** 4
    return p4_T


def __p4_s(s):
    '''
    饱和区压强计算
    辅助方法
    '''
    hsat = __h4_s(s)
    if s > -0.0001545495919 and s <= 3.77828134:
        p4_s = hs2p(hsat, s)
    elif s > 3.77828134 and s <= 5.210887663:
        p4_s = hs2p(hsat, s)
    elif s > 5.210887663 and s < 9.155759395:
        p4_s = hs2p(hsat, s)
    else:
        p4_s = -1
    return p4_s


def __t4_P(p):
    '''
    饱和区温度计算
    辅助方法
    '''
    beta = math.pow(p, 0.25)
    e = math.pow(beta, 2) - 17.073846940092 * beta + 14.91510861353
    f = 1167.0521452767 * math.pow(beta, 2) + 12020.82470247 * beta - 4823.2657361591
    g = -724213.16703206 * math.pow(beta, 2) - 3232555.0322333 * beta + 405113.40542057
    d = 2 * g / (-f - math.pow((math.pow(f, 2) - 4 * e * g), 0.5))
    t4_p = (650.17534844798 + d - math.pow((math.pow((650.17534844798 + d), 2) - 4 * (-0.23855557567849 + 650.17534844798 * d)), 0.5)) / 2
    return t4_p


def __h4_s(s):
    if s > -0.0001545495919 and s <= 3.77828134:
        ii = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 7, 8, 12, 12, 14, 14, 16, 20, 20, 22, 24, 28, 32, 32]
        Ji = [14, 36, 3, 16, 0, 5, 4, 36, 4, 16, 24, 18, 24, 1, 4, 2, 4, 1, 22, 10, 12, 28, 8, 3, 0, 6, 8]
        ni = [0.332171191705237, 6.11217706323496E-04, -8.82092478906822, -0.45562819254325, -2.63483840850452E-05, -22.3949661148062, -4.28398660164013, -0.616679338856916, -14.682303110404, 284.523138727299, -113.398503195444, 1156.71380760859, 395.551267359325, -1.54891257229285, 19.4486637751291, -3.57915139457043, -3.35369414148819, -0.66442679633246, 32332.1885383934, 3317.66744667084, -22350.1257931087, 5739538.75852936, 173.226193407919, -3.63968822121321E-02, 8.34596332878346E-07, 5.03611916682674, 65.5444787064505]
        sigma = s / 3.8
        eta = 0
        for i in range(0, 27):
            eta = eta + ni[i] * math.pow((sigma - 1.09), ii[i]) * math.pow((sigma + 0.0000366), Ji[i])
        h4_s = eta * 1700
    elif s > 3.77828134 and s <= 4.41202148223476:
        ii = [0, 0, 0, 0, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 10, 10, 10, 32, 32]
        Ji = [1, 4, 10, 16, 1, 36, 3, 16, 20, 36, 4, 2, 28, 32, 14, 32, 36, 0, 6]
        ni = [0.822673364673336, 0.181977213534479, -0.011200026031362, -7.46778287048033E-04, -0.179046263257381, 4.24220110836657E-02, -0.341355823438768, -2.09881740853565, -8.22477343323596, -4.99684082076008, 0.191413958471069, 5.81062241093136E-02, -1655.05498701029, 1588.70443421201, -85.0623535172818, -31771.4386511207, -94589.0406632871, -1.3927384708869E-06, 0.63105253224098]
        sigma = s / 3.8
        eta = 0
        for i in range(0, 19):
            eta = eta + ni[i] * math.pow((sigma - 1.09), ii[i]) * math.pow((sigma + 0.0000366), Ji[i])
        h4_s = eta * 1700
    elif s > 4.41202148223476 and s <= 5.85:
        ii = [0, 0, 0, 1, 1, 5, 6, 7, 8, 8, 12, 16, 22, 22, 24, 36]
        Ji = [0, 3, 4, 0, 12, 36, 12, 16, 2, 20, 32, 36, 2, 32, 7, 20]
        ni = [1.04351280732769, -2.27807912708513, 1.80535256723202, 0.420440834792042, -105721.24483466, 4.36911607493884E+24, -328032702839.753, -6.7868676080427E+15, 7439.57464645363, -3.56896445355761E+19, 1.67590585186801E+31, -3.55028625419105E+37, 396611982166.538, -4.14716268484468E+40, 3.59080103867382E+18, -1.16994334851995E+40]
        sigma = s / 5.9
        eta = 0
        for i in range(0, 16):
            eta = eta + ni[i] * math.pow((sigma - 1.02), ii[i]) * math.pow((sigma - 0.726), Ji[i])
        h4_s = math.pow(eta, 4) * 2800
    elif s > 5.85 and s < 9.155759395:
        ii = [1, 1, 2, 2, 4, 4, 7, 8, 8, 10, 12, 12, 18, 20, 24, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36]
        Ji = [8, 24, 4, 32, 1, 2, 7, 5, 12, 1, 0, 7, 10, 12, 32, 8, 12, 20, 22, 24, 2, 7, 12, 14, 24, 10, 12, 20, 22, 28]
        ni = [-524.581170928788, -9269472.18142218, -237.385107491666, 21077015581.2776, -23.9494562010986, 221.802480294197, -5104725.33393438, 1249813.96109147, 2000084369.96201, -815.158509791035, -157.612685637523, -11420042233.2791, 6.62364680776872E+15, -2.27622818296144E+18, -1.71048081348406E+31, 6.60788766938091E+15, 1.66320055886021E+22, -2.18003784381501E+29, -7.87276140295618E+29, 1.51062329700346E+31, 7957321.70300541, 1.31957647355347E+15, -3.2509706829914E+23, -4.18600611419248E+25, 2.97478906557467E+34, -9.53588761745473E+19, 1.66957699620939E+24, -1.75407764869978E+32, 3.47581490626396E+34, -7.10971318427851E+38]
        sigma1 = s / 5.21
        sigma2 = s / 9.2
        eta = 0
        for i in range(0, 30):
            eta = eta + ni[i] * math.pow((1 / sigma1 - 0.513), ii[i]) * math.pow((sigma2 - 0.524), Ji[i])
        h4_s = math.exp(eta) * 2800
    else:
        h4_s = -1
    return h4_s
