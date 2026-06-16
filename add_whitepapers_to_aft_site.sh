#!/usr/bin/env bash
set -Eeuo pipefail

SITE_DIR="$HOME/aft_company_site"
WEB_DIR="$SITE_DIR/site"
INDEX="$WEB_DIR/index.html"
STAMP="$(date +%Y%m%d_%H%M%S)"

echo "== Adding whitepapers section to AFT company site =="

if [ ! -f "$INDEX" ]; then
  echo "Missing site index: $INDEX" >&2
  exit 1
fi

mkdir -p "$WEB_DIR/whitepapers" "$SITE_DIR/backups"
cp "$INDEX" "$SITE_DIR/backups/index_before_whitepapers_${STAMP}.html"

###############################################################################
# Whitepapers landing page
###############################################################################

cat > "$WEB_DIR/whitepapers/index.html" <<'HTML'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AFT Whitepapers | Advanced Frontier Technologies</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Public-safe whitepapers and technical briefs from Advanced Frontier Technologies.">
  <style>
    :root {
      --bg: #070b14;
      --panel: #101827;
      --text: #eef4ff;
      --muted: #a8b3c7;
      --line: #263247;
      --accent: #67e8f9;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: radial-gradient(circle at top, #14213d 0, var(--bg) 45%);
      color: var(--text);
      line-height: 1.6;
    }
    header, main, footer {
      max-width: 1040px;
      margin: auto;
      padding: 32px 20px;
    }
    nav {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: center;
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
    }
    nav a {
      color: var(--muted);
      text-decoration: none;
      margin-left: 16px;
      font-size: 14px;
    }
    nav a:hover { color: var(--accent); }
    h1 {
      font-size: clamp(36px, 6vw, 64px);
      line-height: 1.04;
      margin: 48px 0 18px;
    }
    p { color: var(--muted); font-size: 18px; }
    .card {
      border: 1px solid var(--line);
      background: rgba(16, 24, 39, 0.78);
      border-radius: 18px;
      padding: 22px;
      margin: 22px 0;
    }
    .card h2 { margin-top: 0; }
    .button {
      display: inline-block;
      border: 1px solid var(--accent);
      color: var(--bg);
      background: var(--accent);
      padding: 10px 16px;
      border-radius: 999px;
      text-decoration: none;
      font-weight: 700;
      margin-top: 8px;
    }
    .tag {
      display: inline-block;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 5px 10px;
      color: var(--muted);
      font-size: 13px;
      margin: 4px 6px 4px 0;
    }
    .notice {
      border: 1px solid var(--line);
      background: rgba(255,255,255,0.04);
      border-radius: 18px;
      padding: 18px;
      color: var(--muted);
      font-size: 15px;
    }
    footer {
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 14px;
    }
  </style>
</head>
<body>
  <header>
    <nav>
      <div><strong>Advanced Frontier Technologies</strong></div>
      <div>
        <a href="/">Home</a>
        <a href="/whitepapers/">Whitepapers</a>
        <a href="/#contact">Contact</a>
      </div>
    </nav>

    <h1>Whitepapers & Technical Briefs</h1>
    <p>
      Public-safe concept papers, technical briefs, and proposal summaries from Advanced Frontier Technologies.
    </p>
  </header>

  <main>
    <div class="notice">
      Materials in this section are public-safe summaries. They are prototype-backed, validation-first,
      and evidence-controlled. They do not claim certified life-safety readiness, clinical readiness,
      procurement approval, production readiness, patent-secured status, or government endorsement unless
      separately verified in an authorized written record.
    </div>

    <section class="card">
      <h2>AFT Sovereign Agentic Lattice for Defense Science Discovery</h2>
      <p>
        A public-safe executive concept brief describing AFT’s proposed SMILEQT Sovereign Lattice Runtime,
        Paladin Governance layer, and T.R.E.Y. OMEGA simulation approach for DARPA-facing research pathways.
      </p>
      <div>
        <span class="tag">Agentic AI</span>
        <span class="tag">Governance</span>
        <span class="tag">Simulation</span>
        <span class="tag">DARPA-facing concept</span>
      </div>
      <a class="button" href="/whitepapers/aft-sovereign-agentic-lattice-darpa-concept.html">Read brief</a>
    </section>

    <section class="card">
      <h2>Additional Whitepapers</h2>
      <p>
        Additional public-safe technical briefs will be added here as they are reviewed and cleared for public release.
      </p>
    </section>
  </main>

  <footer>
    © <span id="year"></span> Advanced Frontier Technologies · UEI: W2MEEUJACRJ3 · CAGE: 1ZV02. All rights reserved.
    <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  </footer>
</body>
</html>
HTML

###############################################################################
# DARPA concept brief page
###############################################################################

cat > "$WEB_DIR/whitepapers/aft-sovereign-agentic-lattice-darpa-concept.html" <<'HTML'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AFT Sovereign Agentic Lattice | DARPA Concept Brief</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Public-safe DARPA-facing concept brief for AFT Sovereign Agentic Lattice.">
  <style>
    :root {
      --bg: #070b14;
      --panel: #101827;
      --text: #eef4ff;
      --muted: #a8b3c7;
      --line: #263247;
      --accent: #67e8f9;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: #070b14;
      color: var(--text);
      line-height: 1.65;
    }
    header, main, footer {
      max-width: 980px;
      margin: auto;
      padding: 32px 20px;
    }
    nav {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: center;
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
    }
    nav a {
      color: var(--muted);
      text-decoration: none;
      margin-left: 16px;
      font-size: 14px;
    }
    nav a:hover { color: var(--accent); }
    h1 {
      font-size: clamp(34px, 6vw, 58px);
      line-height: 1.06;
      margin: 42px 0 14px;
    }
    h2 {
      margin-top: 42px;
      border-top: 1px solid var(--line);
      padding-top: 26px;
    }
    p, li { color: var(--muted); font-size: 17px; }
    strong { color: var(--text); }
    .meta, .notice {
      border: 1px solid var(--line);
      background: rgba(16, 24, 39, 0.78);
      border-radius: 18px;
      padding: 20px;
      margin: 24px 0;
    }
    .notice {
      background: rgba(255,255,255,0.04);
      font-size: 15px;
      color: var(--muted);
    }
    code {
      color: var(--accent);
      background: rgba(255,255,255,0.05);
      padding: 2px 6px;
      border-radius: 6px;
    }
    footer {
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 14px;
    }
  </style>
</head>
<body>
  <header>
    <nav>
      <div><strong>Advanced Frontier Technologies</strong></div>
      <div>
        <a href="/">Home</a>
        <a href="/whitepapers/">Whitepapers</a>
        <a href="/#contact">Contact</a>
      </div>
    </nav>

    <h1>AFT Sovereign Agentic Lattice for Defense Science Discovery</h1>
    <p>
      Public-safe executive concept brief for DARPA-facing research pathways.
    </p>

    <div class="meta">
      <p><strong>Proposer:</strong> Advanced Frontier Technologies</p>
      <p><strong>Principal Investigator:</strong> Trevor Yohn, Founder & Systems Architect</p>
      <p><strong>Date:</strong> June 16, 2026</p>
      <p><strong>Entity Identifiers:</strong> UEI <code>W2MEEUJACRJ3</code> · CAGE <code>1ZV02</code></p>
      <p><strong>Public Posture:</strong> Prototype-backed · Validation-first · Evidence-controlled</p>
    </div>
  </header>

  <main>
    <div class="notice">
      This brief is a public-safe concept summary. It is not a formal government submission and does not imply
      government endorsement, procurement approval, certification, clinical readiness, life-safety approval,
      production readiness, patent-secured status, or operational validation.
    </div>

    <h2>Problem Statement</h2>
    <p>
      Current agentic AI systems lack rigorous mathematical, systems-theoretic, and information-theoretic
      foundations for scalable, explainable collaboration in complex science-discovery tasks. This limits their
      usefulness in contested, edge, and high-consequence environments where autonomous reasoning, simulation,
      adaptation, and traceability must be governed, reproducible, and auditable.
    </p>

    <h2>AFT Proposed Direction</h2>
    <p>
      Advanced Frontier Technologies proposes the <strong>SMILEQT Sovereign Lattice Runtime</strong>, integrated
      with <strong>Paladin Governance</strong> and the <strong>T.R.E.Y. OMEGA physics/simulation layer</strong>.
      The proposed system is a prototype-backed, validation-first, 21-agent discrete lattice architecture designed
      to support governed agent collaboration, simulation-driven principle extraction, and reproducible evidence
      packaging.
    </p>

    <h2>Core Components</h2>
    <ul>
      <li><strong>SMILEQT Sovereign Lattice Runtime:</strong> A structured 21-agent collaboration architecture for role separation, state tracking, and traceable reasoning.</li>
      <li><strong>Paladin Governance:</strong> A state-machine oversight layer for policy, priority, evidence, and safety constraints.</li>
      <li><strong>T.R.E.Y. OMEGA Physics Layer:</strong> A simulation-oriented runtime for lattice, CFD-style, and physics-informed experimentation.</li>
      <li><strong>BrainV3 Cause-Effect Reasoning:</strong> A causal reasoning component for hypothesis tracking and principle extraction.</li>
      <li><strong>Docker/MCP Deployment Skeleton:</strong> A modular local/edge deployment model for reproducible runtime packaging and transition experiments.</li>
    </ul>

    <h2>Technical Area Alignment</h2>
    <p>
      The concept can be framed toward mathematically grounded agent collaboration, simulation-to-principle
      workflows, or transition-oriented edge deployment depending on the selected solicitation pathway.
    </p>

    <ul>
      <li><strong>Mathematical agent collaboration:</strong> Discrete lattice structures, temporal state evolution, and information-filtering mechanisms for explainable agent coordination.</li>
      <li><strong>Simulation-to-principle extraction:</strong> Workflows that convert simulation outputs into auditable principles, reusable decision rules, and evidence-backed discovery packets.</li>
      <li><strong>Transition architecture:</strong> Dockerized service modules, MCP-style tool routing, local-first deployment, and evidence-controlled restoration packages.</li>
    </ul>

    <h2>Existing Prototype Evidence</h2>
    <p>
      AFT has assembled a local Docker-based prototype environment and a public-safe software repository that
      demonstrate a company site, public demo API, governance/status endpoint, 21-agent lattice demonstration,
      evidence pipeline service, T.R.E.Y. OMEGA simulation stub, and reproducible service packaging workflow.
    </p>

    <p>
      Public-safe repository: <code>trev-AdvancedFrontierTechnologies/Public-Stack</code>
    </p>

    <h2>Expected Impact</h2>
    <p>
      If successful, the proposed work would enable more rigorous foundations for multi-agent scientific discovery,
      explainable collaboration among autonomous reasoning agents, reproducible simulation-to-principle pipelines,
      sovereign edge-deployable runtime packages, and governed experimentation for defense-relevant technology
      discovery.
    </p>

    <h2>Risk Boundary</h2>
    <p>
      All claims are prototype-backed and validation-first. AFT does not claim that the current system is certified,
      production-ready, clinically ready, life-safety approved, procurement approved, patent-secured, or operationally
      validated. Full validation, independent benchmarking, cybersecurity review, and certification would be required
      prior to any regulated, defense-operational, clinical, emergency-response, or procurement-sensitive deployment.
    </p>

    <h2>Point of Contact</h2>
    <p>
      <strong>Trevor Yohn</strong><br>
      Founder & Systems Architect<br>
      Advanced Frontier Technologies<br>
      <strong>Email:</strong> trev@smileqt.com<br>
      <strong>General Contact:</strong> contact@advancedfrontiertechnologies.com
    </p>
  </main>

  <footer>
    © <span id="year"></span> Advanced Frontier Technologies · UEI: W2MEEUJACRJ3 · CAGE: 1ZV02. All rights reserved.
    <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  </footer>
</body>
</html>
HTML

###############################################################################
# Patch home page nav and add whitepapers teaser section
###############################################################################

python3 <<'PY'
from pathlib import Path

index = Path.home() / "aft_company_site/site/index.html"
s = index.read_text()

# Add nav link if absent.
if 'href="/whitepapers/"' not in s:
    s = s.replace(
        '<a href="#platforms">Platforms</a>',
        '<a href="#platforms">Platforms</a>\n        <a href="/whitepapers/">Whitepapers</a>'
    )

# Add whitepapers section before procurement or contact if absent.
section = """
    <section id="whitepapers" style="margin-top:56px;">
      <h2>Whitepapers & Technical Briefs</h2>
      <p>
        Public-safe concept papers and technical briefs covering AFT's prototype-backed,
        validation-first work in sovereign AI, governed agentic systems, simulation-driven discovery,
        and evidence-controlled deployment.
      </p>
      <div class="procurement-box">
        <p><strong>Featured:</strong> AFT Sovereign Agentic Lattice for Defense Science Discovery</p>
        <p>
          A DARPA-facing public-safe concept brief describing SMILEQT Sovereign Lattice Runtime,
          Paladin Governance, and T.R.E.Y. OMEGA simulation workflows.
        </p>
        <p><a class="button secondary" href="/whitepapers/">View whitepapers</a></p>
      </div>
    </section>

"""

if 'id="whitepapers"' not in s:
    if '    <section id="procurement"' in s:
        s = s.replace('    <section id="procurement"', section + '    <section id="procurement"')
    elif '    <section id="contact"' in s:
        s = s.replace('    <section id="contact"', section + '    <section id="contact"')
    else:
        s = s.replace('</main>', section + '</main>')

index.write_text(s)
PY

###############################################################################
# Reload and verify
###############################################################################

echo
echo "== Reloading company site =="
docker exec aft_company_site nginx -s reload >/dev/null 2>&1 || docker restart aft_company_site >/dev/null

echo
echo "== Verifying local pages =="
curl -fsS http://127.0.0.1:8088/health
echo
curl -fsS http://127.0.0.1:8088/whitepapers/ | grep -E "Whitepapers|Sovereign Agentic Lattice|UEI|CAGE"
curl -fsS http://127.0.0.1:8088/whitepapers/aft-sovereign-agentic-lattice-darpa-concept.html | grep -E "DARPA|Sovereign Agentic Lattice|W2MEEUJACRJ3|1ZV02"

echo
echo "== Creating site backup =="
tar czf "$HOME/aft_company_site_whitepapers_${STAMP}.tar.gz" -C "$HOME" aft_company_site
ls -lh "$HOME/aft_company_site_whitepapers_${STAMP}.tar.gz"

###############################################################################
# Optional sync to Public-Stack repo if present
###############################################################################

if [ -d "$HOME/aft-public-software/.git" ]; then
  echo
  echo "== Syncing site changes to Public-Stack repo =="
  mkdir -p "$HOME/aft-public-software/site"
  cp -a "$WEB_DIR/." "$HOME/aft-public-software/site/"

  cd "$HOME/aft-public-software"
  git add site
  if git diff --cached --quiet; then
    echo "No Public-Stack site changes to commit."
  else
    git commit -m "Add public whitepapers section"
    git push
  fi
fi

echo
echo "DONE."
echo "Whitepapers:"
echo "  http://127.0.0.1:8088/whitepapers/"
echo "Featured brief:"
echo "  http://127.0.0.1:8088/whitepapers/aft-sovereign-agentic-lattice-darpa-concept.html"
