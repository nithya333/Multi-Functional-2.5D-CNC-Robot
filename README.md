# Custom Python Software for GCODE generator, visualiser and sender
## Overview
Affordable precision automation remains out of reach for many due to high costs and operational complexity. This project presents a 2.5D CNC Robot that bridges the gap between digital content and physical output. By combining a high-stability CoreXY mechanism with a multimodal Python-based software suite, this system enables users including those with motor impairments to create with ease.

## Key Features
- Multimodal Input Support: Generate G-code directly from speech commands, formatted text, raster images, or instant screen captures.
- Precision CoreXY Gantry: Utilizes fixed NEMA 17 motors and a crossed-belt routing scheme to minimize moving mass and enhance repeatability to $\pm0.2$ mm.
- Modular "2.5D" Head: Planar X-Y motion coupled with a servo-actuated Z-axis for tool lifting, supporting pens, markers, and 250mW laser modules.
- Unified Software Suite: A single Python environment for G-code Generation, Visual Previews, and Asynchronous Serial Transmission to the hardware.

## Technical Stack
- Microcontroller: Arduino Uno (Atmega328P) running modified GRBL 0.9i firmware.
- Actuators: 2x NEMA 17 Stepper Motors (X-Y) and 1x SG90 Servo (Z-axis).
- Software: Python 3.x, OpenCV (for image processing), svg_to_gcode library, and custom serial drivers.
- Mechanism: Dual M8 linear rods with GT2 timing belts and LM8UU bearings.

## System Architecture
The software pipeline processes inputs through a 3-step engine:
- Parsing: Speech is converted via an offline engine; images are vectorized into SVG.
- G-code Generation: RS-274D compliant commands are rendered using linear interpolation algorithms.
- Visualization & Send: The path is previewed on-screen before being sent serially to the Arduino G-code interpreter.

## Instructions to run
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
