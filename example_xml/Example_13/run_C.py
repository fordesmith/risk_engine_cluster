#!/usr/bin/env python

import glob

import os
import runpy
ore_helpers = runpy.run_path(os.path.join(os.path.dirname(os.getcwd()), "risk_engine-helper.py"))
RiskEngine = ore_helpers['OreExample']

import sys
risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

# Case C
risk_engine.print_headline("Run RiskEngine (case C (swap usd), 1st order regression)")
risk_engine.run("Input/ore_C1.xml")
risk_engine.get_times("Output/log_1.txt")
risk_engine.save_output_to_subdir(
    "case_C_usd_swap",
    ["log_1.txt", "dim_evolution_1.txt", "dim_regression_1.txt"]
)
risk_engine.print_headline("Run RiskEngine (case C (swap usd), 2nd order regression)")
risk_engine.run("Input/ore_C2.xml")
risk_engine.save_output_to_subdir(
    "case_C_usd_swap",
    ["log_2.txt", "dim_evolution_2.txt", "dim_regression_2.txt"]
)

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("dim_evolution_C_swap_usd")
risk_engine.plot(os.path.join("case_C_usd_swap", "dim_evolution_1.txt"), 0, 3, 'y', "Zero Order Regression")
risk_engine.plot(os.path.join("case_C_usd_swap", "dim_evolution_1.txt"), 0, 4, 'c', "First Order Regression")
risk_engine.plot(os.path.join("case_C_usd_swap", "dim_evolution_2.txt"), 0, 4, 'm', "Second Order Regression")
risk_engine.decorate_plot(title="Example 13 (C) - DIM Evolution Swap USD", xlabel="Timestep", ylabel="DIM")
risk_engine.save_plot_to_file()

# plot the regression ? how ?
