"""
argument_parser.py

Description:
This module defines the argument parser for the
METRIC command line interface.

Authors:
    - Ollie Tooth
"""
import argparse

from ..__init__ import __version__


def create_parser():
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        description=f"METRIC {__version__} command line interface",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Add METRIC CLI actions:
    parser.add_argument(
        "action",
        choices=["run", "validate"],
        help="Specify METRIC action: 'run' to compute AMOC diagnostics and write to file, or 'validate' to validate existing AMOC diagnostics against observations.",
    )

    # Add METRIC CLI required arguments:
    parser.add_argument('-c', type=str, action='store', dest='config_file',
                        required=True, help='Path for netcdf file(s) containing temperature data.')

    # Add METRIC CLI optional arguments:
    parser.add_argument('-t', type=str, action='store', dest='temperature_file',
                        required=False, help='Path for netcdf file(s) containing temperature data.')

    parser.add_argument('-s', type=str, action='store', dest='salinity_file',
                        required=False, help='Path for netcdf file(s) containing salinity data.')

    parser.add_argument('-v', type=str, action='store', dest='velocity_file',
                        required=False, help='Path for netcdf file(s) containing meridional velocity data.')

    parser.add_argument('-taux', type=str, action='store', dest='taux_file',
                        required=False, help='Path for netcdf file(s) containing zonal wind stress data.')

    parser.add_argument('-ssh', type=str, action='store', dest='ssh_file',
                        required=False, help='Path for netcdf file(s) containing Sea Surface Height data.')

    parser.add_argument('--name', type=str, action='store', dest='name', 
                        default=None, help='Name used in output files. Overrides value in config file.')

    parser.add_argument('--outdir', type=str, action='store', dest='outdir',
                        default=None, help='Path used for output data. Overrides value in config file.')

    parser.add_argument('--shift', type=str, action='store', dest='shift_date',
                        default=None, help='Shift dates.')

    return parser
