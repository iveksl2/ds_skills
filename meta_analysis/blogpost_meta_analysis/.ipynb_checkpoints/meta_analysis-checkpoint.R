# https://ebmh.bmj.com/content/22/4/153
# 
#install.packages(c('meta', 'metasens'))

library(meta)
library(metasens)
library(dplyr)

setwd('~/Desktop/blogpost_meta_analysis/')
settings.meta( digits = 2 )


#Supplamental Material
# assuming file is containted in the working directory
joy = read.csv('ebmental-2019-November-22-4-153-inline-supplementary-material-1.txt') 

View(joy)

# To be used later for subgroup analysis of missing data
joy$miss = ifelse((joy$drop.h + joy$drop.p) == 0 , c("Without missing data"), c("With missing data")) 

m.publ = metabin(resp.h, resp.h + fail.h , resp.p, resp.p + fail.p, 
                 data = joy, 
                 studlab = paste0(author,"(", year, ")"), method.tau = "PM" )

forest(m.publ, 
       sortvar = year, 
       prediction = TRUE , 
       label.left = " Favours placebo", 
       label.right = " Favours haloperidol" ) 

m.publ.sub = update(m.publ, byvar = miss, print.byvar = FALSE )

# Small Study Bias
funnel(m.publ)

#Publication Bias
funnel(m.publ, contour.levels = c (0.9, 0.95, 0.99), col.contour = c ( "darkgray ", "gray", "lightgray" ))

# Further Packages: https://cran.r-project.org/web/views/MetaAnalysis.html
