
import getopt
import re
import sys
from math import *
import os

Deg2Rad = 2.0 * pi / 360.0
p = {}
font = None
XLineOffset = 0
XIndentList = ""
Depth = 0.1
SafeZ = 2
Spindle = 0.
output_gcode = ""
font = None
# =======================================================================
class Character:
    def __init__(self, key):
        self.key = key
        self.stroke_list = []
        self.stroke_list_groups = []

    def __repr__(self):
        return "%s" % (self.stroke_list)

    def get_xmax(self):
        try:
            return max([s.xmax for s in self.stroke_list[:]])
        except ValueError:
            return 0

    def get_ymax(self):
        try:
            return max([s.ymax for s in self.stroke_list[:]])
        except ValueError:
            return 0

# =======================================================================
class Line:

    def __init__(self, coords):
        self.xstart, self.ystart, self.xend, self.yend = coords
        self.xmax = max(self.xstart, self.xend)
        self.ymax = max(self.ystart, self.yend)
        self.xmin = min(self.xstart, self.xend)
        self.ymin = min(self.ystart, self.yend)

    def __repr__(self):
        return "Line([%s, %s, %s, %s])" % (self.xstart, self.ystart, self.xend, self.yend)


class StrokeGroup:
    def __init__(self):
        self.lines = []
        self.xmax = -sys.maxsize-1
        self.ymax = -sys.maxsize-1
        self.xmin = sys.maxsize
        self.ymin = sys.maxsize

    def addLine(self, line):
        self.lines.append(line)
        self.xmax = max(self.xmax, line.xmax)
        self.xmin = min(self.xmin, line.xmin)
        self.ymax = max(self.ymax, line.ymax)
        self.ymin = min(self.ymin, line.ymin)


def inside_cmp(g1, g2):
    if g1.xmin < g2.xmin and g1.xmax > g2.xmax and g1.ymin < g2.ymin and g1.ymax > g2.xmax:
        return 1
    return -1

def inside_first(strokes):
    # pass1 : divide strokes
    o_stroke = None
    stroke_groups = []
    distance = 1
    for stroke in strokes:
        if o_stroke is not None:
            dx = stroke.xstart-o_stroke.xend
            dy = stroke.ystart-o_stroke.yend
            distance = sqrt(dx * dx + dy * dy)
        if distance > 0.001:
            stroke_group = StrokeGroup()
            stroke_groups.append(stroke_group)
        stroke_group.addLine(stroke)
        o_stroke = stroke

    # pass2: order stroke, first inside one
    # stroke_groups.sort(inside_cmp)
    # print(stroke_groups[0])
    # stroke_groups.sort()

    # pass3: return order strokes
    order_strokes = []
    for sg in stroke_groups:
        for line in sg.lines:
            order_strokes.append(line)

    return stroke_groups, order_strokes


# =======================================================================
# This routine parses the .cxf font file and builds a font dictionary of
# line segment strokes required to cut each character.
# Arcs (only used in some fonts) are converted to a number of line
# segemnts based on the angular length of the arc. Since the idea of
# this font description is to make it support independant x and y scaling,
# we can not use native arcs in the gcode.
# =======================================================================
def parse(filein, fontfile):
    font = {}
    key = None
    num_cmds = 0
    line_num = 0
    xmax, ymax = 0, 0

    for text in filein:
        # format for a typical letter (lowercase r):
        ##comment, with a blank line after it
        #
        # [r] 3
        # L 0,0,0,6
        # L 0,6,2,6
        # A 2,5,1,0,90
        #
        line_num += 1
        end_char = re.match('^$', text)  # blank line
        if end_char and key:  # save the character to our dictionary
            font[key] = Character(key)

            font[key].stroke_list_groups, font[key].stroke_list = inside_first(stroke_list)

            font[key].xmax = xmax
            # if num_cmds != cmds_read:
            #     print (f"; warning: discrepancy in number of commands {fontfile}, line {line_num}, {num_cmds} != {cmds_read} ")
            # print ("; warning: discrepancy in number of commands %s, line %s, %s != %s ".format(fontfile, line_num, num_cmds, cmds_read))

        version_ = re.match('^# Version:\s+([\d\.]+)', text)
        if version_:
            version = version_.group(1)
            if version.split('.')[0] != '1':
                print ("; Unsupported font version (%s)".format(fontfile))
                sys.exit(1)

        new_cmd = re.match('^\[(.+?)\]\s+(\d+)', text)
        if new_cmd:  # new character
            key = new_cmd.group(1)
            num_cmds = int(new_cmd.group(2))  # for debug
            cmds_read = 0
            stroke_list = []
            xmax, ymax = 0, 0

#        new_cmd = re.match('^\[(\d+)\]\s+(.)', text)
#        if new_cmd:  # new character
#            ccode = int(new_cmd.group(1), 16)

        line_cmd = re.match('^L (.*)', text)
        if line_cmd:
            cmds_read += 1
            coords = line_cmd.group(1)
            coords = [float(n) for n in coords.split(',')]
            stroke_list += [Line(coords)]
            xmax = max(xmax, coords[0], coords[2])
            ymax = max(ymax, coords[1], coords[3])

        arc_cmd = re.match('^A (.*)', text)
        if arc_cmd:
            cmds_read += 1
            coords = arc_cmd.group(1)
            coords = [float(n) for n in coords.split(',')]
            xcenter, ycenter, radius, start_angle, end_angle = coords
            # since font defn has arcs as ccw, we need some font foo
            if (end_angle < start_angle):
                start_angle -= 360.0
            # approximate arc with line seg every 20 degrees
            segs = int((end_angle - start_angle) / 20) + 1
            angleincr = (end_angle - start_angle) / segs
            xstart = cos(start_angle * pi / 180) * radius + xcenter
            ystart = sin(start_angle * pi / 180) * radius + ycenter
            angle = start_angle
            for i in range(segs):
                angle += angleincr
                xend = cos(angle * pi / 180) * radius + xcenter
                yend = sin(angle * pi / 180) * radius + ycenter
                coords = [xstart, ystart, xend, yend]
                stroke_list += [Line(coords)]
                xmax = max(xmax, coords[0], coords[2])
                ymax = max(ymax, coords[1], coords[3])
                xstart = xend
                ystart = yend

        arc_cmd = re.match('^AR (.*)', text)
        if arc_cmd:
            cmds_read += 1
            coords = arc_cmd.group(1)
            coords = [float(n) for n in coords.split(',')]
            xcenter, ycenter, radius, end_angle, start_angle = coords
            # since font defn has arcs as ccw, we need some font foo
            if end_angle < start_angle:
                start_angle -= 360.0
            # approximate arc with line seg every 20 degrees
            segs = int((end_angle - start_angle) / 20) + 1
            angleincr = (end_angle - start_angle) / segs
            xstart = cos(end_angle * pi / 180) * radius + xcenter
            ystart = sin(end_angle * pi / 180) * radius + ycenter
            angle = end_angle
            for i in range(segs):
                angle -= angleincr
                xend = cos(angle * pi / 180) * radius + xcenter
                yend = sin(angle * pi / 180) * radius + ycenter
                coords = [xstart, ystart, xend, yend]
                stroke_list += [Line(coords)]
                xmax = max(xmax, coords[0], coords[2])
                ymax = max(ymax, coords[1], coords[3])
                xstart = xend
                ystart = yend

    return font

# =======================================================================


# def get_xmax():
#     try:
#         return max([s.xmax for s in stroke_list[:]])
#     except ValueError:
#         return 0


# def get_ymax():
#     try:
#         return max([s.ymax for s in stroke_list[:]])
#     except ValueError:
#         return 0


# =======================================================================
def sanitize(string):
    retval = ''
    good = ' ~!@#$%^&*_+=-{}[]|\:;"<>,./?'
    for char in string:
        if char.isalnum() or good.find(char) != -1:
            retval += char
        else:
            retval += (' 0x%02X ' % ord(char))
    return retval


def laser_power(pwr = 0, laser_range = 1000):
    global Spindle
    Spindle = pwr*laser_range
#  return "S%.0f" % (pwr*laser_range)
# =======================================================================


def o9000(p1, p2, p3, Feed):
    p28 = p2*p[1004]
    p29 = p3*p[1005]
    p30 = sqrt(p28*p28 + p29*p29)
    p31 = atan2(p29, p28)
    p32 = p30*cos(p31+p[1006]*Deg2Rad)
    p33 = p30*sin(p31+p[1006]*Deg2Rad)
    if p1 < 0.5:
        out = "M03 S40; \n"
        out += "G00 X%f Y%f; \n" % (p32+p[1002], p33+p[1003])
        out += "M05 S10"
    else:
        out = "G01 X%f Y%f S%.0f F%.0f" % (p32 + p[1002], p33 + p[1003], Spindle, Feed)

    return out


def code(arg, visit, last, fontfile = "normalcxf", XStart = 0, YStart = 0, YLineOffset = 0, XScale = 1, YScale = 1, CSpaceP = 25, WSpaceP = 100, Angle = 0, Mirror = 0, Flip = 0, Feed = 4000, Postamble = "", Preamble = "", laser_operative_pwr = 0):
    global p
    global XLineOffset
    global XIndentList
    global Depth
    global SafeZ
    global output_gcode
    
    String = arg

    str1 = ""
    # erase old gcode as needed
    gcode = []

    if visit != 0:
        # all we need is new X and Y for subsequent lines
        gcode.append("; ===================================================================")
        gcode.append('; Engraving: "%s" ' % (String))
        gcode.append('; Line %d ' % visit)

        p[1002] = XStart
        if XLineOffset:
            if XIndentList.find(str(visit)) != -1:
                p[1002] = XStart + XLineOffset

        p[1003] = YStart - (YLineOffset * visit)

    else:
        gcode.append('; Code generated by text2laser.py ')
        gcode.append('; Engraving: "%s"' % (String))
        gcode.append('; Fontfile: %s ' % (fontfile))

        p[1000] = SafeZ
        p[1001] = Depth

        p[1002] = XStart
        if XLineOffset:
            if XIndentList.find(str(visit)) != -1:
                p1002 = XStart+XLineOffset

        p[1003] = YStart
        p[1004] = XScale
        p[1005] = YScale
        p[1006] = Angle
        gcode.append(Preamble)

    laser_power(0)

    font_word_space = max(font[key].get_xmax() for key in font) * (WSpaceP / 100.0)
    font_char_space = font_word_space * (CSpaceP / 100.0)

    xoffset = 0  # distance along raw string in font units

    # calc a plot scale so we can show about first 15 chars of string
    # in the preview window
    PlotScale = 15 * font['A'].get_xmax() * XScale / 150

    for char in String:
        if char == ' ':
            xoffset += font_word_space
            continue
        try:
            gcode.append(";character '%s'" % sanitize(char))
            first_stroke = True
            for stroke_group in font[char].stroke_list_groups:
                first_stroke = True
                for stroke in stroke_group.lines:
                    x1 = stroke.xstart + xoffset
                    y1 = stroke.ystart
                    if Mirror == 1:
                        x1 = -x1
                    if Flip == 1:
                        y1 = -y1
                    # check and see if we need to move to a new discontinuous start point
                    if first_stroke:
                        first_stroke = False
                        # lift engraver, rapid to start of stroke, drop tool
                        laser_power(0)
                        gcode.append(o9000(0., x1, y1, Feed))
                        laser_power(laser_operative_pwr)
                    x2 = stroke.xend + xoffset
                    y2 = stroke.yend
                    if Mirror == 1:
                        x2 = -x2
                    if Flip == 1:
                        y2 = -y2
                    gcode.append(o9000(1., x2, y2, Feed))

            # move over for next character
            char_width = font[char].get_xmax()
            xoffset += font_char_space + char_width

        except KeyError:
            gcode.append("; warning: character '0x%02X' not found in font defn" % ord(char))

        gcode.append("")  # blank line after every char block

    laser_power(0)

    # finish up with icing
    if last:
        gcode.append(Postamble)

    for line in gcode:
        # sys.stdout.write(line + '\n')
        output_gcode += line + '\n'


################################################################################################################







def convert(stringlist, fontfile = "normal.cxf", XStart = 0, YStart = 0, YLineOffset = 0, XScale = 1, YScale = 1, CSpaceP = 25, WSpaceP = 100, Angle = 0, Mirror = 0, Flip = 0, Feed = 4000, Postamble = "", Preamble = ""):
    debug = 0
    Preamble = """
    G90         ; 
    M03 S40 ;
    """

    Postamble = """
    M5          ; Disable Laser/Spindle
    """
    
    global p
    global XLineOffset
    global XIndentList
    global Depth
    global SafeZ
    global output_gcode
    global font 
    # stringlist = [stringlist]
    stringlist = stringlist.split("\n")
    print(stringlist)
    # file = open(fontfile, encoding="utf-8")
    c_w_d = os.getcwd()
    c_w_d = os.path.join(os.path.join(c_w_d, "cxf_fonts"), fontfile)
    print(c_w_d)
    if not os.path.exists(c_w_d):
        print( "; font not found")
        sys.exit(1)

    file = open(c_w_d, errors="ignore")
    font = parse(file, fontfile)  # build stroke lists from font file
    file.close()
    font_line_height = max(font[key].get_ymax() for key in font)

    if YLineOffset == 0:
        YLineOffset = YScale*font_line_height
    else:
        YLineOffset = YScale * font_line_height * YLineOffset/100.

    output_gcode = ""
    for index, item in enumerate(stringlist):
        code(item, index, index == (len(stringlist) - 1), fontfile, XStart, YStart, YLineOffset, XScale, YScale, CSpaceP, WSpaceP, Angle, Mirror, Flip, Feed, Postamble, Preamble)

    return output_gcode

if __name__ == "__main__":
    strlist = input("enter the sentence")
    g_o = convert(strlist, "cursive.cxf")
    print(g_o)