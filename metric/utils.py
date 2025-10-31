"""
Module containing utility functions

Authors:
    - Fred Castruccio
    - Ollie Tooth
"""
# -- Import required packages -- #
import configparser
from os import path

import numpy as np
import datetime
import cftime

class ShapeError(Exception):
    pass


def get_config(args):
    """ Return configuration options as <configparser> object. """
    config = configparser.ConfigParser()
    config.read(args['config_file'])

    return config


def get_config_opt(config, section, option):
    """ Return option if exists, else None """
    if config.has_option(section, option):
        return config.get(section, option)
    else:
        return None


def get_ncdates(config, nc, tvar='time'):
    """ Return dates from netcdf time coordinate """
    t = nc.variables[tvar]
    dts = cftime.num2date(t[:], t.units, calendar=t.calendar)
    mpldts = np.array([datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second) for dt in dts])
    if config.has_option('output', 'shift_date'):
      dtshift = config.get('output', 'shift_date')
      mpldtshift = datetime.datetime(np.int(dtshift[:4]), np.int(dtshift[4:6]), np.int(dtshift[6:8]))
      tdelta = mpldtshift - mpldts[0]
      mpldts = mpldts + tdelta
      
    return mpldts


def get_datestr(dates, date_format):
    """ Return string of form 'mindate-maxdate' for specified format """
    # Create date string from CFTime datetime objects:
    if isinstance(dates[0], cftime.datetime):
        if date_format == "Y":
            fmt = "%Y"
        elif date_format == "M":
            fmt = "%Y-%m"
        elif date_format == "D":
            fmt = "%Y-%m-%d"
        else:
            raise ValueError(f"Invalid date_format: '{date_format}'. Options are 'Y', 'M', 'D'.")
        datestr = f"{dates[0].strftime(fmt)}-{dates[-1].strftime(fmt)}"
    # Create date string from numpy datetime64:
    elif isinstance(dates[0], np.datetime64):
        datestr = '%s-%s' % (np.datetime_as_string(dates[0], unit=date_format), 
                            np.datetime_as_string(dates[-1], unit=date_format))
    else:
        raise TypeError(f"Invalid type ({type(dates[0])}) for dates. Expected cftime.datetime or np.datetime64.")

    return datestr


def get_cftime_calendar(times):
    """ Return calendar of cftime datetime array. """
    clsname = times[0].__class__.__name__
    calendar = clsname.replace("Datetime", "").lower()
    if calendar.endswith("day"):
        calendar = calendar.replace("day", "_day")

    return calendar


def get_savename(outdir, name, dates, date_format, suffix=''):
    """ Return savename for output file """
    datestr = get_datestr(dates, date_format)
    savename = path.join(outdir,'%s_%s%s' % (name, datestr, suffix))
    
    return savename


def get_daterange(dates1, dates2):
    """ Return min and max date range for overlapping period """
    mindt = max([dates1.min(),dates2.min()])
    maxdt = min([dates1.max(),dates2.max()])
    
    return mindt, maxdt


def get_dateind(dates, mindt, maxdt):
    """ Return index to extract data over specified date range """
    return (dates >= mindt) & (dates <= maxdt)


def get_indrange(vals,minval,maxval):
    """ 
    Return max and min indices to use for simple slicing when
    updating multi-dim np.array that avoids creation of copies.
        
    """ 
    
    if vals.ndim != 1:
        raise ShapeError('get_inds: expected 1-d numpy array')
        
    inds = np.where((vals >= minval) & (vals < maxval))[0]
    
    if len(inds) != 0:
        minind = inds.min()
        maxind = inds.max() + 1
    else:
        raise ValueError('get_inds: no matching data')
        
    return minind, maxind
    
    

def find_nearest(array, val, min=False):
    """ Returns index for value in array that is closest to val. """
    if not isinstance(array, np.ndarray):
        raise TypeError('Array must be a np.ndarray object')

    abs_array = np.absolute(array - val)
    minval = abs_array.min()
    inds = np.where(abs_array == minval)[0]

    if len(inds) > 1:
        if min:
            inds = np.where(array == array[inds].min())[0]
        else:
            inds = np.where(array == array[inds].max())[0]
    
    return inds
