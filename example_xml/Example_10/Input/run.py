#!/usr/bin/env python

import glob
import os
import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

# whithout collateral
risk_engine.print_headline("Run RiskEngine to produce NPV cube and exposures, without collateral")
risk_engine.run("Input/ore.xml")
risk_engine.get_times("Output/log.txt")
risk_engine.save_output_to_subdir(
    "collateral_none",
    ["log.txt", "xva.csv"] + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
)

# Threshhold>0
risk_engine.print_headline("Run RiskEngine to postprocess the NPV cube, with collateral (threshold>0)")
risk_engine.run("Input/ore_threshold.xml")
risk_engine.save_output_to_subdir(
    "collateral_threshold",
    ["log.txt", "xva.csv"]
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "colva*")))
)

# mta=0
risk_engine.print_headline("Run RiskEngine to postprocess the NPV cube, with collateral (threshold=0)")
risk_engine.run("Input/ore_mta.xml")
risk_engine.save_output_to_subdir(
    "collateral_mta",
    ["log.txt", "xva.csv"]
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "colva*")))
)

# threshhold=mta=0
risk_engine.print_headline("Run RiskEngine to postprocess the NPV cube, with collateral (threshold=mta=0)")
risk_engine.run("Input/ore_mpor.xml")
risk_engine.save_output_to_subdir(
    "collateral_mpor",
    ["log.txt", "xva.csv"]
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "colva*")))
)


# threshhold>0 with collateral
risk_engine.print_headline("Run RiskEngine to postprocess the NPV cube, with collateral (threshold>0), exercise next break")
risk_engine.run("Input/ore_threshold_break.xml")
risk_engine.save_output_to_subdir(
    "collateral_threshold_break",
    ["log.txt", "xva.csv"]
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "colva*")))
)

# threshhold>0 with collateral and dynamic initial margin
risk_engine.print_headline("Run RiskEngine to postprocess the NPV cube, with collateral (threshold>0) and dynamic initial margin")
risk_engine.run("Input/ore_threshold_dim.xml")
risk_engine.save_output_to_subdir(
    "collateral_threshold_dim",
    ["log.txt", "xva.csv", "dim_regression.txt", "dim_evolution.txt"]
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "exposure*")))
    + glob.glob(os.path.join(os.getcwd(), os.path.join("Output", "colva*")))
)

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("nocollateral_epe")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_1.csv"), 2, 3, 'b', "EPE Swap 1")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_2.csv"), 2, 3, 'r', "EPE Swap 2")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_3.csv"), 2, 3, 'g', "EPE Swap 3")
risk_engine.plot(os.path.join("collateral_none", "exposure_nettingset_CPTY_A.csv"), 2, 3, 'm', "EPE NettingSet")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("nocollateral_ene")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_1.csv"), 2, 4, 'b', "ENE Swap 1")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_2.csv"), 2, 4, 'r', "ENE Swap 2")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_3.csv"), 2, 4, 'g', "ENE Swap 3")
risk_engine.plot(os.path.join("collateral_none", "exposure_nettingset_CPTY_A.csv"), 2, 4, 'm', "ENE NettingSet")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("nocollateral_allocated_epe")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_1.csv"), 2, 5, 'b', "Allocated EPE Swap 1")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_2.csv"), 2, 5, 'r', "Allocated EPE Swap 2")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_3.csv"), 2, 5, 'g', "Allocated EPE Swap 3")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("nocollateral_allocated_ene")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_1.csv"), 2, 6, 'b', "Allocated ENE Swap 1")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_2.csv"), 2, 6, 'r', "Allocated ENE Swap 2")
risk_engine.plot(os.path.join("collateral_none", "exposure_trade_Swap_3.csv"), 2, 6, 'g', "Allocated ENE Swap 3")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("threshold_epe")
risk_engine.plot(os.path.join("collateral_none", "exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE NettingSet")
risk_engine.plot(os.path.join("collateral_threshold","exposure_nettingset_CPTY_A.csv"), 2, 3, 'r', "EPE NettingSet, Threshold 1m")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("threshold_allocated_epe")
risk_engine.plot(os.path.join("collateral_threshold","exposure_trade_Swap_1.csv"), 2, 5, 'b', "Allocated EPE Swap 1")
risk_engine.plot(os.path.join("collateral_threshold","exposure_trade_Swap_2.csv"), 2, 5, 'r', "Allocated EPE Swap 2")
risk_engine.plot(os.path.join("collateral_threshold","exposure_trade_Swap_3.csv"), 2, 5, 'g', "Allocated EPE Swap 3")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("mta_epe")
risk_engine.plot(os.path.join("collateral_none","exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE NettingSet")
risk_engine.plot(os.path.join("collateral_mta","exposure_nettingset_CPTY_A.csv"), 2, 3, 'r', "EPE NettingSet, MTA 100k")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("mpor_epe")
risk_engine.plot(os.path.join("collateral_none","exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE NettingSet")
risk_engine.plot(os.path.join("collateral_mpor","exposure_nettingset_CPTY_A.csv"), 2, 3, 'r', "EPE NettingSet, MPOR 2W")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("collateral")
risk_engine.plot(os.path.join("collateral_threshold","colva_nettingset_CPTY_A.csv"), 2, 3, 'b', "Collateral Balance", 2)
risk_engine.decorate_plot(title="Example 10", ylabel="Collateral Balance")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("colva")
risk_engine.plot(os.path.join("collateral_threshold","colva_nettingset_CPTY_A.csv"), 2, 4, 'b', "COLVA Increments", 2)
risk_engine.decorate_plot(title="Example 10", ylabel="COLVA")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("collateral_floor")
risk_engine.plot(os.path.join("collateral_threshold","colva_nettingset_CPTY_A.csv"), 2, 6, 'b', "Collateral Floor Increments", 2)
risk_engine.decorate_plot(title="Example 10", ylabel="Collateral Floor Increments")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("threshold_break_epe")
risk_engine.plot(os.path.join("collateral_threshold","exposure_nettingset_CPTY_A.csv"), 2, 3, 'b', "EPE NettingSet, Threshold 1m")
risk_engine.plot(os.path.join("collateral_threshold_break","exposure_nettingset_CPTY_A.csv"), 2, 3, 'r', "EPE NettingSet, Threshold 1m, Breaks")
risk_engine.decorate_plot(title="Example 10")
risk_engine.save_plot_to_file()
