
def P(x):
    return x**3 + 3*x**2 + 3*x #1 3 3

def t(x):
    return x

g = 2
def E(x):
    return g**x # g = 8

# #
# • Verifier
# – samples a random value s, i.e., secret
# – calculates encryptions of s for all powers i in 0, 1, ..., d, i.e.: E(s**i) = (g**s)**i
# – evaluates unencrypted target polynomial with s: t(s)
# – encrypted powers of s are provided to the prover: E(s**1) = (g**s)**1 E(s*2) = (g**s)**2 .. E(s**d) = (g**s)**d
def Verfier(s):
    Es0 = E(s**0)
    Es1 = E(s**1)
    Es2 = E(s**2)
    Es3 = E(s**3)
    ts = t(s)
    print(f"ts,Es1,Es2,Es3 =  {[ts, Es0,Es1, Es2, Es3]}")
    return [ts,Es0,Es1,Es2,Es3]


# • Prover
# – calculates polynomial h(x) = p(x)/t(x);
# - using encrypted powers s1 s2 s3 and coefficients c0, c1, . . . , cn evaluat E(p(s)) = g**p(s) = ((g**s)**d)Cd  * ...((g**s)**2)C2  *((g**s)**1)C1
# and d similarly E (h(s)) = g ** h(s)
# - the resulting g**p and g**h are provided to the verifi
sec_num = 2
Verfiergivednum = Verfier(sec_num)

def Prover(Verfiergivednum):
    c3 = 1
    c2 = 3
    c1 = 3
    c0 = 0
    def h(x):
        return x**2 +3*x + 3 # hc2 = 1 hc1 = -3
    ts,s0,s1,s2,s3 = Verfiergivednum
    hc0,hc1 ,hc2 = [3,3,1]
    #E(p(s)) =
    res_p = (s1**c1)  * (s2 ** c2) * (s3**c3)
    print(f"(s1**c1) = {(s1**c1)},(s2 ** c2)={(s2 ** c2)},(s3**c3) = {(s3**c3)}")
    print(f"res_p={res_p}")
    res_h = (s0**hc0)*(s1**hc1)* (s2 ** hc2)
    print(f"res_h = {s1 ** hc1 * s2 ** hc2}")
    print([res_p,res_h])
    return (res_p,res_h)

# • Verifier
# – The last step for the verifier is to checks that p = t(s) · h in encrypted space g**p == (g**h)**t(s)  == g**(t(s) * h)
g_p,g_h = Prover(Verfiergivednum)

def verifier_final(g_p,g_h,g,sec_num):
    print(f"g_p = {g_p}")
    print(f"g_h = {g_h}")
    t_s = t(sec_num)
    print(f"g_h**t_s = {g_h**t_s}")
    if ( g_p == g_h**t_s):
        return True
    else:
        return False
print_final = verifier_final(g_p,g_h,g,sec_num)
print(print_final)




