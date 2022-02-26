# 0.1 earnings_monthly_snapshot

**Purpose**: Create a table with the avg_weekly_earnings per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`, `industry`]

**Non additive facts**: [ `avg_weekly_earnings` ]

### Caveats:
1. This is excluding unclassified businesses
2. Some industries are missing `avg_weekly_earnings` for some geos/industry pairs, but there are no missing values when industry = `'All industries [T001]'`

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `industry`: North American Industry Classification System (NAICS), to get all industries filter to `Industrial aggregate excluding unclassified businesses [11-91N]`
4. `avg_weekly_earnings`: Average weekly earnings including overtime