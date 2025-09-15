"""
Module containing main routines to calculate
METRIC AMOC diagnostics.

Authors:
    - Fred Castruccio
    - Ollie Tooth
"""
# -- Import required packages -- #
import os
import errno
import glob

from . import utils, sections, rapid, move, samba



def compute_amoc_transport(args):
    """ Parse options and compute amoc """
    config = utils.get_config(args)

    # Update name in config file
    if args['name'] is not None:
        config.set('output', 'name', args['name'])

    # Update outdir in config file
    if args['outdir'] is not None:
        config.set('output', 'outdir', args['outdir'])

    # Update shift_date in config file
    if args['shift_date'] is not None:
        config.set('output', 'shift_date', args['shift_date'])

    # Update shift_date in config file
    if utils.get_config_opt(config, 'options', 'eos') is None:
        config.set('options', 'eos', 'teos10')

    # Check files and options 
    if not utils.path.exists(args['config_file']):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['config_file'])
    if not glob.glob(args['temperature_file']):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['temperature_file'])
    if not glob.glob(args['salinity_file']):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['salinity_file'])
    if not glob.glob(args['velocity_file']):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['velocity_file'])
    if args['taux_file']:
      if not glob.glob(args['taux_file']):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['taux_file'])
    if args['ssh_file']:
      if not glob.glob(args['ssh_file']):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args['ssh_file'])

    if config.get('options','array') == 'RAPID':
      if not args['taux_file']:
        raise RuntimeError('Path for netcdf file(s) containing zonal wind stress data must be provided for RAPID array.')

    if config.get('options','array') == 'SAMBA':
      if not args['taux_file']:
        raise RuntimeError('Path for netcdf file(s) containing zonal wind stress data must be provided for SAMBA array.')

    if config.getboolean('options', 'td_geo'):
      if not args['ssh_file']:
        raise RuntimeError('Path for netcdf file(s) containing Sea Surface Height data must be provided for top-down geostrophic method')

    # Read data
    t = sections.ZonalSections(args['temperature_file'], config, 'temperature')
    s = sections.ZonalSections(args['salinity_file'], config, 'salinity')
    v = sections.ZonalSections(args['velocity_file'], config, 'meridional_velocity')
    if config.get('options','array') == 'RAPID':
      tau = sections.ZonalSections(args['taux_file'], config, 'taux')
    if config.get('options','array') == 'SAMBA':
      tau = sections.ZonalSections(args['taux_file'], config, 'taux')
    if config.getboolean('options', 'td_geo'):
      ssh = sections.ZonalSections(args['ssh_file'], config, 'ssh')

    # Interpolate T & S data onto v-grid
    t_on_v = sections.interpolate(t, v)
    s_on_v = sections.interpolate(s, v)
    if config.getboolean('options', 'td_geo'):
      ssh_on_v = sections.interpolate(ssh, v)
    else:
      ssh_on_v = None

    # Return integrated transports section as netcdf object
    if config.get('options','array') == 'MOVE':
      trans = move.transports.calc_transports_from_sections(
          config, v, t_on_v, s_on_v, ssh_on_v)
      # Plot diagnostics                                                                                                      
      if config.getboolean('output','plot'):                                                                                   
        move.plotdiag.plot_diagnostics(config, trans)
    elif config.get('options','array') == 'RAPID':
      trans = rapid.transports.calc_transports_from_sections(
          config, v, tau, t_on_v, s_on_v, ssh_on_v)
      # Plot diagnostics                                                                                                      
      if config.getboolean('output','plot'):                                                                                   
        rapid.plotdiag.plot_diagnostics(config, trans)
    elif config.get('options','array') == 'SAMBA':
      trans = samba.transports.calc_transports_from_sections(
          config, v, tau, t_on_v, s_on_v, ssh_on_v)
      # Plot diagnostics                                                                                                      
      if config.getboolean('output','plot'):                                                                                   
        samba.plotdiag.plot_diagnostics(config, trans)

    # Write data
    #print 'SAVING: %s' % trans.filepath()
    trans.close()






