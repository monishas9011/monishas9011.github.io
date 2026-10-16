---
layout: single
title: "Every redesign is an information architecture project"
date: 2026-10-16
categories: [thoughts]
tags: [technical-writing, information-architecture, documentation, strategy]
author_profile: true
header:
  teaser: /assets/images/blog8-header.png
---

<img src="/assets/images/blog8-header.png" alt="Every page redesign is an Information Architecture decision" style="width: 75%; display: block; margin: 0 auto 1.5em auto;">

This sounds like an overstatement until you look at what actually happens. You cut a section. You decide not to build a page because something elsewhere already covers it. You leave a body of content on another team's platform and link to it instead. Each of those changes what a reader can find and how they find it. Each one is an architectural decision.

The decisions get made either way. The only variable is whether you make them deliberately, or inherit them from whatever the old structure happened to do.

Here are seven questions a redesign will ask you. You don't get to skip any of them. You only get to choose whether you answer them on purpose.

---

## 1. Boundaries: what belongs here at all

Before you decide how content is structured, decide what content is in scope.

Most redesigns treat this as settled. The assumption is that the boundary of the space is the boundary of what's in it today. That assumption is almost always wrong, because the current contents are a record of what previous teams happened to publish, not a considered decision about what belongs.

On one project, a large body of enablement material lived on a separate platform owned by another team. The question wasn't whether that content was good. It was whether it belonged inside our information space, adjacent to it, or linked from it. Three different answers, three different architectures.

A related question came up with frequently asked questions. The obvious move was to build a FAQ section. The decision was not to, because a community forum already served that need and served it better. That's a boundary drawn on purpose rather than by omission.

Ask early: what are the neighbouring content systems, who owns them, and where does the edge sit?

## 2. Inventory: what you actually have

You can't restructure what you haven't enumerated.

This is the least interesting step and reliably the longest. It's also the one teams skip, because the navigation looks like an inventory. It isn't. Navigation is a map of what someone once believed existed, maintained by people who had other priorities.

A real inventory turns up three things you didn't expect. Content that exists but is unreachable. Content that's reachable by two different paths that disagree with each other. And content that everyone assumed existed and doesn't.

When we audited coverage against the actual feature set rather than the existing content list, the gap was much larger than the number everyone had been quoting. Neither number was dishonest. They were measured against different denominators, and nobody had examined the denominator.

Do the inventory first. Expect it to take longer than the restructuring that follows.

## 3. Grouping: how things nest

This is the part people mean when they say information architecture. It's the visible output: categories, hierarchy, depth.

The recurring failure is grouping content the way the product is built rather than the way people look for it. Internal structure is seductive because it's already agreed, already documented, and matches how teams are organised. It's also invisible to the reader, who arrives with a task rather than an org chart.

When the two conflict, the reader's model wins. That's uncomfortable, because defending it means telling colleagues their team's shape isn't going to show up in the navigation.

## 4. Labels: what you call things

Naming is architecture, not copy.

A perfect hierarchy with internal names is unfindable. The gap between what a team calls a feature and what a reader calls it is where most searches fail, and it rarely closes on its own, because the internal term is the one everyone in the room already uses.

Part of our redesign involved reopening a feature's name. The internal term was accurate and well established. It wasn't the term readers typed. Renaming was harder than restructuring, and mattered more.

Test your labels with people who don't work on the product. If a name needs explaining, it isn't doing its job.

## 5. Entry points: how people arrive

Almost nobody arrives at your homepage.

People land in the middle of your structure: from a search engine, a support reply, a link inside the product, a colleague's message. A hierarchy that only makes sense when read from the top is broken for most of the traffic it receives.

Instead of designing the landing page, we mapped every entry point for each type of content: where a reader could arrive from, and what they would see when they got there. The exercise changed the design, because several routes led to pages that made no sense without context the reader didn't have.

Every page is a landing page. Structure has to survive being entered in the middle.

## 6. Access: who can see what

This one gets treated as a permissions detail to settle after launch. It's structure.

If parts of your space are visible only to some readers, you don't have one architecture. You have several overlapping ones, and each reader experiences a different shape. That's manageable, but only if you design it rather than discover it.

There are usually three states, not two. Public. Restricted behind a sign-in. And a third, awkward category: technically reachable by anyone with a link, but never intended for a general audience. We found content in that third state which was entirely appropriate for the audience it was built for, and a problem the moment the surrounding space became public.

Label every item by visibility during the inventory. The third state is the one that causes trouble.

## 7. Lifecycle: what happens to what you replace

Redesigns create orphans: superseded pages, dead links, articles that now say something the product no longer does.

For each replaced item, there are three options. Redirect it to whatever supersedes it. Archive it so it stays available but stops being promoted. Or remove it. Choosing nothing means choosing the fourth option, which is leaving it in place to contradict the new content.

There's an opportunity here worth naming. Nobody deprecates documentation voluntarily: there's no reward for it and there's always something more pressing. A redesign is usually the only moment an organisation will agree to clean up. Use the cover while you have it.

---

## The default is still an answer

None of these questions are optional. A redesign that ignores boundaries inherits them. A redesign that skips the inventory restructures a subset of what exists and calls it complete. A redesign that treats access as a permissions task ships a structure that behaves differently for different readers, and finds out later.

The work isn't adding an information architecture phase to your project. It's recognising that you're already doing the work, and deciding to do it deliberately.
