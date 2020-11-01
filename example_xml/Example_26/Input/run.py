import os
import sys
sys.path.append('Helpers/')
import TradeGenerator


sys.path.append('../')
sys.path.append('../')
from risk_engine-helper import RiskEngine

risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)

risk_engine.print_headline("Running in currency trades")
risk_engine.run("Input/ois_ore.xml")

risk_engine.print_headline("Running EUR out of currency trades")
risk_engine.run("Input/EUR_xois_ore.xml")

risk_engine.print_headline("Running USD out of currency trades")
risk_engine.run("Input/USD_xois_ore.xml")

