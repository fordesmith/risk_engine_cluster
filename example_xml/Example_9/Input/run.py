#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for CrossCurrencySwaps")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot results: Cross Currency Swap exposures, with and without FX reset")

risk_engine.setup_plot("example_xccy_reset")
risk_engine.plot("exposure_trade_XCCY_Swap_EUR_USD.csv", 2, 3, 'b', "Swap")
risk_engine.plot("exposure_trade_XCCY_Swap_EUR_USD_RESET.csv", 2, 3, 'r', "Resettable Swap")
risk_engine.decorate_plot(title="Example 9", legend_loc="upper left")
risk_engine.save_plot_to_file()
