# key point
# 1. difference between ∀u ∃o / ∀u (P(u) → ∃o ...
# 2. Skolem


# ---------------------------------------------------------------
# A1	每位 premium 使用者 都有一筆訂單，其金額 < 100 元 且 已出貨。	用 ∀∃∧；含謂詞 AmountLt100(o) 與 Ship(o)。
    # ∀u ∃o (premium(u) -> (Owner(u,o) ∧ (AmountLt100(o) ∧ Ship(o)))) 
        # 對每一位使用者，至少可以挑出一筆訂單；如果那位使用者剛好是 premium，則 那 筆被挑出的訂單必須是他的、金額低於 100 元，而且已經出貨。
        # 放前面會過早篩選

    # ! ∀u ( Premium(u) → ∃o (Owner(u,o) ∧ (AmountLt100(o) ∧ Ship(o)))
        # 每一位 premium 使用者至少擁有一筆訂單，且那筆訂單金額低於 100 元並且已出貨。

# A2	有且只有一筆訂單同時滿足「未付款且未取消」。	用 ∃o [ … ∧ ∀o′ … ]; 請給出 唯一性 條件。
    # ∃o1 ∀o2 (o1!=o2 ->  ~Paid(o1) ∧ ~ Cancel(o1) ∧ (Paid(o2) ∨ Cancel(o2)))
        # 這說的是：若 o₂ 跟 o₁ 不同，就斷言 o₁ 未付款且 o₂ 已付款或已取消
    # ! ∃o1 [(~P(o1) ∧ ~ C(o1)) ∧ ∀o2((~P(o2) ∧ ~ C(o2)) -> (o2 = o1))]
        # 分別先說明，存在一個o1滿足條件，且，所有滿足同條件的o2，那麼他等同於o1  ->> 存在且排除第二筆

# A3	若使用者 沒有 2FA，則他 所有 訂單都不得標記為 urgent。	用 ¬Has2FA(u) 作前件，嵌套 ∀o。
    # ∀u (¬Has2FA(u) -> ∀o(¬urgent(u) -> Owner(u,o) ))
    #! ∀u (¬Has2FA(u) -> ∀o(Owner(u,o) -> ¬urgent(u)))

# A4	不存在一位使用者擁有 所有 premium 訂單。	用 ¬∃u ∀o (PremiumOrder(o) → Owner(u,o))。
    # ¬∃u ∀o (PremiumOrder(o) -> Owner(u,o))

# ---------------------------------------------------------------
# B1	¬∀o (Ship(o) ∨ Cancel(o))	化成 “∃o …” 並把否定推到原子前；解釋語意。
    # ∃o (~Ship(o) ∧ ~Cancel(o)) 存在訂單沒寄送且沒取消

# B2	∀u (Has2FA(u) → ∃o Owner(u,o))	用 Imp→∨、DM、Dist 轉成 前束 (Prenex) CNF。
    # ∀u (Has2FA(u) → ∃o Owner(u,o)) 這要怎麼轉換？
    # ! Skolemization 把 存在量詞帶入函數 f(x)
    #  ∀u (~Has2FA(u) v Owner(u,f(u)))

# B3	((p → q) ↔ r) → (¬q ∨ r)	用 10 條替換規則把箭號與↔全消，最後給 CNF。
    # [(p∧¬q)∨r]∨[(r∧p∧¬q)]∨(¬q∨r)

# ---------------------------------------------------------------
# C1 前提：若訂單已付款就會出貨；存在一筆已出貨訂單。
# 結論：存在一筆已付款訂單。
    # ∀o(Paid(o) -> Ship(o)), ∃o Ship(o)
    # 推不出結論，他只有單向的imply

# C2 前提：若模型失敗→告警；若告警→寫入 Slack；沒有寫入 Slack。
# 結論：模型沒有失敗。
    # HS 將第一前提變成，模型失敗 →寫入 Slack
    # MT後建為假，前建為真，得到模型沒失敗

# C3 前提：所有訂單要麼出貨要麼取消（不可皆假）；存在一筆未出貨訂單。
# 結論：該筆訂單已取消。
    # S v C , ~S
    # C 訂單已取消

# C4 前提：任何 premium 使用者的每筆訂單均已付款；存在未付款訂單。
# 結論：該訂單不屬於任何 premium 使用者。
    # MT 否定後建否定前建，該訂單不屬於任何 premium 使用者

# ---------------------------------------------------------------
# ! ∃x[P(x)∧∀y(P(y)→y=x)]  唯一性的模版
# E1	每位使用者若擁有訂單，就僅擁有一筆未付款訂單。	用 ∀ 與 唯一量詞：∃!o […]; 或顯式寫 (∃o … ∧ ∀o′ …)
    # ∀u ∃!o (Owner(u,o) -> ~Paid(o))
    # ∀u((∃o1 (Owner(u,o1) -> ~Paid(o1)) ∧ ∃o2 (Owner(u,o2) -> ~Paid(o2)) -> o1 = o2)

    # ∀u [ (∃o Owner(u,o)) → ∃!o (Owner(u,o) ∧ ¬Paid(o)) ]
    # ∀u[¬∃o Owner(u,o) ∨ (∃o₀(P) ∧ ∀o(P(o)→o=o₀))] where P ≡ Owner(u,o)∧¬Paid(o)

# E2	正好三筆訂單金額 > 1000。	用“存在三個兩兩不等”〔提示：∃o₁∃o₂∃o₃ (…) ∧ pairwise ≠ ∧ ∀ō ≠ o₁,o₂,o₃ → ¬High(ō)〕
    # ∃o₁∃o₂∃o₃ [(Sum(o1+o2+o3) > 1000) ∧ o1!=o2 ∧ o2!=o3 ∧ o3!=o1]
    # ! ∃o₁∃o₂∃o₃ [ pairwise ≠ ∧ High(o₁) ∧ High(o₂) ∧ High(o₃) ∧ ∀o (High(o) → (o=o₁∨o=o₂∨o=o₃)) ]

# E3	沒有任何 premium 使用者同時擁有所有 urgent 訂單。	嵌套 ¬∃u ∀o (Urgent(o) → Owner(u,o))
    # ~∃u (Premium(u) -> ∀o(Urgent(o) -> Owner(u,o)))
    # ! ¬∃u [ Premium(u) ∧ ∀o (Urgent(o) → Owner(u,o)) ]

# E4	每筆訂單恰好被兩位不同使用者同時擁有。	∀o ∃u₁∃u₂ (u₁≠u₂ ∧ Owner(u₁,o) ∧ Owner(u₂,o) ∧ ∀u (Owner(u,o)→(u=u₁∨u=u₂)))
    # ! ∀o ∃u₁∃u₂ (u₁≠u₂ ∧ Owner(u₁,o) ∧ Owner(u₂,o) ∧ ∀u (Owner(u,o)→(u=u₁∨u=u₂))) # ! 前半段處理「不同兩」用戶同時擁有，後半段處理「限定這兩人」

# E5	若使用者不是 admin，則存在另一位 admin 能看見他所有訂單。	用 ¬Admin(u) → ∃v [Admin(v) ∧ ∀o (Owner(u,o)→CanView(v,o))]
    #  ~Admin(u1) -> ∃u2 [Admin(u2) ∧ ∀o(Owner(u1,o) -> View(u2,o))]
    # ! ∀u₁ ( ¬Admin(u₁) → ∃u₂ [ u₂≠u₁ ∧ Admin(u₂) ∧ ∀o ( Owner(u₁,o) → CanView(u₂,o) ) ] )

# E6	某些訂單由所有非 premium 使用者共同擁有。	∃o ∀u (¬Premium(u) → Owner(u,o))
    # ∃o ∀u (¬Premium(u) → Owner(u,o))

# ---------------------------------------------------------------
# F1	¬∃o ∀u (Paid(o) → Owner(u,o))	推否定進原子並改全稱：∀o ∃u (Paid(o) ∧ ¬Owner(u,o))
    # ∀o ∃u (Paid(o) ∧ ¬Owner(u,o)) # ! 這邊要變成 ∀o ∃u

# F2	∀u ∃o (Owner(u,o) ∧ Urgent(o))	將量詞交換為 ∃o ∀u … 是否等價？如否，給反例（列兩人一單）。
    # 所有用戶存在一個訂單並且是緊急的
    # ∃o ∀u (Owner(u,o) ∧ Urgent(o)) 存在一用戶擁有所有訂單並且訂單是緊急的
    # 兩者不等價。轉換成自然語言就不相同

# F3	∀o ((Paid(o) ∨ Cancel(o)) ∧ ¬(Paid(o) ∧ Cancel(o)))	寫成沒有 ∨、¬ 在外層的 Prenex CNF。
    # ∀o [ (Paid(o) ∨ Cancel(o)) ∧ (¬Paid(o) ∨ ¬Cancel(o)) ]

# F4	∃u (Has2FA(u) ↔ Premium(u))	先拆 ↔，再用 Imp → ∨、DM，把否定推到底並拉量詞到最外。
    # ∃u ((~H(u) v P(u)) ∧ (~P(u) v H(u)))

# ---------------------------------------------------------------
# G1 前提  # ① ∀o (Ship(o) → Paid(o)) ② ∃o Cancel(o)
# 結論：∃o Paid(o)
# ↑ 有效或無效？若無效，給出只含 1 筆訂單的反例。
    # 無效，給的第二條件完全不相關，沒辦法幫助得到結論

# G2 前提  # ① ∃u ∀o (Owner(u,o) → Ship(o)) ② ∃o ¬Ship(o)
# 結論：∃u ¬Owner(u,o)
# （注意 u, o 自由與綁定範圍）
    # 這邊的前提是，存在一個用戶他的所有訂單都寄送了，以及，存在一個訂單沒有寄送
    # 想推論得到，存在一用戶不是該訂單的所有人
    # ! 至少會有一個人，不可能是該訂單所有人（因為有一個用戶只要有訂單都送了）  經典的 MT

# G3 前提 # ① ∀u (Premium(u) → Has2FA(u)) ② ∃u ¬Premium(u)
# 結論：∃u ¬Has2FA(u)
    # 所有用戶如果有P則他有通過認證
    # 存在用戶非P
    # ! 不能推論，無法基於 MT 是基於為假的後建，非前建