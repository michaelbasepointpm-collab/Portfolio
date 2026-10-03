# Michael Tapia: Leasing & Property Management Portfolio

A one-page portfolio website for lease-up and leasing work:

1. **Lease-up portfolio**: Sunrise Village, Timbre & Harmony, The Hawthorn and ALMA Gastown (head leasing coordinator), plus REN (leasing agent).
2. **Multifamily portfolio**: the six Basepoint rental buildings.
3. **Strata leasing**: downtown and Main Street condo suites.
4. **How I run a lease-up**, **leasing intelligence**, **what an owner gets**, experience, brokerage and contact.

Plus `sample-dashboard/`: a lease-up dashboard with **fictional** data, showing the reporting format.

Plain HTML, CSS and JavaScript. No database. It runs on GitHub Pages for free.

## Folder structure

```
index.html                    The page (generated, but safe to edit by hand)
sample-dashboard/index.html   Sample lease-up dashboard (fictional data, self-contained)
assets/
  css/styles.css              Colours, fonts, layout
  js/main.js                  Scroll route, drawing animations, sketch/photo toggle
  img/
    favicon.svg               Browser-tab icon
    social-preview.png        Image LinkedIn shows when the link is shared
    profile/                  Headshot (WebP + JPG)
    photos/                   Building photos and renderings, sized for the web
    illustrations/            Building line drawings as standalone SVG files
    brokerage/                Put basepoint-logo.svg here to replace the text wordmark
tools/
  content.py                  All building text and facts
  page.template.html          Page layout with placeholders
  sketches.py, mf_sketches.py Building line drawings
  build.py                    Rebuilds index.html: py tools/build.py .
  social-preview.html         Source for social-preview.png
_originals/                   Full-size original images (not published, see .gitignore)
```

## Preview on your computer

Double-click `index.html`.

## Publish on GitHub Pages

1. Sign in at github.com and create a new **public** repository, for example `michael-tapia-portfolio`.
2. Choose **uploading an existing file** and drag in everything in this folder **except** `_originals` and `.claude`.
3. Click **Commit changes**.
4. Go to **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then **Save**.
5. After a minute or two, the site is live at `https://YOUR-USERNAME.github.io/michael-tapia-portfolio/`.
6. In `index.html`, change the `og:image` line to the full address (for example `https://YOUR-USERNAME.github.io/michael-tapia-portfolio/assets/img/social-preview.png`) so LinkedIn shows the preview image.

To use your own domain later (for example `michaeltapia.ca`), add it under **Settings → Pages → Custom domain**.

## Editing content

For a quick text fix, edit `index.html` directly. For bigger changes (new buildings, new sketches), edit `tools/content.py` and run `py tools/build.py .` from this folder. That regenerates `index.html`, so copy any hand edits into `content.py` first.

## When the licence arrives

In `tools/content.py`, change `LICENSED = False` to `LICENSED = True`, then run `py tools/build.py .`. The brokerage section and the title under the photo switch to the licensed wording. Don't switch it before the BCFSA licence is issued.

## Sources for building facts

Building facts come from public sources: Brightside Community Homes, Basepoint Real Estate Group, Forum Asset Management / ALMA, Hudson Projects, Rize Alliance, West Haven and the City of Vancouver. Where sources disagreed (for example unit counts at Selkirk and 911 W 71st), the site leaves the disputed number out.

## Privacy

The site shows no tenant, applicant or owner information, and no strata unit numbers. Keep it that way when adding content.
