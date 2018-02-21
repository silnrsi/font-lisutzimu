APPNAME='lisutzimu'
VERSION='1.401'
LICENSE='ofl.txt'
out='results'
COPYRIGHT = "Copyright (c) 1998-2018, David Morse with Reserved Font Name LisuTzimu"

fname = 'LisuTzimu'
for e in ('Regular', 'Bold', 'Italic', 'BoldItalic') :
    f = font(target = fname+'-'+e+'.ttf',
             source = 'source/LisuTzimu-'+e+'.ufo',
             copyright = COPYRIGHT,
             license = ofl('LisuTzimu'))

