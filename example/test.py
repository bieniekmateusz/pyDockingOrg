from dockingorg import Enamine

with Enamine() as enamine: 
	results = enamine.search_smiles(["O=C(NC=1C=CC=CC1)NC=2C=CC=NC2"])
	print(results)