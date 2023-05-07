# Semantic data model

## URI design

The base url is <http://graph.data-for.good.bg/resource/> 

### Chitalishte main object

### The explanatory form in SKOS

same fields everywhere

```bash
egrep -ho "\"form\[.*?\"" ../data/info_cards/* | sort | uniq -c | less -S
```

### Observations in CUBE


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


# Tasks

- Parse individual jsons with observations and load them in table [HERE](https://docs.google.com/spreadsheets/d/1I4_AXQlygviE3HXBX_klZR64QEuie5Mo-gK17Lz8P78/edit#gid=1730432966)
- Write OR transformation and transform individual obseravations into RDF following the CUBE model
- Create a SKOS taxonomy in table [HERE](https://docs.google.com/spreadsheets/d/1I4_AXQlygviE3HXBX_klZR64QEuie5Mo-gK17Lz8P78/edit#gid=1653429745)
- Write OntoRefine SPARQL transformation  

- Write competency questions (queries in text form) [HERE](https://docs.google.com/spreadsheets/d/1I4_AXQlygviE3HXBX_klZR64QEuie5Mo-gK17Lz8P78/edit#gid=375110053)

- Transform federated query so that it loads ALL of the cities and associated data
- Write a sparql query for each competency quesiton


