# 0.3 gdp_yearly_snapshot

**Purpose**: Create a table with the gdp per province and canada wide.

**Grain unique column set**: [`year_begin_date`, `geo`, `industry`]

**Semi additive facts**: [ `gdp` ]

### Caveats:
1. This is excluding unclassified businesses

### Schema
1. `year_begin_date`: 1st day of year being analyzed
2. `geo`: Province
3. `industry`: North American Industry Classification System (NAICS), to get all industries filter to `All industries [T001]`
4. `gdp`: Gross Domestic Product