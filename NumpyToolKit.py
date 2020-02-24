import numpy as np

class NPDict:
    '''
    This class was built to search dict type numpy arrays
    Dict is a python dictionary
    kformat is the format to use for the keys. Default set to 20 character unicode string
    vformat is the format to use for the values. Default set to python object type
    ###
    example:
    d = {'a1': 1.2345, 'a2': 2.445556, 'a3': [4.5365, 3.56545]}
    ###
    nd = NPDict(d)
    >>> nd.get_keys()
    ['a1', 'a2', 'a3']
    >>> nd.get_values()
    array([1.2345, 2.445556, list([4.5365, 3.56545])], dtype=object)
    >>> nd.get('a3')
    [4.5365, 3.56545]
    ###
    nd2 = nd.array_from()
    >>> nd2['keys']
    array(['a1', 'a2', 'a3'], dtype='<U20')
    >>> nd2['values']
    array([1.2345, 2.445556, list([4.5365, 3.56545])], dtype=object)
    '''
    def __init__(self, Dict, kformat='U20', vformat='O'):
        self.Dict = Dict
        self.names = ['keys', 'values']
        self.formats = [kformat, vformat]
        self.dtype = self.d_type()
        self.keys = self.names[0]
        self.values = self.names[1]
        self.array = self.array_from()
    '''
    '''
    def d_type(self):
        return dict(names=self.names, formats=self.formats)
    '''
    '''
    def array_from(self):
        return np.asarray(list(self.Dict.items()), dtype=self.dtype)
    '''
    '''
    def get_keys(self):
        return list(self.Dict.keys())
    '''
    '''
    def get_values(self):
        return self.array[self.values]
    '''
    '''
    def get(self, Name):
        idx = self.get_keys().index(Name)
        data = self.array[self.values]
        return data[idx]

class NPSearch:
    '''
    This class was built to search numpy arrays for min, max and index values along columns
    arr is the numpy array to search.
    The default axis is set to 0. In an array of coordinates, 0 is the x axis, 1 is the y axis, and 2 is the z axis
    ###
    example:
    >>> arr = np.array([[1.2753, 3.7454, 2.8635],[0.3566, 1.8265, 3.6422],[4.5677, 0.4456, 1.3332],[2.5533, 1.5522, 0.4477]], dtype=float)
    >>> nps = NPSearch(arr)
    >>> nps.get_max_idx()
    2
    >>> nps.get_max()
    array([4.5677, 0.4456, 1.3332])
    >>> nps.get_min_idx()
    1
    >>> nps.get_min()
    array([0.3566, 1.8265, 3.6422])
    >>> nps.get_max_idx(1)
    0
    >>> nps.get_max(1)
    array([1.2753, 3.7454, 2.8635])
    >>> nps.get_min_idx(1)
    2
    >>> nps.get_min(1)
    array([4.5677, 0.4456, 1.3332])
    >>> nps.get_max_idx(2)
    1
    >>> nps.get_max(2)
    array([0.3566, 1.8265, 3.6422])
    >>> nps.get_min_idx(2)
    3
    >>> nps.get_min(2)
    array([2.5533, 1.5522, 0.4477])
    '''
    def __init__(self, arr):
        self.arr = np.asarray(arr)
        self.len = self.arr.shape[0]
        self.indexes = np.arange(self.len)
    '''
    '''
    def npSet(self, arr1, arr1):
        return np.intersect1d(arr1, arr2)
    '''
    '''
    def get_index(self, arr, item):
        return arr.tolist().index(item)
    '''
    '''
    def get_clip(self, min, max, axis=0,):
        data = self.arr[:,axis]
        return self.get_index(data, np.clip(data, min, max))
    '''
    '''
    def get_max_idx(self, axis=0):
        data = self.arr[:,axis]
        return self.get_index(data, np.max(data))
    '''
    '''
    def get_min_idx(self, axis=0):
        data = self.arr[:,axis]
        return self.get_index(data, np.min(data))
    '''
    '''
    def get_max(self, axis=0):
        return self.arr[self.get_max_idx(axis)]
    '''
    '''
    def get_min(self, axis=0):
        return self.arr[self.get_min_idx(axis)]
    '''
    '''
    def greater_than(self, value, axis=0):
        return np.where(self.arr[:,axis] >= value)
    '''
    '''
    def lesser_than(self, value, axis=0):
        return np.where(self.arr[:,axis] <= value)
    '''
    '''
    def in_between(self, max, min, axis=0):
        return np.intersect1d(np.where(self.arr[:,axis] <= max), np.where(self.arr[:,axis] >= min))
    '''
    '''
    def not_between(self, max, min, axis=0):
        return np.append(np.where(self.arr[:,axis] >= max), np.where(self.arr[:,axis] <= min))
    '''
    '''
    def box_in(self, amax, amin, bmax, bmin, a=0, b=1):
        mask = (self.arr[:,a] <= amax) & (self.arr[:,a] >= amin) & (self.arr[:,b] <= bmax) & (self.arr[:,b] >= bmin)
        return self.indexes[mask]
    '''
    '''
    def box_out(self, amax, amin, bmax, bmin, a=0, b=1):
        bi = self.box_in(amax, amin, bmax, bmin, a, b)
        mask = np.isin(self.indexes, bi, invert=True)
        return self.indexes[mask]
    '''
    '''
    def cube_in(self, amax, amin, bmax, bmin, cmax, cmin, a=0, b=1, c=2):
        mask = (self.arr[:,a] <= amax) & (self.arr[:,a] >= amin) & (self.arr[:,b] <= bmax) & (self.arr[:,b] >= bmin) & (self.arr[:,c] <= cmax) & (self.arr[:,c] >= cmin)
        return self.indexes[mask]
    '''
    '''
    def cube_out(self, amax, amin, bmax, bmin, cmax, cmin, a=0, b=1, c=2):
        ci = self.cube_in(amax, amin, bmax, bmin, cmax, cmin, a, b, c)
        mask = np.isin(self.indexes, ci, invert=True)
        return self.indexes[mask]
    '''
    '''
    def dist_vecs(self, arg):
        vecs = self.arr - arg
        return vecs
    '''
    '''
    def dist_arr(self, arg):
        vecs = self.arr - arg
        return np.linalg.norm(vecs, axis=1)
    '''
    '''
    def dist_max(self, arg):
        data = self.dist_arr(arg)
        return self.get_index(data, np.max(data))
    '''
    '''
    def dist_min(self, arg):
        data = self.dist_arr(arg)
        return self.get_index(data, np.min(data))
    '''
    '''
    def in_range(self, arg, value):
        data = self.dist_arr(arg)
        return np.where(data <= value)
    '''
    '''
    def out_of_range(self, arg, value):
        data = self.dist_arr(arg)
        return np.where(data >= value)
    '''
    '''
    def limited_range(self, arg, max, min):
        data = self.dist_arr(arg)
        return np.intersect1d(np.where(data <= max), np.where(data >= min))
    '''
    '''
    def limited_range_inv(self, arg, max, min):
        data = self.limited_range(arg, max, min)
        mask = np.isin(self.indexes, data, invert=True)
        return self.indexes[mask]
    '''
    '''

