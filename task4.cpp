/*A palindromic number reads the same both ways. The largest palindrome made from the product of two digit numbers is 9009 = 91*99.
Find the largest palindrome made from the product of two 3-digit numbers.*/

# include <stdio.h>

int main(){
	int product,reversed=0,original,remainder,palin;
	
	for(int i=100;i<=999;i++){
		for(int j=100;j<999;j++){
			product = i*j;
			original = product;
			
			while(product!=0){ 	
			remainder = product%10;
		    reversed = reversed*10+remainder;
		    product/=10;
			}
			if(original == reversed && original>palin){
			palin = original;
			}
			reversed = 0;
		}
	}
	
	printf("The largest palindrome made from the product of two 3-digit numbers is: %d", palin);
	return 0;
}