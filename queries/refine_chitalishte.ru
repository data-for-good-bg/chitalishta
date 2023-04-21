base <http://graph.data-for.good.bg/resource/>
prefix wd: <http://www.wikidata.org/entity/>
prefix s: <http://schema.org/>
CONSTRUCT {
  ?id a s:Organization ;
    s:name ?name ;
    s:location ?place ;
    s:address ?address ;
    s:vatID ?eic ;
    s:email ?email ;
    s:telephone ?tel ;
    s:url ?url ;
.
} WHERE {
  BIND(URI(CONCAT("chitalishte/",?c_id)) as ?id)
  BIND(?c_name as ?name)
  BIND(URI(CONCAT(str(wd:),?c_wd_place)) as ?wd_place)
  BIND(?c_address as ?address)
  BIND(?c_eic as ?eic)
  BIND(?c_email as ?email)
  BIND(?c_tel as ?tel)
  BIND(URI(?c_url) as ?url)
}