#!/usr/bin/bash

###########################################################
# create_eORCA025_ERA5_1m_links.ksh
#
# Create symbolic links for eORCA025-ERA5 monthly mean
# fields.
# Date Created: 12/11/2024
###########################################################
date

SRC_NAME=/dssgfs01/scratch/npd/simulations/eORCA025_ERA5/
CONFIG=eORCA025_1m

echo "In Progress: Creating symbolic links for eORCA025 monthly mean output."
# 1. Create symbolic links to monthly mean fields - 1976-2024.
for grid in {grid_T,grid_U,grid_V}
do
    for yr in {1976..2023}
    do
        for mt in {01..12}
        do
            for filename in `ls ${SRC_NAME}/${yr}/${CONFIG}_${grid}_${yr}${mt}-${yr}${mt}.nc`
            do
            ln -s ${filename} ${CONFIG}_${grid}_${yr}${mt}.nc
            done
        done
    done
    echo "Completed: Created symbolic links for eORCA025 monthly mean ${grid} output."
done
