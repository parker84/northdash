# 0.3 canada_gdp_yearly_snapshot

**Purpose**: Create a table with the gdp for Canada.

**Grain unique column set**: [`month_begin_date`, `industry`]

**Semi additive facts**: [ `gdp` ]

### Caveats:
1. This is excluding unclassified businesses

### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `industry`: North American Industry Classification System (NAICS), to get all industries filter to `All industries [T001]`
4. `gdp`: Gross Domestic Product