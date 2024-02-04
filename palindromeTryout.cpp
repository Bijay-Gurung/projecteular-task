//check the palindrome number.
#include <stdio.h>
int main(){
	int num,reversed,remainder,original;
	printf("Enter number: ");
	scanf("%d",&num);
	original = num;
	while(num!=0){
		remainder = num%10;
		reversed = reversed*10+remainder;
		num/=10;
	}
	
	if(original==reversed){
		printf("The given number is palindrome");
	}
	else{
		printf("The given number is not palindrome");
	}
	return 0;
}