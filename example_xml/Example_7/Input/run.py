#!/usr/bin/env python

import sys
sys.path.append('../')
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")

npv = open("Output/npv.csv")
call = []
put = []
for line in npv.readlines():
    if "CALL" in line:
        line_list = line.split(',')
        call=([[0.0,float(line_list[6])],[float(line_list[3]), float(line_list[6])]])
    if "PUT" in line:
        line_list = line.split(',')
        put=([[0.0, float(line_list[6])],[float(line_list[3]), float(line_list[6])]])

risk_engine.print_headline("Plot results: Simulated exposures vs analytical option prices")

risk_engine.setup_plot("forward")
risk_engine.plot("exposure_trade_FXFWD_EURUSD_10Y.csv", 2, 3, 'b', "EPE")
risk_engine.plot("exposure_trade_FXFWD_EURUSD_10Y.csv", 2, 4, 'r', "ENE")
risk_engine.plot_line([0, call[1][0]], [call[0][1], call[1][1]], color='g', label="Call Price")
risk_engine.plot_line([0, put[1][0]], [put[0][1], put[1][1]], color='m', label="Put Price")
risk_engine.decorate_plot(title="Example 7 - FX Forward")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("option")
risk_engine.plot("exposure_trade_FX_CALL_OPTION_EURUSD_10Y.csv", 2, 3, 'b', "EPE")
risk_engine.plot("exposure_trade_FX_PUT_OPTION_EURUSD_10Y.csv", 2, 3, 'r', "ENE")
risk_engine.plot_line([0, call[1][0]], [call[0][1], call[1][1]], color='g', label="Call Price")
risk_engine.plot_line([0, put[1][0]], [put[0][1], put[1][1]], color='m', label="Put Price")
risk_engine.decorate_plot(title="Example 7 - FX Option")
risk_engine.save_plot_to_file()
