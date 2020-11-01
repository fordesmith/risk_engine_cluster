#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Plot results: Simulated exposures")

risk_engine.setup_plot("CPI Swap")
risk_engine.plot("exposure_trade_CPI_Swap_1.csv", 2, 3, 'b', "EPE CPI Swap")
risk_engine.decorate_plot(title="Example 17", ylabel="Exposure")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("YoY Swap")
risk_engine.plot("exposure_trade_YearOnYear_Swap.csv", 2, 3, 'b', "EPE YoY Swap")
risk_engine.decorate_plot(title="Example 17", ylabel="Exposure")
risk_engine.save_plot_to_file()

risk_engine.run("Input/ore_capfloor.xml")
risk_engine.get_times("Output/log_capfloor.txt")
