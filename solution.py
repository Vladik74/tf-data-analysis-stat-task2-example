import pandas as pd
import numpy as np

from scipy.stats import gamma

chat_id = 496613075 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array):
    alpha = 1 - p
    k = 2/(56*56)
    q1 = gamma(len(x), 1).ppf((1-alpha)/2)
    q2 = gamma(len(x), 1).ppf((1+alpha)/2)
    sum = np.sum(x)
    return (k*((q1+sum)/2)-1/2, k*((q2+sum)/2)-1/2)
