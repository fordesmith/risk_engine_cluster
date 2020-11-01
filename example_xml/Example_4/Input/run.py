#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures, without collateral")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("example_swaption")
risk_engine.plot("exposure_trade_Swap.csv", 2, 3, 'b', "EPE Forward Swap")
risk_engine.plot("exposure_trade_SwaptionCash.csv", 2, 3, 'r', "EPE Swaption (Cash)")
risk_engine.plot("exposure_trade_SwaptionPhysical.csv", 2, 3, 'g', "EPE Swaption (Physical)")
risk_engine.decorate_plot(title="Example 4", ylabel="Exposure")
risk_engine.save_plot_to_file()
