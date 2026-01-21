# Instructions for Adding Screenshots to GitHub Repository

## Step 1: Create Images Directory

In your local repository, create the directory structure:

```bash
cd /path/to/Residential-HVAC-Performance-Baseline-
mkdir -p docs/images
```

## Step 2: Save Screenshots

Save your screenshots with these filenames in the `docs/images/` directory:

1. `climate_comparison.png` - Screenshot from 12:24 AM showing climate comparison and efficiency deviation
2. `runtime_performance.png` - Screenshot showing today's runtime with zone balance gauge
3. `temperature_trends.png` - 48-hour temperature trend chart
4. `efficiency_trend.png` - 7-day efficiency deviation trend with HDD comparison
5. `runtime_analysis.png` - Daily runtime per HDD and floor runtime comparison
6. `recovery_rates.png` - Recovery rate trend showing 1F and 2F performance
7. `mtd_summary.png` - Month-to-date runtime and gas efficiency summary
8. `system_alerts.png` - System health alerts for short-cycling, efficiency, and UA
9. `spc_chart.png` - Statistical process control chart with 7-day rolling average

## Step 3: Add Files to Git

```bash
git add docs/images/*.png
git add REALTIME_MONITORING_2026.md
git commit -m "Add real-time monitoring documentation with Jan 20, 2026 cold snap analysis"
```

## Step 4: Push to GitHub

```bash
git push origin main
```

## Step 5: Verify Images Display

After pushing, visit your repository on GitHub and navigate to `REALTIME_MONITORING_2026.md` to verify all images display correctly.

---

## Alternative: Use GitHub Issues for Image Hosting (Quick Method)

If you don't want to commit images to the repository:

1. Create a new GitHub Issue in your repository
2. Drag and drop each screenshot into the issue comment box
3. GitHub will upload and provide URLs like: `https://user-images.githubusercontent.com/...`
4. Copy these URLs
5. Replace the image paths in the markdown file:

```markdown
![Climate Comparison](https://user-images.githubusercontent.com/YOUR_USER_ID/XXXXX/climate_comparison.png)
```

6. Close the issue (or keep it as "Documentation Images" reference)

---

## Screenshot Mapping Reference

| Markdown Reference | Your Original File | Description |
|-------------------|-------------------|-------------|
| climate_comparison.png | Screenshot_2026-01-20_212621.png | Climate status and efficiency deviation |
| runtime_performance.png | Screenshot_2026-01-20_084229.png | Zone balance and cycle analysis |
| temperature_trends.png | Screenshot_2026-01-20_090111.png | 48h temperature with outdoor conditions |
| efficiency_trend.png | Screenshot_2026-01-20_212703.png | 7-day efficiency deviation trend |
| runtime_analysis.png | Screenshot_2026-01-20_212602.png | Daily and weekly runtime charts |
| recovery_rates.png | Screenshot_2026-01-20_090237.png | Recovery rate trends by zone |
| mtd_summary.png | Screenshot_2026-01-20_212532.png | MTD runtime and gas efficiency |
| system_alerts.png | Screenshot_2026-01-20_212459.png | System health status alerts |
| spc_chart.png | Screenshot_2026-01-20_212427.png | Statistical process control |

---

## Optional: Update README.md

Add a link to the new documentation in your main README.md:

```markdown
## Repository Structure

├── BASELINE_REPORT.md          # Complete technical analysis (2022-2025)
├── REALTIME_MONITORING_2026.md # Real-time dashboard documentation (NEW)
├── DATA_SUMMARY.md              # Quick-reference metrics and tables
├── METHODOLOGY.md               # Billing-aligned calculation methodology
└── data/                        # Raw operational datasets
```

And in the "Applications" section:

```markdown
### Current

* Real-time performance monitoring via Home Assistant (Jan 2026+)
* Justification for whole-house energy monitor investment
* Diagnostic baseline for HVAC contractor communications
* Performance verification for high-efficiency equipment
```
