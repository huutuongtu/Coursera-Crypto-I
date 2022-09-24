import math 
 
def discreteLogarithm(a, b, m):
 
    n = int(math.sqrt (m) + 1) 
 
    # Calculate a ^ n
    an = 1 
    for i in range(n):
        an = (an * a) % m 
 
    value = [0] * m 
 
    # Store all values of a^(n*i) of LHS
    cur = an 
    for i in range(1, n + 1):
        if (value[ cur ] == 0):
            value[ cur ] = i 
        cur = (cur * an) % m 
     
    cur = b 
    for i in range(n + 1):
         
        # Calculate (a ^ j) * b and check
        # for collision
        if (value[cur] > 0):
            ans = value[cur] * n - i 
            if (ans < m):
                return ans 
        cur = (cur * a) % m 
 
    return -1 
 
# Driver code
a = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568 
b = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333 
m = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171 
print(discreteLogarithm(a, b, m)) 