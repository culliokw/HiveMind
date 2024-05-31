#! /bin/sh

printf "What mode would you like?\n"
printf "Mode 1: From\nMode 2: Replying To\nMode 3: Date\nMode 4: Subject\n"
printf "Your Choice: "
read mode
if [ "$mode" == 1 ]; then key_substr="From:" && file_substr="_from"; fi
if [ "$mode" == 2 ]; then key_substr="In-Reply-To" && file_substr="_replies"; fi
if [ "$mode" == 3 ]; then key_substr="Date:" && file_substr="_date"; fi
if [ "$mode" == 4 ]; then key_substr="Subject: \[Eeglablist\]" && file_substr="_subject"; fi

for i in $(ls -1 | grep -P '\d{4}.txt')

do
	#echo "$key_substr"
	declare name=$(echo "$i" | awk -F. '{print $1}' | sed "s/$/$file_substr/")
	#echo "${year}.txt"
	awk 'split($0,a," ")' $i | awk "/^$key_substr/" > "${name}.txt"
done
