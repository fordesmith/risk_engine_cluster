#!/usr/bin/env python

import os
import sys
sys.path.append('../')
from risk_engine-helper import RiskEngine

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

# TODO: Extend the DIM related postprocessor output so that we can avoid scaling and squaring while plotting
risk_engine.setup_plot("dim_regression_A_swap_eur")
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 6, 'c', 'Simulation Data', marker='+', linestyle='', exponent=2.0, yScale=1e10, xScale=1, zoom=7, rescale=True)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_0.txt"), 1, 2, 'm', 'Zero Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_1.txt"), 1, 2, 'g', 'First Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1)
risk_engine.plotScaled(os.path.join("case_A_eur_swap", "dim_regression_2.txt"), 1, 2, 'b', 'Second Order Regression', exponent=2.0, yScale=2.33*2.33*1e10, xScale=1, legendLocation='upper right')
risk_engine.decorate_plot(title="Example 13 (A) - DIM Regression Swap EUR, Timestep 100", xlabel='Rate', ylabel='Clean NPV Variance')
risk_engine.save_plot_to_file()

# Case B
risk_engine.print_headline("Run RiskEngine (case B (swaption eur), 1st order regression, t=300)")
risk_engine.run("Input/ore_B1.xml")
risk_engine.get_times("Output/log_1.txt")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_1.txt", "dim_evolution_1.txt", "dim_regression_1.txt"]
)
risk_engine.print_headline("Run RiskEngine (case B (swaption eur), 2nd order regression, t=300)")
risk_engine.run("Input/ore_B2.xml")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_2.txt", "dim_evolution_2.txt", "dim_regression_2.txt"]
)
risk_engine.print_headline("Run RiskEngine (case B (swaption eur), zero order regression, t=300)")
risk_engine.run("Input/ore_B0.xml")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_0.txt", "dim_evolution_0.txt", "dim_regression_0.txt"]
)

risk_engine.print_headline("Run RiskEngine (case B (swaption eur), 1st order regression, t=100)")
risk_engine.run("Input/ore_B1b.xml")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_1b.txt", "dim_evolution_1b.txt", "dim_regression_1b.txt"]
)
risk_engine.print_headline("Run RiskEngine (case B (swaption eur), 2nd order regression, t=100)")
risk_engine.run("Input/ore_B2b.xml")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_2b.txt", "dim_evolution_2b.txt", "dim_regression_2b.txt"]
)
risk_engine.print_headline("Run RiskEngine (case B (swaption eur), zero order regression, t=100)")
risk_engine.run("Input/ore_B0b.xml")
risk_engine.save_output_to_subdir(
    "case_B_eur_swaption",
    ["log_0b.txt", "dim_evolution_0b.txt", "dim_regression_0b.txt"]
)

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("dim_evolution_B_swaption_eur")
risk_engine.plot(os.path.join("case_B_eur_swaption", "dim_evolution_1.txt"), 0, 3, 'y', "Zero Order Regression")
risk_engine.plot(os.path.join("case_B_eur_swaption", "dim_evolution_1.txt"), 0, 4, 'c', "First Order Regression")
risk_engine.plot(os.path.join("case_B_eur_swaption", "dim_evolution_2.txt"), 0, 4, 'm', "Second Order Regression")
risk_engine.decorate_plot(title="Example 13 (B) - DIM Evolution Swaption (physical delivery) EUR", xlabel="Timestep", ylabel="DIM")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("dim_regression_B_swaption_eur_t300")
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_1.txt"), 1, 6, 'c', 'Simulation Data', marker='+', linestyle='', exponent=2.0, yScale=1e9, xScale=1, zoom=7, rescale=True)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_0.txt"), 1, 2, 'm', 'Zero Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_1.txt"), 1, 2, 'g', 'First Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_2.txt"), 1, 2, 'b', 'Second Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1, legendLocation='upper right')
risk_engine.decorate_plot( title="Example 13 (B) - DIM Regression Swaption (physical delivery) EUR, Timestep 300", xlabel="Regressor", ylabel="Clean NPV Variance")
risk_engine.save_plot_to_file()

risk_engine.setup_plot("dim_regression_B_swaption_eur_t100")
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_1b.txt"), 1, 6, 'c', 'Simulation Data', marker='+', linestyle='', exponent=2.0, yScale=1e9, xScale=1, zoom=7, rescale=True)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_0b.txt"), 1, 2, 'm', 'Zero Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_1b.txt"), 1, 2, 'g', 'First Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1)
risk_engine.plotScaled(os.path.join("case_B_eur_swaption", "dim_regression_2b.txt"), 1, 2, 'b', 'Second Order Regression', exponent=2.0, yScale=2.33*2.33*1e9, xScale=1, legendLocation='upper right')
risk_engine.decorate_plot( title="Example 13 (B) - DIM Regression Swaption (physical delivery) EUR, Timestep 100", xlabel="Regressor", ylabel="Clean NPV Variance")
risk_engine.save_plot_to_file()

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

# Case D
risk_engine.print_headline("Run RiskEngine (case D (swap eur-usd), 1st order regression)")
risk_engine.run("Input/ore_D1.xml")
risk_engine.get_times("Output/log_1.txt")
risk_engine.save_output_to_subdir(
    "case_D_eurusd_swap",
    ["log_1.txt", "dim_evolution_1.txt", "dim_regression_1.txt"]
)
risk_engine.print_headline("Run RiskEngine (case D (swap eur-usd), 2nd order regression)")
risk_engine.run("Input/ore_D2.xml")
risk_engine.save_output_to_subdir(
    "case_D_eurusd_swap",
    ["log_2.txt", "dim_evolution_2.txt", "dim_regression_2.txt"]
)

risk_engine.print_headline("Plot results")

risk_engine.setup_plot("dim_evolution_D_swap_eurusd")
risk_engine.plot(os.path.join("case_D_eurusd_swap", "dim_evolution_1.txt"), 0, 3, 'y', "Zero Order Regression")
risk_engine.plot(os.path.join("case_D_eurusd_swap", "dim_evolution_1.txt"), 0, 4, 'c', "First Order Regression")
risk_engine.plot(os.path.join("case_D_eurusd_swap", "dim_evolution_2.txt"), 0, 4, 'm', "Second Order Regression")
risk_engine.decorate_plot(title="Example 13 (D) - DIM Evolution Swap EUR-USD", xlabel="Timestep", ylabel="DIM")
risk_engine.save_plot_to_file()
