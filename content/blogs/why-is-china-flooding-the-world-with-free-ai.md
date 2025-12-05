+++
title = 'Why is China Flooding the World with Free AI?'
date = 2025-12-01T09:00:00-05:00
tags = ["AI", "China", "Open Source", "Geopolitics"]
draft = false
+++


Open Twitter on any given day and you're bound to see some new LLM release. However, it seems for every update to GPT/Claude/Gemini, we get 10 updates (or net new releases) from Chinese labs. This began exciting - progress is progress. But it has started to feel eerie. Why is China doing this? Almost all of the improvements made in open source LLMs have been at the hands of the Chinese. 

On the news and you'll see countless discussions about "The AI Race" that we are participating in with China. There is much less discussion about the different strategies that the US and China are taking to win this race. When a US lab releases a new model, they offer it (1) through their 'chatbot' product and (2) via their API for others to build with. Compare this to a Chinese lab: they release the model directly on Huggingface, where end users download the entire model and run it themselves. 

Giving away the model weights seems altruistic, but it cannot be. This *is* China we're talking about... so the question remains: Why is China giving away their LLMs while US holds theirs behind lock and key?

## The Open Source Flood

Over the past year, Chinese companies have released a flood of open source AI models. DeepSeek, Qwen, Kimi, GLM, MiniMax - new ones every few weeks, all under permissive licenses, weights available for anyone to download.

And these aren't second-tier models. As of November 2025, the leaderboard has Kimi K2 Instruct as the leading open source model. It's competitive with leading US closed models (GPT-5, Gemini 3, Claude 4.5 Opus) and significantly better than any US open source alternative.

![LLM Intelligence Index Leaderboard](/images/blogs/china-free-ai/llm_leaderboard_chart.png)

Looking at the chart, 10 of the top 12 open source models are Chinese. The only US entries are OpenAI's gpt-oss models.

Before 2025, open source AI moved slowly. Then 2025 hit: DeepSeek R1 in January, Qwen 3 in March, MiniMax M1 in summer, Kimi K2 and GLM-4.5 in July, then ByteDance models, more Qwen releases, even Meituan (China's DoorDash) releasing a trillion-parameter model.

These companies are spending millions on training and giving the results away. That seems insane - unless you realize they were never going to make money on models anyway.


## Why China Can't Charge

The US strategy is straightforward: train expensive models, monetize through APIs and subscriptions. OpenAI, Anthropic, and Google can do this because they have paying customers. Enterprises will pay for GPT-5 API access. Consumers will pay $20/month for ChatGPT. The model is the product.

Chinese companies don't have this option. They're boxed out on two fronts.

### *Internationally: Blocked Out*

US companies have access to the market that matters most - Western enterprises with AI budgets. No Fortune 500 CISO is going to approve production data flowing through a Chinese AI service, but they'll happily sign an OpenAI contract.

OpenAI, Anthropic, and Google all blocked access from China in 2022. The US companies chose to cut off access. That means Chinese AI companies have zero path to selling API access to Western enterprises.

### *Domestically: Race to the Bottom*

And domestically, the economics collapsed immediately. When DeepSeek open-sourced R1, Baidu announced they'd open-source Ernie. Then Alibaba, Tencent, ByteDance - everyone followed within weeks. If your competitor releases a frontier model for free, you can't charge for yours.

So Chinese AI companies found themselves boxed out internationally and commoditized domestically. The API business model that funds OpenAI and Anthropic was dead on arrival.

### *Commoditization as Strategy*

Here's where it gets interesting. Brett Adcock, CEO of Figure AI, said it directly when ending their OpenAI partnership in February 2025: "LLMs are getting smarter yet more commoditized. For us, LLMs have quickly become the smallest piece of the puzzle."

If models become commoditized, the money flows elsewhere. To the bottom of the stack: infrastructure to run the models. To the top of the stack: applications and devices that use them. And to the middle: the ecosystem of developers building on top.

China looked at this landscape and made a bet: we can't win the model monetization game, so let's accelerate commoditization and win everything else.

## Why China Doesn't Need to Charge

As we assume with Chinese companies, state funding reshapes the economics. DeepSeek's parent company got designated a "national high-tech enterprise" in 2023 which provided them tax breaks, subsidies, and state-backed capital. The founder met with Premier Li Qiang (#2 to Xi) in early 2024. After R1 launched, Bank of China announced a $137 billion AI infrastructure fund.

When the government is funding your compute, ROI isn't measured at the company level. It's measured nationally.

## The Real Play: Hardware

This is where the strategy crystallizes. If you can't make money on models, what do you do with them?

**You use them to sell hardware.**

### *Chips*

China is still under US chip export controls and can't (easily) get the best Nvidia GPUs. So Chinese companies optimized their models to run on Huawei Ascend chips. DeepSeek V3.2 launched with first-day support for Huawei's CANN software stack.

If DeepSeek and Qwen become the global default and they're optimized to run on Chinese chips, demand flows toward Chinese semiconductors instead of Nvidia.

There's an irony here. US export controls were supposed to slow China's AI development by restricting access to advanced chips. Instead, they forced innovation - and created an incentive to build an alternative hardware ecosystem.

### *Robots and Devices*

The hardware strategy extends beyond just chips. Over half of publicly listed humanoid robotics companies are Chinese. DJI dominates drones. China manufactures most AI-enabled consumer devices globally.

Free models that run well on Chinese hardware create demand across the entire stack - from the chips running inference to the robots and devices using these models in the real world.

## Where This Leaves Us

China has proven adaptable. Western markets closed to them? Fine, can't monetize there anyway. Domestic competition destroyed pricing power? Fine, state funding removes the need for returns. Can't get Nvidia chips? Fine, optimize for Huawei and build that ecosystem instead.

The strategy crystallizes: free models create demand for Chinese hardware (chips, robots, consumer devices) and capture the developer ecosystem that builds on top. The models were never the product. They're the distribution mechanism.

The US is betting that closed, monetizable models will fund the research needed to stay ahead. China is betting that commoditized, free models will let them win on hardware and ecosystem even if they're not always at the frontier.

Both strategies are coherent. We're about to find out which one wins.

---

## Sources

**Leaderboard:** [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  
**Policy:** [China's 2017 AI Development Plan](https://digichina.stanford.edu/work/full-translation-chinas-new-generation-artificial-intelligence-development-plan-2017/), [European Guanxi on China's Open-Weight Strategy](https://www.europeanguanxi.com/post/from-policy-blueprint-to-industrial-practice-china-s-embrace-of-open-weight-ai), [MERICS on China's AI Model](https://merics.org/en/report/chinas-ai-development-model-era-technological-deglobalization)  
**Analysis:** [The Diplomat on Chinese Open Source Dominance](https://thediplomat.com/2025/07/china-now-dominates-open-source-ai-how-much-does-that-matter/), [GetLago on DeepSeek Economics](https://www.getlago.com/blog/deepseek-open-source)  
**Hardware:** [Tom's Hardware on DeepSeek + Chinese Chips](https://www.tomshardware.com/tech-industry/deepseek-new-model-supports-huawei-cann), [MERICS on Hardware Self-Reliance](https://merics.org/en/report/chinas-drive-toward-self-reliance-artificial-intelligence-chips-large-language-models), [Hazy Research on Gross Domestic Intelligence](https://hazyresearch.stanford.edu/blog/2025-11-28-gdi)  
**Funding:** [Yahoo on Zhipu AI State Backing](https://finance.yahoo.com/news/front-line-chinas-ai-ambitions-134830733.html)