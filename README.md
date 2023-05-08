# Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies

Also known as the S.U.S.A.M.O.G.U.S.

Wouldn't it be nice to get the exact chance of a skill winning against a set power?  
With that information, the clashing ability of different sinners could be compared in a quantifiable way.  
This tool approximates every sinner's ability to win a clash against a single coin skill of a set power, and the expected damage from each sinner skill.
This information can then be used to generate a set of tier lists.

---

## Tier Lists

[Tier lists based solely on data can be found here.](tier_lists/)

[A detailed writeup can be found here.](https://null-machine.github.io/limbus-company-roll-analyzer/)

---

## Reading Sinner Charts

[Clash charts can be found here.](charts/)

- Each chart provides an overview of a sinner's clashing ability.
- The Y-axis represents the chance of winning the clash.
- The X-axis represents the power required to win the clash.
- The coloured lines represent win chances at varying sanity levels.
	- In other words, cyan, grey and magenta lines are associated a chance of 0.95, 0.5 and 0.05 of getting heads respectively.
- For example, if a skill has the cyan line at x=12 and y=0.75, it has a 75% chance of beating a 12 at maximum sanity.

![G Corp Gregor's Chart](charts/gregor_g_corp.png)

### Aggregate & Raw Damage

- A subchart's aggregate is the integral of the clash lines, which roughly approximates the power that skill can comfortably beat. The first value is for the max line, and the second is for the min line.
- A subchart's raw is the sum of all coins on a max roll. The first value is for the max roll, and the second is for the min roll. Offense level is indicated on the side.
- The main chart's aggregate is a weighted average of all skill aggregates. It compares average clash power between sinners.
- The main chart's raw is a weighted average of all skill raws. It approximates the average damage a sinner will output. Please be aware that this is arguably the most misleading statistic, since it ignores effects and statuses. Furthermore, players can manipulate tempo to ensure hard-hitting skills will be present during enemy staggers and use weaker skills to manipulate thresholds, so the raws of individual skills are more worthy of analysis.
- The weighting used for averages assumes three s1, two s2 and one s3 per pool.
	- Since the game uses a "refill bag by bag" system instead of a "used skills requeue into the pool" system, weak skills cannot be removed from the pool just by keeping them in a bottom slot (but this can still be used to greed for tempo).
	- However, ego and defense usage consumes slots, so players that manipulate draw will be able to reduce the effective pool size regardless.

### Assumptions & Notes

- Additional prime or weak charts will be generated for sinners with passives or conditionals, with the additional charts representing an abnormal state.
	- For example, each Faust identity has an additional prime chart to represent her kit while Representation Emitter's passive is active.
	- Determining a sinner's default state is is somewhat arbitrary, so sinner.yaml files can be viewed to see the chosen numbers.
- Due to technical limitations, Ishmael's prime charts treat Snagharpoon's passive as if it can contribute to damage. Please refer to regular Ishmael charts for more accurate representations of her raw damage values. Additionally, Kurokumo Hong Lu's prime chart should be used for damage, and his regular chart should be used for clashes. A similar bug is present for Sevens Outis.
- Enemy offense level is assumed to be 35.
	- Technically, this could be anything for the purposes of comparing aggregates, since it affects everyone in a constant way.
- Due to how it takes a difference of 5 or more offense level to have it influence clash power, aggregate represents a discontinuous behaviour. A sinner with marginally more aggregate than another will only see better performance given specific conditions.

---

## Other Approaches

A common alternative approach for approximating clashing ability is to use other sinner skills as a point of reference and pit everyone against each other to see who wins the most. While this works for providing a realistic PvP tier list, it operates under the assumption that enemies will have similar rolls to sinners.

This tool is engineered to be encounter agnostic. It considers clashes and damage totals at all relevant power levels, not just those of other sinners or existing content.

---

Made by LOWERCASE#0357.
