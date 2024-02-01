from rdkit import Chem
from rdkit.Chem import PandasTools
import pandas as pd  # for typehinting below

from smallworld_api import SmallWorld

aspirin = 'O=C(C)Oc1ccccc1C(=O)O'
smiles = 'C=C(Cl)CNC(=O)C1(CC)CCC1'
sw = SmallWorld()
results: pd.DataFrame = sw.search(smiles, dist=5, db=sw.REAL_dataset, length=100)

from IPython.display import display
display(results)

sim = results.sort_values(by='ecfp4')

# search many - example
smiles = ['NC(=O)CN1N=C(Cl)SC1=O',
 'CCN(CCO)C(=O)CS(=O)CC']
 # 'COCCN(CC1CCCNC1)C1CC1',
 # 'C=C(Cl)CNC(=O)C1(CC)CCC1',
 # 'CCN(C(=O)C1=NNC=N1)C1CCCC1',
 # 'COC1(C(=O)NCC(C)C)CCC1',
 # 'CC1=CC=C(NC(=O)C(C)(C)C)C(C)=N1',
 # 'NS(=O)(=O)CC1=CC=C(Cl)C=C1Br',
 # 'CCOC1CC(N)(C(=O)NC)C1(C)C',
 # 'CC1=CC=C(NC(=O)C2(CN)CC2)N=C1']

# many_results : pd.DataFrame = sw.search_many(smiles, dist=5, db=sw.REAL_dataset, length=100)
#display(many_results)