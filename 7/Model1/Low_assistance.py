#!/usr/bin/python
#-*- coding: utf-8 -*-

from Driver import Driver

class Low_assistance(Driver):
    def __init__(self):
        self.cruise_control = None
        self.line_keeper = None

