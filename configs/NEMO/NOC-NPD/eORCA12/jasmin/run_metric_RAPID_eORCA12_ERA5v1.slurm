#!/bin/bash
#SBATCH --job-name=metric_RAPID_M1m_eORCA12
#SBATCH --time=24:00:00
#SBATCH --mem=24G
#SBATCH --account=noc_msm
#SBATCH --partition=standard
#SBATCH --qos=standard

GLOBIGNORE="*"
# ------------------------------------------------------------------------------
# run_metric_RAPID_eORCA12.sh
# 
# Description: Script to run METRIC RAPID 26N AMOC diagnostic for eORCA12 Near-
# Present Day (NPD) simulation.
#
# Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
#
# Created On: 2025-08-15
# ------------------------------------------------------------------------------

# -- Input arguments to ./run_metric -- #
# Filepaths to config file:
fpath_config=./config_RAPID_eORCA12.ini

# Filepaths to eORCA12 monthly mean output files:
filedir="/gws/nopw/j04/atlantis/atb299/NPD/eORCA12"

# -- Python Environment -- #
# Activate miniconda environment:
source .../miniforge3/bin/activate
conda activate env_npd_diags

# -- Run METRIC -- #
for yr in {1976..2024}
do
    echo "In Progress: Calculating ${yr} RAPID 26N AMOC Diagnostics..."
    fpath_T="${filedir}/${yr}/eORCA12_1m_grid_T_*.nc"
    fpath_V="${filedir}/${yr}/eORCA12_1m_grid_V_*.nc"
    fpath_U="${filedir}/${yr}/eORCA12_1m_grid_U_*.nc"

    metric run -c $fpath_config -t $fpath_T -s $fpath_T -v $fpath_V -ssh $fpath_T -taux $fpath_U

    echo "Completed: Calculated ${yr} RAPID 26N AMOC Diagnostics."
done
