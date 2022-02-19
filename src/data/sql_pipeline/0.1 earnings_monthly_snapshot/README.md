# 0.1 earnings_monthly_snapshot

**Purpose**: Create a table with the avg_weekly_earnings per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`]

**Non additive facts**: [ `avg_weekly_earnings` ]

### Caveats:
1. This is excluding unclassified businesses

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province or Canada if it's at the Canada wide level
3. `avg_weekly_earnings`: Average weekly earnings including overtime