Anisha Patel
AnishaPatel77

cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep "a" | grep "[umocft]" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,}" 

gunzip -c dictionary.gz | grep "b" | grep "[atirnl]" | grep -v "[bcdefghjkmopqsuvwxyz]" | grep -E ".{4,}" 

gunzip -c dictionary.gz | grep "c" | grep "[amodin]" | grep -v "[bcefghjklmopqrstuvwxyz]" | grep -E ".{4,}" 

gunzip -c dictionary.gz | grep "z" | grep "[naoigr]" | grep -v "[bcdefghjklmpqstuvwxyz]" | grep -E ".{4,}" 