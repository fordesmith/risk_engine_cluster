#!/usr/bin/env python

import glob

import os
import runpy
ore_helpers = runpy.run_path(os.path.join(os.path.dirname(os.getcwd()), "risk_engine-helper.py"))
RiskEngine = ore_helpers['OreExample']

import sys
risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

# Case A
risk_engine.print_headline("Run RiskEngine (case A (swap eur), 1st order regression)")
risk_engine.run("Input/ore_A1.xml")
risk_engine.get_times("Output/log_1.txt")
risk_engine.save_output_to_subdir(
    "case_A_eur_swap",
    ["log_1.txt", "dim_evolution_1.txt", "dim_regression_1.txt"]
)
risk_engine.print_headline("Run RiskEngine (case A (swap eur), 2nd order regression)")
risk_engine.run("Input/ore_A2.xml")
risk_engine.save_output_to_subdir(
    "case_A_eur_swap",
    ["log_2.txt", "dim_evolution_2.txt", "dim_regression_2.txt"]
)
risk_engine.print_headline("Run RiskEngine (case A (swap eur), zero order regression)")
risk_engine.run("Input/ore_A0.xml")
risk_engine.save_output_to_subdir(
    "case_A_eur_swap",
    ["log_0.txt", "dim_evolution_0.txt", "dim_regression_0.txt"]
)

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("dim_evolution_A_swap_eur")
risk_engine.plot(os.path.join("case_A_eur_swap", "dim_evolution_1.txt"), 0, 3, 'y', "Zero Order Regression")
risk_engine.plot(os.path.join("case_A_eur_swap", "dim_evolution_1.txt"), 0, 4, 'c', "First Order Regression")
risk_engine.plot(os.path.join("case_A_eur_swap", "dim_evolution_2.txt"), 0, 4, 'm', "Second Order Regression")
#risk_engine.plot(os.path.join("case_A_eur_swap", "dim_evolution_2.txt"), 0, 6, 'r', "Simple DIM")
risk_engine.decorate_plot(title="Example 13 (A) - DIM Evolution Swap EUR", xlabel="Timestep", ylabel="DIM")
risk_engine.save_plot_to_file()

#risk_engine.setup_plot("dim_regression_A_swap_eur")
#risk_engine.plot(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 6, 'k', "Delta NPV", marker='+', linestyle='', rescale=True, zoom=5)
#risk_engine.plot(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 5, 'y', "Zero Order Regression")
#risk_engine.plot(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 2, 'c', "First Order Regression")
#risk_engine.plot(os.path.join("case_A_eur_swap", "dim_regression_2.txt"), 1, 2, 'm', "Second Order Regression")
##risk_engine.plot(os.path.join("case_A_eur_swap", "dim_regression_2.txt"), 1, 7, 'r', "Simple DIM")
#risk_engine.decorate_plot(title="Example 13 (A) - DIM Regression Swap EUR, Timestep 100", xlabel="Regressor", ylabel="Variance")
#risk_engine.save_plot_to_file()

# TODO: Extend the DIM related postprocessor output so that we can avoid scaling and squaring while plotting
risk_engine.setup_plot("dim_regression_A_swap_eur")
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 6, 'c', 'Simulation Data', marker='+', linestyle='', exponent=2.0, yScale=1e10, xScale=1, zoom=7, rescale=True)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_0.txt"), 1, 2, 'm', 'Zero Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 2, 'g', 'First Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_2.txt"), 1, 2, 'b', 'Second Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1, legendLocation='upper right')
risk_engine.decorate_plot(title="Example 13 (A) - DIM Regression Swap EUR, Timestep 100", xlabel='Rate', ylabel='Clean NPV Variance')
risk_engine.save_plot_to_file()

