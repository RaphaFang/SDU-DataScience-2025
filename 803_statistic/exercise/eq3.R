data = c(7.5, 7.8, 7.2, 7.5, 7.3, 7.8, 7.2, 8.1, 7.9, 8.0,
8.0, 7.3, 7.3, 7.4, 7.8, 7.6, 7.6, 7.6, 7.7, 7.5,
7.9, 7.3, 8.0, 7.4, 7.4, 7.2, 7.4, 7.5, 7.9, 7.3,
7.4, 8.2, 7.4, 7.5, 7.6, 7.4, 7.5, 7.2, 8.0, 7.3,
7.8, 7.8, 7.5, 7.6, 7.8, 7.3, 8.0, 7.4, 7.5, 7.9)

data_m = mean(data)
data_sd = sd(data)

SE = data_sd / sqrt(50)
T_score = (data_m - 7.5) / SE
df = length(data) -1

p_value = 2 * pt(T_score, df=df, lower.tail = FALSE) # 0.02451206
# lower.tail = TRUE → 左尾
# lower.tail = FALSE → 右尾
# 這邊的 * 2 ，才是變成雙尾巴
# ------------------------------------------------
# χ² = Σ (O−E)² / E
data_set <- matrix(
  c(10,14,
    19,18,
    35,41,
    22,21,
    5,3,
    7,5),
  nrow = 6,
  byrow = TRUE
)

E <- chisq.test(data_set)$expected
chi_sq <- sum((data_set - E)^2 / E)

p_value = pchisq(chi_sq, (6-1)*(2-1),lower.tail = FALSE)

# ------------------------------------------------
multiply = function(x) {
    result = x * 2
    return (result)

}

for (i in seq(5)) {
    multiply(i)
    print(result) 
}