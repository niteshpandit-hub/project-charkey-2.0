import unittest
from currency_settlement import CurrencySettlementEngine

class TestCurrencySettlement(unittest.TestCase):
    def test_dollar_value_drop_impact(self):
        # Dollar dropped from 84.00 to 83.00 (INR appreciated)
        engine = CurrencySettlementEngine(base_usd_inr_rate=84.00, current_usd_inr_rate=83.00)
        report = engine.analyze_trade_impact(import_volume_usd=1000, export_volume_usd=500)
        
        # System should identify Rupee strengthening
        self.assertEqual(report["currency_status"], "INR_STRENGTHENED")
        # Import savings must be positive (we saved 1000 INR)
        self.assertTrue(report["import_savings_inr"] > 0)

if __name__ == "__main__":
    unittest.main()
