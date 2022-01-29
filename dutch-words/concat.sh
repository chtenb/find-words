rm all.txt && cat *.txt | tr -dc [:graph:][:cntrl:] | sort -u  > all.txt
