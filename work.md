---
layout: single
title: "Work"
author_profile: false
permalink: /work/
---

<style>
  * { box-sizing: border-box; }

  .hint {
    font-size: 12px;
    color: #bbb;
    margin-bottom: 32px;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
    margin-top: 8px;
  }

  .card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 10px;
    padding: 24px;
    cursor: pointer;
    transition: box-shadow 0.2s, border-color 0.2s;
  }

  .card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    border-color: #ccc;
  }

  .card.open {
    border-color: #1a1a1a;
  }

  .card-tag {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 8px;
  }

  .card-title {
    font-size: 16px;
    font-weight: 600;
    color: #1a1a1a;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .card-title .arrow {
    font-size: 14px;
    color: #ccc;
    transition: transform 0.2s;
  }

  .card.open .arrow {
    transform: rotate(180deg);
    color: #1a1a1a;
  }

  .card-desc {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
    margin-top: 14px;
    display: none;
    border-top: 1px solid #f0f0f0;
    padding-top: 14px;
  }

  .card.open .card-desc {
    display: block;
  }
</style>

<p class="hint">Click a card to read more</p>

<div class="grid">

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">AI</div>
    <div class="card-title">Agentic Doc Generation <span class="arrow">↓</span></div>
    <div class="card-desc">Designed the workflow the team now runs at scale. Ran the experiments that proved bulk generation fails — documented four distinct failure modes — then proposed the distributed model that became the operating architecture. Restructured the delivery pipeline to run review and publishing in parallel, cutting the overall timeline.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">AI</div>
    <div class="card-title">Team AI Transformation <span class="arrow">↓</span></div>
    <div class="card-desc">Designed and ran a structured AI training programme — workshops, guides, and hands-on sessions. Content output nearly tripled and the entire team moved faster across the board. 100% adoption.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">AI</div>
    <div class="card-title">Executive Reporting <span class="arrow">↓</span></div>
    <div class="card-desc">Built a weekly HTML report delivered to the CTO and CPO — tracking team velocity, module coverage, week-over-week progress, and blockers in one place. Replaced a manual newsletter with a communication tool that gives leadership the full picture at a glance. Designed and automated using AI.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">AI</div>
    <div class="card-title">Analytics Dashboards <span class="arrow">↓</span></div>
    <div class="card-desc">Built four Looker Studio dashboards across seven data sources — giving leadership its first live view of documentation health: content coverage, doc staleness, failed customer searches, team workload, and publishing velocity. Designed and automated using AI — dashboards update automatically every month, no manual effort required.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Strategy</div>
    <div class="card-title">Interactive AI Doc Layer <span class="arrow">↓</span></div>
    <div class="card-desc">Pitched a strategic vision for treating the documentation portal like a product — roadmap, measurement, and iteration cycles tied to customer usage patterns. The pitch was absorbed into a larger AI initiative I'm currently building. Details coming soon.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Strategy</div>
    <div class="card-title">Product Coverage <span class="arrow">↓</span></div>
    <div class="card-desc">Led a team-wide documentation audit across 91 product areas, establishing gap mapping and data-driven prioritisation based on actual config usage data.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Strategy</div>
    <div class="card-title">Self-Serve Coverage <span class="arrow">↓</span></div>
    <div class="card-desc">Achieved 100% documentation coverage across all features available on the product UI — a company OKR — reducing support ticket volume directly.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Infrastructure</div>
    <div class="card-title">Measurement Frameworks <span class="arrow">↓</span></div>
    <div class="card-desc">Designed the first-ever in-app documentation measurement framework at Eightfold — tracking the full journey from content awareness to feature adoption using Pendo. Previously, effectiveness was measured by email open rates alone. Now it covers completion rate, drop-off analysis, and feature activation.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Partnerships</div>
    <div class="card-title">Cross-Functional Partnerships <span class="arrow">↓</span></div>
    <div class="card-desc">Built strategic partnerships with Solutions Delivery, Engineering, Product, UX, and Customer Success teams. Launched an Implementation Portal, converted internal knowledge into customer-facing documentation, and conducted AI tooling training across teams.</div>
  </div>

  <div class="card" onclick="toggle(this)">
    <div class="card-tag">Writing</div>
    <div class="card-title">Writing & Documentation <span class="arrow">↓</span></div>
    <div class="card-desc">Across Eightfold, Yellow.ai, and Zoho — 10 years building documentation governance as a system: the processes, guardrails, and maintenance workflows that keep documentation consistent, accurate, and scalable across teams and products.</div>
  </div>

</div>

<script>
  function toggle(card) {
    card.classList.toggle('open');
  }
</script>
