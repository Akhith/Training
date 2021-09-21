#! /bin/bash
echo Enter a password :
read pass
length=${#pass}
if [[ $length -lt 8 ]]
then
        echo weak password length must be atleast 8
else
        if [ -z `echo $pass | grep [0-9]` ]
        then
       	     echo weak password must weak password must include numbers
        else 
		if [ -z `echo $pass | grep [a-z]` ]
		then
		       echo weak password must include lower case
	        else
			if [ -z `echo $pass | grep [A-Z]` ]
               		then
                       		echo weak password must include upper case
                	else

				echo strong password
	
			fi
		fi		
	fi
fi
