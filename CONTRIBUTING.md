# Contributing to Residential HVAC Performance Baseline

Thank you for your interest in contributing to this residential energy performance research! This project documents real-world high-efficiency HVAC system performance to help homeowners, contractors, and researchers understand achievable efficiency targets in Climate Zone 5A.

## Ways to Contribute

### 1. Methodology Improvements

If you identify opportunities to improve the **Billing-Aligned methodology** or statistical validation approaches:

1. Open an issue describing the proposed enhancement
2. Include mathematical justification or references
3. If possible, demonstrate the improvement using the existing 2022-2025 dataset

**Examples:**

- Alternative balance point optimization methods
- Improved DHW/space heating separation algorithms
- Enhanced uncertainty quantification techniques

### 2. Comparative Data

This baseline would benefit from similar datasets in:

- Different climate zones (especially 4A, 5B, 6A)
- Different equipment vintages (pre-2015 vs. post-2020)
- Different building types (ranch, split-level, multi-family)

**If you have your own data:**

1. Open an issue titled "Comparative Dataset: [Your Climate Zone/Building Type]"
2. Share aggregated performance metrics (no raw utility bills required)
3. Document your equipment and envelope specifications

### 3. Analysis Scripts

Reproducibility is critical. If you develop analysis tools for:

- Automated billing-aligned calculations
- Weather data integration (NOAA API)
- Visualization of efficiency trends

Please contribute them to a `/scripts` directory with:

- Clear documentation
- Dependencies list (`requirements.txt` or equivalent)
- Example usage

### 4. Documentation Enhancements

Found a typo? Unclear explanation? Suggestions for:

- Improved clarity in technical sections
- Additional explanatory diagrams
- Cross-references between documents

Submit a pull request or open an issue.

---

## Contribution Guidelines

### Issue Reports

When opening an issue, please include:

**For Methodology Questions:**

- Section reference (e.g., "METHODOLOGY.md, Section 3.2")
- Specific calculation or assumption in question
- Your proposed alternative (if applicable)

**For Data Quality Concerns:**

- Metric in question (e.g., "2025 Heating Intensity: 95.5 CCF/1k HDD")
- Reason for concern (outlier, inconsistency, etc.)
- Supporting calculations

**For Documentation Improvements:**

- Document and section reference
- Specific text to change
- Proposed revision

### Pull Requests

1. **Fork the repository**
2. **Create a descriptive branch name:**
   - `methodology/balance-point-optimization`
   - `docs/clarify-UA-calculation`
   - `data/comparative-zone-6A`
3. **Make focused changes:** One topic per PR
4. **Test calculations:** If modifying methodology, verify against existing 2022-2025 results
5. **Update documentation:** If changing calculations, update all affected documents
6. **Submit PR with clear description:** What changed and why

### Code Style (if applicable)

For any analysis scripts:

- **Python:** Follow PEP 8
- **R:** Follow tidyverse style guide
- **Comments:** Explain *why*, not just *what*
- **Docstrings:** Describe inputs, outputs, and assumptions

---

## What NOT to Submit

### ❌ Raw Personal Data

**Do NOT commit:**

- Your actual utility bills (PDFs, scans, etc.)
- Addresses or specific location information
- Account numbers or personal identifiers

**Instead:**

- Share aggregated metrics only
- Use descriptive anonymized labels (e.g., "Home A, Climate Zone 5A")

### ❌ Promotional Content

This is a technical research repository, not a platform for:

- HVAC contractor advertising
- Product endorsements
- Affiliate links

---

## Discussion Topics

Open for community input:

1. **Balance Point Methodology:** Is HDD neutral-band optimization superior to regression-based approaches?
2. **DHW Variance Resolution:** How to reconcile the 15% Navien meter discrepancy?
3. **Dehumidifier Optimization:** Real-world validation of dew point control savings
4. **Regional Benchmarks:** What constitutes "efficient" varies by climate—help establish zone-specific targets

Join the discussion in [Issues](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/issues).

---

## Citation and Use

This data is freely available under the MIT License. If you use this methodology or reference this baseline in:

- Academic papers
- Professional reports
- Blog posts or articles
- Conference presentations

Please cite as:

```
Collis, W. K. (2026). Residential HVAC Performance Baseline: A Four-Year 
Longitudinal Study in Climate Zone 5A. GitHub Repository. 
https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-
```

---

## Questions?

**Technical Methodology:** Open an issue with the `question` label  
**Data Interpretation:** Open an issue with the `data-question` label  
**General Collaboration:** Email via GitHub profile or open a discussion

---

## Acknowledgments

Contributors who improve this baseline will be credited in:

- README.md acknowledgments section
- Specific document revision notes
- Future academic publications (if applicable)

Thank you for helping advance residential energy efficiency research!

---

**Repository Maintainer:** [@wkcollis1-eng](https://github.com/wkcollis1-eng)  
**Last Updated:** January 2026
