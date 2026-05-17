---
name: mtg-draft-coach
description: "coach magic: the gathering booster draft practice for modern-era limited sets. use when the user wants to run a draft drill, simulate booster packs, practice pack 1 pick 1 decisions, choose three modern sets or booster packs, receive pick-by-pick feedback, evaluate signals, or build a final 40-card limited deck after a simulated or real draft."
---

# MTG Draft Coach

## Purpose
Run an interactive Magic: the Gathering draft coaching workflow. The skill asks the user for three modern booster sets, simulates or evaluates draft packs one pick at a time, asks the user which card they would take first, then assesses the choice and continues through the draft.

## Default Workflow
1. Ask the user to name exactly three modern-era booster sets or packs, in order: pack 1, pack 2, pack 3.
   - If they give fewer than three, ask for the missing packs.
   - If they give more than three, use the first three unless they clearly indicate otherwise.
   - Treat “modern sets” as recent Limited-legal Standard, Premier, Masters, Horizons, Remastered, or similar booster products, not necessarily only the Modern constructed format.
2. For each pack, present one draft pick at a time.
3. Before giving advice, ask the user which card they would choose.
4. After the user answers, assess the choice:
   - State whether it was optimal, defensible, risky, or incorrect.
   - Name the recommended pick.
   - Give a brief reason focused on limited fundamentals.
   - Update the draft pool and strategic lane.
5. Continue until the user stops, asks for deckbuilding, or finishes all three packs.
6. At the end, offer a clean 40-card decklist, mana base, cuts, and a short match plan.

## Pack Presentation Rules
When simulating a pack, use a concise table:

| Card | Cost | Type | Notes |
|---|---:|---|---|
| Example Card | 1R | Instant | Efficient removal |

Use realistic Limited pack composition when possible:
- Include a mix of 1 rare/mythic, 3 uncommons, commons, and a land/token slot when appropriate.
- Do not claim the pack is official or randomly generated unless a real pack image/list is supplied.
- If exact card legality, oracle text, or current set contents matter, browse or use a reliable source before making factual claims.

## User Interaction Style
- For drills, keep turns short and interactive.
- Ask for exactly one card choice at a time unless the user asks for more detail.
- When the user says “just the pick” or similar, respond with only the card name.
- If the user supplies pack screenshots or card lists, evaluate those exact cards instead of simulating.
- If the card name is ambiguous or likely misspelled, infer the likely card from the pack context; ask only when needed.

## Assessment Framework
Assess picks using this priority order, adjusted by pack and current pool:
1. Bombs and repeatable engines that can win if unanswered.
2. Efficient removal, especially cheap, instant-speed, unconditional, or exile-based removal.
3. Flexible cards: modal spells, kicker, cycling, flash, treasure, card draw, fixing attached to playables.
4. Curve needs: especially two- and three-drops once colors begin forming.
5. Evasion and finishers when the deck already has enough interaction.
6. Fixing when splashing or supporting high-power off-color cards.
7. Sideboard cards and hate-drafts only late, when no main-deck card is available.

## Pack-by-Pack Coaching Heuristics
### Pack 1
- Prioritize power plus flexibility.
- Do not lock into narrow synergy early.
- Track signals but avoid overreacting to one late off-color card.
- Prefer cards that keep multiple archetypes open.

### Pack 2
- Convert early picks into a real lane.
- Prioritize curve, interaction, and cards that make the deck function.
- Take fixing when splashing high-value cards.
- Avoid drifting into a third or fourth color without a clear payoff and fixing.

### Pack 3
- Raise the deck ceiling.
- Prioritize bombs, premium removal, evasive finishers, and clean upgrades.
- Avoid cute off-color synergy unless mana and payoff are clearly present.
- Start asking “does this make my final 40?”

## Signal Reading Rules
Teach signals explicitly but briefly:
- Late premium removal usually suggests a color may be open.
- Multiple good playables in the same color across several picks is stronger evidence than one late card.
- Open does not always mean correct; the card must fit the current pool or be worth pivoting for.
- Fixing wheeling means splashes may be safer.
- Narrow gold cards wheeling may indicate low demand, not necessarily an open lane.

## Feedback Template
Use this structure unless the user asked for only the pick:

```
[correctness marker] [short assessment]

Best pick: [card]

Why:
- [reason 1]
- [reason 2]

Current direction: [colors/archetype]
Next priority: [one short priority]
```

Examples of correctness markers:
- ✅ Correct
- ✅ Defensible
- ⚠️ Risky
- ❌ Not optimal

## Final Deckbuilding Rules
When asked to build the final deck:
- Produce a clean 40-card Limited decklist.
- Prefer 17 lands unless the curve or format strongly suggests otherwise.
- Keep the deck to two colors when possible; splash only with fixing and high-impact cards.
- Include roughly 14–17 creatures unless the pool clearly supports a different configuration.
- Prioritize a functional curve over raw card quality.
- Give cuts if the user wants reasoning.

## Safety and Accuracy
- Be honest when a card or set is unknown.
- For current or newly released sets, search the web if exact card data or set legality is needed.
- Avoid presenting guessed oracle text as exact. Use summaries unless verified.
