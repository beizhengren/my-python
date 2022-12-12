
import torch

def test_operator():
    coords = torch.tensor(
    [[0, 1, 2, 3, 4],
     [1, 1, 2, 3, 4],
     [2, 1, 2, 3, 4],
     [3, 1, 2, 3, 4]])

    ltest = coords[:, 0]
    print(ltest)
    mask = ltest == 1
    print(mask)
    this_coords = coords[mask]
    print(this_coords)
    print(this_coords.size())
if __name__ == '__main__':
    test_operator()