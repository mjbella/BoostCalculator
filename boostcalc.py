#!/usr/bin/env python

import sys
import math
import pdb

try:
    vin_max = float(raw_input("What is the max input voltage?\r\n"))
    vin_min = float(raw_input("What is the min input voltage?\r\n"))
    vout = float(raw_input("What is the output voltage??\r\n"))
    eff = float(raw_input("What is your efficency?!?!?!?!???!!\r\n"))
    fsw = float(raw_input("What is the switching frequency!?\r\n"))
    iout = float(raw_input("What is output current?\r\n"))
except:
    print "Use NUMBERS you DUMMY!"    
    sys.exit()

eff = eff / 100.0

D = 1 - ( ( vin_min * eff ) / vout )

# TODO: Change this number later!
dI_l_est = 0.2 * iout * ( vout / vin_min )

# TODO: Change this to use the nominal input voltage later!!!!
L = ( vin_min * ( vout - vin_min ) ) / ( dI_l_est * fsw * vout )

dI_l = (vin_min * D) / (fsw * L)

# Peak Inductor Current (http://www.ti.com/lit/ds/symlink/tps630251.pdf)
IL_peak = (iout / (eff * (1 - D))) + ((vin_max * D) / (2 * fsw * L))

i_sw_max = (dI_l / 2) + (iout / (1 - D))

print "Your duty cycle will be: %.2f" % D
print "Your estimated ripple current will be: %.2f" % dI_l_est
print "Your inductor needs to be at least: %.2f uH" % (L * 1e6)
print "Your (real) ripple current will be: %.2f" % dI_l
print "Your inductor needs to have a saturation current higher than: %.2f" % IL_peak
print "Your max switch current is going to be: %.2f" % i_sw_max

