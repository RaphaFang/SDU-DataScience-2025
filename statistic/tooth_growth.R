# 載入資料
data("ToothGrowth")
head(ToothGrowth)

# 查看資料結構
str(ToothGrowth)

# 過濾出劑量為 2.0 的資料
df <- subset(ToothGrowth, dose == 2.0)

# 觀察 VC vs OJ 的牙齒增長差異
boxplot(len ~ supp, data = df, main = "Tooth Growth by Supplement Type (2mg dose)", ylab = "Tooth Length")

# 執行 t 檢定
result <- t.test(len ~ supp, data = df)
print(result)