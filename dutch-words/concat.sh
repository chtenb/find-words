rm all.txt && cat *.txt | tr -dc [:graph:][:cntrl:] | tr '[A-Z]' '[a-z]' | sort -u  > all.txt
