# coding=utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Data loader for UCI letter, spam and MNIST datasets.
'''

# Necessary packages
import numpy as np
from keras.datasets import mnist

from utils import binary_sampler


def data_loader(data_name, miss_rate):
  '''Loads datasets and introduce missingness.
  
  Args:
    - data_name: letter, spam, or mnist
    - miss_rate: the probability of missing components
    
  Returns:
    data_x: original data
    miss_data_x: data with missing values
    data_m: indicator matrix for missing components
  '''

  # Load data,这里的数据集只有letter和spam两个,
  # 如果不想下载数据集的话可以跑跑开源数据集mnist，
  if data_name in ['letter', 'spam', 'ec', 'uk', '1min']:
    file_name = 'data/' + data_name + '.csv'
    data_x = np.loadtxt(file_name, delimiter=",", skiprows=1)
  elif data_name == 'mnist':
    (data_x, _), _ = mnist.load_data()
    data_x = np.reshape(np.asarray(data_x), [60000, 28 * 28]).astype(float)

  # Parameters
  no, dim = data_x.shape

  # Introduce missing data
  # 这里对数据集进行随机的掩码处理，可以理解为让他随机的把
  # 参数配置中的miss_rate指定值这里是20%的数数变为nan,也就是缺失值
  data_m = binary_sampler(1 - miss_rate, no, dim)
  miss_data_x = data_x.copy()
  miss_data_x[data_m == 0] = np.nan

  return data_x, miss_data_x, data_m
