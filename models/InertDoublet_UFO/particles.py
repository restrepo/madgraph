# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 8.0 for Linux x86 (64-bit) (February 23, 2011)
# Date: Wed 16 Sep 2015 11:36:06


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

ne = Particle(pdg_code = 12,
              name = 'ne',
              antiname = 'Ne',
              spin = 2,
              color = 1,
              mass = Param.Mnue,
              width = Param.ZERO,
              texname = 'ne',
              antitexname = 'Ne',
              charge = 0,
              GhostNumber = 0)

Ne = ne.anti()

nm = Particle(pdg_code = 14,
              name = 'nm',
              antiname = 'Nm',
              spin = 2,
              color = 1,
              mass = Param.Mnum,
              width = Param.ZERO,
              texname = 'nm',
              antitexname = 'Nm',
              charge = 0,
              GhostNumber = 0)

Nm = nm.anti()

nl = Particle(pdg_code = 16,
              name = 'nl',
              antiname = 'Nl',
              spin = 2,
              color = 1,
              mass = Param.Mnut,
              width = Param.ZERO,
              texname = 'nl',
              antitexname = 'Nl',
              charge = 0,
              GhostNumber = 0)

Nl = nl.anti()

e = Particle(pdg_code = 11,
             name = 'e',
             antiname = 'E',
             spin = 2,
             color = 1,
             mass = Param.Me,
             width = Param.ZERO,
             texname = 'e',
             antitexname = 'E',
             charge = -1,
             GhostNumber = 0)

E = e.anti()

m = Particle(pdg_code = 13,
             name = 'm',
             antiname = 'M',
             spin = 2,
             color = 1,
             mass = Param.MM,
             width = Param.ZERO,
             texname = 'm',
             antitexname = 'M',
             charge = -1,
             GhostNumber = 0)

M = m.anti()

l = Particle(pdg_code = 15,
             name = 'l',
             antiname = 'L',
             spin = 2,
             color = 1,
             mass = Param.MTA,
             width = Param.ZERO,
             texname = 'l',
             antitexname = 'L',
             charge = -1,
             GhostNumber = 0)

L = l.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'U',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'U',
             charge = 2/3,
             GhostNumber = 0)

U = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'C',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'C',
             charge = 2/3,
             GhostNumber = 0)

C = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 'T',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 'T',
             charge = 2/3,
             GhostNumber = 0)

T = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'D',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'D',
             charge = -1/3,
             GhostNumber = 0)

D = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 'S',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 'S',
             charge = -1/3,
             GhostNumber = 0)

S = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'B',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'B',
             charge = -1/3,
             GhostNumber = 0)

B = b.anti()

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1)

ghG__tilde__ = ghG.anti()

h = Particle(pdg_code = 25,
             name = 'h',
             antiname = 'h',
             spin = 1,
             color = 1,
             mass = Param.mh,
             width = Param.Wh,
             texname = 'h',
             antitexname = 'h',
             charge = 0,
             GhostNumber = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.ZERO,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.ZERO,
                     texname = 'G^+',
                     antitexname = 'G^-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0)

G__minus__ = G__plus__.anti()

P__tilde__H0 = Particle(pdg_code = 35,
                        name = '~H0',
                        antiname = '~H0',
                        spin = 1,
                        color = 1,
                        mass = Param.MH0,
                        width = Param.WH0,
                        texname = '~H0',
                        antitexname = '~H0',
                        charge = 0,
                        GhostNumber = 0)

P__tilde__A0 = Particle(pdg_code = 36,
                        name = '~A0',
                        antiname = '~A0',
                        spin = 1,
                        color = 1,
                        mass = Param.MA0,
                        width = Param.WA0,
                        texname = '~A0',
                        antitexname = '~A0',
                        charge = 0,
                        GhostNumber = 0)

P__tilde__H__plus__ = Particle(pdg_code = 37,
                               name = '~H+',
                               antiname = '~H-',
                               spin = 1,
                               color = 1,
                               mass = Param.MHch,
                               width = Param.WHch,
                               texname = '~H+',
                               antitexname = '~H-',
                               charge = 1,
                               GhostNumber = 0)

P__tilde__H__minus__ = P__tilde__H__plus__.anti()

