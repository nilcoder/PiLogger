#!/usr/bin/python
import spidev
import time
import def_1 #MCP23s17 Definitions

# This file is used to configure the MCP23s17
# Assumes the register definitions are imported into script using this file
# Set the data to the required configuration
# These settings will be imported for setting the following registers during
#  an initialisation routine

IODIRA = 0xF0   #used in testing only
IPOLA = 0x00
GPINTENA = 0x00
DEFVALA = 0x00
INTCONA = 0x00
IOCON = 0x20    #sequential addressing disabled
GPPUA = 0xF0    #used in testing only
OLATA = 0x00

IODIRB = 0xFF
IPOLB = 0x00
GPINTENB = 0x00
DEFVALB = 0x00
INTCONB = 0x00
IOCONB = 0x00
GPPUB = 0x00
OLATB = 0x00

CMD_WRITE= 0x40
CMD_READ= 0x41
"""
IOCON BITS
bit 7 BANK: Controls how the registers are addressed
1 = The registers associated with each port are separated into different banks
0 = The registers are in the same bank (addresses are sequential)
bit 6 MIRROR: INT Pins Mirror bit
1 = The INT pins are internally connected
0 = The INT pins are not connected. INTA is associated with PortA and INTB is associated with PortB
bit 5 SEQOP: Sequential Operation mode bit.
1 = Sequential operation disabled, address pointer does not increment.
0 = Sequential operation enabled, address pointer increments.
bit 4 DISSLW: Slew Rate control bit for SDA output.
1 = Slew rate disabled.
0 = Slew rate enabled.
bit 3 HAEN: Hardware Address Enable bit (MCP23S17 only).
Address pins are always enabled on MCP23017.
1 = Enables the MCP23S17 address pins.
0 = Disables the MCP23S17 address pins.
bit 2 ODR: This bit configures the INT pin as an open-drain output.
1 = Open-drain output (overrides the INTPOL bit).
0 = Active driver output (INTPOL bit sets the polarity).
bit 1 INTPOL: This bit sets the polarity of the INT output pin.
1 = Active-high.
0 = Active-low.
bit 0 Unimplemented: Read as a 0

GPPU BITS
PU7:PU0: These bits control the weak pull-up resistors on each pin (when configured as an input)
<7:0>.
1 = Pull-up enabled.
0 = Pull-up disabled.

IOCON.BANK = 1 or 0
BANK0   BANK1
00h     00h     IODIRA
10h     01h     IODIRB
01h     02h     IPOLA
11h     03h     IPOLB
02h     04h     GPINTENA
12h     05h     GPINTENB
03h     06h     DEFVALA
13h     07h     DEFVALB
04h     08h     INTCONA
14h     09h     INTCONB
05h     0Ah     IOCON
15h     0Bh     IOCON
06h     0Ch     GPPUA
16h     0Dh     GPPUB
07h     0Eh     INTFA
17h     0Fh     INTFB
08h     10h     INTCAPA
18h     11h     INTCAPB
09h     12h     GPIOA
19h     13h     GPIOB
0Ah     14h     OLATA
1Ah     15h     OLATB
"""


def init_mcp23s17():
    
# Initialise the MCP23s17 with above register configurations
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1000000 #976000 15600000 Max is 31200000 but waveform distorted.

    print "***Start setting register configs***"
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IOCON,IOCON])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IODIRA,IODIRA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IPOLA,IPOLA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_GPINTENA,GPINTENA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_DEFVALA,DEFVALA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_INTCONA,INTCONA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_GPPUA,GPPUA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_OLATA,OLATA])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IODIRB,IODIRB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IPOLB,IPOLB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_GPINTENB,GPINTENB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_DEFVALB,DEFVALB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_INTCONB,INTCONB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_IOCONB,IOCONB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_GPPUB,GPPUB])
    spi.xfer2([CMD_WRITE,def_1.MCP23x17_OLATB,OLATB])
    print "***Done setting register configs***"
    spi.close
    return ()