-- SQL Script for Layer 3: DPI Transaction & Formalization Ledger

-- 1. Create Table for Real-time DPI Transactions (UPI/NPCI Mapped)
CREATE TABLE IF NOT EXISTS dpi_transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    merchant_id VARCHAR(50) NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    transaction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_mode VARCHAR(20) DEFAULT 'UPI',
    status VARCHAR(20) DEFAULT 'SUCCESS'
);

-- 2. Create Table for Merchant Credit Profiles (Formalized Economy Data)
CREATE TABLE IF NOT EXISTS merchant_credit_profiles (
    merchant_id VARCHAR(50) PRIMARY KEY,
    business_name VARCHAR(100) NOT NULL,
    total_volume_inr DECIMAL(15, 2) DEFAULT 0.00,
    transaction_count INT DEFAULT 0,
    credit_score_rating INT DEFAULT 500, -- Dynamic rating between 300 and 900
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
