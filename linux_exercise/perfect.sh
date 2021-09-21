#! /bin/bash 
echo Enter a number : 
read num
n=$num
sum=0
i=1
while [ $i -lt $num ]
do
	if [ $(( num % $i )) == 0 ];then
		sum=$(( $sum + $i ))
	fi
	i=$(($i + 1))
done
if [ $sum = $n ];then
	echo $n is perfect Number
else
	echo $n is not perfect Number
fi

