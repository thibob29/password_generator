#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from var import *

nb=input("Number of passwords : ")
length=input("Password length : ")

while (idx < nb):
    password=''
    idx+=1
    for i in range(length):
        password += random.choice(chars)
    print password
