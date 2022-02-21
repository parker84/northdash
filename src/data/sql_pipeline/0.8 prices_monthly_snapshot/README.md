# 0.5 low_income_yearly_snapshot

**Purpose**: Create a table with the consumer price index (CPI) per province and canada wide.

**Grain unique column set**: [`month_begin_date`, `geo`, `product_group`]

**Non additive facts**: [ `consumer_price_index` ]

### Caveats:


### Schema
1. `month_begin_date`: 1st day of month being analyzed
2. `geo`: Province/Country (Canada is the only country option though)
3. `product_group`: Products and product groups, for all products use `All-items`
4. `consumer_price_index`: The Consumer Price Index (CPI) is an indicator of changes in consumer prices experienced by Canadians. It is obtained by comparing, over time, the cost of a fixed basket of goods and services purchased by consumers. Since the basket contains goods and services of unchanging or equivalent quantity and quality, the index reflects only pure price change.