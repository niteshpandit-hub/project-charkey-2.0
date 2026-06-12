class WorkingCapitalRiskEngine:
    def __init__(self, merchant_id, monthly_turnover, current_liabilities, cash_reserve):
        """
        Initializes advanced credit risk assessment under varying macro-economic conditions.
        """
        self.merchant_id = merchant_id
        self.turnover = monthly_turnover        # Monthly digital sales volume in INR
        self.liabilities = current_liabilities  # Immediate short-term debts/dues
        self.cash = cash_reserve                # Liquid cash buffer available

    def simulate_macro_stress(self, stress_factor=0.20):
        """
        Simulates an economic downturn (e.g., a 20% drop in market demand/velocity)
        to evaluate business solvency and default risk.
        """
        # Stressed turnover after market shock
        stressed_turnover = self.turnover * (1 - stress_factor)
        
        # Stressed Liquidity Ratio calculation
        total_available_liquidity = self.cash + stressed_turnover
        liquidity_ratio = total_available_liquidity / self.liabilities if self.liabilities > 0 else 999.0

        # Risk stratification based on banking prudence norms
        if liquidity_ratio < 1.0:
            return {
                "risk_level": "CRITICAL_RISK",
                "stressed_liquidity_ratio": round(liquidity_ratio, 2),
                "credit_action": "DENY_CREDIT_LINE",
                "analyst_note": "High insolvency risk. Cash flows insufficient to cover current liabilities under economic stress."
            }
        elif 1.0 <= liquidity_ratio < 1.5:
            return {
                "risk_level": "MODERATE_RISK",
                "stressed_liquidity_ratio": round(liquidity_ratio, 2),
                "credit_action": "APPROVE_WITH_COLLATERAL",
                "analyst_note": "Business is stable but has thin margins to absorb multi-quarter macroeconomic shocks."
            }
        else:
            return {
                "risk_level": "LOW_RISK",
                "stressed_liquidity_ratio": round(liquidity_ratio, 2),
                "credit_action": "APPROVE_SOVEREIGN_CREDIT",
                "analyst_note": "Excellent asset-liability matching. Highly resilient to market downturns."
            }

if __name__ == "__main__":
    # Simulating a retail shop during a 20% market slowdown
    # Turnover: 2,000,000 INR | Liabilities: 1,500,000 INR | Cash: 100,000 INR
    risk_analyst = WorkingCapitalRiskEngine(
        merchant_id="MERC-9901", 
        monthly_turnover=200000, 
        current_liabilities=150000, 
        cash_reserve=10000
    )
    
    stress_report = risk_analyst.simulate_macro_stress(stress_factor=0.20)
    print(f"--- Macro-Economic Stress Audit for {risk_analyst.merchant_id} ---")
    print(f"Risk Evaluation: {stress_report['risk_level']}")
    print(f"Stressed Liquidity Ratio: {stress_report['stressed_liquidity_ratio']}")
    print(f"Banking Action: {stress_report['credit_action']}")
