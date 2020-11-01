#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV for equity derivatives")
risk_engine.run("Input/ore.xml")

risk_engine.print_headline("Plot results: Simulated exposures (Equity call option, forward, swap)")

risk_engine.setup_plot("eq_call")
risk_engine.plot("exposure_trade_EqCall_Luft.csv", 2, 3, 'r', "Call EPE")
risk_engine.plot("exposure_trade_EqForwardTrade_Luft.csv", 2, 3, 'b', "Fwd EPE")
risk_engine.decorate_plot(title="Example 16 - Simulated exposures for Luft call option and fwd trade")
risk_engine.save_plot_to_file()

#risk_engine.setup_plot("eq_swap")
#risk_engine.plot("exposure_trade_EquitySwap_1.csv", 2, 3, 'r', "Equity Swap 1 EPE")
#risk_engine.plot("exposure_trade_EquitySwap_2.csv", 2, 4, 'b', "Equity Swap 2 ENE")
#risk_engine.decorate_plot(title="Example 16 - Simulated exposures for Equity Swaps")
#risk_engine.save_plot_to_file()
