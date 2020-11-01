#!/usr/bin/env python

import sys
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

risk_engine.print_headline("Run RiskEngine to price European Payer Swaptions")
risk_engine.run("Input/ore_payer_swaption.xml")

risk_engine.print_headline("Run RiskEngine to price European Receiver Swaptions")
risk_engine.run("Input/ore_receiver_swaption.xml")

risk_engine.print_headline("Plot results: Simulated exposures vs analytical Swaption prices")

risk_engine.setup_plot("swaptions")
risk_engine.plot("exposure_trade_Swap_20.csv", 2, 3, 'b', "EPE")
risk_engine.plot("exposure_trade_Swap_20.csv", 2, 4, 'r', "ENE")
risk_engine.plot_npv("npv_payer.csv", 6, 'g', 'Payer Swaption', marker='s')
risk_engine.plot_npv("npv_receiver.csv", 6, 'm', "Receiver Swaption", marker='s')
risk_engine.decorate_plot(title="Example 2")
risk_engine.save_plot_to_file()
