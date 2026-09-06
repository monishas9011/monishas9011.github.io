---
layout: single
title: "Setting up automation as a technical writer: where to start"
date: 2026-09-06
categories: [thoughts]
tags: [technical-writing, automation, docs-as-code, MCP, claude-code]
author_profile: true
header:
  teaser: /assets/images/blog6-header.png
---

<img src="/assets/images/blog6-header.png" alt="Setting Up Automation as a Technical Writer" style="width: 75%; display: block; margin: 0 auto 1.5em auto;">

Every technical writer has a moment where they think, "*didn't I just do this exact thing last week?*" Formatting checks before every publish, hunting down broken links after every release, confirming which articles reference a term that just changed. None of it is hard — it's just the same motion, over and over, and it quietly eats the hours you meant to spend actually writing.

The good news: most of these moments are automatable. The hard part isn't the tooling — it's knowing *which* task is worth automating in the first place.

## How to spot the task worth automating

Before you build anything, run the task through three questions:

1. **Frequency** — How many times have I done this exact thing this month?
2. **Pattern** — Is the input and output basically the same shape every time?
3. **Effort vs. value** — Does doing this manually cost me more time than automating it would, over a few cycles?

If a task clears all three, it's not a "nice to have" automation — it's a task quietly asking to be fixed.

## A knowledge base is code too

A knowledge base isn't just a pile of articles — it's a system, the same way a codebase is one. Articles depend on each other, reference the same features, break when something upstream changes, and go stale if nobody's watching. Once you see it that way, automation stops feeling like an engineering thing bolted onto writing, and starts feeling like ordinary maintenance — the same reason engineers automate builds, tests, and cleanup for their codebase.

Take release week, for me. Every cycle, I ran the same loop: check which existing articles might be affected by the change, open each candidate, re-read it, and confirm whether it needed an update. Across dozens of articles, under release-week time pressure, that added up fast — every single cycle.

Run it through the three questions: same task every release (frequency), same shape each time — search, open, read, judge (pattern), and the manual version was costing more focused hours than a fix would (effort vs. value). Clear yes on all three. So instead of manually searching and rereading, I built a small custom MCP for it — I just open the Claude Code terminal, describe what changed, and it surfaces the articles actually relevant to that change, so I can confirm relevance in a fraction of the time instead of re-reading a dozen articles to rule out ten of them.

## Where automation shows up for TWs

A few categories worth knowing, even if you never touch all of them:

- **Publishing** — build/deploy pipelines that turn your Markdown into a live site automatically (more on this in a future post)
- **Quality checks** — prose linting, broken-link checks, running automatically before anything ships
- **Content generation** — turning demo or webinar transcripts into a first-draft help article instead of writing one from a blank page
- **Maintenance** — flagging content that's gone stale or hasn't been touched in months

## Start smaller than you think

The temptation once you see this pattern is to automate everything at once. Don't. Pick the one task that keeps showing up and costing you real time, fix that first, and let the next automation reveal itself the same way this one did — by being annoying enough, often enough, to notice.
