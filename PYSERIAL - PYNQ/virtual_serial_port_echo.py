"""

    --------- VIRTUAL SERIAL PORT DRIVER (VSPD) PYTHON TESTER ---------

        - Run VSPD and pair defined SERIAL_PORT_1 with SERIAL_PORT_2
        - Install with pip pyserial and run the python file

"""
import serial
import time
import threading
import sys
SERIAL_MSG = 'hello world'
SERIAL_MSG_BYTES = len(SERIAL_MSG)
SERIAL_PORT_1 = 'COM1'
SERIAL_PORT_2 = 'COM2'
SERIAL_BAUD = 115200

def serial_echo_thread():
    ser1.write(SERIAL_MSG.encode())
    while(True):
        if(ser1.isOpen() and ser2.isOpen()):
            if(ser2.inWaiting()>0):
                time.sleep(0.5)
                msg_read = ser2.read(SERIAL_MSG_BYTES)
                print(msg_read)
                ser2.write(msg_read)
                time.sleep(0.5)
                msg_read = ser1.read(SERIAL_MSG_BYTES)
                print(msg_read)
                ser1.write(msg_read)
                

if __name__ == "__main__" :
    ser1 = serial.Serial(SERIAL_PORT_1,SERIAL_BAUD)
    ser2 = serial.Serial(SERIAL_PORT_2,SERIAL_BAUD)
    time.sleep(1)
    th_1 = threading.Thread(target = serial_read_thread)

    th_1.start()
    time.sleep(60)

    ser1.close()
    ser2.close()
    print('Program finish')
    #raise Exception('Program finish')
    sys.exit()
