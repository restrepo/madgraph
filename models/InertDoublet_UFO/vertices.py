# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 8.0 for Linux x86 (64-bit) (February 23, 2011)
# Date: Wed 16 Sep 2015 11:36:06


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.h, P.h, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_16})

V_2 = Vertex(name = 'V_2',
             particles = [ P.P__tilde__A0, P.P__tilde__A0, P.P__tilde__A0, P.P__tilde__A0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_19})

V_3 = Vertex(name = 'V_3',
             particles = [ P.P__tilde__A0, P.P__tilde__A0, P.P__tilde__H0, P.P__tilde__H0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_17})

V_4 = Vertex(name = 'V_4',
             particles = [ P.P__tilde__H0, P.P__tilde__H0, P.P__tilde__H0, P.P__tilde__H0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_19})

V_5 = Vertex(name = 'V_5',
             particles = [ P.P__tilde__A0, P.P__tilde__A0, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_17})

V_6 = Vertex(name = 'V_6',
             particles = [ P.P__tilde__H0, P.P__tilde__H0, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_17})

V_7 = Vertex(name = 'V_7',
             particles = [ P.P__tilde__H__minus__, P.P__tilde__H__minus__, P.P__tilde__H__plus__, P.P__tilde__H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_18})

V_8 = Vertex(name = 'V_8',
             particles = [ P.P__tilde__A0, P.P__tilde__A0, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_9 = Vertex(name = 'V_9',
             particles = [ P.h, P.h, P.P__tilde__H0, P.P__tilde__H0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_21})

V_10 = Vertex(name = 'V_10',
              particles = [ P.h, P.h, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_20})

V_11 = Vertex(name = 'V_11',
              particles = [ P.h, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_63})

V_12 = Vertex(name = 'V_12',
              particles = [ P.P__tilde__A0, P.P__tilde__A0, P.h ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_67})

V_13 = Vertex(name = 'V_13',
              particles = [ P.h, P.P__tilde__H0, P.P__tilde__H0 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_66})

V_14 = Vertex(name = 'V_14',
              particles = [ P.h, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_64})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_17 = Vertex(name = 'V_17',
              particles = [ P.g, P.g, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_13})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_10})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_21 = Vertex(name = 'V_21',
              particles = [ P.g, P.g, P.g, P.h ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_14})

V_22 = Vertex(name = 'V_22',
              particles = [ P.g, P.g, P.g, P.g, P.h ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
              couplings = {(1,1):C.GC_15,(0,0):C.GC_15,(2,2):C.GC_15})

V_23 = Vertex(name = 'V_23',
              particles = [ P.D, P.d, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_56})

V_24 = Vertex(name = 'V_24',
              particles = [ P.S, P.s, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_59})

V_25 = Vertex(name = 'V_25',
              particles = [ P.B, P.b, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_54})

V_26 = Vertex(name = 'V_26',
              particles = [ P.E, P.e, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_57})

V_27 = Vertex(name = 'V_27',
              particles = [ P.M, P.m, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_58})

V_28 = Vertex(name = 'V_28',
              particles = [ P.L, P.l, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_61})

V_29 = Vertex(name = 'V_29',
              particles = [ P.U, P.u, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_62})

V_30 = Vertex(name = 'V_30',
              particles = [ P.C, P.c, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_55})

V_31 = Vertex(name = 'V_31',
              particles = [ P.T, P.t, P.h ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_60})

V_32 = Vertex(name = 'V_32',
              particles = [ P.D, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_33 = Vertex(name = 'V_33',
              particles = [ P.S, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_34 = Vertex(name = 'V_34',
              particles = [ P.B, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_35 = Vertex(name = 'V_35',
              particles = [ P.U, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_36 = Vertex(name = 'V_36',
              particles = [ P.C, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_37 = Vertex(name = 'V_37',
              particles = [ P.T, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_11})

V_38 = Vertex(name = 'V_38',
              particles = [ P.a, P.W__minus__, P.P__tilde__A0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_42})

V_39 = Vertex(name = 'V_39',
              particles = [ P.a, P.W__minus__, P.P__tilde__H0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_40 = Vertex(name = 'V_40',
              particles = [ P.W__minus__, P.P__tilde__A0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_28})

V_41 = Vertex(name = 'V_41',
              particles = [ P.W__minus__, P.P__tilde__H0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_26})

V_42 = Vertex(name = 'V_42',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_4})

V_43 = Vertex(name = 'V_43',
              particles = [ P.a, P.W__plus__, P.P__tilde__A0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_44})

V_44 = Vertex(name = 'V_44',
              particles = [ P.a, P.W__plus__, P.P__tilde__H0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_45 = Vertex(name = 'V_45',
              particles = [ P.W__plus__, P.P__tilde__A0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_28})

V_46 = Vertex(name = 'V_46',
              particles = [ P.W__plus__, P.P__tilde__H0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_27})

V_47 = Vertex(name = 'V_47',
              particles = [ P.W__minus__, P.W__plus__, P.P__tilde__A0, P.P__tilde__A0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_23})

V_48 = Vertex(name = 'V_48',
              particles = [ P.W__minus__, P.W__plus__, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_23})

V_49 = Vertex(name = 'V_49',
              particles = [ P.W__minus__, P.W__plus__, P.P__tilde__H0, P.P__tilde__H0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_23})

V_50 = Vertex(name = 'V_50',
              particles = [ P.W__minus__, P.W__plus__, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_23})

V_51 = Vertex(name = 'V_51',
              particles = [ P.W__minus__, P.W__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_65})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_5})

V_53 = Vertex(name = 'V_53',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_41})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_24})

V_55 = Vertex(name = 'V_55',
              particles = [ P.a, P.Z, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_51})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Z, P.P__tilde__A0, P.P__tilde__H0 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_48})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Z, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_49})

V_58 = Vertex(name = 'V_58',
              particles = [ P.W__minus__, P.Z, P.P__tilde__A0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_59 = Vertex(name = 'V_59',
              particles = [ P.W__minus__, P.Z, P.P__tilde__H0, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_60 = Vertex(name = 'V_60',
              particles = [ P.W__plus__, P.Z, P.P__tilde__A0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_61 = Vertex(name = 'V_61',
              particles = [ P.W__plus__, P.Z, P.P__tilde__H0, P.P__tilde__H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_45})

V_63 = Vertex(name = 'V_63',
              particles = [ P.Z, P.Z, P.P__tilde__A0, P.P__tilde__A0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_53})

V_64 = Vertex(name = 'V_64',
              particles = [ P.Z, P.Z, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_53})

V_65 = Vertex(name = 'V_65',
              particles = [ P.Z, P.Z, P.P__tilde__H0, P.P__tilde__H0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_53})

V_66 = Vertex(name = 'V_66',
              particles = [ P.Z, P.Z, P.P__tilde__H__minus__, P.P__tilde__H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_52})

V_67 = Vertex(name = 'V_67',
              particles = [ P.Z, P.Z, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_68})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_25})

V_69 = Vertex(name = 'V_69',
              particles = [ P.D, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_70 = Vertex(name = 'V_70',
              particles = [ P.S, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_71 = Vertex(name = 'V_71',
              particles = [ P.B, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_72 = Vertex(name = 'V_72',
              particles = [ P.E, P.e, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_73 = Vertex(name = 'V_73',
              particles = [ P.M, P.m, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_74 = Vertex(name = 'V_74',
              particles = [ P.L, P.l, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_75 = Vertex(name = 'V_75',
              particles = [ P.U, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_76 = Vertex(name = 'V_76',
              particles = [ P.C, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_77 = Vertex(name = 'V_77',
              particles = [ P.T, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_78 = Vertex(name = 'V_78',
              particles = [ P.E, P.ne, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_79 = Vertex(name = 'V_79',
              particles = [ P.M, P.nm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_80 = Vertex(name = 'V_80',
              particles = [ P.L, P.nl, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_81 = Vertex(name = 'V_81',
              particles = [ P.D, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_30})

V_82 = Vertex(name = 'V_82',
              particles = [ P.S, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_31})

V_83 = Vertex(name = 'V_83',
              particles = [ P.B, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_84 = Vertex(name = 'V_84',
              particles = [ P.D, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_33})

V_85 = Vertex(name = 'V_85',
              particles = [ P.S, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_34})

V_86 = Vertex(name = 'V_86',
              particles = [ P.B, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_87 = Vertex(name = 'V_87',
              particles = [ P.D, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_36})

V_88 = Vertex(name = 'V_88',
              particles = [ P.S, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_37})

V_89 = Vertex(name = 'V_89',
              particles = [ P.B, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_38})

V_90 = Vertex(name = 'V_90',
              particles = [ P.Ne, P.e, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Nm, P.m, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Nl, P.l, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_93 = Vertex(name = 'V_93',
              particles = [ P.U, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_69})

V_94 = Vertex(name = 'V_94',
              particles = [ P.C, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_72})

V_95 = Vertex(name = 'V_95',
              particles = [ P.T, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_75})

V_96 = Vertex(name = 'V_96',
              particles = [ P.U, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_70})

V_97 = Vertex(name = 'V_97',
              particles = [ P.C, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_73})

V_98 = Vertex(name = 'V_98',
              particles = [ P.T, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_76})

V_99 = Vertex(name = 'V_99',
              particles = [ P.U, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_71})

V_100 = Vertex(name = 'V_100',
               particles = [ P.C, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_74})

V_101 = Vertex(name = 'V_101',
               particles = [ P.T, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_77})

V_102 = Vertex(name = 'V_102',
               particles = [ P.D, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_46})

V_103 = Vertex(name = 'V_103',
               particles = [ P.S, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_46})

V_104 = Vertex(name = 'V_104',
               particles = [ P.B, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_46})

V_105 = Vertex(name = 'V_105',
               particles = [ P.E, P.e, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_47})

V_106 = Vertex(name = 'V_106',
               particles = [ P.M, P.m, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_47})

V_107 = Vertex(name = 'V_107',
               particles = [ P.L, P.l, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_39,(0,1):C.GC_47})

V_108 = Vertex(name = 'V_108',
               particles = [ P.U, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,1):C.GC_46,(0,0):C.GC_40})

V_109 = Vertex(name = 'V_109',
               particles = [ P.C, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_40,(0,1):C.GC_46})

V_110 = Vertex(name = 'V_110',
               particles = [ P.T, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_40,(0,1):C.GC_46})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Ne, P.ne, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_50})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Nm, P.nm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_50})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Nl, P.nl, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_50})

