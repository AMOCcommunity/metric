#!/usr/bin/env bash
GLOBIGNORE="*"
# ------------------------------------------------------------------------------
# run_metric_RAPID_eORCA025.sh
# 
# Description: Script to run METRIC RAPID AMOC diagnostic for eORCA025 Near-
# Present Day (NPD) simulation.
#
# Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
#
# Created On: 2024-11-18
# ------------------------------------------------------------------------------

# -- Input arguments to ./run_metric -- #
# Filepaths to config file:
fpath_config=/dssgfs01/working/otooth/Diagnostics/metric/configs/npd/eORCA025/config_RAPID_eORCA025.ini

# Filepaths to eORCA025 monthly mean output files:
fdir=/dssgfs01/working/otooth/Diagnostics/metric/configs/npd/eORCA025/links/eORCA025_ERA5v0

fpath_T=${fdir}/eORCA025_1m_grid_T_*.nc
fpath_V=${fdir}/eORCA025_1m_grid_V_*.nc
fpath_U=${fdir}/eORCA025_1m_grid_U_*.nc

# -- Python Environment -- #
# Activate miniconda environment:
source /home/otooth/miniconda3/etc/profile.d/conda.sh
conda activate env_metric

# -- Run METRIC -- #
echo "In Progress: Calculating RAPID 26N AMOC Diagnostics..."

# Move to metric directory:
cd /dssgfs01/working/otooth/Diagnostics/metric
# Call metric script:
./run_metric.py -c $fpath_config -t $fpath_T -s $fpath_T -v $fpath_V -ssh $fpath_T -taux $fpath_U

echo "Completed: Calculated RAPID 26N AMOC Diagnostics."
