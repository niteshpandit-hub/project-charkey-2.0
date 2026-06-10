import datetime

class AACLEngine:
    def __init__(self, exam_id, scheduled_date, buffer_days=30, daily_penalty_rate=500):
        """
        AACL Engine initializes the strict tracking parameters for national examinations.
        """
        self.exam_id = exam_id
        self.scheduled_date = datetime.datetime.strptime(scheduled_date, "%Y-%m-%d")
        self.buffer_days = buffer_days
        self.daily_penalty_rate = daily_penalty_rate # Surcharge amount in INR per day delayed

    def calculate_administrative_liability(self, actual_release_date):
        """
        Computes the delay duration and automated financial surcharges if the buffer is breached.
        """
        actual_date = datetime.datetime.strptime(actual_release_date, "%Y-%m-%d")
        deadline_date = self.scheduled_date + datetime.timedelta(days=self.buffer_days)
        
        if actual_date <= deadline_date:
            return {
                "status": "SUCCESS",
                "days_delayed": 0,
                "penalty_inr": 0,
                "message": "Examination cycle executed within the legally permitted statutory buffer."
            }
        else:
            days_delayed = (actual_date - deadline_date).days
            total_penalty = days_delayed * self.daily_penalty_rate
            return {
                "status": "BREACH_DETECTED",
                "days_delayed": days_delayed,
                "penalty_inr": total_penalty,
                "message": f"CRITICAL: Regulatory buffer breached by {days_delayed} days. Administrative surcharge active."
            }

# Example validation logic
if __name__ == "__main__":
    # Supposing an exam was supposed to declare results by June 1, 2026
    tracker = AACLEngine(exam_id="UGC-NET-2026", scheduled_date="2026-06-01")
    
    # Simulating a delayed release on July 15, 2026 (beyond the 30-day buffer)
    audit_report = tracker.calculate_administrative_liability(actual_release_date="2026-07-15")
    print(f"Audit Status: {audit_report['status']}")
    print(f"Total Penalty Imposed: ₹{audit_report['penalty_inr']}")
