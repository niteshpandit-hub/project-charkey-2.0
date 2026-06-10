class DPIAnalyticsEngine:
    def __init__(self, merchant_id, total_volume, tx_count):
        self.merchant_id = merchant_id
        self.total_volume = total_volume # Total financial velocity in INR
        self.tx_count = tx_count         # Number of successful transactions

    def evaluate_credit_worthiness(self):
        """
        Calculates a financial inclusion credit rating based on DPI data footprints.
        """
        # Base credit score
        base_score = 500
        
        # Velocity and Volume adjustments
        volume_bonus = min(200, int(self.total_volume / 10000))  # +1 point for every 10,000 INR, max 200
        consistency_bonus = min(200, self.tx_count * 2)          # +2 points per stable transaction, max 200
        
        final_credit_score = base_score + volume_bonus + consistency_bonus
        final_credit_score = min(900, final_credit_score) # Absolute cap at 900
        
        if final_credit_score >= 750:
            eligibility = "HIGH_ELIGIBILITY"
            msg = "Merchant eligible for Sovereign Infrastructure Credit Pool."
        else:
            eligibility = "STANDARD_ELIGIBILITY"
            msg = "Merchant requires further transaction velocity build-up."
            
        return {
            "merchant_id": self.merchant_id,
            "calculated_score": final_credit_score,
            "status": eligibility,
            "recommendation": msg
        }

if __name__ == "__main__":
    # Simulating a small vendor with 1,50,000 INR velocity and 120 digital payments
    vendor_analysis = DPIAnalyticsEngine(merchant_id="MERCH-8891", total_volume=150000, tx_count=120)
    report = vendor_analysis.evaluate_credit_worthiness()
    print(f"Merchant Credit Rating: {report['calculated_score']} | Status: {report['status']}")
