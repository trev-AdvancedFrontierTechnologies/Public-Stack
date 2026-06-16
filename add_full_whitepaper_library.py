from pathlib import Path
import re
import html

ROOT = Path.home() / "aft-public-software"
SITE = ROOT / "site"
WHITE = SITE / "whitepapers"
WHITE.mkdir(parents=True, exist_ok=True)

CONTACT_EMAIL = "trev@smileqt.com"
GENERAL_EMAIL = "contact@advancedfrontiertechnologies.com"
UEI = "W2MEEUJACRJ3"
CAGE = "1ZV02"

papers = [
    ("Core Architecture", "AFT Sovereign Agentic Lattice", "Governed 21-agent lattice architecture for structured multi-agent collaboration, state tracking, simulation linkage, and evidence-controlled reasoning."),
    ("Core Architecture", "SMILEQT Sovereign Lattice Runtime", "Runtime design for discrete lattice-based agent orchestration, role separation, agent communication, and traceable collaboration."),
    ("Core Architecture", "Paladin Governance Runtime", "Governance layer for priority handling, claim control, validation boundaries, safety posture, evidence review, and state-machine oversight."),
    ("Core Architecture", "BrainV3 Cause-Effect Reasoning", "Causal reasoning framework for hypothesis tracking, system-state interpretation, principle extraction, and evidence-linked reasoning."),
    ("Core Architecture", "T.R.E.Y. OMEGA Simulation Layer", "Physics-informed and lattice-oriented simulation framework for experimentation, simulation-to-principle extraction, and technical discovery workflows."),
    ("Core Architecture", "Evidence-Controlled Deployment", "AFT’s approach to Docker packaging, service manifests, checksums, ProofPackets, validation status, and public/private evidence separation."),
    ("Core Architecture", "ProofPacket Evidence Architecture", "Framework for organizing technical claims, prototype evidence, validation gaps, screenshots, logs, benchmarks, and partner-diligence materials."),
    ("Core Architecture", "Sovereign Edge Runtime Architecture", "Local-first, edge-deployable runtime architecture for controlled AI, simulation, governance, and service orchestration."),

    ("Public Software & DevOps", "Public-Stack Repository Overview", "Description of AFT’s public-safe GitHub repository, demo API, static site, whitepapers, governance endpoint, and Docker Compose examples."),
    ("Public Software & DevOps", "AFT Docker/MCP Runtime Skeleton", "Technical overview of the Docker/MCP routing model, service layout, local deployment structure, and reproducibility goals."),
    ("Public Software & DevOps", "Public-Safe Software Release Policy", "Rules for what can and cannot be published publicly, including secrets, model weights, logs, binders, Docker archives, .env files, and private evidence."),
    ("Public Software & DevOps", "Service Manifest and Restoration Workflow", "How AFT packages services, images, volumes, manifests, hashes, and restore helpers for prototype preservation and diligence review."),
    ("Public Software & DevOps", "GitHub Pages Public Website Deployment", "AFT’s static website publication approach using GitHub Pages, DNS, custom domain routing, and public documentation workflows."),

    ("Agentic AI & Governance", "Governed Agentic AI Systems", "Company-wide framework for safe, auditable, validation-first agentic systems."),
    ("Agentic AI & Governance", "Agent Collaboration Beyond Chatbot Chains", "Why AFT uses structured agent lattices instead of loosely connected prompt chains."),
    ("Agentic AI & Governance", "Discrete Lattice Coordination for Multi-Agent Systems", "Conceptual basis for using discrete combinatorial structures to coordinate agents and preserve explainability."),
    ("Agentic AI & Governance", "Agent State, Memory, and Evidence Boundaries", "How AFT separates state, memory, reasoning traces, evidence, and public/private outputs."),
    ("Agentic AI & Governance", "Human Oversight in High-Consequence Agentic Workflows", "Human-in-the-loop and human-on-the-loop concepts for prototype, pilot, and regulated contexts."),
    ("Agentic AI & Governance", "Claim Governance for AI Outputs", "AFT’s approach to separating hypothesis, prototype evidence, benchmark evidence, validated result, and certified claim."),
    ("Agentic AI & Governance", "Paladin Priority Model", "Explanation of priority ordering for correctness, IP, legal, safety, evidence, and operational boundaries."),

    ("Simulation & Science Discovery", "Simulation-to-Principle Extraction", "How AFT proposes converting simulation outputs into reusable principles, decision rules, and evidence-backed explanations."),
    ("Simulation & Science Discovery", "Lattice-Based Scientific Discovery Workflows", "Use of lattice structures for hypothesis generation, simulation planning, and traceable discovery."),
    ("Simulation & Science Discovery", "Physics-Informed Agentic Experimentation", "Combining simulation tools, agentic reasoning, causal tracking, and governance controls."),
    ("Simulation & Science Discovery", "OpenFOAM/GMSH-Inspired Simulation Workflows", "Public-safe overview of CFD-style and mesh-based experimentation concepts."),
    ("Simulation & Science Discovery", "Genesis/Lysis Modeling Concepts", "Concept-stage description of formation, transformation, breakdown, and system-state evolution modeling."),
    ("Simulation & Science Discovery", "Benchmarking Governed Agentic Systems", "Metrics and evaluation pathways for collaboration quality, reproducibility, drift, causal traceability, and validation progress."),
    ("Simulation & Science Discovery", "Entropy-Sieve Information Filtering", "Conceptual paper on information filtering, signal extraction, and evidence selection within agentic systems."),
    ("Simulation & Science Discovery", "Temporal Mechanics and State Evolution in Agent Lattices", "Public-safe overview of time-aware state updates, event tracking, and dynamic reasoning."),

    ("Emergency Response & Healthcare-Adjacent Concepts", "Flying Triage Concept", "Public-safe overview of AFT’s emergency-response and digital-twin concept direction."),
    ("Emergency Response & Healthcare-Adjacent Concepts", "Emergency Response Digital Twin Framework", "Modeling scene state, resources, triage flow, and response coordination under strict validation boundaries."),
    ("Emergency Response & Healthcare-Adjacent Concepts", "Human-Supervised Triage Support Research", "Research concept for assisting triage planning without claiming medical-device, clinical, or life-safety readiness."),
    ("Emergency Response & Healthcare-Adjacent Concepts", "Responder Scene Intelligence Concepts", "High-level overview of scene understanding, routing, alerts, and evidence-controlled situational modeling."),
    ("Emergency Response & Healthcare-Adjacent Concepts", "Healthcare-Adjacent Simulation Boundaries", "Clear separation between research simulations, decision-support prototypes, and regulated clinical systems."),
    ("Emergency Response & Healthcare-Adjacent Concepts", "Validation Pathway for Emergency-Response AI Concepts", "Steps needed before any emergency-response or healthcare-adjacent concept could move beyond prototype review."),

    ("Government & Transition Readiness", "AFT Public Capability Statement", "Company overview, identifiers, technical focus areas, NAICS-style positioning, and contact information."),
    ("Government & Transition Readiness", "Sovereign Systems for Government-Facing Research", "Broad non-solicitation-specific paper on AFT’s relevance to sovereign AI, edge systems, simulation, and governed autonomy."),
    ("Government & Transition Readiness", "Validation-First Government Transition Pathway", "Prototype to technical diligence to controlled pilot to independent validation to procurement pathway."),
    ("Government & Transition Readiness", "Edge-Deployed Governed AI for Contested Environments", "Public-safe overview of local-first AI/runtime concepts for degraded connectivity and sovereign operation."),
    ("Government & Transition Readiness", "Build/Adapt/Sustain Software Architecture", "Modular architecture for rapidly adapting software components while preserving governance and evidence controls."),
    ("Government & Transition Readiness", "Procurement Claim Boundary and Evidence Control", "How AFT communicates readiness without implying approval, award, certification, endorsement, or operational validation."),

    ("Partner / Investor Materials", "AFT Company Technical Overview", "Broad technical summary of AFT’s platforms, architecture, prototype evidence, and validation posture."),
    ("Partner / Investor Materials", "Partner Discovery Brief", "Overview for collaborators, labs, integrators, and strategic partners."),
    ("Partner / Investor Materials", "Investor Technical Diligence Brief", "Public-safe explanation of what has been prototyped, what remains to validate, and what the company is building toward."),
    ("Partner / Investor Materials", "Platform Roadmap and Milestone Framework", "Product and research roadmap across Paladin, SMILEQT, T.R.E.Y. OMEGA, ProofPacket, Flying Triage, and Public-Stack."),
    ("Partner / Investor Materials", "AFT Intellectual Property Development Posture", "Public-safe IP posture without claiming patent-secured status unless filings are verified."),
    ("Partner / Investor Materials", "Commercialization Pathways for Governed Agentic Systems", "Potential markets, transition paths, and validation requirements."),

    ("Security, Safety & Compliance", "Public-Safe Repository Security Policy", "What AFT prevents from entering public repos: keys, secrets, credentials, archives, .env, model weights, logs, and private records."),
    ("Security, Safety & Compliance", "Prototype Cybersecurity Boundary", "Difference between local prototype security, production cybersecurity, compliance review, and authority-to-operate pathways."),
    ("Security, Safety & Compliance", "Evidence Handling and Redaction Policy", "How AFT separates public materials, NDA materials, private binders, partner records, and regulated information."),
    ("Security, Safety & Compliance", "Safety Case Development for Agentic Systems", "Early structure for building safety cases around AI/agentic workflows."),
    ("Security, Safety & Compliance", "Responsible AI and Validation Controls", "AFT’s company-wide responsible AI posture: human oversight, evidence boundaries, testing, auditability, and no unsupported claims."),
]

def slugify(s):
    s = s.lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

category_context = {
    "Core Architecture": {
        "purpose": "define the technical spine of AFT's company-wide architecture",
        "audience": "technical reviewers, partners, integrators, and diligence teams",
        "methods": ["structured architecture review", "runtime boundary definition", "evidence mapping", "controlled prototype iteration"],
    },
    "Public Software & DevOps": {
        "purpose": "explain the public-safe software, documentation, and deployment practices around AFT's repository and site",
        "audience": "developers, open-source reviewers, partners, and technical diligence teams",
        "methods": ["GitHub workflow hygiene", "Dockerized examples", "public-safety checks", "release boundary review"],
    },
    "Agentic AI & Governance": {
        "purpose": "describe how AFT approaches governed agentic systems without unsupported readiness claims",
        "audience": "AI researchers, safety reviewers, integrators, and partner teams",
        "methods": ["agent-state separation", "human oversight design", "claim boundary control", "governance event logging"],
    },
    "Simulation & Science Discovery": {
        "purpose": "outline simulation-linked discovery workflows under a validation-first posture",
        "audience": "simulation teams, research partners, labs, and technical reviewers",
        "methods": ["simulation planning", "hypothesis tracking", "principle extraction", "benchmark design"],
    },
    "Emergency Response & Healthcare-Adjacent Concepts": {
        "purpose": "separate concept-stage emergency-response and healthcare-adjacent modeling from regulated deployment claims",
        "audience": "emergency-response partners, healthcare-adjacent reviewers, validation teams, and technical collaborators",
        "methods": ["research-only modeling", "human-supervised workflow design", "scene-state simulation", "validation pathway planning"],
    },
    "Government & Transition Readiness": {
        "purpose": "explain transition-oriented architecture and readiness boundaries without implying award, approval, endorsement, or procurement status",
        "audience": "government-facing partners, integrators, procurement-adjacent reviewers, and technical transition teams",
        "methods": ["capability mapping", "pilot planning", "validation milestone design", "evidence-controlled communication"],
    },
    "Partner / Investor Materials": {
        "purpose": "support company-level diligence with clear separation between prototype evidence, roadmap, and validated claims",
        "audience": "partners, advisors, investors, collaborators, and strategic reviewers",
        "methods": ["technical diligence framing", "roadmap mapping", "risk-boundary review", "evidence summary packaging"],
    },
    "Security, Safety & Compliance": {
        "purpose": "define AFT's public-safety, security, redaction, and validation control posture",
        "audience": "security reviewers, compliance teams, partners, and internal maintainers",
        "methods": ["secret scanning", "redaction policy", "safety case planning", "prototype cybersecurity boundary review"],
    },
}

STYLE = """
<style>
:root{--bg:#070b14;--panel:#101827;--text:#eef4ff;--muted:#a8b3c7;--line:#263247;--accent:#67e8f9}
*{box-sizing:border-box}
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#070b14;color:var(--text);line-height:1.65}
header,main,footer{max-width:980px;margin:auto;padding:32px 20px}
nav{display:flex;justify-content:space-between;gap:16px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:18px;flex-wrap:wrap}
nav a{color:var(--muted);text-decoration:none;margin-left:16px;font-size:14px}
nav a:hover{color:var(--accent)}
h1{font-size:clamp(34px,6vw,58px);line-height:1.06;margin:42px 0 14px}
h2{margin-top:42px;border-top:1px solid var(--line);padding-top:26px}
p,li{color:var(--muted);font-size:17px}
strong{color:var(--text)}
.meta,.notice{border:1px solid var(--line);background:rgba(16,24,39,.78);border-radius:18px;padding:20px;margin:24px 0}
.notice{background:rgba(255,255,255,.04);font-size:15px;color:var(--muted)}
code{color:var(--accent);background:rgba(255,255,255,.05);padding:2px 6px;border-radius:6px}
.button{display:inline-block;border:1px solid var(--accent);color:#07111f;background:var(--accent);padding:10px 16px;border-radius:999px;text-decoration:none;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:26px}
.card{border:1px solid var(--line);background:rgba(16,24,39,.78);border-radius:18px;padding:20px}
.tag{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:5px 10px;color:var(--muted);font-size:13px;margin:4px 6px 4px 0}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:14px}
</style>
"""

def page(title, category, abstract):
    ctx = category_context[category]
    methods = "".join(f"<li>{html.escape(m.capitalize())}.</li>" for m in ctx["methods"])
    title_e = html.escape(title)
    category_e = html.escape(category)
    abstract_e = html.escape(abstract)
    purpose_e = html.escape(ctx["purpose"])
    audience_e = html.escape(ctx["audience"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title_e} | Advanced Frontier Technologies</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{abstract_e}">
{STYLE}
</head>
<body>
<header>
<nav>
<div><strong>Advanced Frontier Technologies</strong></div>
<div><a href="/">Home</a><a href="/whitepapers/">Whitepapers</a><a href="/#contact">Contact</a></div>
</nav>
<h1>{title_e}</h1>
<p>{abstract_e}</p>
<div class="meta">
<p><strong>Category:</strong> {category_e}</p>
<p><strong>Organization:</strong> Advanced Frontier Technologies</p>
<p><strong>Public posture:</strong> Prototype-backed · Validation-first · Evidence-controlled</p>
<p><strong>Entity identifiers:</strong> UEI <code>{UEI}</code> · CAGE <code>{CAGE}</code></p>
</div>
</header>
<main>
<div class="notice">
This paper is a public-safe company brief. It does not claim certified life-safety readiness,
clinical readiness, procurement approval, production readiness, patent-secured status,
government endorsement, operational validation, FedRAMP authorization, or authority to operate.
Any regulated, operational, clinical, emergency-response, defense, or procurement-sensitive use
would require independent validation, cybersecurity review, contractual authorization, and applicable certification.
</div>

<h2>Executive Summary</h2>
<p>
{title_e} is part of AFT's company-wide whitepaper library. Its purpose is to {purpose_e}
while preserving a clear boundary between public demonstrations, private diligence materials,
prototype evidence, and future validation work.
</p>
<p>
The intended audience includes {audience_e}. This paper is written as a public-safe summary and
should be read as a planning, architecture, and partner-discovery artifact rather than as a
certification, procurement, or deployment claim.
</p>

<h2>Problem Context</h2>
<p>
High-consequence technical systems require more than isolated demos. They require traceable
architecture, reproducible evidence, governed claims, human-review boundaries, and a disciplined
transition path from prototype to independently evaluated pilot. AFT's work is organized around
that separation: what has been prototyped, what is being proposed, what remains unvalidated, and
what evidence would be required before any sensitive deployment.
</p>

<h2>AFT Approach</h2>
<p>
AFT frames this topic through a prototype-backed, validation-first, evidence-controlled model.
The approach emphasizes modular runtime components, public-safe documentation, reproducible
examples, controlled language, and traceability across agentic, simulation, governance, and
deployment workflows.
</p>
<ul>
{methods}
<li>Public/private evidence separation.</li>
<li>Clear distinction between demonstration, pilot, validation, and certified deployment.</li>
</ul>

<h2>Representative Architecture</h2>
<p>
Relevant AFT components may include SMILEQT Sovereign Lattice Runtime, Paladin Governance,
T.R.E.Y. OMEGA simulation workflows, BrainV3 cause-effect reasoning, Evidence Locker concepts,
ProofPacket-style documentation, Docker/MCP deployment skeletons, and the Public-Stack repository.
Not every component is required for every use case; the purpose of the architecture is to keep
capabilities modular, governable, and reviewable.
</p>

<h2>Evidence and Validation Path</h2>
<p>
Public-facing evidence should remain limited to non-sensitive screenshots, demo endpoints,
repository files, service summaries, whitepapers, and controlled descriptions. More detailed
evidence, including logs, private binders, internal runtime packages, benchmark details, partner
records, or proprietary implementation notes, should remain private or NDA-bound until reviewed.
</p>
<p>
A mature validation path would include reproducible test cases, benchmark definitions, independent
review, cybersecurity review, human-oversight procedures, risk analysis, and domain-specific
certification where applicable.
</p>

<h2>Risks and Boundaries</h2>
<ul>
<li>Prototype demonstrations should not be presented as production systems.</li>
<li>Research concepts should not be presented as certified emergency-response, clinical, or life-safety tools.</li>
<li>Government-facing language should not imply award, approval, endorsement, or procurement status.</li>
<li>Benchmark language should remain qualified unless independently verified.</li>
<li>Private infrastructure details, credentials, logs, raw paths, customer data, partner records, and sensitive archives should not be published.</li>
</ul>

<h2>Recommended Next Steps</h2>
<ul>
<li>Maintain this paper as a public-safe overview.</li>
<li>Use private ProofPacket materials for deeper diligence when appropriate.</li>
<li>Define validation milestones before pilot claims.</li>
<li>Keep GitHub, website, and partner materials aligned with the same claim boundary.</li>
</ul>

<h2>Point of Contact</h2>
<p>
<strong>Trevor Yohn</strong><br>
Founder & Systems Architect<br>
Advanced Frontier Technologies<br>
<strong>Email:</strong> {CONTACT_EMAIL}<br>
<strong>General Contact:</strong> {GENERAL_EMAIL}
</p>
<p><a class="button" href="/whitepapers/">Back to whitepapers</a></p>
</main>
<footer>
© <span id="year"></span> Advanced Frontier Technologies · UEI: {UEI} · CAGE: {CAGE}. All rights reserved.
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</footer>
</body>
</html>
"""

# Write individual pages.
items = []
for category, title, abstract in papers:
    slug = slugify(title)
    path = WHITE / f"{slug}.html"
    path.write_text(page(title, category, abstract), encoding="utf-8")
    items.append((category, title, abstract, slug))

# Build index grouped by category.
groups = {}
for category, title, abstract, slug in items:
    groups.setdefault(category, []).append((title, abstract, slug))

cards = []
for category, entries in groups.items():
    links = []
    for title, abstract, slug in entries:
        links.append(f"""
<section class="card">
<h3>{html.escape(title)}</h3>
<p>{html.escape(abstract)}</p>
<a class="button" href="/whitepapers/{slug}.html">Read paper</a>
</section>
""")
    cards.append(f"""
<h2>{html.escape(category)}</h2>
<div class="grid">
{''.join(links)}
</div>
""")

index_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AFT Whitepapers | Advanced Frontier Technologies</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Company-wide public-safe whitepapers and technical briefs from Advanced Frontier Technologies.">
{STYLE}
</head>
<body>
<header>
<nav>
<div><strong>Advanced Frontier Technologies</strong></div>
<div><a href="/">Home</a><a href="/whitepapers/">Whitepapers</a><a href="/#platforms">Platforms</a><a href="/#contact">Contact</a></div>
</nav>
<h1>Company Whitepapers & Technical Briefs</h1>
<p>
Public-safe papers, concept briefs, and technical notes covering Advanced Frontier Technologies'
work across sovereign systems, governed agentic AI, simulation, evidence packaging, edge deployment,
emergency-response concepts, healthcare-adjacent modeling, partner discovery, security, and transition planning.
</p>
<div class="meta">
<p><strong>Library size:</strong> {len(papers)} public-safe whitepaper pages</p>
<p><strong>Posture:</strong> Prototype-backed · Validation-first · Evidence-controlled</p>
<p><strong>Entity identifiers:</strong> UEI <code>{UEI}</code> · CAGE <code>{CAGE}</code></p>
</div>
</header>
<main>
<div class="notice">
These materials are public-safe summaries. They do not claim certified life-safety readiness, clinical readiness,
procurement approval, production readiness, patent-secured status, government endorsement, operational validation,
FedRAMP authorization, or authority to operate.
</div>
{''.join(cards)}
</main>
<footer>
© <span id="year"></span> Advanced Frontier Technologies · UEI: {UEI} · CAGE: {CAGE}. All rights reserved.
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</footer>
</body>
</html>
"""
(WHITE / "index.html").write_text(index_html, encoding="utf-8")

# Update home page teaser.
home = SITE / "index.html"
if home.exists():
    s = home.read_text(encoding="utf-8")
    if 'href="/whitepapers/"' not in s:
        s = s.replace('<a href="#platforms">Platforms</a>', '<a href="#platforms">Platforms</a>\\n        <a href="/whitepapers/">Whitepapers</a>')
    teaser = """
    <section id="whitepapers" style="margin-top:56px;">
      <h2>Company Whitepapers & Technical Briefs</h2>
      <p>
        Explore AFT's public-safe library of 51 whitepapers covering sovereign systems,
        governed agentic AI, simulation, evidence-controlled deployment, emergency-response
        concepts, partner discovery, security, and validation-first transition planning.
      </p>
      <div class="procurement-box">
        <p><strong>Whitepaper Library:</strong> Full company-wide public-safe technical brief catalog.</p>
        <p><a class="button secondary" href="/whitepapers/">View whitepapers</a></p>
      </div>
    </section>
"""
    if '<section id="whitepapers"' in s:
        start = s.find('<section id="whitepapers"')
        end = s.find('</section>', start)
        if end != -1:
            end += len('</section>')
            s = s[:start] + teaser + s[end:]
    elif '    <section id="procurement"' in s:
        s = s.replace('    <section id="procurement"', teaser + '\\n    <section id="procurement"')
    elif '</main>' in s:
        s = s.replace('</main>', teaser + '\\n</main>')
    home.write_text(s, encoding="utf-8")

print(f"Wrote {len(papers)} whitepaper pages to {WHITE}")
