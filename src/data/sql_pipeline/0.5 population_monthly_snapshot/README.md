# 0.5 population_monthly_snapshot

**Purpose**: Create a table with the population per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`, `age_group`, `sex`]

**Semi additive facts**: [ `population` ]

### Caveats:
1. This doesn't include population for under 15 years old

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `age_group`: Age group of the population, for all ages (that we have population estimates for) use `15 years and over`
4. `sex`: The sex of the population, for all sexes filter to `Both sexes`
4. `population`: Estimated population of the group