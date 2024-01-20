cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep "[oznrica]" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,}" | wc -l