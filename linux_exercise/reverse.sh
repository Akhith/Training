#! /bin/bash 
echo Enter a number : 
read num
n=$num
rev=0
while [ $num -gt 0 ] 
do
	d=$(( $num % 10 ))
	rev=$(( $d + $rev * 10 ))
	num=$(( $num / 10 ))	
done
echo Reverse of $n is $rev 
