import numpy as np

def test1():
    print('Test 1:\n')
    A = np.random.randint(1, 100, size = (2, 3, 5))
    print('Matrix is:\n{}'.format(A))
    print('-------------------------')
    idx_max = np.argmax(A)
    print("max flatten idx is: {}".format(idx_max))

    print('-------------------------')
    idx_max_unravel = np.unravel_index(idx_max, A.shape)
    print("max unravel idx is: {}".format(idx_max_unravel))
    print('max value is {}'.format(A[idx_max_unravel]))

def test2():
    print('Test 2:\n')
    res_idx = np.unravel_index([22, 41, 37], (7, 6))
    # res_idx = np.unravel_index(22, (7, 6))
    print(res_idx)

def test3():
    
    dty = np.array([1])
    print(dty.dtype)
    print('dty.dtype is:\n')
    
    dims = 3
    tmp = np.arange(2 ** dims)
    print('tmp is:\n')
    print(tmp)
    
    tmp1 = [2] * dims
    print('tmp1 is:\n')
    print(tmp1)

    # unravel_idx is tuple    
    unravel_idx = np.unravel_index(tmp, tmp1)
    print('unravel_idx is:')
    print(unravel_idx)

    norm = np.stack(unravel_idx, axis = 1)
    print('norm is:')
    print(norm)
    print(norm.shape)

    cust_norm = norm.astype(dty.dtype)
    print('cust_norm is:')
    print(cust_norm)
    print(cust_norm.shape)

    corner_norm = cust_norm[[0, 1, 3, 2]]
    print('corner_norm is:\n')
    print(corner_norm)
    
def main():
    # test1()
    # test2()
    test3()

if __name__ == '__main__':
    main()
    