# 0.3 provincial_gdp_yearly_snapshot

**Purpose**: Create a table with the gdp per province.

**Grain unique column set**: [`year_begin_date`, `geo`, `industry`]

**Semi additive facts**: [ `gdp` ]

### Caveats:
1. This is excluding unclassified businesses
2. Some industries are missing `avg_weekly_earnings` for some geos/industry pairs, there are also missing values when industry = `'All industries [T001]'` (see below)
```
       year_begin_date                        geo               industry  gdp
4054        1997-01-01                    Nunavut  All industries [T001]  NaN
8440        1998-01-01                    Nunavut  All industries [T001]  NaN
96391       2019-01-01  Newfoundland and Labrador  All industries [T001]  NaN
96737       2019-01-01       Prince Edward Island  All industries [T001]  NaN
97073       2019-01-01                Nova Scotia  All industries [T001]  NaN
97409       2019-01-01              New Brunswick  All industries [T001]  NaN
97746       2019-01-01                     Quebec  All industries [T001]  NaN
98084       2019-01-01                    Ontario  All industries [T001]  NaN
98422       2019-01-01                   Manitoba  All industries [T001]  NaN
98759       2019-01-01               Saskatchewan  All industries [T001]  NaN
99090       2019-01-01                    Alberta  All industries [T001]  NaN
99425       2019-01-01           British Columbia  All industries [T001]  NaN
99761       2019-01-01                      Yukon  All industries [T001]  NaN
100099      2019-01-01      Northwest Territories  All industries [T001]  NaN
100437      2019-01-01                    Nunavut  All industries [T001]  NaN
100774      2020-01-01  Newfoundland and Labrador  All industries [T001]  NaN
101117      2020-01-01       Prince Edward Island  All industries [T001]  NaN
101455      2020-01-01                Nova Scotia  All industries [T001]  NaN
101793      2020-01-01              New Brunswick  All industries [T001]  NaN
102131      2020-01-01                     Quebec  All industries [T001]  NaN
102468      2020-01-01                    Ontario  All industries [T001]  NaN
102802      2020-01-01                   Manitoba  All industries [T001]  NaN
103140      2020-01-01               Saskatchewan  All industries [T001]  NaN
103473      2020-01-01                    Alberta  All industries [T001]  NaN
103810      2020-01-01           British Columbia  All industries [T001]  NaN
104146      2020-01-01                      Yukon  All industries [T001]  NaN
104474      2020-01-01      Northwest Territories  All industries [T001]  NaN
104815      2020-01-01                    Nunavut  All industries [T001]  NaN
```

### Schema
1. `year_begin_date`: 1st day of year being analyzed
2. `geo`: Province
3. `industry`: North American Industry Classification System (NAICS), to get all industries filter to `All industries [T001]`
4. `gdp`: Gross Domestic Product