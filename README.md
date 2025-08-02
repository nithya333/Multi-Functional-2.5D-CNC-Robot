# Custom Python Software for GCODE generator, visualiser and sender
* Run: principal.py
* interface.py, interface.ui, ui_functions.py, file_rc.py, file.qrc are necessary
* Helper functions python scripts: "helper_xxx.py" for several functionalities
* Temporary files: Created for parsing/storing input and output, stored as "temp_xxx.xxx"


## Install
* Potrace (https://potrace.sourceforge.net/) 
* ImageMagick (https://imagemagick.org/index.php)


## Librariers
* run pip install -r requiements.txt
* svg-to-gcode library is edited, hence take the zip file from this folder


### Image to Gcode 
Original library: https://pypi.org/project/svg-to-gcode/#history
svg-to-gcode library is edited, hence take the zip file from this folder
Changes marked as [#$# My Change #$#]:
* svg_to_gcode/compiler/interfaces/_abstarct_interface.py => def linear_move_g0()
* svg_to_gcode/compiler/interfaces/_gcode.py => 'G1'->'G01', linear_move_g0()
* svg_to_gcode/compiler/_compiler.py => linear_move -> linear_move_g0()

### Text2Gcode
Reference: https://github.com/fzellini/text2laser/tree/main
This routine parses the .cxf font file and builds a font dictionary of line segment strokes required to cut each character.
Arcs (only used in some fonts) are converted to a number of line segemnts based on the angular length of the arc.


### Gcode Sender
https://grbl-plotter.de/index.php?id=form-setup#flowcontrol
https://github.com/gnea/grbl/wiki/Grbl-v1.1-Interface#streaming-a-g-code-program-to-grbl

Streaming Protocol: Character-Counting [buffer of 128 bytes sent to Arduino, old commands removed after receiving Rx 'ok']
Host PC needs to maintain a standing count of how many characters it has sent to Grbl and then subtract the number of characters corresponding to the line executed with each Grbl response. It always ensures Grbl's serial read buffer is filled, while never overflowing it. It maximizes Grbl's performance by keeping the look-ahead planner buffer full by better utilizing the bi-directional data flow of the serial port.

Grbl has two buffers, the serial receive buffer and the planner buffer where it's actually executing from. I'm assuming that the GUI effectively only sees one buffer, and when grbl moves a line from the receive buffer to the planner buffer is irrelevant, only the "ok" received upon execution. The receive buffer has a 128 char limit and the planner buffer has a 16-line limit.

tqdm part from : https://github.com/ShyBoy233/PyGcodeSender [wrong logic - Not working]

### GCODE Visualisation - gcode2img
https://pypi.org/project/gcode2image/

### Speech Recognition
* Offline speech recognition : https://alphacephei.com/vosk/
* To select the model (VOSK model) : https://alphacephei.com/vosk/models


