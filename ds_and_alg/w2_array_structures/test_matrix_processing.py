import numpy as np
from d_organize_and_challenge import process_matrix

def test_process_matrix_add():
    A = np.array([[10, 20], [30, 40]])
    B = np.array([[1, 2], [3, 4]])
    result = process_matrix(A, B)
    expected = np.array([], dtype=int).reshape(1, 0)
    assert np.array_equal(result, expected)

def test_process_matrix_broadcast():
    A = np.array([[10, 20], [30, 40]])
    B = np.array([1, 2])  # broadcasting → [[11, 22], [31, 42]]
    result = process_matrix(A, B)
    expected = np.array([[]])
    assert np.array_equal(result, expected)

def test_process_matrix_fail():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([9, 9, 9])
    try:
        process_matrix(A, B)
        # 理論上是跑不到下面，因為except
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Cannot broadcast or add"


# pytest ds_and_alg/w2_array_structures/test_matrix_processing.py

# if __name__ == "__main__":
# 保護檔案中沒有要調用的測試，因為當調用檔案中的函數，其他內容也會被執行