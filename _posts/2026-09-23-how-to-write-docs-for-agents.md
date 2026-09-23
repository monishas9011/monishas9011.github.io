---
layout: single
title: "How to write docs for agents"
date: 2026-09-23
categories: [thoughts]
tags: [technical-writing, AI, agents, docs-as-code]
author_profile: true
header:
  teaser: /assets/images/blog7-header.png
---

<img src="/assets/images/blog7-header.png" alt="How to write docs for agents" style="width: 75%; display: block; margin: 0 auto 1.5em auto;">

Somewhere in the last year, our audience quietly changed. It's not just people opening our docs anymore, it's agents. Claude Code answering a question by fetching a page. A RAG pipeline pulling one paragraph out of context. A support bot summarizing a policy doc in half a second. If your writing only makes sense to a human reading top to bottom, an agent grabbing one chunk out of order won't get it.

Here's what actually changes when you write for that reader too.

## Hot tips for writing docs agents can actually use

- **Make every section stand alone.** Agents often retrieve one chunk, not the whole page. "As discussed above" means nothing to something that never saw "above."
- **Front-load the answer.** Skip the warm-up paragraph. Say the fact in sentence one.
- **Use descriptive links, not "click here."** An agent following a link needs the link text to *be* the description.
- **Reach for structure over prose.** Tables, steps, code blocks: agents pattern-match structure far more reliably than they parse dense paragraphs for the same fact.
- **Cut the marketing language.** "Seamlessly," "powerful," "game-changing" is noise an agent has to filter past to find the actual fact.
- **Publish a manifest, not just pages.** Formats like `llms.txt` give agents an explicit index instead of making them infer structure by crawling. [Browse sites already publishing one](https://directory.llmstxt.cloud/) to see what a good one looks like.

## How I actually found this out

I stumbled onto this by accident, looking into `llms.txt`, a format sites now publish specifically so agents can read them efficiently. Reading the spec, I went and checked my own site to see how far behind I was.

I wasn't behind. I already had a `feed.xml`, a `sitemap.xml`, and structured metadata on every page: a clean, structured list of everything I've published, no rendering or guessing required. I'd set all of it up months ago for SEO and so RSS readers could subscribe to my posts. I never once thought about agents when I did it. Turns out a feed reader and an agent want the exact same thing: a plain list of what exists, not a page they have to parse to figure it out. `llms.txt` is solving a problem RSS solved decades ago. I already had the fix running in the background.

So I went further and pulled up my blog's quality checker, a script I run before every post goes live. One rule jumped out immediately: descriptive link text, not "click here" or "read more." I'd built that in July, purely so human readers wouldn't hit a vague link and bounce. Not one thought about agents.

Then I checked the rest of the checker. Almost every rule held up the same way. One H1 per post, no skipped heading levels: added so my posts wouldn't ramble, and it also means anything reading my headings gets a clean outline instead of guessing structure from font size. Alt text required on every image: added for accessibility, and it's the only way a text-only reader knows what the image even shows. A filler-phrase check flagging things like "it is important to note": added to tighten my prose, and it has the exact same effect as cutting noise for a reader that's scanning for the fact, not the flourish.

I never designed a single one of these for agents. I designed all of them so a human wouldn't roll their eyes and close the tab. Writing clearly for people was never really a different skill from writing clearly for machines. We just didn't know we needed to check.
