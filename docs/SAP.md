2\. Statistical Analysis Plan (SAP) for the IIT Protocol

This formal Statistical Analysis Plan outlines the methodology for processing clinical data collected during the 12-week open-label evaluation of the unmixed Cupric (\(Cu^{2+}\)) formulation.

2.1 Populations for Analysis

-   **Intent-to-Treat (ITT) Population:** Includes all enrolled participants who receive at least one dose of the therapeutic cupric formulation. The ITT population serves as the primary dataset for demographic and baseline characteristics.
-   **Per-Protocol (PP) Population:** Consists of all participants who complete the full 12-week regimen, miss no more than one scheduled safety evaluation, and strictly adhere to target dosing constraints. The PP population acts as the primary group for efficacy endpoint testing.
-   **Safety Population:** Includes all patients who receive any amount of the study compound, used exclusively to track adverse events (AEs) and liver enzyme spikes.

2.2 Endpoint Evaluations

-   **Primary Efficacy Endpoint:** The percentage of patients achieving a stable target therapeutic serum copper range (\(70\text{--}140\ \mu\text{g/dL}\)) by Week 4.
-   **Secondary Efficacy Endpoints:**
    -   Mean change from baseline in Absolute Neutrophil Count (ANC) at Week 4, 8, and 12.
    -   Mean change from baseline in Mean Corpuscular Volume (MCV) at Week 12.
-   **Primary Safety Endpoints:** Incidence of hepatotoxicity, defined as alanine aminotransferase (ALT) or aspartate aminotransferase (AST) elevations exceeding \(2\times\) the Upper Limit of Normal (ULN).

2.3 Statistical Methodology

```
Primary Endpoint Proportions Hypothesis:
H0: P_success <= 0.60  (Null Hypothesis: Baseline clinical success rate is 60% or lower)
Ha: P_success > 0.60   (Alternative Hypothesis: Success rate with unmixed cupric exceeds 60%)

Tested using a one-sided exact binomial test at a significance level (alpha) of 0.05.

```

-   **Continuous Variables Analysis:** Longitudinal shifts in serum copper, ceruloplasmin, and ANC metrics will be evaluated using a **Repeated Measures ANOVA** or a linear mixed-effects model to account for missing intra-treatment data points over the 12-week lifecycle.
-   **Handling of Missing Data:** Missing values for primary endpoints within the ITT population will be managed using **Last Observation Carried Forward (LOCF)** as a conservative standard baseline.
-   **Sample Size Sensitivity:** With an enrollment target of \(N=45\), a true success rate of 80% provides \(>85\%\) statistical power to reject the null hypothesis (\(P \le 0.60\)) using an exact binomial setup with an alpha of 0.05.

* * * * *
