def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    l = (a*b) // gcd(a, b)
    return (l)

def package(a, b):
    print(f"the gcd: {gcd(a, b)}, the lcm: {lcm(a, b)}, the a*b: {a*b}")

package(15, 50)