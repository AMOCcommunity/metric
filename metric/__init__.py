"""
METRIC is a package to calculate diagnostics of the Atlantic Meridional 
Overturning Circulation (AMOC) using output from an ocean general circulation
model for comparison with observed data from the RAPID array at 26.5N, MOVE array at 16N,
and SAMBA array at 34.5S.

METRIC is adapted from RapidMoc by Chris Roberts at ECMWF (chris.roberts@ecmwf.int)

Author:
Fred Castruccio, NCAR (fredc@ucar.edu)
"""


from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
