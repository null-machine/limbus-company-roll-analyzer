# Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies

Also known as the S.U.S.A.M.O.G.U.S.

Wouldn't it be nice to get the exact chance of a skill winning against a set power?  
With that information, the clashing ability of different sinners could be compared in a quantifiable way.  
This tool approximates every sinner's ability to win a clash against a single coin skill of a set power, and uses that to generate a few tier lists.

---

## Reading Sinner Charts

[Clash charts can be found here.](/charts/)

- Each chart provides an overview of a sinner's clashing ability.
- The three sub-charts evaluate the performance of each of the sinner's skills.
- The Y-axis represents the chance of winning the clash.
- The X-axis represents the power required to win the clash.
- The three coloured lines represent win chances at maximum, zero and minimum sanity.
	- In other words, cyan, yellow and magenta lines are associated a chance of 0.95, 0.5 and 0.05 of getting heads respectively.
- For example, if a skill has the cyan line at x=12 and y=0.75, it has a 75% of beating a 12 at maximum sanity.

![G Corp Gregor's Chart](/gregor_g_corp.png)

### Aggregate & Variance

- A subchart's aggregate is the integral of the cyan line, which roughly approximates the power that skill can comfortably beat at max sanity.
- A subchart's variance is the area between the cyan and magenta lines divided by the skill's aggregate, which roughly approximates the skill's ability to perform well at low sanity. Lower values are more desirable.
	- This number is kept as a saving grace to some sinners that were affected pretty harshly by the sanity changes, e.g. Blade Lineage Yi Sang.
- The main chart's aggregate is a weighted sum of all skill aggregates. It can be used to compare average power between sinners.
	- Since defense cycling is being patched, it should be a decent point of comparison.
- The main chart's variance is a weighted average of all skill variances. It approximates how well a sinner can tolerate low sanity or bad luck, with lower values being more desirable.

### Assumptions

- Additional prime or base charts will be generated for sinners with passives or conditionals that can be reasonably met, with the additional charts representing an abnormal state.
	- For example, each Faust identity has an additional prime chart to represent her clashing ability while Representation Emitter's passive is active.
- Determining a sinner's default state is is somewhat arbitrary, so sinner.yaml files can be viewed to see the chosen numbers.
- Enemy offense level is assumed to be 35.
	- Technically, this value could be anything for the purposes of comparison, since it affects everyone the same way.
	- But, 35 is the displayed level of refraction railway at the end screen, so it should result in numbers players are used to seeing.

---

## Tier Lists

Sinners and their skills can be sorted by their aggregates. [The tier lists can be found in the tier_lists folder](/tier_lists/).

Remember that this tool solely evaluates clashing ability. It provides no information about a sinner's utility or defensive options, so their position in the lists here may not necessarily be entirely reflective their overall power.

If game balance is to be trusted, those with poor clashing ability probably attempt to compensate for that with some other part of their kit (which is especially true for tanks).

---

## Other Approaches

A common alternative approach for approximating clashing ability is to use other sinner skills as a point of reference and pit everyone against each other to see who wins the most. While this works for providing a realistic PvP tier list, it operates under the assumption that enemies will have similar rolls to sinners.

This tool works by integrating win chance curves, which should probably be more encounter agnostic. It considers clashes at all relevant power levels, not just those of other sinners or existing content.

---

Made by LOWERCASE#0357.
