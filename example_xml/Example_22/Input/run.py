#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine for Sensitivity Analysis (simulating full volatility surfaces)")
risk_engine.run("Input/ore_fullSurface.xml")
risk_engine.get_times("Output/log_fullSurface.txt")

risk_engine.print_headline("Run RiskEngine for Sensitivity Analysis (simulating volatility atm strikes only)")
risk_engine.run("Input/ore_atmOnly.xml")
risk_engine.get_times("Output/log_atmOnly.txt")



