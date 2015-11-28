import sys, re, math

eref = -74.942080057698
tol = 1e-11

returncode = 1
for line in sys.stdin:
    x = re.match('\*\* Hartree-Fock energy =\s*([-\d.]+)', line)
    if x:
        efound_str = x.group(1)
        if (math.fabs(eref - float(efound_str)) < tol):
            returncode = 0

sys.exit(returncode)