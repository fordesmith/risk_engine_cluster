#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine with flat vols")
risk_engine.run("Input/ore_flat.xml")

risk_engine.print_headline("Run RiskEngine with smiles")
risk_engine.run("Input/ore_smile.xml")
