#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures, without collateral")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("plot_callable_swap")
risk_engine.plot("exposure_trade_Swap.csv", 2, 3, 'b', "EPE Swap")
risk_engine.plot("exposure_trade_Swaption.csv", 2, 4, 'r', "ENE Swaption")
risk_engine.plot("exposure_nettingset_CPTY_A.csv", 2, 3, 'g', "EPE Netting Set")
risk_engine.plot("exposure_trade_ShortSwap.csv", 2, 3, 'm', "EPE Short Swap")
risk_engine.decorate_plot(title="Example 5")
risk_engine.save_plot_to_file()
