"""
main_cli.py

Description:
This module defines the command line interface
for the METRIC package.

Authors:
    - Ollie Tooth
"""
import sys
import logging
from .argument_parser import __version__, create_parser

from metric.metric import compute_amoc_diagnostics, validate_amoc_diagnostics

logger = logging.getLogger(__name__)


def metric_banner():
    """Add METRIC banner to log."""
    logger.info(
        f"""

    → → → → → → → → → → → → → → → →
   ↑            METRIC             ↓
    ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ←

        version: {__version__}

""",
        extra={"simple": True},
    )


def initialise_logging():
    """Initialise METRIC logging configuration."""
    logging.basicConfig(
        stream=sys.stdout,
        format="→ →  METRIC  ← ←  | %(levelname)10s | %(asctime)s | %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def process_action(args):
    """Process the selected action."""
    if len(sys.argv) == 1:
        args.parser.print_help()
        sys.exit(0)

    # === Process Actions === #
    if args['action'] == "run":

        # -- Process Run Arguments -- #
        if 'move' in args['config_file'].lower():
            logging.info('Calculating MOVE 16N AMOC diagnostics using:')
        elif 'rapid' in args['config_file'].lower():
            logging.info('Calculating RAPID 26.5N AMOC diagnostics using:')
        elif 'samba' in args['config_file'].lower():
            logging.info('Calculating SAMBA 34.5S AMOC diagnostics using:')
        for key in args.keys():
            if key == 'config_file':
                logging.info('Path to config file: {}'.format(args[key]))
            if key == 'temperature_file':
                logging.info('Path to temperature file(s): {}'.format(args[key]))
            if key == 'salinity_file':
                logging.info('Path to salinity file(s): {}'.format(args[key]))
            if key == 'velocity_file':
                logging.info('Path to meridional velocity file(s): {}'.format(args[key]))
            if key == 'ssh_file':
                logging.info('Path to sea surface height file(s): {}'.format(args[key]))
            if key == 'taux_file':
                logging.info('Path to zonal wind stress file(s): {}'.format(args[key]))
            if key == 'name':
                logging.info('Output files name (Overrides value in config file): {}'.format(args[key]))
            if key == 'outdir':
                logging.info('Output data path (Overrides value in config file): {}'.format(args[key]))
            if key == 'shift_date':
                logging.info('Shift output dates for plotting such that the output time series start with {}'.format(args[key]))
        
        # -- Compute AMOC diagnostics -- #
        compute_amoc_diagnostics(args)
    
    elif args['action'] == "validate":

        # -- Process Validate Arguments -- #
        if 'rapid' in args['config_file'].lower():
            logging.info('Validating RAPID 26.5N AMOC diagnostics using:')
        for key in args.keys():
            if key == 'config_file':
                logging.info('Path to config file: {}'.format(args[key]))

        validate_amoc_diagnostics(args)

    else:
        raise NotImplementedError(f"metric {args['action']} not implemented. Choose from 'run' or 'validate'.")


def metric():
    """
    Run the METRIC command line interface.
    """
    initialise_logging()
    metric_banner()

    parser = create_parser()
    args = parser.parse_args()

    process_action(vars(args))

    logging.info("✔ METRIC terminated successfully ✔")
    sys.exit(0)
