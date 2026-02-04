# Quick Start: Uploading to GitHub

## Files in This Repository

This repository contains a complete set of professional documentation for your HVAC baseline:

```
📁 Repository Root
├── README.md                    # Main repository overview and navigation
├── BASELINE_REPORT.md           # Complete technical analysis (17,000+ words)
├── METHODOLOGY.md               # Detailed calculation procedures
├── DATA_SUMMARY.md              # Quick reference tables and metrics
├── SYSTEM_SPECIFICATIONS.md     # Equipment technical specifications
├── CONTRIBUTING.md              # Guidelines for community contributions
├── CHANGELOG.md                 # Version history and updates
├── LICENSE                      # MIT License for open sharing
└── .gitignore                   # Protects personal data from accidental commits
```

---

## Option 1: Upload via GitHub Web Interface (Easiest)

### Step 1: Navigate to Your Repository
Go to: https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-

### Step 2: Upload Files
1. Click **"Add file"** → **"Upload files"**
2. Drag all 9 files from this folder into the upload area:
   - README.md
   - BASELINE_REPORT.md
   - METHODOLOGY.md
   - DATA_SUMMARY.md
   - SYSTEM_SPECIFICATIONS.md
   - CONTRIBUTING.md
   - CHANGELOG.md
   - LICENSE
   - .gitignore

### Step 3: Commit Changes
1. Scroll down to **"Commit changes"**
2. **Commit message:** `Initial commit - v1.2.1 baseline documentation`
3. **Extended description (optional):**
   ```
   - Complete 4-year performance baseline (2022-2025)
   - Billing-aligned methodology documentation
   - Energy monitoring ROI analysis
   - System specifications and maintenance guidelines
   ```
4. Click **"Commit changes"**

---

## Option 2: Upload via Git Command Line

### Step 1: Clone Your Repository
```bash
cd ~/Documents  # or wherever you want to work
git clone https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-.git
cd Residential-HVAC-Performance-Baseline-
```

### Step 2: Copy Files
Copy all 9 files from the `/home/claude/hvac-baseline/` directory into your cloned repo directory.

### Step 3: Add and Commit
```bash
git add .
git commit -m "Initial commit - v1.2.1 baseline documentation"
```

### Step 4: Push to GitHub
```bash
git push origin main
```

---

## Option 3: Download Files First

If you don't have direct access to upload, I can prepare all files as a ZIP archive for you to download, then upload to GitHub.

---

## After Upload: Verify Your Repository

### Check the README Display
1. Navigate to your repository homepage
2. Verify that README.md renders correctly with:
   - Table of contents
   - Performance badges
   - Summary metrics table

### Verify File Links
Click through the links in README.md to ensure:
- BASELINE_REPORT.md loads properly
- METHODOLOGY.md displays equations correctly
- DATA_SUMMARY.md tables render cleanly

### Create Your First Release (Optional but Recommended)

1. Go to **"Releases"** in the right sidebar
2. Click **"Create a new release"**
3. **Tag version:** `v1.2.1`
4. **Release title:** `Version 1.2.1 - Four-Year Baseline (2022-2025)`
5. **Description:**
   ```
   Initial public release of residential HVAC performance baseline.
   
   **Highlights:**
   - 4-year statistical validation (CV < 8%)
   - Billing-aligned methodology
   - 33% better than regional efficiency average
   - Complete equipment specifications
   
   **Performance Metrics:**
   - Site EUI: 41.7 kBTU/ft²-yr
   - Heating Intensity: 95.5 CCF/1k HDD
   - Building UA: 480 BTU/hr-°F
   ```
6. Click **"Publish release"**

---

## Customization Tips

### Before Uploading, Consider

1. **Email Address:** The CONTRIBUTING.md references email via GitHub profile. Update if you want a specific contact method.

2. **P.E. Status:** BASELINE_REPORT.md footer says "P.E. (pending)". Update when appropriate.

3. **Privacy Check:** All files are anonymized with "Central Connecticut" rather than specific address. Verify no personal data slipped through.

4. **Future Data:** The .gitignore protects `/data/raw/*.csv` from accidental commits. Keep utility bills local!

---

## Next Steps After Upload

### 1. Enable GitHub Pages (Optional)
Turn your docs into a website:
1. Settings → Pages
2. Source: Deploy from main branch
3. Select `/docs` or root directory
4. Your baseline becomes accessible at `wkcollis1-eng.github.io/Residential-HVAC-Performance-Baseline-`

### 2. Set Up Issues
Create issue templates for:
- Methodology questions
- Data contributions
- Documentation improvements

### 3. Star Your Own Repo
Help with discoverability!

---

## Troubleshooting

**Problem:** README.md doesn't display properly  
**Solution:** Check for markdown syntax errors (tables, headers)

**Problem:** Files uploaded but not rendering  
**Solution:** Ensure file extensions are exactly `.md` (not `.md.txt`)

**Problem:** .gitignore not working  
**Solution:** Verify filename is exactly `.gitignore` (with leading dot)

---

## Questions?

If you encounter issues during upload, let me know and I can:
- Adjust any file formatting
- Create a ZIP archive for manual download
- Help debug git commands

---

**Repository URL:** https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-  
**Current Version:** 1.2.1  
**Files Ready:** 9 documents totaling ~40,000 words
