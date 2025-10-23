import numpy as np
import copy
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage

"""
z^(i) = w^T x^(i) + b
â^(i) = a^(i) = sigmoid(z^(i))
L(a^(i), y^(i)) = -y^(i) log(a^(i)) - (1-y^(i)) log(1-a^(i))

∂J/∂w = (1/m) * X (A - Y)^T
∂J/∂b = (1/m) * Σ_i (a^(i) - y^(i))

w := w - a * dw
b := b - a * db

dw > 0 代表 cost 對 w₁ 的變化是正的 → w₁ 越大 cost 越高。 所以你要讓 w₁ 變小。
dw < 0 代表 cost 對 w₁ 的變化是負的 → w₁ 越大 cost 越低。 所以你要讓 w₁ 變大。
"""

def sigmoid(z):
    s = 1/(1+np.exp(-z))
    return s

def initialize_with_zeros(dim):
    w = np.zeros((dim, 1))
    b = 0.0
    return w, b

def propagate(w, b, X, Y):
    m = X.shape[1]
    
    Z = w.T@X + b
    A = sigmoid(Z)
    cost = -(1/m) * np.sum(Y*np.log(A) + (1-Y) * np.log(1-A))

    dz = A - Y
    dw = (1/m) * X@dz.T
    db = (1/m) * np.sum(A-Y)
    
    cost = np.squeeze(np.array(cost))
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost

def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False):
    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    
    costs = []
    
    for i in range(num_iterations):  # 實際跑時，num_iterations當然會更大
        grads, cost = propagate(w, b, X, Y)
        
        dw = grads["dw"]
        db = grads["db"]
        
        w = w - learning_rate * dw
        b = b - learning_rate * db
        
        if i % 100 == 0:
            costs.append(cost)
        
            if print_cost:
                print ("Cost after iteration %i: %f" %(i, cost))
    
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    A = sigmoid(w.T@X + b)
        
    for i in range(A.shape[1]):
        if A[0,i]> 0.5:
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0
    
    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    w, b = np.zeros((X_train.shape[0], 1)), 0.0
    params, grads, costs = optimize(w, b, X_train, Y_train, num_iterations=num_iterations, learning_rate=learning_rate, print_cost=print_cost)
    w = params["w"]
    b = params["b"]
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b,X_train)
    
    if print_cost:
        print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
        print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d

learning_rates = [0.01, 0.001, 0.0001]
models = {}


# --------------------------------------------------------------------------------------------------------------------------------------------
for lr in learning_rates:
    print ("Training a model with learning rate: " + str(lr))
    models[str(lr)] = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=1500, learning_rate=lr, print_cost=False)
    print ('\n' + "-------------------------------------------------------" + '\n')

for lr in learning_rates:
    plt.plot(np.squeeze(models[str(lr)]["costs"]), label=str(models[str(lr)]["learning_rate"]))

plt.ylabel('cost')
plt.xlabel('iterations (hundreds)')

legend = plt.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()

"""
0.01：下降很快（收斂速度快），但初期震盪劇烈。
0.001：下降平滑，但明顯較慢。
0.0001：幾乎沒下降，代表學習率太小，模型還在「山腰上」沒走完。

不是月大月好
如果 α 太大，那個減法會「過頭」，
你不是往谷底走，而是直接跳到山的另一邊。
但一旦 α 超過這臨界值，更新就會「震盪甚至發散」。
"""