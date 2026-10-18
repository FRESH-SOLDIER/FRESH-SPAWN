# Fresh Spawn: notes for improvement runs

Live site: https://fresh-soldier.github.io/FRESH-SPAWN/
Game data and images come from RAWG. Every page must keep the visible link back to RAWG and every game must link to its RAWG page.

## Rules for automated improvement runs
- Edit `src/template.html` (design, layout, behavior). Never hand-edit `index.html`; run `python3 build.py` to regenerate it.
- Make ONE focused improvement per run. Test it in a browser (Playwright, Chromium at /opt/pw-browsers/chromium) at desktop (1100px) and phone (400px) width, with no console errors, before pushing.
- Do NOT add ads, affiliate links, analytics or trackers. The owner has not signed up for any program.
- Do NOT add new external hosts or API calls. Keep every required credit and link back (see footer).
- Do NOT copy or re-host audio or artwork beyond the picture sheets already in `sheets/`.
- Do not put the owner's real name or email anywhere. Commit as `FRESH-SOLDIER <FRESH-SOLDIER@users.noreply.github.com>`.
- After pushing, wait 2 minutes and check that the live page returns 200 and its title is correct. If it is broken, revert the commit and push the revert.
- Append one line to `CHANGELOG.md`: date, what changed, why.
