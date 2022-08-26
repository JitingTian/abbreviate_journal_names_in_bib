# library.bib is exported from the Mendeley software

# delete abstract, doi, keywords
sed -i '/abstract = {/d' library.bib
sed -i '/doi = {/d' library.bib
sed -i '/keywords = {/d' library.bib

# change generic, report, to article
sed -i 's/@generic/@article/g' library.bib
sed -i 's/@report/@article/g' library.bib
