# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 8.0 for Linux x86 (64-bit) (February 23, 2011)
# Date: Wed 16 Sep 2015 11:36:06


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*CW)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-(ee**2*complex(0,1))/(2.*CW)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*CW)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*GH)',
                 order = {'HIG':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(G*GH)',
                 order = {'HIG':1,'QCD':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2*GH',
                 order = {'HIG':1,'QCD':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-2*complex(0,1)*lam2',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-4*complex(0,1)*lam2',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-6*complex(0,1)*lam2',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(complex(0,1)*lam3)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*lam3) - complex(0,1)*lam4 - complex(0,1)*lam5',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(complex(0,1)*lam3) - complex(0,1)*lam4 + complex(0,1)*lam5',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(ee**2*complex(0,1))/(2.*SW**2)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((ee**2*complex(0,1))/SW**2)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CW**2*ee**2*complex(0,1))/SW**2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'ee/(2.*SW)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM1x1*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM1x2*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(CKM1x3*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CKM2x1*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(CKM2x2*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM2x3*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM3x1*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CKM3x2*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CKM3x3*ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(CW*ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(CW*ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(CW*ee*complex(0,1))/SW',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-ee**2/(2.*SW)',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee**2*complex(0,1))/(2.*SW)',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ee**2/(2.*SW)',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(-2*CW*ee**2*complex(0,1))/SW',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(ee*complex(0,1)*SW)/(6.*CW)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(CW*ee)/(2.*SW) - (ee*SW)/(2.*CW)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(CW*ee*complex(0,1))/(2.*SW) + (ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(CW*ee*complex(0,1))/(2.*SW) + (ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(CW*ee**2*complex(0,1))/SW - (ee**2*complex(0,1)*SW)/CW',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ee**2*complex(0,1)) + (CW**2*ee**2*complex(0,1))/(2.*SW**2) + (ee**2*complex(0,1)*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = 'ee**2*complex(0,1) + (CW**2*ee**2*complex(0,1))/(2.*SW**2) + (ee**2*complex(0,1)*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((complex(0,1)*MB)/v)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((complex(0,1)*MC)/v)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((complex(0,1)*MD)/v)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((complex(0,1)*Me)/v)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*MM)/v)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((complex(0,1)*MS)/v)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*MT)/v)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((complex(0,1)*MTA)/v)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*MU)/v)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-6*complex(0,1)*lam*v',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(complex(0,1)*lam3*v)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee**2*complex(0,1)*v)/(2.*SW**2)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(complex(0,1)*lam3*v) - complex(0,1)*lam4*v - complex(0,1)*lam5*v',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(complex(0,1)*lam3*v) - complex(0,1)*lam4*v + complex(0,1)*lam5*v',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'ee**2*complex(0,1)*v + (CW**2*ee**2*complex(0,1)*v)/(2.*SW**2) + (ee**2*complex(0,1)*SW**2*v)/(2.*CW**2)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

