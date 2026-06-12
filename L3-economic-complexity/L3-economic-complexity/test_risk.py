import unittest
from working_capital_risk import WorkingCapitalRiskEngine

class TestWorkingCapitalRisk(unittest.TestCase):
    def test_low_risk_solvency(self):
        # Business with strong cash flow and minimal liability
        engine = WorkingCapitalRiskEngine(
            merchant_id="SAFE-01", 
            monthly_turnover=500000, 
            current_liabilities=100000, 
            cash_reserve=50000
        )
        report = engine.simulate_macro_stress(stress_factor=0.20)
        self.assertEqual(report["risk_level"], "LOW_RISK")
        self.assertEqual(report["credit_action"], "APPROVE_SOVEREIGN_CREDIT")

    def test_critical_risk_insolvency(self):
        # Deeply leveraged business with zero cash backup during a shock
        engine = WorkingCapitalRiskEngine(
            merchant_id="RISK-02", 
            monthly_turnover=100000, 
            current_liabilities=200000, 
            cash_reserve=0
        )
        report = engine.simulate_macro_stress(stress_factor=0.20)
        self.assertEqual(report["risk_level"], "CRITICAL_RISK")
        self.assertEqual(report["credit_action"], "DENY_CREDIT_LINE")

if __name__ == "__main__":
    unittest.main()
