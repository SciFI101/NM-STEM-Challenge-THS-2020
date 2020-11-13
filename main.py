#
#  We need to give everything a paint-job; remove ANY mention of
#  the past project. Algorithims.py doesn't need much changing
#  just some code removal. Other than that everything we need and
#  more for graphing is here.
#

import algorithims

# Produce Data
mw_production = []
z = 2
while True:
    z = z*2
    mw_production.append(z)
    print(z)
    if z > 1000000:
        break

# Post-processing of produced data
time = [x for x in range(len(mw_production))]

# Visualize data
algorithims.dict_to_graph({'mW Production': mw_production, 'Time (s)': time}, 'Graph')