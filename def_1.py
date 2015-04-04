#!/usr/bin/python

# MCP23x17 Registers IOCON.BANK=0
MCP23x17_IODIRA = 0x00
MCP23x17_IPOLA = 0x02
MCP23x17_GPINTENA = 0x04
MCP23x17_DEFVALA = 0x06
MCP23x17_INTCONA = 0x08
MCP23x17_IOCON = 0x0A
MCP23x17_GPPUA = 0x0C
MCP23x17_INTFA = 0x0E
MCP23x17_INTCAPA = 0x10
MCP23x17_GPIOA = 0x12
MCP23x17_OLATA = 0x14
MCP23x17_IODIRB = 0x01
MCP23x17_IPOLB = 0x03
MCP23x17_GPINTENB = 0x05
MCP23x17_DEFVALB = 0x07
MCP23x17_INTCONB = 0x09
MCP23x17_IOCONB = 0x0B
MCP23x17_GPPUB = 0x0D
MCP23x17_INTFB = 0x0F
MCP23x17_INTCAPB = 0x11
MCP23x17_GPIOB = 0x13
MCP23x17_OLATB = 0x15

# Bits in the IOCON register
IOCON_UNUSED = 0x01
IOCON_INTPOL = 0x02
IOCON_ODR = 0x04
IOCON_HAEN = 0x08
IOCON_DISSLW = 0x10
IOCON_SEQOP = 0x20
IOCON_MIRROR = 0x40
IOCON_BANK_MODE = 0x80

# SPI Command codes
CMD_WRITE= 0x40
CMD_READ= 0x41

# Default initialisation mode
IOCON_INIT = (IOCON_SEQOP)
