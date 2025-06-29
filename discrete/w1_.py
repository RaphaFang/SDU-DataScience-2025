from itertools import product

def truth_table(expr, vars=('p','q')):
    envs = list(product([0, 1], repeat=len(vars)))
    for i,j in envs:
        print(f"{i} {j} | {expr(i,j)}")
# ---------------------------------------------------------------
# 這是邏輯 p and q
# truth_table(lambda p,q: p and q)
# 0 0 | 0
# 0 1 | 1
# 1 0 | 1
# 1 1 | 1

# ---------------------------------------------------------------
# p or q
# truth_table(lambda p,q: p or q)
# 0 0 | 0
# 0 1 | 0
# 1 0 | 0
# 1 1 | 1

# ---------------------------------------------------------------
# ! 目標是找到 Tautology
# ---------------------------------------------------------------
# modus ponens (MP)
# p -> q (T)
# p(T)
# QED, q(T)
from sympy import symbols, Implies, And, simplify_logic

p, q = symbols('p q')
rule = Implies(And(Implies(p, q), p), q)      # (p→q) ∧ p ⇒ q
print(simplify_logic(rule))                   # → True


# ---------------------------------------------------------------
# ! Modus Tollens (MT)
# p -> q (T)
# q (F)
# QED, p (F)

# ---------------------------------------------------------------