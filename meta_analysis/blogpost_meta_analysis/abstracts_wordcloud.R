library(easyPubMed)
library(magrittr)
library(rentrez) # https://cran.r-project.org/web/packages/rentrez/rentrez.pdf


my_query <- 'Damiano Fantini[AU] AND "2018"[PDAT]'
my_entrez_id <- get_pubmed_ids(my_query)
my_abstracts_txt <- fetch_pubmed_data(my_entrez_id, format = "abstract")

head(my_abstracts_txt)

my_abstracts_xml <- fetch_pubmed_data(pubmed_id_list = my_entrez_id)
my_titles <- custom_grep(my_abstracts_xml, "ArticleTitle", "char")


my_query <- "soroush zaghi[AU]"
my_entrez_id <- get_pubmed_ids(my_query)

my_abstracts_txt <- fetch_pubmed_data(my_entrez_id, format = "abstract")

## ---- rentrez ---
r_search <- entrez_search(db="pubmed", term="R Language")

records <- entrez_search(db="pubmed", term="(Michael Awad[AUTH]) AND (sleep)")
records <- entrez_search(db="pubmed", term="(Soroush Zaghi[AUTH])")

summaries <- entrez_summary(db='pubmed', id=records$ids)
titles <- extract_from_esummary(summaries, c('title'))
rquery.wordcloud(titles)

## from net------
search <- entrez_search(term="(Michael Awad[AUTH]) AND (sleep)", db="pubmed")
rec <- parse_pubmed_xml(entrez_fetch(db="pubmed", id=search$ids, rettype="xml"))
abstracts <- lapply(rec, function(x) x$abstract) %>% unlist
