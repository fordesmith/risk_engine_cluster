#!/usr/bin/env python

import sys
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce T0 Bond")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")
