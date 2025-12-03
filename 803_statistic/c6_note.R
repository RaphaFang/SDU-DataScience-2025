p_hat <- 571/670 # 0.8522388

SE = sqrt(p_hat * (1-p_hat) / 670) # 0.01370956
ME = 1.96 * SE # 0.02687073

lowerInt = p_hat - ME # 0.8253681
upperInt = p_hat + ME # 0.8791095
# 得到有 95% 信心 真實數據就躺在這兩者區間

# ------------------------------------------------
# c6, p34
# 這可以作為算出H0 是否為真的算是有差異

p_zero <- 0.8
p_hat <- 571/670 # 0.8522388

SE = sqrt(p_zero * (1-p_zero) / 670)
Z = (p_hat - p_zero) / SE

p_value <- 1 - pnorm(Z) # 0.0003618758
# 這邊 1-0.9994, 0.9994 是 pnorm(這邊丟入Z)
# 因為p_value對比任何的alpha都很小，所以都能拒絕 H0
# 通常都是檢查 p_value 有沒有小於 0.05

# ------------------------------------------------
# p35
# Hypothesis Testing
p_hat = 0.11
p_zero = 0.1
n = 1001
SE = sqrt(p_zero * (1-p_zero) / n)
Z = (p_hat - p_zero) / SE

p_value = 1 - pnorm(Z) # 0.1457997

# ------------------------------------------------
# CI Estimation：這是透過一筆資料，去推算真實差，計算 95%落點
# 拿兩組樣本算出比例差 p̂₁−p̂₂，用兩組的標準誤組成差值的 SE，再用 z×SE 做出比例差的信賴區間；若區間包含 0 → 代表資料不足以顯示兩組有差異。
p_duke = 69 / 105
p_us = 454 / 680
p_hat = p_duke - p_us # -0.0105042

SE = sqrt(p_duke * (1-p_duke)/ 105 + p_us*(1-p_us)/ 680)
ME = 1.96*SE # 0.09745139

low = p_hat - ME # -0.1079556
high = p_hat + ME # 0.08694719

# ------------------------------------------------
# Two-proportion Z test
# 使用 pooled proportion 估計 H₀ 下的共同 p₀，
# 由此得到檢定用的 SE，再利用 Z 統計量和雙尾 p-value 判斷是否能拒絕 H₀：p₁ = p₂。
p_pooled = (69 + 454) / (105 + 680)
SE_HT = sqrt(p_pooled*(1-p_pooled)/105 + p_pooled*(1-p_pooled)/680)
Z = (p_hat - 0) / SE_HT

p_value = 2 * pnorm(Z) # 0.8317603 超大 無法拒絕