#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to illustrate use of discount ratio curve")

risk_engine.print_headline("Run with USD base currency")
risk_engine.run("Input/ore_usd_base.xml")

risk_engine.print_headline("Run with EUR base currency using GBP-IN-EUR discount modified ratio curve")
risk_engine.run("Input/ore_eur_base.xml")
