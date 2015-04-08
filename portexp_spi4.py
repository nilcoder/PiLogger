#!/usr/bin/python
"""
Test manual entry again
"""

import spidev
import time
import def_1 #MCP23s17 Definitions
import mcp23s17_conf #MCP23s17 register configuration setup

retdata = 0     #
var = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000 #976000 15600000 Max is 31200000 but waveform distorted.

CMD_WRITE = 0x40 # Device address (A0-A2)
CMD_READ = 0x41 # Read from dev address 0x00

#Configure MCP23s17 as per configuration file settings in mcp23s17_conf
mcp23s17_conf.init_mcp23s17()

# Set 0-3 GPA pins as outputs and 4-7 inputs by setting
# bits of IODIRA register to 0xF0
#spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_IODIRA,0xF0]) # 0-3 OP 4-7 IP
#spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_IOCON,0x20]) # do not inc addr pointer (sequential operation disabled)
#spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_GPPUA,0xF0]) # pull up all inputs
# Set 0-3 as output and 4-7 as input bits 0xF0
#spi.xfer([DEVICE,MCP23x17_OLATA,0x0F])

def binary(num, pre='0b', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

def readcmd(cmd,value):
    var=spi.xfer2([def_1.CMD_READ,cmd,value])
    return var

while True:
    
    #spi.xfer2([CMD_WRITE,MCP23x17_OLATA,MyData])
    #print MyData
    #time.sleep(0.5)
    print 'start'
    #readcmd(def_1.MCP23x17_GPPUA,0x00)
    #print binary(var[2])
    # read OLATA - Port A latched input
    var=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_OLATA,0x00])
    print "OLATA"
    print binary(var[2])
    # read GPPUA
    print "GPPUA"
    var=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_GPPUA,0x00])
    print binary(var[2])
    # read GPIOA
    retdata=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_GPIOA,0x00])
    print "GPIOA"
    print binary(var[2])
    # read GPIOB
    retdata=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_GPIOB,0x00])
    print "GPIOB"
    print binary(var[2])
    # read IOCON
    var=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_IOCON,0x00])
    print "IOCON"
    print binary(var[2])
    # read IODIRA
    var=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_IODIRA,0x00])
    print "IODIRA"
    print binary(var[2])

    #r=spi.xfer2([CMD_READ,MCP23x17_GPIOA,0x00])
    #spi.xfer([DEVICE,MCP23x17_GPIOA,0])
    #ReadReg = spi.readbytes(8)
    #print r#(r[0],r[1],r[2])
    time.sleep(0.5)
