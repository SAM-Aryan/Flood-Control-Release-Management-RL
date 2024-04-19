from pyswmm import Simulation
import swmmio

# The Input Area image is present in the file src directory.
with Simulation('src\input.inp') as sim:
    for step in sim:
        pass

crs = 'epsg:3728' # Coordinate Reference System
simulation_info = swmmio.Model("src\input.inp", crs=crs)

# Here is the mapped control flow for the presented area in interactive HTML format.
# A sample picture for the same has been added to the file structure as well.
swmmio.create_map(simulation_info, filename="outputMap.html")