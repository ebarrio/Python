
try:
    import serial
except ImportError:
    print('Pyserial is not installed.')
    raise
import time
import threading

SERIAL_MSG_BYTES = 3
SERIAL_PORT = 'COM11'
SERIAL_BAUD = 115200

def serial_read_thread():
    print('Hello')
    if(zynq_uart.inWaiting()>0):
        msg_read = zynq_uart.read(SERIAL_MSG_BYTES)
        print(msg_read)

if __name__ == "__main__" :
    zynq_uart = serial.Serial(SERIAL_PORT,SERIAL_BAUD)
    time.sleep(1)
    th_1 = threading.Timer(0.5 , serial_read_thread)
    th_1.start()
    time.sleep(10)
    #zynq_uart.close()
