# How to Push This New Repo to GitHub

## Step 1: Create New Repo on GitHub

1. Go to https://github.com/new
2. Owner: vamsy16
3. Repository name: `performance-prospecting-system`
4. Description: "Find brands already running performance marketing + Audit them + Write outreach that gets replies. 4 skills for agency prospecting."
5. Public
6. DO NOT initialize with README (we already have)
7. Click "Create repository"

## Step 2: Push from This Workspace

Run these commands in terminal (in this Arena workspace, the folder is already ready):

```bash
cd /home/user/performance-prospecting-system

# Init git
git init
git add .
git commit -m "Initial commit: 4 prospecting skills - performance-lead-audit, ig-whatsapp-audit, lead-prospecting, outreach-personalizer + templates + demo Magicbricks audit"

# Add remote (replace with your repo URL)
git branch -M main
git remote add origin https://github.com/vamsy16/performance-prospecting-system.git

# Push
git push -u origin main
```

If you have SSH:
```bash
git remote add origin git@github.com:vamsy16/performance-prospecting-system.git
git push -u origin main
```

## Step 3: Install & Use Anywhere

After push, install in any Claude Code / Cursor / Codex project:

```bash
npx skills add vamsy16/performance-prospecting-system
npx skills add vamsy16/marketingskills
```

Then say:

```
"Find 5 D2C brands running ads in India"
"Audit boat-lifestyle.com for outreach"
"Audit Instagram @drbatras for WhatsApp funnel"
```

## Step 4: Use as Claude Code Plugin (Optional)

```bash
/plugin marketplace add vamsy16/performance-prospecting-system
/plugin install performance-prospecting-system
```

Then `/performance-lead-audit` etc.

---

## What's Inside This Repo

- skills/performance-lead-audit/SKILL.md (orchestrates ads+cro+analytics+competitor+cold-email)
- skills/ig-whatsapp-audit/SKILL.md (IG as landing page + WhatsApp funnel)
- skills/lead-prospecting/SKILL.md (Find spenders via Ad Library)
- skills/outreach-personalizer/SKILL.md (Roast/Value/FOMO templates)
- templates/ (CSV + demo audits + checklists)
- README.md, LICENSE, marketplace.json

Ready to push.
