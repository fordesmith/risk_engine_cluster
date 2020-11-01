#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot results: Simulated exposures")

risk_engine.setup_plot("cmsspread")
risk_engine.plot("exposure_trade_CMS_Spread_Swap.csv", 2, 3, 'b', "Swap EPE")
risk_engine.plot("exposure_trade_CMS_Spread_Swap.csv", 2, 4, 'r', "Swap ENE")
risk_engine.decorate_plot(title="Example 28 - Simulated exposures for CMS Spread trades")
risk_engine.save_plot_to_file()

