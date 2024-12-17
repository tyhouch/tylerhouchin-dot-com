---
title: "Entering the Inference Era"
date: 2024-10-06
author: "Tyler Houchin"
tags: ["AI", "Inference", "Scaling Laws", "GPT-4", "GPT-o1", "AI Infrastructure"]
---

In the world of AI, one of the most transformative insights has been the concept of **scaling laws**—the idea that increasing the amount of compute, data, and model size leads to predictable gains in model intelligence. This principle became evident as AI models like GPT-3 and GPT-4 evolved. For example, GPT-3, with an estimated training cost of $10-20 million, was a massive leap forward in natural language understanding. However, GPT-4, with a training cost of around $100 million, required nearly 40 times more energy and compute than GPT-3. In return, it exhibited significantly improved language comprehension, reasoning, and overall intelligence. This increase in raw compute was a direct factor in the model’s heightened capabilities, demonstrating how scaling laws play out in the realm of model pre-training.

But we are now seeing these scaling laws apply not just to pre-training but increasingly to **inference-time compute** as well. Advanced models like GPT-o1, which focus on reasoning and cognitive tasks, require substantial computational resources during every inference, not just during training. Unlike traditional models that execute pre-trained functions with relatively little compute, reasoning models iteratively improve their outputs by considering multiple steps and feedback loops. This process dramatically increases the computational demands during inference, making it a persistent, long-term cost factor.

In fact, I believe that, in the long term, **more compute will be spent on inference than on pre-training**. While pre-training is typically a one-time expense, inference occurs each time a model is used, meaning that models like GPT-o1, which are tasked with advanced reasoning, will incur substantial costs over their operational lifetime. This shift is reshaping the economics of AI infrastructure and pushing companies to rethink their spending priorities.

This leads to critical questions about **trade-offs**. As inference costs rise, is it more economical to continue scaling up inference infrastructure, or should we invest upfront in optimizing models for efficiency at inference? For example, should enterprises spend more to distill or fine-tune smaller, specialized models that, while expensive to post-train, would be more cost-effective during inference? These trade-offs will be increasingly relevant as reasoning models become central to AI applications.

Ultimately, the next phase of AI spending will revolve around optimizing inference costs. Companies and investors who focus on the infrastructure for these compute-heavy tasks—whether through hardware innovations, specialized cloud solutions, or efficient model architectures—will be at the forefront of AI’s future.