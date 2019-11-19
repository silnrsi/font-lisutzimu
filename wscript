#!/usr/bin/python
# this is a smith configuration file

# set the font name, version, licensing and description
APPNAME = "LisuTzimu"
fontfamily=APPNAME

DESC_SHORT = "Font for the Lisu (Fraser) script"
DESC_NAME = "LisuTzimu"

getufoinfo('source/' + fontfamily + '-Regular' + '.ufo')
# BUILDLABEL = "alpha"

for dspace in ('Roman', 'Italic'):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax"),
                pdf = fret(params="-r -oi"),
    )
