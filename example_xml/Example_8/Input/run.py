#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_helperimport RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for Cross Currency Swaps")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot Cross Currency Swap results")

risk_engine.setup_plot("example_ccswap")
risk_engine.plot("exposure_trade_CCSwap.csv", 2, 3, 'b', "EPE CCSwap")
risk_engine.plot("exposure_trade_CCSwap.csv", 2, 4, 'r', "ENE CCSwap")
risk_engine.decorate_plot(title="Example 8")
risk_engine.save_plot_to_file()
