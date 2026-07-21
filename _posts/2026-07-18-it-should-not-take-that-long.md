---
layout: single
title: '"It shouldn''t take that long" — what''s really happening on our end'
date: 2026-07-18
categories: [thoughts]
tags: [technical-writing, documentation, career, AI]
author_profile: true
header:
  teaser: /assets/images/blog3-header.png
---

<img src="/assets/images/blog3-header.png" alt="It shouldn't take that long" style="width: 75%; display: block; margin: 0 auto 1.5em auto;">

We're hearing this one a lot more lately. And I think I know why.

Stakeholders have started handing us their own documents (AI-generated write-ups, screenshots included) and saying, essentially, "here you go." And sure, if the job were to take that document and hit Publish, they'd be right. It wouldn't take long at all. But publishing is where our job begins, not ends.

---

## Step one: verifying the flow

The first thing I do with any handoff, human-written or AI-generated, is replicate the flow myself. I open the product, I follow the steps, and almost every time, the sequential order in the document doesn't match what actually happens on screen. The feature behaves differently than described. A step is missing. Two steps are in the wrong order.

And the AI-generated version? Oh, it's thorough. It has a Definition section. It has a Key Benefits section (I know). It has an Executive Summary explaining what the feature does in three confident, beautifully structured paragraphs.

What it doesn't have is accuracy. AI doesn't hallucinate quietly. It hallucinates in complete sentences with excellent grammar. Which means I'm not just editing for style. I'm fact-checking every claim against the live product, hunting for the places where the prose sounds right but the information is wrong.

---

## Step two: structure doesn't exist yet, and that's my job

What I receive is text. What users need is a document.

That gap, between text and document, is invisible to everyone but me. It's where I decide: does this need a table or a list? Where do headings go, and what should they say? How do I categorize this information so that the person who needs step 4 doesn't have to read steps 1 through 3 to find it?

These aren't cosmetic decisions. They're architectural. And they have to be consistent, not just internally within this doc, but across every other document we've published. Readers notice when one doc calls it "Prerequisites" and another calls it "Before You Begin" and a third just buries the requirements in paragraph two without a heading at all.

I'm the one making sure that doesn't happen.

---

## Step three: the screenshots are a whole thing

Let's talk about the screenshots, because this one deserves its own section.

Every screenshot goes through a verification pass: does it contain real user data, real email addresses, real names, anything that should not be published on a documentation site?

And while I'm doing that, I'm also checking something else entirely: is this screenshot even current? Documentation gets written at a point in time. The UI doesn't stay still. A button that was labeled "Submit" in the screenshot might now say "Save and Continue." A field that lived on screen two might have moved to screen three in the last release. The text in the document still references the old label, so now I'm not just swapping out screenshots. I'm tracking down every place in the content where that UI label appears and updating those too.

And then, mid-review, a Slack ping arrives: *"Hey, just so you know, that feature no longer exists. We changed it to XYZ."*

So now I'm not just updating a screenshot. I'm going back through the entire document to find every place this feature was mentioned, every step that referenced it, every heading built around it, and reworking all of it to reflect the update.

Then, after the PII check and the currency check: do we even need this many screenshots? There's a threshold where a doc stops being helpful and starts being a scroll-through experience with captions. Knowing where that line is comes from exposure to real readers, and that judgment is mine to make.

---

## The work that lives between the steps

There's the translation work: taking what stakeholders know deeply, what they want to say, and what users actually need, and finding the sentence that serves all three without lying to any of them.

And there's the governance work: making sure this new doc doesn't contradict the three existing docs about the same topic, that the terminology is consistent, and that the screenshots don't show a UI that was deprecated in Q2.

None of this appears in the final document. Which means none of it is legible to the people saying "it shouldn't take that long."

---

A tool can produce text. A technical writer produces documentation.

And documentation takes exactly as long as it takes.
