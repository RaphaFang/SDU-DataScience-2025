coffee <- c(85, 88, 90, 83, 87, 92, 84, 86, 89, 91)
no_coffee <- c(80, 78, 82, 79, 77, 81, 76, 83, 80, 79)

t.test(coffee, no_coffee)
# p-value = 3.914e-06

# ----------------------------------------------------
scores <- c(82, 85, 79, 88, 90, 76, 84, 83)
t.test(scores, mu = 80)
# p-value = 0.07326
# Null hypothesis: 𝐻 0 : 𝜇 = 𝜇 0 
# Alternative hypothesis: 𝐻 𝑎 : 𝜇 ≠ 𝜇 0

t.test(scores, mu = 80, alternative="greater")
# p-value = 0.03663
# Null hypothesis: 𝐻 0 : 𝜇 ≤ 𝜇 0
# Alternative hypothesis: 𝐻 𝑎 : 𝜇 > 𝜇 0

t.test(scores, mu = 80, alternative="less")
# p-value = 0.9634
# Null hypothesis: 𝐻 0 : 𝜇 ≥ 𝜇 0
# Alternative hypothesis: 𝐻 𝑎 : 𝜇 < 𝜇 0