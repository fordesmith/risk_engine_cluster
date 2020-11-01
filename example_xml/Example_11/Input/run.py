#!/usr/bin/env python

import os
import runpy
ore_helpers = runpy.run_path(os.path.join(os.path.dirname(os.getcwd()), "risk_helper.py"))
RiskEngine = ore_helpers['OreExample']

import sys
risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")
 
risk_engine.print_headline("Plot results")
 
risk_engine.setup_plot("BaselMeasures")
risk_engine.plot("exposure_trade_Swap.csv", 2, 3, 'b', "EPE")
risk_engine.plot("exposure_trade_Swap.csv", 2, 8 ,'c', "BASEL EE")
risk_engine.plot("exposure_trade_Swap.csv", 2, 9 ,'r', "BASEL EEE")

epe = risk_engine.get_output_data_from_column("xva.csv", 20, 1)
from decimal import Decimal
risk_engine.plot_hline(Decimal(epe[0]), 'g', "BaselEPE")

eepe = risk_engine.get_output_data_from_column("xva.csv", 21, 1)
risk_engine.plot_hline(Decimal(eepe[0]), 'y', "BaselEEPE")

risk_engine.decorate_plot(title="Example 11 - Basel Measures")
risk_engine.save_plot_to_file()
