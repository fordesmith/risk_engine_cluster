#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine for Sensitivity, Stress and Parametric VaR Analysis")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")


