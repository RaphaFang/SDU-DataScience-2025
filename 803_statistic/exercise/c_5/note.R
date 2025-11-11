popsize = 6019866
inflavour = floor(0.88* popsize)
against = popsize - inflavour

posEntries = c(rep(TRUE, inflavour), rep(FALSE, against))

listSample = sum(sample(posEntries, 100) == TRUE)

caseList = c()
for ( i in 1:100000){
    caseList = c(caseList, sum(sample(posEntries, 100) == TRUE))

}

rr = caseList / 100
hist(rr)
mean(rr)
sd(rr)

# ------------------------------------------------------------------------
qnorm(0.975) # 1.959964 >> 2.5% on both side, 95% interval
qnorm(0.995) # 2.575829 >> 0.5% on both side, 99% interval

# ------------------------------------------------------------------------
# step 1, get the sample from posEntries and store at caseList
caseList = c()
for ( i in 1:100000){
    caseList = c(caseList, sum(sample(posEntries, 100) == TRUE))

}

# ------------------------------------------------------------------------
# step 2, stander error(SE), SE = sqrt((p*(1-p))/n)
# Which is by Central Limit Theorem, CLT, that given enough sample, we'll get normal distribution of our target.

# 標準差（SD） → 看資料本身的分散程度。 標準誤（SE） → 看「樣本統計量」的分散程度。

True_SE = sqrt((0.88*0.12)/100)  # >> 0.03249615

p_hat_list <- caseList / 100
Sample_SE = sd(p_hat_list) # >> 0.03240506

# ------------------------------------------------------------------------
# step 3, set 95% confidence interval, z = 1.96
Z = 1.96

# ------------------------------------------------------------------------
# step 4, Margin of Error, MOE
MOE = Z * Sample_SE  # >> 0.06351392

# ------------------------------------------------------------------------
# step 5, the interval of the data
p_hat_mean = mean(p_hat_list)

lower <- p_hat_mean - MOE
upper <- p_hat_mean + MOE
c(lower, upper)
# [1] 0.8164490 0.9434768

# ------------------------------------------------------------------------
# Z 叫作 test statistic（檢定統計量）。它代表「樣本比例（或平均）離假設值有幾個標準誤遠」。

# 用白話說，Z 是在回答這句話：
# 我觀察到的結果和我假設的狀況，差距有多大？
# 這個差距在統計上「稀有」到應該懷疑假設嗎？