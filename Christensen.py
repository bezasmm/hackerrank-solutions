import numpy as np

def Christensen(s1, s2, s12, ST1,ST2, SC1, SC2, S12):
    default = 10
    if s1 == 0 and (np.isnan(ST1) or np.isnan(SC1)):
        ST1 = SC1 = default
    if s2 == 0 and (np.isnan(ST2) or np.isnan(SC2)):
        ST2 = SC2 = default
    if s12 == 0 and (np.isnan(S12)):
        S12 = default
    IF = np.zeros(2,)
    # Mode 1 - Fiber failure
    IF[0] = s1*(1/ST1-1/SC1)+(s1**2)/(ST1*SC1)
    # Modo 2 - Matrix failure
    IF[1] = s2*(1/ST2-1/SC2)+(s2**2)/(ST2*SC2)+(s12/S12)**2
    return np.nanmax(IF)

