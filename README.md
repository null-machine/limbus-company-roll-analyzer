# Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies

Also known as the S.U.S.A.M.O.G.U.S.

Wouldn't it be nice to get the exact chance of a skill winning against a set power?  
With that information, the clashing ability of different sinners could be compared in a quantifiable way.  
This tool approximates every sinner's ability to win a clash against a single coin skill of a set power, and the expected damage from each sinner skill, and uses that information to generate a set of tier lists.

---

## Reading Sinner Charts

[Clash charts can be found here.](charts/)

- Each chart provides an overview of a sinner's clashing ability.
- The three sub-charts evaluate the performance of each of the sinner's skills.
- The Y-axis represents the chance of winning the clash.
- The X-axis represents the power required to win the clash.
- The three coloured lines represent win chances at maximum, zero and minimum sanity.
	- In other words, cyan, yellow and magenta lines are associated a chance of 0.95, 0.5 and 0.05 of getting heads respectively.
- For example, if a skill has the cyan line at x=12 and y=0.75, it has a 75% chance of beating a 12 at maximum sanity.

![G Corp Gregor's Chart](charts/gregor_g_corp.png)

### Aggregate, Raw & Variance

- Aggregate, variance and raw damage are abbreviated as "agg", "var" and "raw" respectively.
- A subchart's aggregate is the integral of the cyan line, which roughly approximates the power that skill can comfortably beat at max sanity.
- A subchart's raw is the sum of all coins on a max roll without effects or statuses factored in. An approximal encounter agnostic offense damage calculation is used in place of the canon one to favour linear comparison. The exact formula can be viewed in skill.py. Besides that modification, please recognize how this statistic can be misleading (e.g. cloud cutter's extra coins are not factored in).
- A subchart's variance is the summation of a skill's max roll minus the summation of a skill's min roll, then divided by the former. This roughly approximates the skill's ability to perform well at low sanity. Lower values are more desirable.
	- This number is kept as a saving grace to some sinners that were affected pretty harshly by the sanity changes, e.g. Blade Lineage Yi Sang.
- The main chart's aggregate is a weighted average of all skill aggregates. It compares average power between sinners.
- The main chart's raw is a weighted average of all skill raws. It approximates the average damage a sinner will output. Please be aware that this is arguably the most misleading statistic, since it ignores effects and statuses. Furthermore, players can manipulate tempo to ensure hard-hitting skills will be present during enemy staggers and use weaker skills to manipulate thresholds, so the raws of individual skills are more worthy of analysis.
- The main chart's variance is a weighted average of all skill variances. It approximates how well a sinner can tolerate low sanity or bad luck, with lower values being more desirable.
- The weighting used for averages assumes two s1, two s2 and one s3 per pool. Two s1 instead of three s1 per pool is chosen for a few reasons:
	- Despite defense skill cycling being patched, each sinner still has two slots per dashboard, so a weak skill can still theoretically be removed from the pool by just keeping it in a bottom slot, hence the total of five.
	- Furthermore, ego usage consumes slots, so players that manipulate draw will be able to reduce the effective pool size even further.
	- Additionally, evade skills are particularly strong after the sanity patch, so sinners with evade can viably use that instead of s1 in tight situations.

### Assumptions & Notes

- Additional prime or weak charts will be generated for sinners with passives or conditionals, with the additional charts representing an abnormal state.
	- For example, each Faust identity has an additional prime chart to represent her kit while Representation Emitter's passive is active.
	- Determining a sinner's default state is is somewhat arbitrary, so sinner.yaml files can be viewed to see the chosen numbers.
	- Due to technical limitations, Ishmael's prime charts treat Snagharpoon's passive as if it can contribute to damage. Please refer to regular Ishmael charts for more accurate representations of her raw damage values. Additionally, Kurokumo Hong Lu's prime chart should be used for damage, and his regular chart should be used for clashes. A similar bug is present for Sevens Outis.
- Enemy offense level is assumed to be 35.
	- Technically, this could be anything for the purposes of comparing aggregates, since it affects everyone in a constant way.
	- But, 35 is the displayed level of Refraction Railway 1 on its end screen, so it should result in numbers players are used to seeing.

---

## Tier Lists

[Tier lists can be found here.](tier_lists/).

Remember that this tool solely evaluates the rolls of each sinner's three skills. It provides no information about a sinner's utility, defensive options or available ego, so their position in the lists may not accurately reflect their overall power.

If game balance is to be trusted, those with poor rolls may compensate for that with some other part of their kit (especially true for tanks). Likewise, the best rollers may have restraints, such as charge, ammo or health thresholds.

---

## Other Approaches

A common alternative approach for approximating clashing ability is to use other sinner skills as a point of reference and pit everyone against each other to see who wins the most. While this works for providing a realistic PvP tier list, it operates under the assumption that enemies will have similar rolls to sinners.

This tool is engineered to be encounter agnostic. It considers clashes and damage totals at all relevant power levels, not just those of other sinners or existing content.

---

Made by LOWERCASE#0357.
