# 0.2 emissions_yearly_snapshot

**Purpose**: Create a table with the avg_weekly_emissions per province and canada wide per sector.

**Grain unique column set**: [`year_begin_date`, `geo`, `sector`]

**Semi additive facts**: [ `yearly_kilotonnes` ]

### Schema
1. `year_begin_date`: 1st day of year being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `sector`: The sector of emissions, to get all sectors you could use either: `Total, industries and households` or `Total, industries`
4. `yearly_kilotonnes`: Yearly kilotonnes of emissions
