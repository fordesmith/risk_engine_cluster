#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures, without collateral")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.setup_plot("example_swap_cash_physical")
risk_engine.plot("exposure_trade_Swap.csv", 2, 3, 'b', "EPE Swap")
risk_engine.plot("exposure_trade_SwaptionCash.csv", 2, 3, 'r', "EPE Swaption Cash")
risk_engine.plot("exposure_trade_SwaptionPhysical.csv", 2, 3, 'g', "EPE Swaption Physical")
risk_engine.plot("exposure_trade_SwaptionCashPremium.csv", 2, 3, 'c', "EPE Swaption Cash with Premium")
#risk_engine.plot("exposure_trade_SwaptionPhysicalPremium.csv", 2, 3, 'y', "EPE Swaption Physical with Premium")
risk_engine.decorate_plot(title="Example 3")
risk_engine.save_plot_to_file()
