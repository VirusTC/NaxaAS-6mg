"""
Cupric Bioavailability and Total Daily Intake (TDI) Calculator.
Enforces metabolic boundaries to prevent systemic copper toxicity.
"""

def calculate_total_daily_intake(c_oral: float, v_oral: float, alpha: float, c_iv: float, v_iv: float) -> float:
    """
    Calculates the Total Daily Intake (TDI) of Cu2+ ions in milligrams.
    
    Formula:
    TDI = (c_oral * v_oral * alpha) + (c_iv * v_iv)
    
    Parameters:
    c_oral (float): Concentration of oral copper solution (mg/mL).
    v_oral (float): Daily volume of oral solution administered (mL).
    alpha  (float): Gastrointestinal absorption coefficient (typically 0.3 to 0.4).
    c_iv   (float): Concentration of intravenous copper solution (mg/mL).
    v_iv   (float): Daily volume of intravenous solution administered (mL).
    
    Returns:
    float: Total systemic copper load delivered per 24-hour cycle.
    """
    oral_component = c_oral * v_oral * alpha
    iv_component = c_iv * v_iv
    return oral_component + iv_component

def verify_safety_threshold(tdi: float, upper_limit: float = 10.0) -> bool:
    """
    Cross-checks calculated total daily intake against safe physiological caps.
    Default upper limit is set to 10.0 mg/day (Standard Adult UL).
    """
    if tdi > upper_limit:
        return False
    return True

if __name__ == "__main__":
    # Example operational scenario configuration
    ORAL_CONC = 0.5    # 0.5 mg/mL
    ORAL_VOL = 10.0    # 10 mL
    GI_ABSORP = 0.35   # 35% estimated GI uptake
    
    IV_CONC = 0.1      # 0.1 mg/mL
    IV_VOL = 20.0      # 20 mL
    
    MAX_SAFE_UL = 10.0 # 10 mg/day max limit
    
    systemic_load = calculate_total_daily_intake(ORAL_CONC, ORAL_VOL, GI_ABSORP, IV_CONC, IV_VOL)
    is_safe = verify_safety_threshold(systemic_load, MAX_SAFE_UL)
    
    print(f"Calculated Systemic Copper Intake: {systemic_load:.2f} mg/day")
    print(f"Protocol Safety Status: {'APPROVED' if is_safe else 'ALERT: EXCEEDS LIMIT'}")
