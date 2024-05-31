#! /bin/sh

printf "Stripping Names out of From Section\n"

for i in $(ls -1 | grep -P '\2004.txt')

do
	#echo "$key_substr"
	declare name=$(echo "$i" | awk -F. '{print $1}' | sed "s/$/_overall_names/")
	#echo "$name"
	awk -F'[()]' '{ print $2 }' $i | printf
done
