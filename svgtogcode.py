# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 19:37:57 2022

@author: alecf
"""

from principal import *
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from svg_to_gcode.formulas import linear_map

class CustomInterface(interfaces.Gcode):
    def __init__(self):
        super().__init__()
        self.fan_speed = 1
        # self.set_my_speed = 2000
        # self.set_my_speed = Controller.sendSpeed()

    # Override the laser_off method such that it also powers off the fan.
    def laser_off(self):
        # return "M107;\n"+"M107;\n"  # Turn off the fan + turn off the laser
        return "M03 S40"  # Pen up

    # Override the set_laser_power method
    def set_laser_power(self, power):
        if power < 0 or power > 1:
            raise ValueError(f"{power} is out of bounds. Laser power must be given between 0 and 1. "
                             f"The interface will scale it correctly.")

        # return f"M106 S255"  # Turn on the fan + change laser power
        return f"M05 S10"  # Pen down

    # Override the set_movement_speed method
    # def set_movement_speed(self, speed):
    #     # self._next_speed = speed
    #     self._next_speed = 2000
    #     return ''


