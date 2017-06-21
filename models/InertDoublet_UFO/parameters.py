# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 8.0 for Linux x86 (64-bit) (February 23, 2011)
# Date: Wed 16 Sep 2015 11:36:06



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 0.007757951900698216,
                  texname = '\\alpha _w^{-1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_F',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

MMZ = Parameter(name = 'MMZ',
                nature = 'external',
                type = 'real',
                value = 91.1876,
                texname = 'm_Z',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

MMW = Parameter(name = 'MMW',
                nature = 'external',
                type = 'real',
                value = 79.947,
                texname = 'm_W',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

MMC = Parameter(name = 'MMC',
                nature = 'external',
                type = 'real',
                value = 1.2,
                texname = 'm_c',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

MMB = Parameter(name = 'MMB',
                nature = 'external',
                type = 'real',
                value = 4.23,
                texname = 'm_b',
                lhablock = 'FRBlock',
                lhacode = [ 6 ])

MMT = Parameter(name = 'MMT',
                nature = 'external',
                type = 'real',
                value = 175,
                texname = 'm_t',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1172,
               texname = '\\alpha _s',
               lhablock = 'FRBlock',
               lhacode = [ 8 ])

QS = Parameter(name = 'QS',
               nature = 'external',
               type = 'real',
               value = 100.,
               texname = 'Q_s',
               lhablock = 'FRBlock',
               lhacode = [ 9 ])

lamL = Parameter(name = 'lamL',
                 nature = 'external',
                 type = 'real',
                 value = 0.4,
                 texname = '\\lambda _L',
                 lhablock = 'FRBlock',
                 lhacode = [ 10 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _2',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

mmh = Parameter(name = 'mmh',
                nature = 'external',
                type = 'real',
                value = 125.1,
                texname = 'm_h',
                lhablock = 'FRBlock',
                lhacode = [ 12 ])

mmH0 = Parameter(name = 'mmH0',
                 nature = 'external',
                 type = 'real',
                 value = 65.0,
                 texname = 'm_{\\text{H0}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 13 ])

mmA0 = Parameter(name = 'mmA0',
                 nature = 'external',
                 type = 'real',
                 value = 750.0,
                 texname = 'm_A',
                 lhablock = 'FRBlock',
                 lhacode = [ 14 ])

mmHch = Parameter(name = 'mmHch',
                  nature = 'external',
                  type = 'real',
                  value = 750.0,
                  texname = 'm_{\\text{Hch}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 15 ])

Mnue = Parameter(name = 'Mnue',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnue}',
                 lhablock = 'MASS',
                 lhacode = [ 12 ])

Mnum = Parameter(name = 'Mnum',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnum}',
                 lhablock = 'MASS',
                 lhacode = [ 14 ])

Mnut = Parameter(name = 'Mnut',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnut}',
                 lhablock = 'MASS',
                 lhacode = [ 16 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.1057,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wh = Parameter(name = 'Wh',
               nature = 'external',
               type = 'real',
               value = 0.00415,
               texname = '\\text{Wh}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WH0 = Parameter(name = 'WH0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{WH0}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 129.2,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WHch = Parameter(name = 'WHch',
                 nature = 'external',
                 type = 'real',
                 value = 130.6,
                 texname = '\\text{WHch}',
                 lhablock = 'DECAY',
                 lhacode = [ 37 ])

MZ = Parameter(name = 'MZ',
               nature = 'internal',
               type = 'real',
               value = 'MMZ',
               texname = 'm_Z')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'MMW',
               texname = 'm_W')

MC = Parameter(name = 'MC',
               nature = 'internal',
               type = 'real',
               value = 'MMC',
               texname = 'm_c')

MB = Parameter(name = 'MB',
               nature = 'internal',
               type = 'real',
               value = 'MMB',
               texname = 'm_b')

MT = Parameter(name = 'MT',
               nature = 'internal',
               type = 'real',
               value = 'MMT',
               texname = 'm_t')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '0.8408964152537146/cmath.sqrt(Gf)',
              texname = 'v')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value ='2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.97428',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.2253',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.00347',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.2252',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.97345',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.041',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.00862',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.0403',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0.999152',
                   texname = '\\text{CKM3x3}')

mh = Parameter(name = 'mh',
               nature = 'internal',
               type = 'real',
               value = 'mmh',
               texname = 'm_h')

MH0 = Parameter(name = 'MH0',
                nature = 'internal',
                type = 'real',
                value = 'mmH0',
                texname = 'm_{\\text{H0}}')

MA0 = Parameter(name = 'MA0',
                nature = 'internal',
                type = 'real',
                value = 'mmA0',
                texname = 'm_A')

MHch = Parameter(name = 'MHch',
                 nature = 'internal',
                 type = 'real',
                 value = 'mmHch',
                 texname = 'm_{\\text{Hch}}')

CW2 = Parameter(name = 'CW2',
                nature = 'internal',
                type = 'real',
                value = 'MW**2/MZ**2',
                texname = 'c_w^2')

mu1 = Parameter(name = 'mu1',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sqrt(-mh**2)/cmath.sqrt(2)',
                texname = '\\mu _1')

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(MH0**2 - lamL*v**2)',
                texname = '\\mu _2')

GH = Parameter(name = 'GH',
               nature = 'internal',
               type = 'real',
               value = '-(G**2*(1 + (13*mmh**6)/(16800.*MMT**6) + mmh**4/(168.*MMT**4) + (7*mmh**2)/(120.*MMT**2)))/(12.*cmath.pi**2*v)',
               texname = 'G_H')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'mh**2/(2.*v**2)',
                texname = '\\lambda _1')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*(-MH0**2 + MHch**2 + lamL*v**2))/v**2',
                 texname = '\\lambda _3')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = '(MA0**2 + MH0**2 - 2*MHch**2)/v**2',
                 texname = '\\lambda _4')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(-MA0**2 + MH0**2)/v**2',
                 texname = '\\lambda _5')

CW = Parameter(name = 'CW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(CW2)',
               texname = 'c_w')

SW2 = Parameter(name = 'SW2',
                nature = 'internal',
                type = 'real',
                value = '1 - CW2',
                texname = 's_w^2')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/CW',
               texname = 'g_1')

SW = Parameter(name = 'SW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(SW2)',
               texname = 's_w')

g2 = Parameter(name = 'g2',
               nature = 'internal',
               type = 'real',
               value = 'ee/SW',
               texname = 'g_2')

