#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import codecs
import configparser

curdir = os.path.dirname(os.path.realpath(__file__))
pardir = os.path.dirname(curdir)
configPath = os.path.join(pardir, "config")
configFile= os.path.join(configPath, "config.ini")

class ReadConfig():
    def __init__(self):
        fd = open(configFile)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
