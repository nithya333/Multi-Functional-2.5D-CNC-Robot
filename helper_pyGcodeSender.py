import argparse
import os
import sys
import time
import re
import serial
from serial.tools import list_ports
from tqdm import tqdm
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# RX_BUFFER_SIZE = 128
# RX_BUFFER_SIZE = 60
RX_BUFFER_SIZE = 111


def gcode_sender_func(filename, baudrate, port):
    global RX_BUFFER_SIZE
    transmitted_tx_queue = []
    grbl_buffer_free_size = RX_BUFFER_SIZE - 1
    verbose = True
    # Start of the program.
    print('='*130)
    print("Welcome to use this simple python script to send gcode file using serial.")
    print()

    # Check settings before continue.
    print("Current setting:")
    print(f"\tFilename: {filename}")
    print(f"\tPort name: {port}")
    print(f"\tBaud rate: {baudrate}")
    print()
    # while(1):
    #     command = input("Would you like to continue with these settings?[y/n]")
    #     if command.strip().lower() == 'y':
    #         break
    #     elif command.strip().lower() =='n':
    #         sys.exit()
    #     else:
    #         print("Oooops! Please input yes or no.")
    #         continue

    # Loading codes in file
    try:
        f = open(filename, 'r')
        codes = [code for code in f]
        f.close()
        print()
        print(f"Codes in file {filename} have been loaded successfully.")
    except:
        print(f"Cannot open {filename}.")
        sys.exit()

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
    
    # Sending codes.
    print()
    print("Sending codes.")
    s.write(b"\r\n\r\n") # Wake up microcontroller
    time.sleep(1)
    s.reset_input_buffer()
    time.sleep(3)
    s.reset_input_buffer()
    patternX = r'X(\d*\.\d*)'
    patternY = r'Y(\d*\.\d*)'
    pat = r"MPos:(\d*\.\d*),(\d*\.\d*)"
    X_req = 0
    Y_req = 0
    # Minimize window...
    count_ok = 0
    count_gcode = 0
    g_count = 0
    c_line = []
    l_count = 0
    error_count = 0

    start_time = time.time()
    tqdm4codes = tqdm(codes, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}', unit=" codes", ncols=130)
    for code in tqdm4codes:
        # print(f"~~~ {code} ~~~~")
        tqdm4codes.set_postfix(gcode=code) # Show gcode at postfix
        
        if code.strip().startswith(';') or code.isspace() or len(code) <=0:
            continue
        
        # Send g-code program via a more agressive streaming protocol that forces characters into
        # Grbl's serial read buffer to ensure Grbl has immediate access to the next g-code command
        # rather than wait for the call-response serial protocol to finish. This is done by careful
        # counting of the number of characters sent by the streamer to Grbl and tracking Grbl's 
        # responses, such that we never overflow Grbl's serial read buffer. 
        
        # for line in f:
        l_count += 1 # Iterate line counter
        l_block = re.sub('\s|\(.*?\)','',code).upper() # Strip comments/spaces/new line and capitalize
        # l_block = line.strip()
        c_line.append(len(l_block)+1) # Track number of characters in grbl serial read buffer
        grbl_out = '' 
        while sum(c_line) >= RX_BUFFER_SIZE-1 | s.inWaiting() :
            out_temp = s.readline().strip() # Wait for grbl response
            if out_temp.find(b'ok') < 0 and out_temp.find(b'error') < 0 :
                print("    MSG: \"", out_temp, "\"") # Debug response
            else :
                if out_temp.find(b'error') >= 0 : error_count += 1
                g_count += 1 # Iterate g-code counter
                if verbose: print("  REC<"+str(g_count)+": \"", out_temp, "\"")
                del c_line[0] # Delete the block character count corresponding to the last 'ok'
        s.write((l_block + '\n').encode()) # Send g-code block to grbl
        if verbose: print("SND>"+str(l_count)+": \"" + l_block + "\"")
    # Wait until all responses have been received.
    while l_count > g_count :
        out_temp = s.readline().strip() # Wait for grbl response
        if out_temp.find(b'ok') < 0 and out_temp.find(b'error') < 0 :
            print("    MSG: \"", out_temp, "\"") # Debug response
        else :
            if out_temp.find(b'error') >= 0 : error_count += 1
            g_count += 1 # Iterate g-code counter
            del c_line[0] # Delete the block character count corresponding to the last 'ok'
            if verbose: print("  REC<"+str(g_count)+": \"", out_temp, "\"")

    # Wait for user input after streaming is completed
    print("\nG-code streaming finished!")
    end_time = time.time()
    is_run = False
    print(f" Time elapsed: {end_time-start_time:5.2f} seconds \n")

       
    # transmitted_flag = False
    # count_gcode += 1

    # while(not transmitted_flag): # Wait untile the former gcode has been completed.
    #     if (len(code) <= grbl_buffer_free_size):
    #         print(f"TX << {count_gcode}: {len(code)}/{grbl_buffer_free_size}: {code}")
    #         s.write((code + '\n').encode())
    #         grbl_buffer_free_size -= len(code)
    #         transmitted_tx_queue.append(code)
    #         transmitted_flag = True

    #     if (s.in_waiting > 0):
    #         reply = s.readline()

    #         if reply.startswith(b'ok'):
    #             count_ok += 1
    #             cmd = transmitted_tx_queue.pop(0)
    #             print(f"RX >> {count_ok}: {len(cmd)}/{grbl_buffer_free_size}: {reply}: {cmd}")
    #             grbl_buffer_free_size += len(cmd)
    #         else:
    #             print(f"RX >> {count_ok}: {reply}")
    #     else:
    #         time.sleep(0.1)

    s.close() 
    print()
    print(f"no of lines printed {g_count}")
    print("All codes have been sent successfully.")
    print("Congratulation!!!")

    # End of the program.
    print()
    print("Welcome to use this simple script again. Best wishes.")
    print('='*130)

if __name__ =="__main__":
    parser = argparse.ArgumentParser(
        prog="helper_pyGcodeSender",
        description="A simple python script to send gcode file using serial to various machines."
    )

    parser.add_argument("filename", help="gcode to be sent")
    parser.add_argument("-p", "--port", help="serial port", metavar="port name")
    parser.add_argument("-b", "--baudrate", default=115200, type=int, help="baud rate, default 115200", metavar="baud rate")

    args = parser.parse_args()

    # Validate the filename.
    if os.path.exists(args.filename): # Whether exist.
        if os.path.isfile(args.filename): # Whether is a file.
            if args.filename.strip().lower().endswith(".gcode"): # Whether is a gcode file.
                pass
            else:
                print(f"{args.filename} is highly not a gcode file(end with .gcode). Please check it.")
                sys.exit()
        else:
            print(f"{args.filename} is not a file. Please check the filename.")
            sys.exit()
    else:
        print(f"{args.filename} does not exist. Please check the filename.")
        sys.exit()

    # Automatically detect available serial port.
    if len(list_ports.comports()) == 0: # No port detected.
        print("There are no ports available. Please check the connection.")
        sys.exit()
    elif len(list_ports.comports()) == 1: # Only one port detected.
        if args.port is None:
            port = list_ports.comports()[0].name
        else:
            ports = [list_ports.comports()[i].name.strip().lower() for i in range(len(list_ports.comports()))]
            if args.port.strip().lower() in ports:
                port = args.port
            else:
                print(f"Port {args.port} is not in available port list. Please check spelling.")
                print("Available port names:")
                for p in list_ports.comports():
                    print(p.name)
                sys.exit()
    else: # More than one ports are detected, need to specify the port name manually.
        if args.port is None:
            print("There are many ports available. Please specify the port name manually.")
            print("Available port names:")
            for p in list_ports.comports():
                print(p.name)
            sys.exit()
        else:
            ports = [list_ports.comports()[i].name.strip().lower() for i in range(len(list_ports.comports()))]
            if args.port.strip().lower() in ports:
                port = args.port
            else:
                print(f"Port {args.port} is not in available port list. Please check spelling.")
                print("Available port names:")
                for p in list_ports.comports():
                    print(p.name)
                sys.exit()
    gcode_sender_func(args.filename, args.baudrate, port)
    
