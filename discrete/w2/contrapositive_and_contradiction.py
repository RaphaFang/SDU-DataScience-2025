# | 名稱    | 基本假設   | 推導目標  | 結論形式    | 適用情形                |
# | ------- | ------   | -----   | ------     | ------------------- |
# | 直接證   | 前件 *p*  | …       | 得到 *q*    | p→q 且 p 不難用         |
# | 逆否證   | ¬q       | …        | 得到 ¬p    | p→q，q 較難證真，¬q 容易拿   |
# | 反證     | ¬命題     | … → ⟂   | 得到命題真  | “不存在…”、“√2 無理”等否定敘述 |
# ---------------------------------------------------------------
# ! 接下來 pytest 都不要用try except ，而是用 assert
# ---------------------------------------------------------------
# B.1 逆否證
# 命題：若 n² 為偶數，則 n 為偶數。
# (a) 寫出逆否命題 (b) 用逆否證完成證明。
    # 如果要逆否，需要將後建否定
    # n 不為偶數，也就是odd，則他的square必定是奇數（非偶數）
    # 因為奇數意味分解後沒有2，而次方後也不會得到2

# B.1  反證
# 證：不存在整數解 (x,y) 使 x² + y² = 2xy + 1。
    # 所以我要「假設存在」 整數解 (x,y)
    # 轉換得到 (x - y) =  +- 1
    # 反帶回到原先函數得 x y ，得到y平方會是 -1/4，不是整數
    # 我的反正證明了前提為真，證明成功

# ---------------------------------------------------------------
import pytest
import math
# pytest discrete/w2/contrapositive_and_contradiction.py

# B.2
# 逆否證 – 不等式
# 命題：若實數 x > 2 ⇒ 1/x < 0.5。
@pytest.mark.parametrize('x', [0.5, 1, 1.5, 2, 10])
def test_b1(x):
    if 1 / x >= 0.5:
        assert x <= 2
           # 逆否命題成立

# 反證 – 質數
# 證：√5 是無理數。
# key point; 如果不是有理數，跟號的數會是一串小數，再將這小數 square變不回原先數
@pytest.mark.parametrize('y', [5,6,7,8,9,10])
def test_b2(y):
    temp = (y**0.5)
    assert temp*temp == pytest.approx(y), '並非有理數'
    # ! pytest.approx() 不能在誇號內部運算，只能拿來比較

# 函式 square_root(n) 的契約：Pre n ≥ 0；Post (square_root(n))² = n。
# 編寫一條單元測試，利用逆否思路驗證「若輸出平方 ≠ n，則必是 n<0」。
        
@pytest.mark.parametrize('z', [1,4,9,-1,-2])
def test_b3(z):
    def square_root(n):
        assert n >= 0, "Precondition failed: n must be non-negative"
        return math.sqrt(n)

    r = square_root(z)
    assert r*r == pytest.approx(z), 'Statement Fails.'

# ---------------------------------------------------------------