# Homology modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True


a = automodel(env,
              alnfile  = 'output.pir',       # alignment filename
              knowns   = '1GYC',            # codes of the templates
              sequence = 'B0JDP9',              # code of the target
              assess_methods = (assess.DOPE, assess.GA341)
              )
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling
