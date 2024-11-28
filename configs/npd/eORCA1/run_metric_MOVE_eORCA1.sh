#!/usr/bin/env bash
GLOBIGNORE="*"
# ------------------------------------------------------------------------------
# run_metric_MOVE_eORCA1.sh
# 
# Description: Script to run METRIC MOVE 16N AMOC diagnostic for eORCA1 Near-
# Present Day (NPD) simulation.
#
# Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
#
# Created On: 2024-11-19
# ------------------------------------------------------------------------------

# -- Input arguments to ./run_metric -- #
# Filepaths to config file:
fpath_config=/home/otooth/work/Diagnostics/proj_NPD_diag/metric/configs/npd/eORCA1/config_MOVE_eORCA1.ini
# Filepaths to eORCA1 monthly mean output files:
fpath_T="/dssgfs01/scratch/otooth/npd/simulations/eORCA1_JRA55/exp_crt_fbk/eORCA1_1m_grid_T_*.nc"
fpath_V="/dssgfs01/scratch/otooth/npd/simulations/eORCA1_JRA55/exp_crt_fbk/eORCA1_1m_grid_V_*.nc"
fpath_U="/dssgfs01/scratch/otooth/npd/simulations/eORCA1_JRA55/exp_crt_fbk/eORCA1_1m_grid_U_*.nc"

# -- Python Environment -- #
# Activate miniconda environment:
source /home/otooth/miniconda3/etc/profile.d/conda.sh
conda activate env_metric

# -- Run METRIC -- #
echo "In Progress: Calculating MOVE 16N AMOC Diagnostics..."

# Move to metric directory:
cd /home/otooth/work/Diagnostics/proj_NPD_diag/metric
# Call metric script:
./run_metric.py -c $fpath_config -t $fpath_T -s $fpath_T -v $fpath_V -ssh $fpath_T -taux $fpath_U

echo "Completed: Calculated MOVE 16N AMOC Diagnostics."
