---
title: "Entering the Inference Era"
date: 2024-10-06
author: "Tyler Houchin"
tags: ["AI", "Inference", "Scaling Laws", "GPT-4", "o1", "AI Infrastructure"]
---

Scaling laws are one of the most important ideas behind LLMs: increasing compute, data, and model size produces predictable gains in intelligence. The jump from GPT-3 to GPT-4 made this concrete. GPT-3, with an estimated training cost of 10 to 20 million dollars, was already a massive leap in natural language understanding. GPT-4, at roughly 100 million dollars, demanded nearly 40 times more energy and compute, and in return delivered significantly sharper comprehension, reasoning, and overall intelligence. That extra raw compute was a direct driver of its capabilities, a textbook example of scaling laws playing out in pre-training.

But these scaling laws are no longer confined to pre-training. They increasingly apply to inference-time compute as well. Reasoning-focused models like o1 burn substantial compute on every single query, not just during training. Where traditional models run their pre-trained weights with relatively little overhead, reasoning models work through multiple steps and feedback loops to refine each answer. That iterative process drives up the cost of every inference, turning compute into a persistent, ongoing expense rather than a one-time one.

In fact, I believe that over the long term more compute will be spent on inference than on pre-training. Pre-training is a one-time cost; inference is paid every time the model is used. For reasoning-heavy models like o1, those per-query costs accumulate across the entire operational lifetime and eventually dwarf the upfront training bill. That shift is reshaping the economics of AI infrastructure and forcing companies to rethink where they spend.

This raises hard questions about trade-offs. As inference costs climb, is it better to keep scaling up inference infrastructure, or to invest upfront in making models cheaper to run? Should enterprises pay to distill or fine-tune smaller, specialized models that are expensive to post-train but far cheaper per query? These choices only get more consequential as reasoning models move to the center of real applications.

Ultimately, the next phase of AI spending will be defined by the race to optimize inference. The companies and investors who build the infrastructure for these compute-heavy workloads, whether through better hardware, specialized cloud solutions, or more efficient architectures, will be the ones shaping AI’s future.