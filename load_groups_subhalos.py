import numpy as np

import illustris_python as il

# snapshots of interest
snaps = [8, 13, 21] # z = 8, 6, 4

# type of simulation
fp_dm = 'fp'

# save directory
save_dir = "../data_2500/"

# location
if fp_dm == 'dm':
    basePath = '/n/holylfs05/LABS/hernquist_lab/IllustrisTNG/Runs/L205n2500TNG_DM/output'
else:
    basePath = '/n/holylfs05/LABS/hernquist_lab/IllustrisTNG/Runs/L205n2500TNG/output'


halo_fields = ['GroupPos', 'Group_M_Crit200', 'Group_M_TopHat200', 'Group_M_Mean200']
subhalo_fields = ['SubhaloPos', 'SubhaloMassType', 'SubhaloMassInRadType', 'SubhaloSFR', 'SubhaloSFRinRad']
for i in range(len(snaps)):
    snap = snaps[i]

    halo_data = il.groupcat.loadHalos(basePath, snap, fields=halo_fields)    
    for j in range(len(halo_fields)):
        halo_field = halo_fields[j]
        #halo_data[halo_field].dtype
        np.save(f"{save_dir:s}/{halo_field:s}_{snap:d}_{fp_dm:s}.npy", halo_data[halo_field])

    subhalo_data = il.groupcat.loadSubhalos(basePath, snap, fields=subhalo_fields)    
    for j in range(len(subhalo_fields)):
        subhalo_field = subhalo_fields[j]
        #subhalo_data[subhalo_field].dtype
        np.save(f"{save_dir:s}/{subhalo_field:s}_{snap:d}_{fp_dm:s}.npy", subhalo_data[subhalo_field])
