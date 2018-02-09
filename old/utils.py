import matplotlib.style as mps
import numba
import numpy as np
import os


initial_path = None


def set_style():
    style_path = os.path.join(initial_path, 'qacd_xmap.mplstyle')
    mps.use(style_path)



@numba.jit
def median_filter_with_nans(input_array):
    ny, nx = input_array.shape
    output_array = np.empty_like(input_array)
    for j in range(ny):
        jm = j-1 if j > 0 else 0
        jp = j+2 if j < ny-1 else j+1
        for i in range(nx):
            im = i-1 if i > 0 else 0
            ip = i+2 if i < nx-1 else i+1
            output_array[j, i] = np.nanmedian(input_array[jm:jp, im:ip])
    return output_array