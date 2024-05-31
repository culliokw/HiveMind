#! /bin/sh

printf "Stripping Headers out from messages\n"

for i in $(ls -1 | grep -P '\d{4}.txt')

do
	#echo "$key_substr"
	declare name=$(echo "$i" | awk -F. '{print $1}' | sed "s/$/_headers/")
	#echo "$name"
	awk -v RS= -v ORS='\n\n' '/\nFrom: / && !/Original Message/ && !/eeglablist-bounces/' "$i" > "${name}.txt"
done
