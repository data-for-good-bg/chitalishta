PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
base <http://graph.data-for.good.bg/resource/>
prefix wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX p: <http://www.wikidata.org/prop/>
prefix s: <http://schema.org/>
insert {
    graph <graph/wd_places> {
        ?loc a s:City ;
             s:name ?loc_label ;
             s:containedInPlace ?obshtina ;
             .
        ?obshtina a s:AdministrativeArea ;
                  s:name ?obsht_label ;
                  s:containedInPlace ?oblast ;
                  .
        ?oblast a s:AdministrativeArea ;
                s:name ?obl_label ;
                s:containedInPlace wd:Q219 ;
                .
    }
} where {
    {
        select distinct ?loc where {
            [] s:location ?loc .
        }
    }
    service <https://query.wikidata.org/sparql> {
        ?loc rdfs:label ?loc_label ;
             wdt:P131 ?obshtina .
        ?obshtina rdfs:label ?obsht_label .
        filter not exists {
            ?loc p:P131 ?st .
            ?st ps:P131 ?obshtina ;
                pq:P582 []
        }
        ?obshtina wdt:P131 ?oblast .
        ?oblast rdfs:label ?obl_label .
        filter not exists {
            ?obshtina p:P131 ?st1 .
            ?st1 ps:P131 ?oblast ;
                 pq:P582 []
        }
        filter(lang(?loc_label)="bg")
        filter(lang(?obsht_label)="bg")
        filter(lang(?obl_label)="bg")
    }
}