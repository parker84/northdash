# 0.5 unemployment_monthly_snapshot

**Purpose**: Create a table with the unemployment rate per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`, `age_group`, `sex`]

**Non additive facts**: [ `unemployment_rate` ]

### Caveats:
1. This doesn't include data for under 15 years old

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `age_group`: Age group of the population, for all ages (that we have population estimates for) use `15 years and over`
4. `sex`: The sex of the population, for all sexes filter to `Both sexes`
4. `unemployment_rate`: Estimated unemployment rate of the group