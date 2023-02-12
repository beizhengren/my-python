import sys
import numpy as np

def load_pcd_to_ndarray(pcd_path):
    with open(pcd_path) as f:
        while True:
            ln = f.readline().strip()
            if ln.startswith('DATA'):
                break

        points = np.loadtxt(f)
        points = points[:, 0:4]
        points[:, 3] /= 256
        return points 

if __name__ == '__main__':
    pcd_path = sys.argv[1]
    points = load_pcd_to_ndarray(pcd_path)
    np.savetxt("output.txt", points, delimiter=', ')
