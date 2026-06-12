import sqlite3
import math
from datetime import datetime

class NationalGovernanceEngine:
    def __init__(self, db_name=":memory:", current_usd_rate=83.20, base_usd_rate=84.00):
        """
        Initializes the unified core engine with an integrated database 
        and macroeconomic parameters.
        """
        self.base_usd = float(base_usd_rate)
        self.current_usd = float(current_usd_rate)
        self.currency_delta = self.current_usd - self.base_usd
        
        # Connect to Database (In-Memory for testing, change to 'charkey.db' for production)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_national_database()

    def _initialize_national_database(self):
        """
        Executes the integrated SQL Schema to secure the DPI Merchant Footprint 
        and Risk Ledger.
        """
        # 1. Create Core DPI Merchant Footprint Registry
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS National_Merchant_Registry (
            merchant_id TEXT PRIMARY KEY,
            gstin TEXT UNIQUE,
            monthly_upi_volume REAL,
            monthly_upi_count INTEGER,
            registered_state TEXT,
            formalization_date TEXT
        );
        """)

        # 2. Create Dynamic Risk Audit Ledger
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Credit_Stress_Ledger (
            audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            merchant_id TEXT,
            calculated_sri REAL,
            solvency_status TEXT,
            max_eligible_sovereign_loan REAL,
            last_audit_timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (merchant_id) REFERENCES National_Merchant_Registry(merchant_id)
        );
        """)
        self.conn.commit()

    def seed_sample_merchant(self, merchant_id, gstin, volume, count, state):
        """Helper method to populate the registry with active DPI profiles"""
        try:
            today_str = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute("""
            INSERT OR REPLACE INTO National_Merchant_Registry 
            (merchant_id, gstin, monthly_upi_volume, monthly_upi_count, registered_state, formalization_date)
            VALUES (?, ?, ?, ?, ?, ?);
            """, (merchant_id, gstin, volume, count, state, today_str))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database Seeding Error: {e}")

    def calculate_macro_arbitrage(self, national_imports_usd):
        """Calculates exact sovereign savings or losses due to currency fluctuations."""
        if self.currency_delta < 0:
            return national_imports_usd * abs(self.currency_delta)
        return 0.0

    def evaluate_and_log_msme_pool(self, stress_factor=0.20):
        """
        Fetches live DPI records from the SQL registry, evaluates solvency under stress,
        and automatically writes the analysis into the Credit Stress Ledger.
        """
        self.cursor.execute("SELECT merchant_id, monthly_upi_volume FROM National_Merchant_Registry")
        merchants = self.cursor.fetchall()
        
        audit_results = []
        
        for merchant in merchants:
            m_id, turnover = merchant
            
            # Simulated liability baseline (50% of monthly volume) and thin cash buffer
            liabilities = turnover * 0.50
            cash_reserve = turnover * 0.08
            
            # Mathematical Solvency Risk Index (SRI) Calculation
            stressed_turnover = turnover * (1 - stress_factor)
            total_liquidity = cash_reserve + stressed_turnover
            sri = total_liquidity / liabilities if liabilities > 0 else 999.0
            
            # Risk Decision Engine
            if sri >= 1.5:
                status = "SOVEREIGN_CREDIT_APPROVED"
                max_loan = turnover * 2.5  # Higher leverage allowance for stable flows
            else:
                status = "DENIED_HIGH_RISK"
                max_loan = 0.0

            # Write results back to the Credit_Stress_Ledger table
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("""
            INSERT INTO Credit_Stress_Ledger 
            (merchant_id, calculated_sri, solvency_status, max_eligible_sovereign_loan, last_audit_timestamp)
            VALUES (?, ?, ?, ?, ?);
            """, (m_id, round(sri, 2), status, round(max_loan, 2), timestamp))
            self.conn.commit()
            
            audit_results.append({
                "id": m_id,
                "sri": round(sri, 2),
                "status": status,
                "loan": round(max_loan, 2)
            })
            
        return audit_results

    def close_engine(self):
        self.conn.close()


if __name__ == "__main__":
    # Initialize Core Engine with a drop in USD value (Today's rate: 83.20 INR vs Base: 84.00 INR)
    gov_panel = NationalGovernanceEngine(db_name=":memory:", current_usd_rate=83.20)
    
    # 1. Seed Sample Data directly into the SQL Tables
    gov_panel.seed_sample_merchant("MERC-IND-44", "27AAAAA1111A1Z1", 300000.00, 450, "Uttar Pradesh")
    gov_panel.seed_sample_merchant("MERC-IND-99", "27BBBBB2222B2Z2", 120000.00, 180, "Maharashtra")
    
    # 2. Run Macro Forex Arbitrage Calculations
    import_bill_usd = 50000000  # $50 Million National Import Bill
    savings = gov_panel.calculate_macro_arbitrage(national_imports_usd=import_bill_usd)
    
    # 3. Process database rows through the Risk Engine and save to the Ledger
    reports = gov_panel.evaluate_and_log_msme_pool(stress_factor=0.20)
    
    # 4. Print Unified National Dashboard Report
    print("======================================================================")
    print("🏛️   CHARKEY 2.0: INTEGRATED SOVEREIGN DATA & ECONOMIC ENGINE DASHBOARD")
    print("======================================================================")
    print(f"[*] Macro Forex Arbitrage Matrix : Saved ₹{savings:,.2f} on national imports.")
    print("----------------------------------------------------------------------")
    print("[*] Processing Live SQL Registry Audit Profiles:")
    for rep in reports:
        print(f"    -> Merchant: {rep['id']} | SRI Score: {rep['sri']} | Status: {rep['status']} | Credit Limit: ₹{rep['loan']:,.2f}")
    print("======================================================================")
    
    gov_panel.close_engine()
