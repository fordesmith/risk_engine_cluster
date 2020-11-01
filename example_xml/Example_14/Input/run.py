#!/usr/bin/env python

import sys
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Run RiskEngine again to price European Swaptions")
risk_engine.run("Input/ore_swaption.xml")

risk_engine.print_headline("Plot results: Simulated exposures vs analytical swaption prices")

risk_engine.setup_plot("swaptions")
risk_engine.plot("exposure_trade_Swap_20y.csv", 2, 3, 'b', "Swap EPE")
risk_engine.plot("exposure_trade_Swap_20y.csv", 2, 4, 'r', "Swap ENE")
risk_engine.plot("swaption_npv.csv", 3, 4, 'g', "NPV Swaptions", marker='s')
risk_engine.decorate_plot(title="Example 1 - Simulated exposures vs analytical swaption prices")
risk_engine.save_plot_to_file()

