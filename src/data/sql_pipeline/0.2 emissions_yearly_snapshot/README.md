# 0.2 emissions_yearly_snapshot

**Purpose**: Create a table with the avg_weekly_earnings per province and canada wide.

**Grain unique column set**: [`year_begin_date`, `geo`, `sector`]

**Semi additive facts**: [ `yearly_kilotonnes` ]

### Caveats:
1. Some sectors are missing `yearly_kilotonnes` for some geo/sector pairs, but there are no missing values when sector = `'Total, industries and households'`
2. There are also some missing geo/sector/date combos missing: `not all possible combos (20174) exist, only 19754`, but not when you isolate to sector = `'Total, industries and households'`

### Schema
1. `year_begin_date`: 1st day of year being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `sector`: The sector of emissions, to get all sectors you could use either: `Total, industries and households` or `Total, industries`
4. `yearly_kilotonnes`: Yearly kilotonnes of emissions