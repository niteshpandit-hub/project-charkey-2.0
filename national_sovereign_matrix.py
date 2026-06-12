import sqlite3
import math
from datetime import datetime

class SovereignMasterMatrix:
    def __init__(self, db_name="sovereign_core.db", current_usd_rate=83.20, base_usd_rate=84.00):
        """
        The Ultimate Unified Engine combining Layer 1, 2, 3, and 4 into a 
        single automated national statecraft system.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Macro Parameters
        self.base_usd = float(base_usd_rate)
        self.current_usd = float(current_usd_rate)
        self.currency_delta = self.current_usd - self.base_usd
        
        # Initialize All Schemas
        self._boot_all_national_ledgers()

    def _boot_all_national_ledgers(self):
        """Creates tables for all 4 Layers of the Charkey 2.0 Grid"""
        # LAYER 1: Judicial & Institutional Bedrock
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS L1_Judicial_Gridlock (
            case_id TEXT PRIMARY KEY,
            stuck_principal REAL,
            years_elapsed REAL,
            calculated_opportunity_cost REAL
        );
        """)

        # LAYER 2: Human Capital & Academic Timelines
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS L2_Academic_Wastage (
            exam_id TEXT PRIMARY KEY,
            delayed_candidates INTEGER,
            delay_months REAL,
            calculated_tax_loss REAL
        );
        """)

        # LAYER 3: DPI Merchant & Credit Solvency
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS L3_Merchant_DPI_Registry (
            merchant_id TEXT PRIMARY KEY,
            monthly_turnover REAL,
            calculated_sri REAL,
            solvency_status TEXT
        );
        """)

        # LAYER 4: Strategic Autonomy Shield (Tariffs)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS L4_Tariff_Shield (
            product_id TEXT PRIMARY KEY,
            base_import_price REAL,
            foreign_dumping_price REAL,
            imposed_anti_dumping_duty REAL
        );
        """)
        self.conn.commit()

    # ==========================================
    # LAYER 1 LOGIC: Judicial Opportunity Cost
    # ==========================================
    def process_l1_judicial_case(self, case_id, principal, years, cost_of_capital=0.10):
        # Formula: OC = P * (1 + r)^t - P
        opp_cost = principal * math.pow((1 + cost_of_capital), years) - principal
        
        self.cursor.execute("""
        INSERT OR REPLACE INTO L1_Judicial_Gridlock (case_id, stuck_principal, years_elapsed, calculated_opportunity_cost)
        VALUES (?, ?, ?, ?);
        """, (case_id, principal, years, round(opp_cost, 2)))
        self.conn.commit()
        return round(opp_cost, 2)

    # ==========================================
    # LAYER 2 LOGIC: Demographic Dividend Wastage
    # ==========================================
    def process_l2_exam_delay(self, exam_id, total_candidates, months_delayed, avg_monthly_salary=30000.0, tax_rate=0.05):
        # Formula: Loss = Integration of (N * Income * Tax) over delay time
        years_delayed = months_delayed / 12.0
        tax_loss = total_candidates * (avg_monthly_salary * 12.0) * tax_rate * years_delayed
        
        self.cursor.execute("""
        INSERT OR REPLACE INTO L2_Academic_Wastage (exam_id, delayed_candidates, delay_months, calculated_tax_loss)
        VALUES (?, ?, ?, ?);
        """, (exam_id, total_candidates, months_delayed, round(tax_loss, 2)))
        self.conn.commit()
        return round(tax_loss, 2)

    # ==========================================
    # LAYER 3 LOGIC: DPI MSME Solvency
    # ==========================================
    def process_l3_merchant_sri(self, merchant_id, turnover, liabilities, cash, macro_shock=0.20):
        # Formula: SRI = (Cash + Stressed_Turnover) / Liabilities
        stressed_turnover = turnover * (1 - macro_shock)
        total_liquidity = cash + stressed_turnover
        sri = total_liquidity / liabilities if liabilities > 0 else 999.0
        
        status = "CREDIT_WORTHY_APPROVED" if sri >= 1.5 else "HIGH_RISK_DENIED"
        
        self.cursor.execute("""
        INSERT OR REPLACE INTO L3_Merchant_DPI_Registry (merchant_id, monthly_turnover, calculated_sri, solvency_status)
        VALUES (?, ?, ?, ?);
        """, (merchant_id, turnover, round(sri, 2), status))
        self.conn.commit()
        return round(sri, 2), status

    # ==========================================
    # LAYER 4 LOGIC: Strategic Tariff & Forex Arbitrage
    # ==========================================
    def process_l4_anti_dumping_shield(self, product_id, base_domestic_cost, foreign_dump_price):
        # Protect domestic industries if foreign price is lower than production cost
        if foreign_dump_price < base_domestic_cost:
            duty_required = base_domestic_cost - foreign_dump_price
            status = "TARIFF_IMPOSED_PROTECTION_ACTIVE"
        else:
            duty_required = 0.0
            status = "MARKET_STABLE_NO_DUTY"
            
        self.cursor.execute("""
        INSERT OR REPLACE INTO L4_Tariff_Shield (product_id, base_import_price, foreign_dumping_price, imposed_anti_dumping_duty)
        VALUES (?, ?, ?, ?);
        """, (product_id, base_domestic_cost, foreign_dump_price, round(duty_required, 2)))
        self.conn.commit()
        return round(duty_required, 2), status

    def calculate_national_forex_savings(self, import_volume_usd):
        if self.currency_delta < 0:
            return import_volume_usd * abs(self.currency_delta)
        return 0.0

    def shutdown(self):
        self.conn.close()

# ==========================================
# EXECUTION SIMULATION (LIVE TESTING)
# ==========================================
if __name__ == "__main__":
    # Booting the system with an in-memory test setup
    system = SovereignMasterMatrix(db_name=":memory:", current_usd_rate=83.20, base_usd_rate=84.00)
    
    print("======================================================================")
    print("🏛️     CHARKEY 2.0: FULL UNIFIED NATIONAL MASTER SYSTEM DASHBOARD     🏛️")
    print("======================================================================")
    
    # L1: Process a stuck industrial land dispute
    l1_cost = system.process_l1_judicial_case("CASE-LAND-2026", principal=50000000, years=4.5)
    print(f"[Layer 1 Bedrock] Judicial Opportunity Cost (Frozen Capital): ₹{l1_cost:,.2f}")
    
    # L2: Process a delayed administrative recruitment exam
    l2_loss = system.process_l2_exam_delay("EXAM-RECRUIT-09", total_candidates=50000, months_delayed=8)
    print(f"[Layer 2 Labor]   Demographic Dividend Tax Revenue Loss     : ₹{l2_loss:,.2f}")
    
    # L3: Process a local retail chain's transactional UPI data
    sri_score, decision = system.process_l3_merchant_sri("MERC-GORAKHPUR-12", turnover=400000, liabilities=180000, cash=35000)
    print(f"[Layer 3 DPI]     Grassroots MSME Audit -> SRI: {sri_score}      | Status: {decision}")
    
    # L4: Process import protection for local microchip manufacturing
    tariff, shield_status = system.process_l4_anti_dumping_shield("CHIP-SOLAR-5G", base_domestic_cost=1200, foreign_dump_price=850)
    forex_save = system.national_forex_savings = system.calculate_national_forex_savings(import_volume_usd=10000000)
    print(f"[Layer 4 Shield]  Dynamic Anti-Dumping Tariff Levied        : ₹{tariff} per unit")
    print(f"[Layer 4 Shield]  Forex Arbitrage National Savings          : ₹{forex_save:,.2f}")
    print("======================================================================")
    
    system.shutdown()
