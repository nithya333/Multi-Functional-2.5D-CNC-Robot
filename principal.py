# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 00:43:43 2022

@author: CAD01
"""

import interface
import os
# import pathlib
from ui_functions import *
from helper_svgtogcode import *
# from helper_pyGcodeSender import *
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2, imutils
import sys
import speech_recognition as sr
from ttgLib.TextToGcode import ttg
import subprocess
from math import *
# import nest_asyncio
# nest_asyncio.apply()

import sys
# import time
import helper_text2gcode
import serial
from serial.tools import list_ports
import time
from tqdm import tqdm

# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont
import numpy
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from svg_to_gcode.formulas import linear_map
import io
import keyboard

from vosk import Model, KaldiRecognizer
import pyaudio


import glob
import serial
## CONTROLLING CLASS
########################################################################

class Controller:
    def __init__(self):
        ## SCREEN CONFIGURATION
        # Screen 1 - Main
        self.interface_Window = QtWidgets.QMainWindow()
        self.interface_ui = interface.Ui_MainWindow()
        self.interface_ui.setupUi(self.interface_Window)
       
        ## BUTTON CONFIGURATION
        # side menu buttons
        self.interface_ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 180, True)) # Animation
        self.interface_ui.btn_home.clicked.connect(self.show_pagina1)
        self.interface_ui.btn_info.clicked.connect(self.show_pagina2)

        # image editing buttons
        self.interface_ui.load_btn.clicked.connect(self.loadImage)
        self.interface_ui.sharpness_btn.clicked.connect(self.sharp)
        self.interface_ui.invert_btn.clicked.connect(self.inverter)
        self.interface_ui.resize_btn.clicked.connect(lambda: self.resizeImage(self.image, self.height_px, self.width_px))
        self.interface_ui.speak_btn_img.clicked.connect(self.speech2img)
        self.interface_ui.verticalSlider.valueChanged['int'].connect(self.brightness_value)

        # output file buttons
        self.interface_ui.gcode_btn.clicked.connect(self.image2gcode)
        self.interface_ui.visualise_btn.clicked.connect(self.visualise_gcode)
        self.interface_ui.print_btn.clicked.connect(self.startprinting)
        self.interface_ui.save_btn.clicked.connect(self.savePhoto)
        # self.interface_ui.preview_btn_text.clicked.connect(self.type2text)
        self.interface_ui.preview_btn_text.clicked.connect(self.textgcode_preview)
        self.interface_ui.speak_btn.clicked.connect(self.speech2text)
        # self.interface_ui.set_btn_text.clicked.connect(self.textpng2gcode)
        self.interface_ui.set_btn_text.clicked.connect(self.textgcode_generate)

        # preference buttons options
        self.interface_ui.set_btn.clicked.connect(self.getSpeed)

        # Tool control buttons
        self.interface_ui.pen_up.clicked.connect(self.pen_up)
        self.interface_ui.pen_down.clicked.connect(self.pen_down)
        self.interface_ui.laser_on.clicked.connect(self.laser_on)
        self.interface_ui.laser_off.clicked.connect(self.laser_off)

        
    ## MAIN SCREEN PAGES   
    def show_pagina1(self):
        self.interface_ui.stackedWidget.setCurrentWidget(self.interface_ui.page_1)
        
    def show_pagina2(self):
        self.interface_ui.stackedWidget.setCurrentWidget(self.interface_ui.page_3)
    
    ## DISPLAY FUNCTION
    def show_start(self):
        self.interface_Window.show()
    
    ######################################################################################################################################################################
    # MAIN FUNCTIONS OF THE CODE ########################################################################################################################################
    ######################################################################################################################################################################
    ## LOAD USER IMAGE
    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.jpeg)")[0]
        print(self.filename)
        self.image = cv2.imread(self.filename)
        self.interface_ui.verticalSlider.setValue(0)
        self.setPhoto(self.image)

    ## POSITION THE IMAGE ON THE SCREEN
    def setPhoto(self,image):
        # Places the image in the graphic widget
        self.tmp = image
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        scene = QGraphicsScene()
        a = scene.addPixmap(QtGui.QPixmap.fromImage(image))
        a.setFlag(QGraphicsItem.ItemIsMovable)
        self.interface_ui.graphicsView.setScene(scene)

        # calculates and displays image dimensions
        dimensions = self.tmp.shape
        self.height_px = self.tmp.shape[0]
        self.width_px = self.tmp.shape[1]
        h = round(self.height_px*0.2645833333, 2)
        w = round(self.width_px*0.2645833333, 2)
        print('Image Dimension [px]: ',dimensions)
        print('Image Height    [mm]: ',h)
        print('Image Width     [mm]: ',w) 
        self.interface_ui.height_box.setValue(h)
        self.interface_ui.width_box.setValue(w)
        
    ## RESIZING THE IMAGE
    def resizeImage(self, image, height, width):
        try:
            height_input = round(self.interface_ui.height_box.value()* 3.7795275591, None)
            width_input = round(self.interface_ui.width_box.value()* 3.7795275591, None)
            self.resized = cv2.imread(self.filename)
            if height_input != height and width_input == width:
                new_height = height_input
                self.image = imutils.resize(self.resized, None, new_height)
            elif width_input != width and height_input == height:
                new_width = width_input
                self.image = imutils.resize(self.resized, new_width, None)
            elif width_input != width and height_input != height:
                new_height = height_input
                new_width = width_input
                self.image = imutils.resize(self.resized, new_width, new_height)
            self.interface_ui.verticalSlider.setValue(0)
            self.setPhoto(self.image)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
          
            # setting message for Message Box
            msg.setText("Please insert an image!")
              
            # setting Message box window title
            msg.setWindowTitle("Warning!")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
              
            # start the app
            retval = msg.exec_()
    
    ## FUNCTIONS TO CHANGE IMAGE BLACK AND WHITE LEVEL (brightness_value, changeBrightness e  update)
    # gets the slider value of black and white
    def brightness_value(self,value):
        """ This function will take value from the slider
        	for the brightness from 0 to 99
        """
        self.brightness_value_now = value
        print('Brightness: ',value)
        self.update()

    # receives the value of the brightness_value function and sends the image and value to the function 
    # changeBrightness
    def update(self):
        """ This function will update the photo according to the 
            current values of blur and brightness and set it to photo label.
        """
        
        img_up = self.changeBrightness(self.image,self.brightness_value_now)
        self.setPhoto(img_up)
    
    # changes the image colors to black and white. Returning it to the update function
    def changeBrightness(self,img,value):
            originalImage = img
            grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
            (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, value, 255, cv2.THRESH_BINARY)
            image = imutils.resize(blackAndWhiteImage,width=640)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            return blackAndWhiteImage
    ## 
        
    ## CHANGES IMAGE SHARPNESS
    def sharp(self):
        try:
            sharpness = cv2.detailEnhance(self.tmp, sigma_s=10, sigma_r=0.3)
            self.setPhoto(sharpness)
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
          
            # setting message for Message Box
            msg.setText("Please insert an image!")
              
            # setting Message box window title
            msg.setWindowTitle("Warning!")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
              
            # start the app
            retval = msg.exec_()
            
    ## INVERT IMAGE COLORS
    def inverter(self):
        try:
            img_not = cv2.bitwise_not(self.tmp)
            self.setPhoto(img_not)        
            
        except:
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Warning)
         
           # setting message for Message Box
           msg.setText("Please insert an image!")
             
           # setting Message box window title
           msg.setWindowTitle("Warning!")
             
           # declaring buttons on Message Box
           msg.setStandardButtons(QMessageBox.Ok)
             
           # start the app
           retval = msg.exec_()
    
    ## SAVE THE INSERTED PHOTO IN THE CANVAS, THE PHOTO IS SAVED WITH THE EDITIONS (FORMATS: JPG, PNG, TIFF E BMP)
    def savePhoto(self):
       
        try:
           filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
           cv2.imwrite(filename,self.tmp)
           print('Image saved as:',filename)      
            
        except:
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Warning)
         
           # setting message for Message Box
           msg.setText("Please insert an image!")
             
           # setting Message box window title
           msg.setWindowTitle("Warning!")
             
           # declaring buttons on Message Box
           msg.setStandardButtons(QMessageBox.Ok)
             
           # start the app
           retval = msg.exec_()
                

    ## G CODE GENERATION. CANVA IMAGE IS SAVED IN THE SAME DIRECTORY OF THE PROGRAM,
    ## RUN COMMAND LINES IN COMMAND PROMPT TO USE TOOLS
    ## IMAGE MAGICK AND POTRACE, TO TRANSFORM THE IMAGE INTO SVG. THEN YOU USE THE LIBRARY
    ## SVG_TO_GCODE TO CREATE THE OPERATION CODE
    def image2gcode(self):
        # try:
            cv2.imwrite('temp_imgtogcode_imagem.png',self.tmp)
            
            h = str(round(self.height_px*0.2645833333, 2))
            
            os.system ("magick convert temp_imgtogcode_imagem.png temp_imgtogcode_imagem.pgm")
            
            cmd = print("potrace temp_imgtogcode_imagem.pgm -s -H "+h+"pt -o temp_imgtogcode_imagem.svg")
            os.system("potrace temp_imgtogcode_imagem.pgm -s -H "+h+"pt -o temp_imgtogcode_imagem.svg")
            
            moviment_speed = self.interface_ui.vel_displacement.value()
            # cutting_speed = self.interface_ui.vel_laser.value()
            
            # gcode_compiler = Compiler(CustomInterface, moviment_speed, pass_depth=5)
            gcode_compiler = Compiler(CustomInterface, movement_speed = moviment_speed, cutting_speed = 50, pass_depth=5)
            curves = parse_file('temp_imgtogcode_imagem.svg')
            gcode_compiler.append_curves(curves) 
            gcode_file = QFileDialog.getSaveFileName(filter="gcode(*.gcode)")[0]
            gcode_compiler.compile_to_file(gcode_file)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
          
            # setting message for Message Box
            msg.setText("G-code successfully created!")
              
            # setting Message box window title
            msg.setWindowTitle("Success!")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
              
            # start the app
            retval = msg.exec_()
        # except:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
          
        #     # setting message for Message Box
        #     msg.setText("Por favor, insira uma imagem!")
              
        #     # setting Message box window title
        #     msg.setWindowTitle("Aviso!")
              
        #     # declaring buttons on Message Box
        #     msg.setStandardButtons(QMessageBox.Ok)
              
        #     # start the app
        #     retval = msg.exec_()
    
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    
    def startprinting(self):
        try:
            # print("\n\nEntered\n\n")
            # cv2.imwrite('temp_imgtogcode_imagem.png',self.tmp)
            
            # h = str(round(self.height_px*0.2645833333, 2))
            
            # os.system ("magick convert temp_imgtogcode_imagem.png temp_imgtogcode_imagem.pgm")
            
            # cmd = print("potrace temp_imgtogcode_imagem.pgm -s -H "+h+"pt -o temp_imgtogcode_imagem.svg")
            # os.system("potrace temp_imgtogcode_imagem.pgm -s -H "+h+"pt -o temp_imgtogcode_imagem.svg")
            
            # moviment_speed = self.interface_ui.vel_displacement.value()
            # # cutting_speed = self.interface_ui.vel_laser.value()
            
            # # gcode_compiler = Compiler(CustomInterface, moviment_speed, pass_depth=5)
            # gcode_compiler = Compiler(CustomInterface, movement_speed = moviment_speed, cutting_speed = 50, pass_depth=5)
            # curves = parse_file('temp_imgtogcode_imagem.svg')
            # gcode_compiler.append_curves(curves) 
            # gcode_file = QFileDialog.getSaveFileName(filter="gcode(*.gcode)")[0]
            gcode_file = QFileDialog.getOpenFileName(filter="gcode(*.gcode)")[0]

            available_com_port = self.serial_ports()

            dlg = QDialog()
            dlg.setWindowTitle("Print!")
            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            dlg.buttonBox = QDialogButtonBox(QBtn)
            dlg.buttonBox.accepted.connect(dlg.accept)
            dlg.buttonBox.rejected.connect(dlg.reject)
            combobox2 = QComboBox()
            combobox2.addItems(available_com_port)

            dlg.layout = QVBoxLayout()
            message = QLabel("Choose the COM Port of Arduino")
            dlg.layout.addWidget(message)
            dlg.layout.addWidget(combobox2)
            dlg.layout.addWidget(dlg.buttonBox)
            dlg.setLayout(dlg.layout)
            button = dlg.exec()
            # if button:
            #     print("Yes!")
            # else:
            #     print("No!")
            # print(combobox2.currentText())

            # print(f"name of path : {gcode_file} :")
            # gcode_compiler.compile_to_file(gcode_file)
            
            arduino_port = combobox2.currentText()
            # arduino_port = 'COM3'
            arduino_baudrate = '115200'
            printed = False
            if arduino_port and button:
                print(f"\n\ngcode_file {gcode_file}, arduino_baudrate {arduino_baudrate}, arduino_port {arduino_port}\n\n")
                # self.gcode_sender_func(gcode_file, arduino_baudrate, arduino_port)
                # self.gcode_sender_func('st.gcode')
                status = subprocess.call(['python', 'helper_pyGcodeSender.py', '-p', arduino_port, '-b', arduino_baudrate, gcode_file], shell=True)

                if (status == 0):
                    print("successfully printed")
                    printed = True
                else:
                    print("not printed")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
          
            # setting message for Message Box
            if printed:
                msg.setText("G-code successfully printed!")
            else:
                msg.setText("Print Unsuccessful, Try again")
              
            # setting Message box window title
            msg.setWindowTitle("Print status!")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
              
            # start the app
            retval = msg.exec_()
        except Exception as e:
            print(f"An error occurred: {e}")
        # except:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
          
        #     # setting message for Message Box
        #     msg.setText("Por favor, insira uma imagem!")
              
        #     # setting Message box window title
        #     msg.setWindowTitle("Aviso!")
              
        #     # declaring buttons on Message Box
        #     msg.setStandardButtons(QMessageBox.Ok)
              
        #     # start the app
        #     retval = msg.exec_()

    def replace_strings_in_file(input_file, output_file):##-->addition
        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Replace the desired strings
            # content = content.replace('M03', ';M03').replace('M05', ';M05')
            content = content.replace('M05', '; M05')
            # Write the modified content back to the file
            with open(output_file, 'w') as file:
                file.write(content)

    def visualise_gcode(self):
        gcode_file = QFileDialog.getOpenFileName(filter="gcode(*.gcode)")[0]
        print(gcode_file)
        self.gcode2img(gcode_file)

    def gcode2img(self, gcode_file):
        input_file = gcode_file ##-->addition
        output_file = os.path.join(os.getcwd(),"temp_gcodetoimg_input.gcode")
        image = os.path.join(os.getcwd(),"temp_gcode2img_output.png")
        # image = "temp_gcode2img_output.png"
        # self.replace_strings_in_file(input_file, output_file)  

        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Replace the desired strings
            # content = content.replace('M03', ';M03').replace('M05', ';M05')
            content = content.replace('M05', '; M5').replace('M03', 'M3').replace('G00', 'G0').replace('G01', 'G1').replace(' S0', '')
            # Write the modified content back to the file
            with open(output_file, 'w') as file:
                file.write(content)

        print(f"\n\nOutput file:\t{output_file}")
        print(f"\n\nImage:\t{image}")
        # subprocess.Popen(f"gcode2image --resolution 0.1 --maxintensity 1 --showimage --flip output_file.gcode temp_gcode2img_output.png")  
        p = subprocess.Popen(f"gcode2image --resolution 0.1 --maxintensity 1 --flip temp_gcodetoimg_input.gcode temp_gcode2img_output.png") 
        p.wait()
        im = cv2.imread("temp_gcode2img_output.png")
        self.setPhoto(im)
            
    def speech2text(self):
        # r= sr.Recognizer()
        # try:
        #     # print(sr.Microphone.list_microphone_names())
        #     with sr.Microphone() as source:
        #       r.adjust_for_ambient_noise(source, duration = 1)
        #       print("Say something")
        #       audio= r.listen(source)
        #       # text= r.recognize_google(audio,language="en-IN", show_all = False)
        #       text= r.recognize(audio, show_all = False)
        #       print(text)
        #     # self.text2png(text)
        #     self.text2gcode_singlestroke(text)
     
        # except Exception as e:
        #    print(e)
 
        speech_str = "" 
        with open("temp_speechtotxt_output.txt", "w") as f:
            f.write("")  #Clears the file for fresh entry
        speech_to_text=subprocess.Popen(["python","helper_speech.py"],shell = True)
        speech_to_text.wait()
        with open("temp_speechtotxt_output.txt", 'r') as f:
            speech_str = f.read()
            # speech = f.readlines()
            # return [line.strip() for line in speech]
            # for line in speech:
            #     print(line)
        print(speech_str)
        self.interface_ui.lineEdit_2.setHtml(speech_str)
        # cursor = self.interface_ui.lineEdit_2.textCursor()
        # cursor.insertText(speech_str)
        # os.remove("temp_speechtotxt_output.txt")
        
    def speech2img(self):
        with open("temp_speechtotxt_output.txt", "w") as f:
            f.write("")  #Clears the file for fresh entry
        speech_to_text=subprocess.Popen(["python","helper_speech.py"],shell = True)
        speech_to_text.wait()

        c_w_d = os.path.join(os.getcwd(),"Images")
        dir_list = os.listdir(c_w_d)
        # file_names_without_ext = [".".join(f.split(".")[:-1]) for f in dir_list]
        file_names_without_ext = {".".join(f.split(".")[:-1]) : ".".join(f.split(".")[1:]) for f in dir_list}
        # print(file_names_without_ext)
        with open("temp_speechtotxt_output.txt", 'r') as f:
            speech = f.read()
            # return [line.strip() for line in speech]
        for line in speech.split('\n'):
            if line in file_names_without_ext.keys():
                print(file_names_without_ext[line])
                self.filename = f"{line}.{file_names_without_ext[line]}"
                self.image = cv2.imread(os.path.join(c_w_d, self.filename))
                self.interface_ui.verticalSlider.setValue(0)
                self.setPhoto(self.image)
                break
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
          
            # setting message for Message Box
            msg.setText("Sorry no matching image found!")
              
            # setting Message box window title
            msg.setWindowTitle("Warning!")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
              
            # start the app
            retval = msg.exec_()
    
    def textgcode_preview(self):
        if self.interface_ui.radioButton_voice.isChecked(): # Boolean whether checked or not
            with open("temp_speechtotxt_output.txt", 'r') as f:
                user_text = f.read()
                
        elif self.interface_ui.radioButton_text.isChecked():
            user_text = self.interface_ui.lineEdit_2.toPlainText()
        print(user_text)
        
        gcode_out = self.text2gcode_singlestroke(user_text)
        self.save_gcodefile("temp_text2gcode_preview.gcode", gcode_out)
        self.gcode2img("temp_text2gcode_preview.gcode")
        os.remove("temp_text2gcode_preview.gcode")
    
    def textgcode_generate(self):
        user_text = self.interface_ui.lineEdit_2.toPlainText()
        gcode_out = self.text2gcode_singlestroke(user_text)
        gcode_file = QFileDialog.getSaveFileName(filter="gcode(*.gcode)")[0]
        # self.gcode2img("temp_text2gcode_preview.gcode")
        self.save_gcodefile(gcode_file, gcode_out)
        self.gcode2img(f"{gcode_file}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        # setting message for Message Box
        msg.setText("G-code successfully created!")
            
        # setting Message box window title
        msg.setWindowTitle("Success!")
            
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
            
        # start the app
        retval = msg.exec_()

    def save_gcodefile(self, gcode_file, gcode_out):
        # with open(f"{gcode_file}", "w") as f:
        #     f.seek(0)
        #     f.truncate()
        # with open (f"{gcode_file}", "w") as gcode_out_file:
        #     gcode_out_file.write(gcode_out)
        ff = open(f"{gcode_file}", "w")
        ff.seek(0)
        ff.truncate()
        ff.write(gcode_out)
        ff.close()


    def text2gcode_singlestroke(self, text_input):
        fontfile = "normal.cxf"
        laser_range = 1000.
        laser_operative_pwr = 0.2
        Feed = 1000

        font_selected = self.interface_ui.combo_box.currentText()
        font_size_spin = self.interface_ui.font_size_spinbox.value()
        line_space_spin = self.interface_ui.line_space_spinbox.value()
        angle = self.interface_ui.angle_slider.value()
        char_space = self.interface_ui.char_space_spinbox.value()
        word_space = self.interface_ui.word_space_spinbox.value()
        moviment_speed = self.interface_ui.vel_displacement.value()
        print(text_input, font_selected, font_size_spin,line_space_spin, angle, char_space, word_space)
        gcode_out = ""

        text_parse = text_input.split("\n")
        for i,line in enumerate(text_parse):
            if len(line) * font_size_spin > 290: # If the line exceeds the width of A4 split and put it in next line
                split_char = 290//font_size_spin
                split = line[0:split_char].rfind(" ")
                str1 = line[0:split]
                str2 = line[split+1:]
                text_parse.pop(i)
                text_parse.insert(i, f" {str2}")
                text_parse.insert(i, str1)
            else:
                text_parse[i] = f" {line}"
        text_input = "\n".join(text_parse)
        gcode_out = helper_text2gcode.convert(text_input, fontfile=font_selected, YLineOffset=line_space_spin, XScale=font_size_spin*0.1, YScale=font_size_spin*0.1, CSpaceP=char_space, WSpaceP=word_space, Angle=angle, Feed=moviment_speed)
        return gcode_out

    def type2text(self):
        user_text = self.interface_ui.lineEdit_2.text()
        self.text2png(user_text)

    def text2png(self, text_input):
        moviment_speed = self.interface_ui.vel_displacement.value()

        # temp_whitebg.png image opened using open
        # function and assigned to variable named img
        img = Image.open('temp_whitebg.png')
        
        # Image is converted into editable form using
        # Draw function and assigned to d1
        d1 = ImageDraw.Draw(img)
        
        # font_size = self.interface_ui.user_font_size.value()
        font_selected = self.interface_ui.combo_box.currentText()

        # Font selection from the downloaded file
        c_w_d = os.getcwd() + "\\Fonts\\"
        myFont = ImageFont.truetype(f'{c_w_d}{font_selected}', 50)
        
        # Decide the text location, color and font
        d1.text((65, 10), text_input, fill =(255, 0, 0),font=myFont)
        
        # show and save the image
        # img.show()
        img.save("temp_imgtogcode_results.png")
        
        image = cv2.imread("temp_imgtogcode_results.png")
        self.setPhoto(image)

    def textpng2gcode(self):
        # h = str(round(self.height_px*0.2645833333, 2))
        h = str(round(770*0.2645833333, 2))
        
        os.system ("magick convert temp_imgtogcode_results.png temp_imgtogcode_results.pgm")
        
        cmd = print("potrace temp_imgtogcode_results.pgm -s -H "+h+"pt -o temp_imgtogcode_results.svg")
        os.system("potrace temp_imgtogcode_results.pgm -s -H "+h+"pt -o temp_imgtogcode_results.svg")
        
        moviment_speed = self.interface_ui.vel_displacement.value()
        # cutting_speed = self.interface_ui.vel_laser.value()
        
        # gcode_compiler = Compiler(CustomInterface, moviment_speed, pass_depth=5)
        gcode_compiler = Compiler(CustomInterface, movement_speed = moviment_speed, cutting_speed = 50, pass_depth=5)
        curves = parse_file('temp_imgtogcode_results.svg')
        gcode_compiler.append_curves(curves) 
        gcode_file = QFileDialog.getSaveFileName(filter="gcode(*.gcode)")[0]
        gcode_compiler.compile_to_file(gcode_file)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        # setting message for Message Box
        msg.setText("G-code successfully created!")
            
        # setting Message box window title
        msg.setWindowTitle("Success!")
            
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
            
        # start the app
        retval = msg.exec_()

    def getSpeed(self):
        try:
            self.speed_input = round(self.interface_ui.vel_displacement.value(), None)
            self.sendSpeed()
            # self.interface_ui.label_23.setValue(speed_input)
            print(f"\n\nSPEED = {self.speed_input}\n\n")
        except Exception as e:
           print(f"\n\n{e}\n\n")
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Warning)
         
           # setting message for Message Box
           msg.setText("Speed not accepted!")
             
           # setting Message box window title
           msg.setWindowTitle("Warning!")
             
           # declaring buttons on Message Box
           msg.setStandardButtons(QMessageBox.Ok)
             
           # start the app
           retval = msg.exec_()

    def sendSpeed(self):
        try:
            return (self.speed_input)
        except:
            print("Error occurred while sending speed_input")

    def send_serially(self,cmd):
        baudrate = 115200
        port = 'COM3'

        # Connectting serial port.
        print()
        print(f"Trying to connect to port {port}.")
        try:
            s = serial.Serial(port, baudrate)
            print(f"Port {port} has been successfully connected.")
        except:
            print(f"Cannot connect to port: {port}. Please check it.")
            print(f"The port is highly beening occupied by another progrom or the baud rate is wrong.")
            sys.exit()
        
        s.write(b"\r\n\r\n") # Wake up microcontroller
        time.sleep(1)
        s.reset_input_buffer()
        time.sleep(2)
        s.reset_input_buffer()
        s.write((cmd + '\n').encode()) # Send g-code block to grbl
        time.sleep(0.5)
        while s.inWaiting():
            out_temp = s.readline().strip() # Wait for grbl response
            if out_temp.find(b'ok') >= 0:
                print("    MSG: \"", out_temp, "\"") # Debug response
            else:
                print("error sending gcode\n")
        s.close() 
        

    def pen_up(self):
        pen_up_cmd = "M03 S40"
        self.send_serially(pen_up_cmd)
    
    def pen_down(self):
        pen_down_cmd = "M05 S10"
        self.send_serially(pen_down_cmd)
    
    def laser_on(self):
        laser_on_cmd = "M09"
        self.send_serially(laser_on_cmd)
    
    def laser_off(self):
        laser_off_cmd = "M08"
        self.send_serially(laser_off_cmd)

    # # def print_screen_pressed(self): #
    # def print_screen_pressed(self, e): #
    #     p = subprocess.Popen(["python","helper_snipping.py"]) ##-->addition
    #     p.wait()
    #     im = cv2.imread('temp_screencapt_img.png')
    #     self.setPhoto(im)



# def initiate_capture_to_gcode():
#     global controller
#     im = cv2.imread('temp_screencapt_img.png')
#     controller.setPhoto(im)
#     # Controller.setPhoto(im)

# first_time = True
# if (first_time):
#     app = QtWidgets.QApplication(sys.argv)
#     controller = Controller()
#     controller.show_start()
#     first_time = False

def print_screen_pressed(e):#
    subprocess.Popen(["python","helper_snipping.py"])##-->addition

if __name__ == '__main__':
    # global controller
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_start()
    # keyboard.on_press_key('print screen', controller.print_screen_pressed, suppress=True) #
    keyboard.on_press_key('print screen', print_screen_pressed, suppress=True) #
    sys.exit(app.exec_())
    
    
