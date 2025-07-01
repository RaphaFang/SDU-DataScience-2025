# 原式	             等值	             說明
# ¬∀x P(x)	        ∃x ¬P(x)	        否定全稱 → 存在反例
# ¬∃x P(x)	        ∀x ¬P(x)	        否定存在 → 全稱否定
# ∀x (P(x)∧Q(x))	∀x P(x) ∧ ∀x Q(x)	全稱分配 ∧
# ∃x (P(x)∨Q(x))	∃x P(x) ∨ ∃x Q(x)	存在分配 ∨


# 謂詞範例：Premium(u), Has2FA(u), Paid(o), Owner(u,o), Ship(o)

# ---------------------------------------------------------------
# ! A
# 1. 所有 Premium 使用者至少有一筆已付款訂單
    # ∀u ( Premium(u) → ∃o [Owner(u,o) ∧ Paid(o)] )

# 2. 某些訂單沒有任何擁有者
    # ∃o ∀u ¬Owner(u,o) <存在訂單 o，使得『對所有使用者 u，都不是 o 的 Owner』>
    #   ∃o ¬ ∀u (Owner(u,o)) <存在一筆訂單 o，且存在某個使用者不是它的 Owner>
    #   ¬∀u Owner(u,o) ≡ ∃u ¬Owner(u,o)， 想像所有人都是學生的反化，至少有一人不是學生

# 3. 若使用者綁了 2FA，則每筆他擁有的訂單都已付款
    # ∀u ( Has2FA(u) → ∀o ( Owner(u,o) → Paid(o) ) )

# 4. 對每筆訂單，都有一個 Premium 擁有者 且 該訂單已出貨
    # ∀o (∃u (Premium(u)∧Owner(u,o)) ∧ Ship(o))

# 5. 存在一個使用者，他擁有 所有未付款訂單
    # ∃u ∀o (¬Paid(o) -> Owner(u,o) )

# 6. 不是所有使用者都具備 2FA
    # ¬∀u Has2FA(u) 或者是 ∃u ¬Has2FA(u)

# 7. 至少有兩位不同使用者同時擁有同一筆訂單
    # ∃u₁ ∃u₂ ∃o ((Owner(u1,o) ∧ Owner(u2,o)) ∧ u1 ≠ u2)

# 8. 所有訂單都已出貨 或 所有未出貨訂單金額 < 100
    # ∀o (Ship(o))  ∨  ∀o (~Ship(o) ->  LowPrice(100))

# ---------------------------------------------------------------
# ! B 
# ¬∀o Paid(o)
    #  ∃o ~ Paid(o) 所有訂單都付款，的反化，存在訂單但沒有付款

# ∃u ∀o (Owner(u,o) → Ship(o)) 存在用戶，所有商品都出貨
    #  ∃u ∀o (~Owner(u,o) or Ship(o)) 存在一個用戶，不是他的東西，或者，已經出貨了

# ¬∃u (Premium(u) ∧ Has2FA(u)) 不存在用戶是P且2fa
    # ∀u ~ (Premium(u) ∧ Has2FA(u)) 所有用戶都不可能同時滿足兩個

# ∀u ∃o Owner(u,o) 所有用戶，至少有一筆訂單
    # ∃u ∀o Owner(u,o) 存在一用戶有所有的訂單都他的

# ---------------------------------------------------------------
# ! C
# 前提： ① 任何出貨的訂單都已付款  ② 某筆訂單未付款
# 結論：該訂單未出貨
    # 1. ∀o (Ship(o) -> Paid(o))
    # 2. ∃o ~Paid(o)
    # MT, 該訂單沒出貨

# 前提： ① 若使用者有 Premium，則必有 2FA ② 某位使用者沒有 2FA
# 結論：此使用者沒有 Premium
    # ∀u (Premium(u) -> 2FA(u))
    # ∃u ~2FA(u)
    # MT, 此使用者沒有 Premium

# ! 前提： ① 所有訂單都要麼出貨，要麼取消（不得同時） ② 目前存在未出貨且未取消的訂單
# 結論：前提相矛盾（證明不可滿足）
    # ∀o (  (Ship(o) ∨ Cancel(o)) ∧ ~(Ship(o) ∧ Cancel(o)) )  # ! 這才是完整的 
    # ∃o ~Ship(o) ∧ ~ Cancel(o)
    # ~(S ∧ C) 矛盾於 ~(S v C)