# chi-square
# 這邊還是C6的 pdf
# the 'degree of freedom (df)', 但是這會有自己的分布圖形，不是之前的normal distribution
p_value = pchisq(24.73, 6-1, lower.tail = FALSE) # 0.0001570929
p_value < 0.05 # TRUE

# ------------------------------------------------

p_value = pchisq(30.89, 3-1, lower.tail = FALSE) # 1.960296e-07
p_value < 0.05 # TRUE

# ------------------------------------------------
# 期望值（expected count）是依據「H₀：兩變數獨立」假設，
# 用行比例 × 列比例 × 總人數計算出的理論人數，所以公式變成 row total × column total ÷ grand total。

p_value = pchisq(1.3121, (3-1)*(3-1),lower.tail = FALSE)
# 0.8593193

# ------------------------------------------------
# 1. 表格的每個觀察值必須彼此獨立
# 2. 每一個 cell 的 expected count（期望次數）至少要 ≥ 5
# 3. df > 1（自由度必須 > 1）

# ------------------------------------------------
# ------------------------------------------------

# t 分布尾巴更長，更扁平更寬，只基於一個para, degrees of freedom(df) 
diffs <- c(698,1104,1037,1889,1911,2416,2761,4382,1839,321)
diffs_mean = mean(diffs)   # 1836.8
diffs_sd = sd(diffs) 

SE = diffs_sd / sqrt(10)
T_score = (diffs_mean - 0) / SE
df = 10 -1

p_value = pt(T_score, df=df, lower.tail = FALSE) # 0.0004030922
# 小於 0.05 我們可以拒絕 H0

# ------------------------------------------------
# A CI for small sample mean
t_star = qt(0.975, df=9) # 2.262157 ## 對照其他組，這t star 是在算95% CI
z_star = qnorm(0.975) # 1.959964

SE = diffs_sd / sqrt(10)
ME = t_star * SE

low = diffs_mean - ME # 994.5304
high = diffs_mean + ME # 2677.07
# 是，如果你的 95% 信賴區間 (CI) 兩端都不包含 0 → 代表平均差異（mean difference）在統計上顯著不為 0。
# 也就是說：6th 與 13th 的平均 traffic 量確實有差異（成對差異不是偶然）。

# ------------------------------------------------ 

d_m = -0.545
d_sd = 8.887
alpha = 0.05

SE = d_sd / sqrt(200)
ME = qt(0.975, df=199) * SE

low = d_m - ME # -1.784189
high = d_m + ME # 0.6941889
    # 區間包含 0：無法拒絕 H₀（平均差 = 0）

T_score = (d_m - 0) / SE
p_value = 2 * pt(abs(T_score), df=199, lower.tail = FALSE)
# 0.3868365
    # p_value 大於 0.05，無法拒絕 H0
    # 雙尾巴，一定要加上 abs