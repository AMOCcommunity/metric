#!/usr/bin/env bash
# ------------------------------------------------------------------------------
# run_concat_metric_eORCA12_ERA5v1.sh
#
# Description: Script to concatenate annual OSNAP AMOC diagnostics for eORCA12
# ERA-5 version 1 NOC Near-Present Day simulation
#
# Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
#
# Created On: 2025-08-18
# ------------------------------------------------------------------------------
# -- Configure Environment -- #
module load jaspy

# -- Concatenate RAPID METRIC -- #
filedir=/gws/nopw/j04/nemo_vol3/otooth/NPD/diagnostics/eORCA12_ERA5_v1/metric_ERA5_v1

echo "In Progress: Concatenating MOVE 16N AMOC diagnostics..."
ncrcat eORCA12_ERA5_v1_*_natl_meridional_transports_at_16N.nc eORCA12_ERA5_v1_1976-01-2024-12_natl_meridional_transports_at_16N.nc
echo "Completed: Concatenated MOVE 16N AMOC diagnostics."

echo "In Progress: Concatenating RAPID 26N AMOC diagnostics..."
ncrcat eORCA12_ERA5_v1_*_natl_meridional_transports_at_26N.nc eORCA12_ERA5_v1_1976-01-2024-12_natl_meridional_transports_at_26N.nc
echo "Completed: Concatenated RAPID 26N AMOC diagnostics."

echo "In Progress: Concatenating SAMBA 34_5S AMOC diagnostics..."
ncrcat eORCA12_ERA5_v1_*_natl_meridional_transports_at_34_5S.nc eORCA12_ERA5_v1_1976-01-2024-12_natl_meridional_transports_at_34_5S.nc
echo "Completed: Concatenated SAMBA 34_5S AMOC diagnostics."
