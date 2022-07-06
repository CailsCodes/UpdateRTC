from distutils.core import setup
import py2exe
from serial.tools import list_ports
import serial, time

setup(console=['updateRTC.py'])