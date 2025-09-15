<p align="center">
<img src="docs/assets/METRIC_logo_v1.png" alt="drawing" width="150"/>
</p>

<p align="center">
</a>
<a href="https://AMOCcommunity.github.io/metric/"><strong>Documentation</strong></a>
- 
<a href="https://github.com/AMOCcommunity/metric/issues"><strong>Report an Issue</strong></a>
</p>


# **METRIC**

Meridional ovErTurning ciRculation diagnostIC (**METRIC**) is a Python package for calculating Atlantic Meridional Overturning Circulation (**AMOC**) diagnostics at observational arrays in ocean general circulation models.

### Background

METRIC originated as a fork of the [**RapidMoc**](https://github.com/cdr30/RapidMoc) package, which enabled users to perform observational-equivalent calculations along the RAPID (26.5°N) array in ocean models.

The latest version of METRIC extends this to allow users to estimate overturning, heat and freshwater transports at:

- **RAPID (26.5°N) array**
- **MOVE (16°N) array**
- **SAMBA (34.5°S) array**

METRIC also includes the option to use alternative observational approaches when estimating meridional volume, heat and freshwater transports.

A new experimental feature is the `metric validate` automated validation feature, which generates a PDF report comparing a given ocean model to available RAPID 26.5°N observations.

## Getting Started:

### Installation 

Users should install **METRIC** into a new virtual environment via GitHub using `pip`:

```{bash}
pip install git+https://github.com/AMOCcommunity/metric.git
```

### Using METRIC

Once **METRIC** has been installed, users can use the `metric` command-line interface to calculate AMOC diagnostics at the RAPID 26.5°N, MOVE 16°N, and SAMBA 34.5°S observing arrays and write outputs to a single netCDF file:

```shell
   metric run [-c] [-t] [-s] [-v] [-ssh] [-taux]
```

After producing AMOC diagnostics at RAPID 26.5°N, users can then generate figures and a PDF report validating their ocean general circulation model against available observations using:

```shell
   metric validate [-c]
```

   #### Required Arguments:
   **-c** = Path to configuration file.\

   #### Optional Arguments:
   **-t** = Path to netcdf file containing temperature data.\
   **-s** = Path to netcdf file containing salinity data.\
   **-v** = Path to netcdf file containing meridional velocity data.\
   **-ssh** = Path to netcdf file containing sea surface height data.\
   **-taux** = Path to netcdf file containing zonal wind stress data.
   **--outdir** = Path to output directory (overwrites configuration file).\
   **--name** = Name of the output file (overwrites configuration file).\
   **--shift** = Shift output dates for plotting.

## Examples:

Example configuration files for **POP** and **NEMO** ocean model outputs are provided for users in the `configs` directory.

Users will also find two example workflows, including SLURM job submission scripts, to run **METRIC** with large multi-file datasets in `configs/NEMO/NOC/`.

## Coming Soon:

* **Validation workflows for MOVE 16°N & SAMBA 34.5°S.
* AMOC Diagnostics for NOAC 47N.
* AMOC Diagnostics for OSNAP.

## Citations

#### **METRIC**

Please cite the associated digital object identifier and **Danabasoglu et al. (2021)** if you use **METRIC** in your research.

**Code:**

Castruccio F. S., 2021: NCAR/metric: metric v0.1. doi/10.5281/zenodo.4708277

[![DOI](https://zenodo.org/badge/331704850.svg)](https://zenodo.org/badge/latestdoi/331704850)

**Publication:**

Danabasoglu, G., Castruccio, F. S.,  Small, R. J., Tomas, R., Frajka-Williams, E., and Lankhorst, M., (2021). Revisiting AMOC Transport Estimates from Observations and Models. *Geophysical Research Letters*, in review. 

#### **Rapidmoc**

The original RapidMoc package should be cited using the associated digital object identifiers and [Roberts et al. (2013)](http://onlinelibrary.wiley.com/doi/10.1002/grl.50930/full)

**Code:**

Roberts, C.D., 2017: cdr30/RapidMoc: RapidMoc v1.0.1. doi:10.5281/zenodo.1036387

**Publlication:**

Roberts, C. D., et al. (2013), Atmosphere drives recent interannual variability of the Atlantic meridional overturning circulation at 26.5°N, Geophys. Res. Lett., 40, 5164–5170 doi:10.1002/grl.50930.
