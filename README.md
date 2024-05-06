 # py4tga

[![image](https://img.shields.io/pypi/v/py4tga.svg)](https://pypi.python.org/pypi/py4tga)

Python for thermogravimetry analysis

-   Free software: MIT license
-   Documentation: /docs/

## Overview

py4tga is a tool set to analyze data from simultaneous thermal analyzers (TGA-DSC). The main objective is a reproducible, well-documented, minimalistic and user-friendly python tool  to read, process, and analyze TGA-DSC data to plot the thermograms (TG, DTG, and DSC) and evaluate process characterstics (total heat flow, peak decomposition temperature, kinetic parameters etc.).

## Implementation

A module-based rolling release cycle is planned with jupyernotebook as the primary user interface. The main challenge (the fun part!) is to figure out a method to implement this tool in such a way that it is intuitive and easy for end-users who are either novice python users or those who just wants to do some TGA analysis without any other time-consuming overheads. This is because there are many proprietary and expensive software which can perform all these analyses in bulk with a few clicks. Therefore, for the end user it becomes a question about time vs cost-of-software.

## Installation

```
pip install py4tga

```
## Status

**not ready for use!**
## Credits

[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
