# Osram Lightify Local Command Line Controller

Allows for command line local control of Osram Lightify Lights

Thanks to [Thomas Friedel](https://github.com/tfriedel) for the Library.

Randomly picks from a list of colors.  Probably could be implemented much better but I'm not really a programmer. :)

Works much faster than the OSRAM Cloud API - I am calling this from my home automation system.

## Example

python3 osram_control.py -g "Great Room" -l "Great Room 01" -a on

## Params

  -g GROUP, --group GROUP
                        Enter the name of the group
  -l LIGHT, --light LIGHT
                        Enter the name of a light in the group
  -a ACTION, --action ACTION
                        Valid Actions are on, off, dim, bright, color,
                        temp_up, temp_down, temp_min, temp_max