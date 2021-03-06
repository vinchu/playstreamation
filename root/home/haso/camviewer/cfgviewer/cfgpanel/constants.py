# coding=utf-8

# Copyright (C) 2016. Haso S.C. J. Macioszek & A. Paszek
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

ZMQ_PORT = '5555'

PIN_ENTER = 26
PIN_ESC = 17
PIN_UP = 14
PIN_DOWN = 15
PIN_LEFT = 19
PIN_RIGHT = 04

BTN_SIGNAL_ESC = 'ESC'
BTN_SIGNAL_ENTER = 'ENTER'
BTN_SIGNAL_LEFT = 'LEFT'
BTN_SIGNAL_RIGHT = 'RIGHT'
BTN_SIGNAL_UP = 'UP'
BTN_SIGNAL_DOWN = 'DOWN'

AUTO_CLOSE_TIME = 20
CYCLE_TIME_DEFAULT = 10
CYCLE_TIME_MAX_INCR = 3600

MAX_CAM_AMOUNT = 4

WIN_SINGLE = '0,0,1060,600'

KEYWORD_NETMASK = "netmask"
KEYWORD_ADDRESS = "address"

CFG_VERSION_FILENAME = "version.txt"
CFG_CAM_IP_FILENAME = "config_cam.cfg"
CFG_MON_IP_FILENAME = "config_mon.cfg"
CFG_SERIAL_FILENAME = "config_serial.cfg"

DEFAULT_SERIAL = "not defined"
DEFAULT_VERSION = 'X.X'

MON_ADDRESS_NOT_CONFIGURED = "not configured"
MON_NETMASK_NOT_CONFIGURED = "not configured"

EMPTY_CONFIG_CONTENT = '||||||\n||||||\n||||||\n||||||\n'

CFG_PATH = '../'
ADMIN_PASS = 'secret'

ERR_MSG_DETAILS = u'%s - invalid value (%s) - required format is: %s'
ERR_MSG_VALIDATION = u'There were validation errors. New configuration values were not saved.'

REGEX_IP_FORMAT = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
REQUIRED_FORMAT_IP_ADDRESS = '<0-255>.<0-255>.<0-255>.<0-255>'

REGEX_IP_ADDRESS = r'%s' % REGEX_IP_FORMAT
REGEX_MON_ADDRESS = r'%s%s' % (KEYWORD_ADDRESS, REGEX_IP_FORMAT)
REGEX_MON_NETMASK = r'%s%s' % (KEYWORD_NETMASK, REGEX_IP_FORMAT)

CAM_STATUS_INIT = '...inicjalizacja...'  # Default value
CAM_STATUS_UNDEFINED = ''  # used when address IP is not defined for camera
CAM_STATUS_OK = 'TAK'
CAM_STATUS_NOT_CONNECTED = 'NIE'
CAM_STATUS_CON_ERROR = 'ERR'
