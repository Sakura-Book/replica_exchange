# Setup PDB
from openmm import *
from openmm.app import *
from openmm.unit import *

# 入力ファイルの準備
pdb = PDBFile('/data2/yingh/openmm-tutorial-msbs/02_alanine_dipeptide/alanine-dipeptide.pdb')
forcefield = ForceField('amber99sbildn.xml', 'tip3p.xml')

# add solvent
modeller = Modeller(pdb.topology, pdb.positions)
print('Adding solvent...')
modeller.addSolvent(forcefield, model='tip3p', padding=1*nanometer)
PDBFile.writeFile(modeller.topology, modeller.positions, open('./structures/ala2_solvated.pdb', 'w'))