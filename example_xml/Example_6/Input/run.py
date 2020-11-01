#!/usr/bin/env python

import sys
import os
sys.path.append('../')
from risk_helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

# Portfolio 1 run
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for portfolio 1")
risk_engine.run("Input/ore_portfolio_1.xml")
risk_engine.get_times("Output/portfolio_1/log.txt")
 
risk_engine.print_headline("Plot results for portfolio 1")
 
risk_engine.setup_plot("portfolio_1")
risk_engine.plot(os.path.join("portfolio_1", "exposure_trade_swap_01.csv"), 2, 3, 'b', "EPE Swap")
risk_engine.plot(os.path.join("portfolio_1", "exposure_trade_collar_01.csv"), 2, 4, 'r', "ENE Collar")
risk_engine.plot(os.path.join("portfolio_1", "exposure_nettingset_CPTY_A.csv"), 2, 4, 'g', "ENE Netting")
#risk_engine.plot(os.path.join("portfolio_1", "exposure_nettingset_CPTY_A.csv"), 2, 3, 'g', "EPE Netting")
risk_engine.decorate_plot(title="Example 6, Portfolio 1")
risk_engine.save_plot_to_file(os.path.join("Output", "portfolio_1"))

# Portfolio 2 run
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for portfolio 2")
risk_engine.run("Input/ore_portfolio_2.xml")
risk_engine.get_times("Output/portfolio_2/log.txt")

risk_engine.print_headline("Plot results for portfolio 2")

risk_engine.setup_plot("portfolio_2")
risk_engine.plot(os.path.join("portfolio_2", "exposure_trade_floor_01.csv"), 2, 3, 'b', "EPE Floor")
risk_engine.plot(os.path.join("portfolio_2", "exposure_trade_cap_01.csv"), 2, 4, 'r', "ENE Cap")
risk_engine.plot(os.path.join("portfolio_2", "exposure_nettingset_CPTY_B.csv"), 2, 3, 'g', "EPE Net Cap and Floor")
risk_engine.plot(os.path.join("portfolio_2", "exposure_trade_collar_02.csv"), 2, 4, 'g', "ENE Collar", offset=1, marker='o', linestyle='')
risk_engine.decorate_plot(title="Example 6, Portfolio 2")
risk_engine.save_plot_to_file(os.path.join("Output", "portfolio_2"))

# Portfolio 3 run
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for portfolio 3")
risk_engine.run("Input/ore_portfolio_3.xml")
risk_engine.get_times("Output/portfolio_3/log.txt")

risk_engine.print_headline("Plot results for portfolio 3")

risk_engine.setup_plot("portfolio_3")
risk_engine.plot(os.path.join("portfolio_3", "exposure_trade_cap_02.csv"), 2, 3, 'b', "EPE Cap")
risk_engine.plot(os.path.join("portfolio_3", "exposure_trade_cap_03.csv"), 2, 4, 'r', "ENE Amortising Cap")
risk_engine.plot(os.path.join("portfolio_3", "exposure_nettingset_CPTY_B.csv"), 2, 3, 'g', "EPE Netted")
risk_engine.decorate_plot(title="Example 6, Portfolio 3")
risk_engine.save_plot_to_file(os.path.join("Output", "portfolio_3"))

# Portfolio 4 run
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for portfolio 4")
risk_engine.run("Input/ore_portfolio_4.xml")
risk_engine.get_times("Output/portfolio_4/log.txt")

risk_engine.print_headline("Plot results for portfolio 4")

risk_engine.setup_plot("portfolio_4")
risk_engine.plot(os.path.join("portfolio_4", "exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE Swap + Collar")
risk_engine.plot(os.path.join("portfolio_4", "exposure_nettingset_CPTY_A.csv"), 2, 4, 'r', "ENE Swap + Collar")
risk_engine.plot(os.path.join("portfolio_4", "exposure_nettingset_CPTY_B.csv"), 2, 3, 'b', "EPE CapFloored Swap", offset=1, marker='o', linestyle='')
risk_engine.plot(os.path.join("portfolio_4", "exposure_nettingset_CPTY_B.csv"), 2, 4, 'r', "ENE CapFloored Swap", offset=1, marker='o', linestyle='')
risk_engine.decorate_plot(title="Example 6, Portfolio 4")
risk_engine.save_plot_to_file(os.path.join("Output", "portfolio_4"))

# Portfolio 5 run
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures for portfolio 5")
risk_engine.run("Input/ore_portfolio_5.xml")
risk_engine.get_times("Output/portfolio_5/log.txt")

risk_engine.print_headline("Plot results for portfolio 5")

risk_engine.setup_plot("portfolio_5")
risk_engine.plot(os.path.join("portfolio_5", "exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE Capped swap")
risk_engine.plot(os.path.join("portfolio_5", "exposure_nettingset_CPTY_A.csv"), 2, 4, 'r', "ENE Capped swap")
risk_engine.plot(os.path.join("portfolio_5", "exposure_nettingset_CPTY_B.csv"), 2, 3, 'b', "EPE Swap + Cap", offset=1, marker='o', linestyle='')
risk_engine.plot(os.path.join("portfolio_5", "exposure_nettingset_CPTY_B.csv"), 2, 4, 'r', "ENE Swap + Cap", offset=1, marker='o', linestyle='')
risk_engine.decorate_plot(title="Example 6, Portfolio 5")
risk_engine.save_plot_to_file(os.path.join("Output", "portfolio_5"))
