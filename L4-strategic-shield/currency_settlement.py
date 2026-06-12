class CurrencySettlementEngine:
    def __init__(self, base_usd_inr_rate, current_usd_inr_rate):
        """
        Initializes the currency volatility tracking engine for trade arbitrage.
        """
        self.base_rate = float(base_usd_inr_rate)
        self.current_rate = float(current_usd_inr_rate)

    def analyze_trade_impact(self, import_volume_usd, export_volume_usd):
        """
        Calculates the financial impact of domestic currency appreciation (dollar drop)
        on national import bills and export revenues.
        """
        # Rate difference (Negative means Dollar dropped / Rupee strengthened)
        rate_shift = self.current_rate - self.base_rate
        percentage_shift = (rate_shift / self.base_rate) * 100

        # Import impact: If dollar drops, we save money on imports
        import_savings_inr = import_volume_usd * abs(rate_shift) if rate_shift < 0 else -(import_volume_usd * rate_shift)
        
        # Export impact: If dollar drops, exporters lose revenue in INR
        export_loss_inr = export_volume_usd * rate_shift if rate_shift < 0 else 0

        # Net Economic Impact
        net_impact_inr = import_savings_inr + export_loss_inr

        if rate_shift < 0:
            status = "INR_STRENGTHENED"
            recommendation = "STRATEGY: Accelerate strategic crude oil imports and build up forex reserves."
        elif rate_shift > 0:
            status = "USD_STRENGTHENED"
            recommendation = "STRATEGY: Enhance export subsidies to keep domestic goods competitive."
        else:
            status = "STABLE"
            recommendation = "STRATEGY: Maintain standard trade corridors."

        return {
            "currency_status": status,
            "rate_change_percent": round(percentage_shift, 2),
            "import_savings_inr": round(import_savings_inr, 2),
            "export_revenue_delta_inr": round(export_loss_inr, 2),
            "net_national_impact_inr": round(net_impact_inr, 2),
            "action_plan": recommendation
        }

if __name__ == "__main__":
    # Supposing base rate was 84.00 INR per USD
    # Today the dollar value dropped to 83.20 INR per USD
    engine = CurrencySettlementEngine(base_usd_inr_rate=84.00, current_usd_inr_rate=83.20)
    
    # Simulating a trade day with $10M imports and $8M exports
    report = engine.analyze_trade_impact(import_volume_usd=10000000, export_volume_usd=8000000)
    
    print("--- LIVE CURRENCY SHIELD AUDIT ---")
    print(f"Status: {report['currency_status']} (Dropped by {abs(report['rate_change_percent'])}%)")
    print(f"Net Savings on Imports: ₹{report['import_savings_inr']}")
    print(f"Net Impact on National Treasury: ₹{report['net_national_impact_inr']}")
    print(f"Policy Action: {report['action_plan']}")
