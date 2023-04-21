# Semantic data model

## URI design

The base url is <http://graph.data-for.good.bg/resource/> 

### Chitalishte main object

### The explanatory form in SKOS

ids

```
grep "form" ../data/info_cards/3706.json 


"form[address][main]",
"form[bulstat]",
"form[phone]",
"form[fax]",
"form[email]",
"form[webpage]",
"form[director]",
"form[secretary]",
"form[teritory][person]",
"form[teritory][users]",
"form[filial][1]",
"form[filial][2]",
"form[regusers]",
"form[regmolba]",
"form[regnew]",
"form[regrej]",
"form[main][biblioid]",
"form[main][treasures]",
"form[main][treasure][regnum]",
"form[main][treasure][nacnum]",
"form[main][activities][clubs]",
"form[main][activities][lang]",
"form[main][activities][kraj]",
"form[main][activities][museum]",
"form[main][activities][clubsnum]",
"form[main][activities][langnum]",
"form[main][activities][krajnum]",
"form[main][activities][museumnum]",
"form[main][ltvorch][folk]",
"form[main][ltvorch][theatre]",
"form[main][ltvorch][dance]",
"form[main][ltvorch][balley]",
"form[main][ltvorch][vocal]",
"form[main][ltvorch][other]",
"form[main][ltvorch][folknum]",
"form[main][ltvorch][theatrenum]",
"form[main][ltvorch][dancenum]",
"form[main][ltvorch][balleynum]",
"form[main][ltvorch][vocalnum]",
"form[main][ltvorch][othernum]",
"form[main][events]",
"form[main][eventsnum]",
"form[main][newactivities][txt]",
"form[main][newactivities][mainsum]",
"form[main][newactivities][partnersum]",
"form[main][injury]",
"form[main][injurysum]",
"form[main][other]",
"form[main][othersum]",
"form[org][meetings]",
"form[org][prereg]",
"form[org][matbase]",
"form[org][subspeople]",
"form[org][personal][all]",
"form[org][personal][hi]",
"form[org][personal][spec]",
"form[org][personal][adm]",
"form[org][personal][other]",
"form[org][obuchenie]",
"form[org][obuchenienum]",
"form[org][sanctions]",
"form[remark]",
```

### An individual observation

Using W3C Cube ontology 
ex: https://gitlab.ontotext.com/ontotext/company-graph/-/blob/master/data/WD/wd-mapping.rq#L86

### Bulgarian administrative entities 

## Building the visualisations

`docker-compose -up` will create a diagram from each `ttl` file in this folder 

