/*
Algorithm: 
We XOR a and b and set a as its new value

For b we want to set it as (a AND b) << 1. 

We repeatively set a as the XOR of a and b

And repeatively set b as the AND + Shift Right by 1 of a bit

Until b == 0

*/

class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = (a ^ b);
            b = tmp;
        }
        return a;
    }
}
