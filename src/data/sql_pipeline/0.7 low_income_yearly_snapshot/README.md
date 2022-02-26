# 0.5 low_income_yearly_snapshot

**Purpose**: Create a table with the low_income rate per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`, `demographic`]

**Non additive facts**: [ `low_income_rate` ]

### Caveats:
1. Some `month_begin_date/geo/demographic` pairs are missing `low_income_rate`, but there are no missing values when `demographic == 'All persons'`

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `demographic`: Demographic of the population, for demographics use `All persons`
4. `low_income_rate`: The % of the demographic in the low income bracket after taxes.