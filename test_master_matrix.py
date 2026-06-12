import unittest
from national_sovereign_matrix import SovereignMasterMatrix

class TestSovereignMasterMatrix(unittest.TestCase):
    def test_full_four_layers_integration(self):
        # Run on in-memory dynamic pipeline
        engine = SovereignMasterMatrix(db_name=":memory:", current_usd_rate=83.20)
        
        # 1. Test Layer 1 Judicial Cost Calculation
        l1 = engine.process_l1_judicial_case("T-L1", 100000, 2)
        self.assertTrue(l1 > 0)
        
        # 2. Test Layer 2 Workforce Wastage Calculation
        l2 = engine.process_l2_exam_delay("T-L2", 1000, 6)
        self.assertTrue(l2 > 0)
        
        # 3. Test Layer 3 Solvency Calculation
        sri, status = engine.process_l3_merchant_sri("T-L3", 50000, 20000, 500)
        self.assertEqual(status, "CREDIT_WORTHY_APPROVED")
        
        # 4. Test Layer 4 Dynamic Protection Tariff
        tariff, shield = engine.process_l4_anti_dumping_shield("T-L4", 500, 350)
        self.assertEqual(tariff, 150.0)
        
        engine.shutdown()

if __name__ == "__main__":
    unittest.main()
