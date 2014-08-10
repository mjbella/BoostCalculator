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
    Lmult= float(raw_input("How much do you want to oversize your inductor by (%)"))
except:
    print "Use NUMBERS you DUMMY!"    
    sys.exit()

Lmult = Lmult / 100
eff = eff / 100.0

D = 1 - ( ( vin_min * eff ) / vout )

print "RESULTS:"

print "Your total duty cycle will be: %.2f" % D

def run_calcs(Nph):
    print "For %d phases..." % Nph
    
    # Average current needed from each phase
    I_l_ph = iout / (Nph * (1 - D))
    
    # TODO: Change this number later!
    dI_l_est = 0.2 * I_l_ph * (1 / D)

    # TODO: Change this to use the nominal input voltage later!!!!
    L = ( vin_min * ( vout - vin_min ) ) / ( dI_l_est * fsw * vout )
    
    L = L * (1 + Lmult)
    
    dI_l = (vin_min * D) / (fsw * L)

    # Peak Inductor Current (http://www.ti.com/lit/ds/symlink/tps630251.pdf)
    IL_peak = (I_l_ph / (eff * (1 - D))) + ((vin_max * D) / (2 * fsw * L))

    # Max switch current
    i_sw_max = (dI_l / 2) + I_l_ph

    print "Your estimated ripple current will be: %.2f" % dI_l_est
    print "Your inductor needs to be approx: %.2f uH" % (L * 1e6)
    print "Your (real) ripple current will be: %.2f" % dI_l
    print "Each inductor needs to have a saturation current higher than: %.2f" % IL_peak
    print "Each inductor needs to handle an average current of %.2f" % I_l_ph
    print "Each switch will need to handle: %.2f A peak." % i_sw_max

for N_ph in [1, 2, 3, 4, 6, 12]:
    run_calcs(N_ph)
    print '\n\r'
    
    
    
