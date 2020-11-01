#!/usr/bin/env python

import sys
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures without horizon shift")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures with horizon shift")
risk_engine.run("Input/ore2.xml")

risk_engine.print_headline("Run RiskEngine again to price European Swaptions")
risk_engine.run("Input/ore_swaption.xml")

risk_engine.print_headline("Plot results: Simulated exposures vs analytical swaption prices")

risk_engine.setup_plot("swaptions")
risk_engine.plot("exposure_trade_Swap_50y.csv", 2, 3, 'b', "Swap EPE (no horizon shift)")
risk_engine.plot("exposure_trade_Swap_50y.csv", 2, 4, 'r', "Swap ENE (no horizon shift)")
risk_engine.plot("exposure_trade_Swap_50y_2.csv", 2, 3, 'g', "Swap EPE (shifted horizon)")
risk_engine.plot("exposure_trade_Swap_50y_2.csv", 2, 4, 'y', "Swap ENE (shifted horizon)")
risk_engine.plot("swaption_npv.csv", 3, 4, 'g', "NPV Swaptions", marker='s')

risk_engine.decorate_plot(title="Example 12 - Simulated exposures with and without horizon shift")
risk_engine.save_plot_to_file()

risk_engine.print_headline("Plot results: Zero rate distribution with and without shift")

risk_engine.setup_plot("rates")
risk_engine.plot_zeroratedist("scenariodump.csv", 0, 23, 5, 'r', label="No horizon shift", title="")
risk_engine.plot_zeroratedist("scenariodump2.csv", 0, 23, 5, 'b', label="Shifted horizon", title="Example 12 - 5y zero rate (EUR) distribution with and without horizon shift")
risk_engine.save_plot_to_file()

