
try:
    import serial
except ImportError:
    print('Pyserial s not installed.')
    raise
import time
import threading

SERIAL_MSG_BYTES = 3
SERIAL_PORT = 'COM11'
SERIAL_BAUD = 115200

def serial_read_thread():
    while(True):
        if(zynq_uart.inWaiting()>0):
            msg_read = zynq_uart.read(SERIAL_MSG_BYTES)
            print(msg_read)
        time.sleep(0.5)

if __name__ == "__main__" :
    zynq_uart = serial.Serial(SERIAL_PORT,SERIAL_BAUD)
    time.sleep(1)
    th_1 = threading.Thread(target = serial_read_thread)
    th_1.start()
    time.sleep(10)
    zynq_uart.close()
    raise Exception('Program finish')