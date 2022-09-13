##################################################################################
# Title                 :   Example Micropython code
# Filename              :   main.py
# Author                :   JEHP
# Origin Date           :   13/09/2022
# Version               :   0.8.0
# Copyright             :   Jorge Higuera 
# Email                 :   jhiguera@ieee.org
# All Rights Reserved
# My_Pythonboard is connected to COM19 115200 bps 
# MicroPython V1.12 on 2019-12-20 PYBv1.1 with STM32F405RG 

#Libraries
import pyb
import time
#import micropython # For emergency exception buffer

#Peripherals
from pyb import Pin, LED, UART, ADC
#from pyb import Timer
#from pyb import uarray
#import array
#micropython.alloc_emergency_exception_buf(100)

#Global variables
#--------------------------------------------------------------
cmdVEGA07 = 'b'         # data format char
#FSM = 'b'

#buf = bytearray(10)
#buf[0:9] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Configure Uart6: Y2: Rx / Y1:Tx
#---------------------------------------------------------------
uart1 = pyb.UART(6)
uart1.init(115200, bits=8, parity=None, stop=1)

# GPIO configuration: outputs related to Enable Pins
#---------------------------------------------------------------
# EN_24Vin: X1
x1_gpio_out = pyb.Pin('X1', Pin.OUT_PP)
x1_gpio_out.low()

# EN_3V3: X2
#x2_gpio_out = pyb.Pin('X2', Pin.OUT_PP)
#x2_gpio_out.low()


# EN_3V3: X3
x3_gpio_out = pyb.Pin('X3', Pin.OUT_PP)
x3_gpio_out.low()

#x3_gpio_out = Pin('X3', Pin.OUT)
#x3_gpio_out.low()

# EN_LED_RED: X4
x4_gpio_out = pyb.Pin('X4', Pin.OUT_PP)
x4_gpio_out.low()

# EN_LED_Lime Botton: X5
x5_gpio_out = pyb.Pin('X5', Pin.OUT_PP)
x5_gpio_out.low()

# EN_LED_Lime Top: X6
x6_gpio_out = pyb.Pin('X6', Pin.OUT_PP)
x6_gpio_out.low()

# EN_LED_PC_AMBER: X7
x7_gpio_out = pyb.Pin('X7', Pin.OUT_PP)
x7_gpio_out.low()

# EN_LED_Green: X8
x8_gpio_out = pyb.Pin('X8', Pin.OUT_PP)
x8_gpio_out.low()

# EN_LED_CYAN: Y9
y9_gpio_out = pyb.Pin('Y9', Pin.OUT_PP)
y9_gpio_out.low()

# EN_LED_Blue: Y10
y10_gpio_out = pyb.Pin('Y10', Pin.OUT_PP)
y10_gpio_out.low()

# EN_LED_Royal_Blue: Y11
y11_gpio_out = pyb.Pin('Y11', Pin.OUT_PP)
y11_gpio_out.low()



# GPIO configuration: Input related to ADC signal channels
#---------------------------------------------------------------

# ADC1: 24Vin channel 
adc1 = pyb.ADC(Pin('X19'))

# ADC2: 24Vcc channel 
adc2 = pyb.ADC(Pin('X20'))
#adc2.read() # read value, 0-4095

# ADC3: 24Vled channel 
adc3 = pyb.ADC(Pin('X21'))
#adc3.read() # read value, 0-4095

# ADC4: 5VSensor channel (Voltage V+ USB from Pybv1.1)
adc4 = pyb.ADC(Pin('X22'))
#adc4.read() # read value, 0-4095

# ADC5: SENSE_I_LED channel  # read value, 0-4095 current sensor
adc5 = pyb.ADC(Pin('X11'))

# ADC6: TEMPERATURE Rt1 sensor channel 
adc6 = pyb.ADC(Pin('X12'))
#adc6.read() # read value, 0-4095

#tim = pyb.Timer(6, freq=10)         # create a timer running at 10Hz
#adc1.read() # read value, 0-4095



# Visualization: LED Configuration  # 1=red, 2=green, 3=yellow, 4=blue
#---------------------------------------------------------------
led_red = pyb.LED(1)        #Led_red (ON/OFF)
led_green = pyb.LED(2)      #Led_green (ON/OFF)
led_yellow = pyb.LED(3)     #Led_yellow (ON/OFF)
led_blue = pyb.LED(4)       #Led_blue(ON/OFF)


#Command definitions
#----------------------------------------------------------------

def Menu_VEGA07_LED_Board(cmdVEGA07):
    #Commands to test VEGA07-SLIM LED BOARD
    

        if cmdVEGA07 == b'1':
            Enable_on_24Vin()
        elif cmdVEGA07 == b'2': 
            Enable_off_24Vin()
        elif cmdVEGA07 == b'3':
            Enable_on_X3()
        elif cmdVEGA07 == b'4':
            Enable_off_X3()
        elif cmdVEGA07 == b'5':
            Read_ADC1_24Vin()  
        else:
            Error_command()
            
#-------------------------------------------------------------------------
#  Enable/disable Power supply control lines
#-------------------------------------------------------------------------
def Enable_on_24Vin():
    #Enable GPIO X1: EN_24Vin
    x1_gpio_out.high()
    #LED signal
    led_green.toggle()
    #UART1 response
    uart1.write('X1: 24Vin power supply enabled')
    uart1.write("\n")

def Enable_off_24Vin():
    #Disable GPIO X1: EN_24Vin
    x1_gpio_out.low()
    #LED signal
    led_green.toggle()
    #UART1 response
    uart1.write('X1: 24Vin power supply disabled')
    uart1.write("\n")
    

def Enable_on_X3():
    #Enable GPIO X3
    x3_gpio_out.high()
    #LED signal
    led_yellow.toggle()
    #UART1 response
    uart1.write(' X3: Vcontrol Jack (4,05V) enabled')
    uart1.write("\n")

def Enable_off_X3():
    #Disable GPIO X3
    x3_gpio_out.low()
    #LED signal
    led_yellow.toggle()
    #UART1 response
    uart1.write('X3: Vcontrol Jack (4,05V) disabled ')
    uart1.write("\n")

#-------------------------------------------------------------------------
# LED Channel control
#-------------------------------------------------------------------------

def Enable_on_Y11_Royal_Blue():
    #Enable GPIO Y11: LED ROYAL BLUE
    y11_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP8: LED Royal Blue was Enabled')
    uart1.write("\n")

def Enable_off_Y11_Royal_Blue():
    #Disable GPIO Y11: LED ROYAL BLUE
    y11_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP8: LED Royal Blue was Disabled')
    uart1.write("\n")

def Enable_on_Y10_Blue():
    #Enable GPIO Y10: LED BLUE
    y10_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP7: LED Blue Enabled')
    uart1.write("\n")

def Enable_off_Y10_Blue():
    #Disable GPIO Y10: LED BLUE
    y10_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP7: LED Blue Disabled')
    uart1.write("\n")

def Enable_on_Y9_Cyan():
    #Enable GPIO Y9: LED CYAN
    y9_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP6: LED Cyan Enabled')
    uart1.write("\n")

def Enable_off_Y9_Cyan():
    #Disable GPIO Y9: LED CYAN
    y9_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP6: LED Cyan Disabled')
    uart1.write("\n")

def Enable_on_X8_Green():
    #Enable GPIO X8: LED GREEN
    x8_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP5: LED Green Enabled')
    uart1.write("\n")

def Enable_off_X8_Green():
    #Disable GPIO X8: LED GREEN
    x8_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP5: LED Green Disabled')
    uart1.write("\n")

def Enable_on_X7_PC_AMBER():
    #Enable GPIO X7: LED PC_AMBER
    x7_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP4: LED PC AMBER Enabled')
    uart1.write("\n")

def Enable_off_X7_PC_AMBER():
    #Disable GPIO X7: LED PC_AMBER
    x7_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP4: LED PC AMBER Disabled')
    uart1.write("\n")

def Enable_on_X6_LIME_TOP():
    #Enable GPIO X6: LED LIME TOP
    x6_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP3: LED LIME TOP Enabled')
    uart1.write("\n")

def Enable_off_X6_LIME_TOP():
    #Disable GPIO X6: LED LIME TOP
    x6_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP3: LED LIME TOP Disabled')
    uart1.write("\n")

def Enable_on_X5_LIME_BOTTOM():
    #Enable GPIO X5: LED LIME_BOTTON
    x5_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP2: LED LIME BOTTOM Enabled')
    uart1.write("\n")

def Enable_off_X5_LIME_BOTTOM():
    #Disable GPIO X5: LED LIME BOTTOM
    x5_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP2: LED LIME BOTTOM Disabled')
    uart1.write("\n")

def Enable_on_X4_RED():
    #Enable GPIO X4: LED RED
    x4_gpio_out.high()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP1: LED RED Enabled')
    uart1.write("\n")

def Enable_off_X4_RED():
    #Disable GPIO X4: LED RED
    x4_gpio_out.low()
    #LED signal
    led_blue.toggle()
    #UART1 response
    uart1.write('TP1: LED RED Disabled')
    uart1.write("\n")

#-------------------------------------------------------------------------
#  Read ADC channels
#-------------------------------------------------------------------------

def Read_ADC1_24Vin():
        
    #buf = bytearray(10)                 # creat a buffer to store the samples of 8 bits
    #adc1.read_timed(buf, tim)           # sample 100 values, taking 10s
    #uart1.write(buf)

    adc1_value = adc1.read()            # 12 bit values
    uart1.write(str(adc1_value))
    uart1.write("\n")

def Read_ADC2_24Vcc():
        
    adc2_value = adc2.read()            # 12 bit values
    uart1.write(str(adc2_value))
    uart1.write("\n")

def Read_ADC3_24Vled():
        
    adc3_value = adc3.read()            # 12 bit values
    uart1.write(str(adc3_value))
    uart1.write("\n")

def Read_ADC4_SENSE_USB_5V():
        
    adc4_value = adc5.read()            # 12 bit values
    uart1.write(str(adc4_value))
    uart1.write("\n")

def Read_ADC5_SENSE_I_LED():
        
    adc5_value = adc5.read()            # 12 bit values
    uart1.write(str(adc5_value))
    uart1.write("\n")

def Read_ADC6_temperature():
        
    adc6_value = adc6.read()            # 12 bit values
    uart1.write(str(adc6_value))
    uart1.write("\n")


def Error_command():
    led_red.on()
    led_green.off()
    led_yellow.off()
    led_blue.off()
    uart1.write("Error! Comando desconocido:  ")
    uart1.write(cmdVEGA07)
    uart1.write("\n")

def leds_blinking_all():
    led_red.toggle()
    led_green.toggle()
    led_yellow.toggle()
    led_blue.toggle()

def init_message():

    leds_blinking_all()
    uart1.write("LEDMOTIVE AUTOMATED TEST PLATFORM (LATEP)")
    uart1.write("\n")
    uart1.write("VEGA07-SLIM LED PCB models: 190018-10 / 190018-15")
    uart1.write("\n")
    uart1.write("FW ver: 0.8")
    uart1.write("\n")
    uart1.write("HW ver: 1.0")
    uart1.write("\n")
    uart1.write("LEDMOTIVE Technologies SL, July 2021")
    uart1.write("\n")

    uart1.write("Menu de comandos")
    uart1.write("\n")

    uart1.write(" (1): Habilitar tension de 24VDC")
    uart1.write("\n")

    uart1.write(" (2): Deshabilitar tension de 24VDC")
    uart1.write("\n")

    uart1.write(" (3): Habilitar tension de control jack (4,05VDC)")
    uart1.write("\n")

    uart1.write(" (4): Deshabilitar tension de control jack (4,05VDC)")
    uart1.write("\n")

    uart1.write(" (5): Leer tension analogica 24VDC")
    uart1.write("\n")

    uart1.write(" (A): Habilitar canal LEDs Royal Blue")
    uart1.write("\n")

    uart1.write(" (B): Deshabilitar canal LEDs Royal Blue")
    uart1.write("\n")

    uart1.write(" (C): Habilitar canal LEDs  Blue")
    uart1.write("\n")

    uart1.write(" (D): Deshabilitar canal LEDs Blue")
    uart1.write("\n")

    uart1.write(" (E): Habilitar canal LEDs  Cyan")
    uart1.write("\n")

    uart1.write(" (F): Deshabilitar canal LEDs Cyan")
    uart1.write("\n")

    uart1.write(" (G): Deshabilitar canal LEDs  Verdes")
    uart1.write("\n")

    uart1.write(" (H): Deshabilitar canal LEDs Verdes")
    uart1.write("\n")

    uart1.write(" (I): Deshabilitar canal LEDs  PC Ambar")
    uart1.write("\n")

    uart1.write(" (J): Deshabilitar canal LEDs PC Ambar")
    uart1.write("\n")

    uart1.write(" (K): Habilitar canal LEDs Lima Top")
    uart1.write("\n")

    uart1.write(" (L): Deshabilitar canal LEDs Lima Top")
    uart1.write("\n")

    uart1.write(" (M): Habilitar canal LEDs Lima Bottom")
    uart1.write("\n")

    uart1.write(" (N): Deshabilitar canal LEDs Lima Bottom")
    uart1.write("\n")

    uart1.write(" (O): Habilitar canal LEDs Rojos")
    uart1.write("\n")

    uart1.write(" (P): Deshabilitar canal LEDs Rojos")
    uart1.write("\n")




    pyb.delay(3000)
    leds_blinking_all()
    

#--------------------------------------------------------------
#Main program using Round-robin scheduling
#---------------------------------------------------------------


init_message()

while True:
    if uart1.any() > 0:
        cmdVEGA07 = uart1.readline()
        if cmdVEGA07 == b'1':
            Enable_on_24Vin()  
        elif cmdVEGA07 == b'2':
            Enable_off_24Vin()
        elif cmdVEGA07 == b'3':
            Enable_on_X3()
        elif cmdVEGA07 == b'4':
            Enable_off_X3()
        elif cmdVEGA07 == b'5':
            Read_ADC1_24Vin()
        elif cmdVEGA07 == b'6':
            Read_ADC2_24Vcc() 
        elif cmdVEGA07 == b'7':
            Read_ADC3_24Vled()
        elif cmdVEGA07 == b'0':
            Read_ADC4_SENSE_USB_5V()
        elif cmdVEGA07 == b'8':
            Read_ADC5_SENSE_I_LED()
        elif cmdVEGA07 == b'9':
            Read_ADC6_temperature()
        elif cmdVEGA07 == b'A':
            Enable_on_Y11_Royal_Blue()
        elif cmdVEGA07 == b'B':
            Enable_off_Y11_Royal_Blue()
        elif cmdVEGA07 == b'C':
            Enable_on_Y10_Blue()
        elif cmdVEGA07 == b'D':
            Enable_off_Y10_Blue()
        elif cmdVEGA07 == b'E':
            Enable_on_Y9_Cyan()
        elif cmdVEGA07 == b'F':
            Enable_off_Y9_Cyan()
        elif cmdVEGA07 == b'G':
            Enable_on_X8_Green()
        elif cmdVEGA07 == b'H':
            Enable_off_X8_Green()
        elif cmdVEGA07 == b'I':
            Enable_on_X7_PC_AMBER()
        elif cmdVEGA07 == b'J':
            Enable_off_X7_PC_AMBER()
        elif cmdVEGA07 == b'K':
            Enable_on_X6_LIME_TOP()
        elif cmdVEGA07 == b'L':
            Enable_off_X6_LIME_TOP()
        elif cmdVEGA07 == b'M':
            Enable_on_X5_LIME_BOTTOM()
        elif cmdVEGA07 == b'N':
            Enable_off_X5_LIME_BOTTOM()
        elif cmdVEGA07 == b'O':
            Enable_on_X4_RED()
        elif cmdVEGA07 == b'P':
            Enable_off_X4_RED()              
        else:
            led_red.toggle()
            uart1.write('Comando desconocido: ')
            uart1.write(cmdVEGA07)