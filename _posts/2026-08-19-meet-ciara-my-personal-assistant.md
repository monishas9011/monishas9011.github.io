---
layout: single
title: "Meet Ciara, my personal assistant(agent)"
date: 2026-08-19
categories: [thoughts]
tags: [technical-writing, AI, productivity, MCP, claude-code]
author_profile: true
header:
  teaser: /assets/images/blog5-header.png
---

<img src="/assets/images/blog5-header.png" alt="Meet Ciara, my personal assistant" style="width: 75%; display: block; margin: 0 auto 1.5em auto;">

No, I did not get one.

Ciara is my work log agent I set up to track everything I work on during the week, synthesise it, and drop it into my notes every Friday. Named her, gave her instructions, connected her to my tools. She's not a person but she does the one thing I've never managed to do consistently myself: keep a clear record of what I actually did.

I've been using her for the past few weeks now, and honestly, it's so easy. Here's why I built her, and how.

## Do you actually know what you did last week?

Most people don't.

Not because they weren't working, but because knowledge work leaves no obvious trail. You finish a doc, close a tab, move to the next thing. By Friday, the week is a blur. By the following Tuesday, it's gone.

And then someone asks you something.

*"Hey, what was the status of that API doc we discussed?"*
*"Did we ever resolve that comment from the engineering team?"*

And you know you dealt with it. You just can't remember where, or when, or what you concluded. So you start digging: Slack, email, your CMS, Jira, calendar, triangulating your own past from six different systems that don't talk to each other.

That's a lot of effort just to answer a question about your own work.

**The problem isn't recall. It's collation.**

Your work is documented. It's just documented in fragments, scattered across every tool you touch. There's no single place that says: here is what you did this week, in plain language, in one place.

This is the gap Ciara fills.

## How I built her

Ciara runs on Claude Code, connected to the tools where my work actually lives:

- **Google Workspace**, Calendar, Gmail, and Drive (pre-built MCP integrations, took minutes to set up)
- **Slack** (same, pre-built connector, a few config steps)
- **My CMS**, I built a custom MCP connector for our documentation portal, since it doesn't have a public one. It gives Ciara read access to my published docs, drafts, and revision history

**MCP (Model Context Protocol)** is the standard that lets an AI agent connect to external tools, think of it as the plumbing that lets Ciara read your actual data, not just chat with you about it.

The second piece is her instruction file, a plain text README that lives in my Claude Code project. It tells Ciara exactly what to do:

- **Where to look:** calendar events I organised or attended, Slack threads I replied in, docs I created or revised, emails where I was the primary sender or decision-maker
- **What to skip:** FYI threads, automated notifications, calendar holds
- **How to group it:** by project, not by tool, and flag anything still open
- **What format I want:** one short paragraph at the top, then bullets by project, then a "still in progress" list at the bottom

That instruction file is the real work. The more precisely you describe what counts as meaningful output versus background noise, the better Ciara's summaries get. I treat it like briefing a new team member: specific, no assumptions, updated when my workflow changes.

## What changes

The next time someone asks me something, in a meeting, on Slack, mid-conversation, I don't have to excavate. I open my notes, find the relevant week, and I have the answer in under a minute.

More useful than that: I stop losing track of my own work. A lot of the cognitive overhead of knowledge work isn't the work itself, it's the ongoing effort of remembering what you did, where things stand, and what's still waiting on you. One clear record per week removes most of that.

## Where to start

If you have Google Workspace and Slack, you can have a basic version of Ciara running today, both have pre-built MCP connectors for Claude Code. Write a simple instruction file, run it at the end of the week, save the output somewhere you'll actually check.

If your most important tool is something custom, a CMS, an internal wiki, a proprietary ticketing system, check if it has an API. If it does, you can build a connector. It's less work than it sounds.

Every Friday, I ask Ciara what I got done. She tells me. It takes about few minutes, and I haven't once had to dig through six tools to answer a question about my own work since.

She's not a person. But she's a pretty good assistant.

<p style="margin-top: 2em; font-weight: 600;">Monisha</p>
