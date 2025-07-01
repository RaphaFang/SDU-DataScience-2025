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
# ! 1. modus ponens (MP)
# (p→q) ∧ p ⇒ q
# p -> q
# p
# QED, q
from sympy import symbols, Implies, And, simplify_logic, Not, satisfiable

p, q = symbols('p q')
rule = Implies(And(Implies(p, q), p), q)     
print(simplify_logic(rule))                   # → True

# ---------------------------------------------------------------
# ! 2. Modus Tollens (MT)
# (p→q) ∧ ~q ⇒ ~p
# p -> q
# ~q
# QED, ~p

# practice
# 1. (p→q)→r 
# 2.  ¬r
# ¬(p→q)  -> T

# 1. (p→q)→(r→s)
# 2. ¬(r→s)
# ¬(p→q)  -> T
p,q,r,s = symbols('p q r s')
p1 = Implies(Implies(p,q),Implies(r,s))
p2 = Not(Implies(p,q))
c = Not(Implies(p,q))    # 如果這邊不加上 Not(),  會得到 q | ~p

expr = Implies(And(p1,p2), c)
print(simplify_logic(expr))
# mt_rule = Implies(, Not(Implies(p,q)))

# ---------------------------------------------------------------
# ! 3. Hypothetical Syllogism (HS) — 假言三段論
# (p→q)∧(q→r)⟹p→r

p, q, r = symbols('p q r')
hs_rule = Implies(And(Implies(p, q), Implies(q, r)), Implies(p, r))
print(simplify_logic(hs_rule))


# practice（這兩個推論思考都錯，可以練習檢查為什麼錯）
# 3. 
# 1. p→(q→r) 2. q→s
# p→(r→s) (結論是推不出來)
# 這可以拆成 p>q, q>r，依HS（HS有確保可以拆開嗎？還是是要其他規則）
# 接著我可以推論 p>q, q→ s 得到 p>s，依HS
# 接著我想要推論的p→(r→s)，可以化約成p>s 依HS
    # ! 可以這樣反證明（counter-example）
    # 1. 這邊都是要證明Tautology，所以我只要找到一個前提都為真，但是結論假，就算找到反例（？）
    # 2. 那麼我就要假設第三題結論為假，也就是p→(r→s) 為F，這時候可以推論p為T，而r>s為F
    # 3. 接著r>s為F，則我可以推論r T, s F
    # 4. 帶入s 到第二前題，得到q為F （基於MT）
    # 5. 同時，p→(q→r) 這也可以滿足 為真 T >(F>T) >> T
    # 6. 得出存在一個前提都為真，但是結論為假的情況
p,q,r,s = symbols('p q r s')
p1 = Implies(p, Implies(q, r))  # p → (q → r)
p2 = Implies(q, s)              # q → s
c = Implies(p, Implies(r, s))  # p → (r → s)

model = satisfiable(And(p1, p2, Not(c)))
print('counter-example :', model)  # {r: True, p: True, q: False, s: False}

# 5. 
# 1. p→q 2. (q∧r)→s	
# (p∧r)→s (結論是可以推出來)
# 關鍵在於第二前提可以拆解成 q>s, r>s ？
# 接著依據HS, p>q, q>s 可得到p>s，p>s,  r>s 二者可以合併（這邊是不是也要一個rule?），就能QED
# ! 正確的作法：正著作，會包含拆解，以及 or 的追加元件概念。或者是反正明

# ---------------------------------------------------------------
# ! 4. Disjunctive Syllogism (DS) — 選言三段論
# (p∨q)∧¬p⟹q　（對稱式也成立：(p∨q)∧¬q⟹p）
# A or B 為真, 其中一者為假，則另一個為真 

# ---------------------------------------------------------------
# ! 5. Constructive Dilemma (CD) — 建構兩難
# (p→q)∧(r→s)∧(p∨r)⟹q∨s
    # 與 Disjunctive Syllogism 相反：CD 是 從前因推出後果的「正向」二選一
# 要基於 MP ，p∨r 任何一個為T，這時候 q∨s 必然為真

# (p→q)→r, (s→t)→u, (p→q)∨(s→t)
# r∨u

# ---------------------------------------------------------------
# ! 6. Simplification (Simp) — 簡化
# p∧q⟹p （亦可推出 q）
# 兩者的連集為真，挑隨便一個都為真

# ---------------------------------------------------------------
# ! 7. Conjunction (Conj) — 合取
# p,q⟹p∧q
# 兩者都是真，兩者的連集為真

# ---------------------------------------------------------------
# ! 8. Addition (Add) — 加法
# p⟹q∨p
# 一者為真，加上 or 也為真