# http://amunategui.github.io/pubmed-query/

library(RISmed)
search_topic <- 'copd' # Chronic Obstructive Pulmonary Disease

search_query <- EUtilsSummary(search_topic, retmax=100, mindate=2012, maxdate=2012)

summary(search_query)
QueryId(search_query)

records<- EUtilsGet(search_query)
class(records)
