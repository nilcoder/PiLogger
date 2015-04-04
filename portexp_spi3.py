#!/usr/bin/python
import spidev
import time
import def_1 #MCP23s17 Definitions

retdata = 0     #

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000 #976000 15600000 Max is 31200000 but waveform distorted.
"""
# Address and write 0x40
# Address and read 0x41
# IODIRA - 0=out 1=in
#CMD_WRITE = 0x40 # Device address (A0-A2)
#CMD_READ = 0x41 # Read from dev address 0x00
MCP23x17_IODIRA = 0x00 # Pin direction register location (0=op 1=ip)
MCP23x17_OLATA  = 0x14 # Register for latching outputs GPIOA
MCP23x17_GPIOA  = 0x12 # Register for inputs GPIOA
MCP23x17_IOCON = 0x0A #
MCP23x17_GPIOB = 0x13 #
MCP23x17_GPPUA = 0x0C # Pull up reg for GPIOA  
"""
CMD_WRITE = 0x40 # Device address (A0-A2)
CMD_READ = 0x41 # Read from dev address 0x00
# Set 0-3 GPA pins as outputs and 4-7 inputs by setting
# bits of IODIRA register to 0xF0
spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_IODIRA,0xF0])
spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_IOCON,0x20])
spi.xfer2([def_1.CMD_WRITE,def_1.MCP23x17_GPPUA,0xF0])
# Set 0-3 as output and 4-7 as input bits 0xF0
#spi.xfer([DEVICE,MCP23x17_OLATA,0x0F])

def binary(num, pre='0b', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

while True:
    
    #spi.xfer2([CMD_WRITE,MCP23x17_OLATA,MyData])
    #print MyData
    #time.sleep(0.5)
    print 'start'
    #retdata=spi.xfer2([CMD_READ,MCP23x17_OLATA,0x00])
    #print "OLATA"
    #print binary(retdata[2])
    # read GPIOA
    retdata=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_GPIOA,0x00])
    print "GPIOA"
    print binary(retdata[2])
    # read GPIOB
    retdata=spi.xfer2([def_1.CMD_READ,def_1.MCP23x17_GPIOA,0x00])
    print "GPIOA"
    print binary(retdata[2])
    # read IOCON
    #retdata=spi.xfer2([CMD_READ,MCP23x17_IOCON,0x00])
    #print "IOCON"
    #print binary(retdata[2])
    # read IODIRA
    #retdata=spi.xfer2([CMD_READ,MCP23x17_MCP23x17_IODIRA,0x00])
    #print "IODIRA"
    #print binary(retdata[2])

    #r=spi.xfer2([CMD_READ,MCP23x17_GPIOA,0x00])
    #spi.xfer([DEVICE,MCP23x17_GPIOA,0])
    #ReadReg = spi.readbytes(8)
    #print r#(r[0],r[1],r[2])
    time.sleep(0.5)
