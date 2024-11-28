#!/usr/bin/env bash
GLOBIGNORE="*"
# ------------------------------------------------------------------------------
# run_metric_SAMBA_eORCA025.sh
# 
# Description: Script to run METRIC SAMBA 34.5S AMOC diagnostic for eORCA025
# Near-Present Day (NPD) simulation.
#
# Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
#
# Created On: 2024-11-19
# ------------------------------------------------------------------------------

# -- Input arguments to ./run_metric -- #
# Filepaths to config file:
fpath_config=/home/otooth/work/Diagnostics/proj_NPD_diag/metric/configs/npd/eORCA025/config_SAMBA_eORCA025.ini
# Filepaths to eORCA025 monthly mean output files:
fpath_T="/home/otooth/work/AtlantiS/jasmin_os/testing/monthly/eORCA025_links/eORCA025_1m_grid_T_*.nc"
fpath_V="/home/otooth/work/AtlantiS/jasmin_os/testing/monthly/eORCA025_links/eORCA025_1m_grid_V_*.nc"
fpath_U="/home/otooth/work/AtlantiS/jasmin_os/testing/monthly/eORCA025_links/eORCA025_1m_grid_U_*.nc"

# -- Python Environment -- #
# Activate miniconda environment:
source /home/otooth/miniconda3/etc/profile.d/conda.sh
conda activate env_metric

# -- Run METRIC -- #
echo "In Progress: Calculating SAMBA 34.5S AMOC Diagnostics..."

# Move to metric directory:
cd /home/otooth/work/Diagnostics/proj_NPD_diag/metric
# Call metric script:
./run_metric.py -c $fpath_config -t $fpath_T -s $fpath_T -v $fpath_V -ssh $fpath_T -taux $fpath_U

echo "Completed: Calculated SAMBA 34.5S AMOC Diagnostics."
