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

'''Main function for UCI letter and spam datasets.
'''

# Necessary packages
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from data_loader import data_loader
from gain import gain
from utils import rmse_loss


def main(args):
    '''Main function for UCI letter and spam datasets.

    Args:
      - data_name: letter or spam
      - miss_rate: probability of missing components
      - batch:size: batch size
      - hint_rate: hint rate
      - alpha: hyperparameter
      - iterations: iterations

    Returns:
      - imputed_data_x: imputed data
      - rmse: Root Mean Squared Error
    '''

    data_name = args.data_name
    miss_rate = args.miss_rate

    gain_parameters = {'batch_size': args.batch_size,
                       'hint_rate': args.hint_rate,
                       'alpha': args.alpha,
                       'iterations': args.iterations}

    # Load data and introduce missingness
    ori_data_x, miss_data_x, data_m = data_loader(data_name, miss_rate)

    # Impute missing data
    imputed_data_x = gain(miss_data_x, gain_parameters)

    # Report the RMSE performance
    rmse = rmse_loss(ori_data_x, imputed_data_x, data_m)

    print('RMSE Performance: ' + str(np.round(rmse, 4)))

    return ori_data_x, imputed_data_x, rmse


def show(acc, pre):
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(acc, color="k", label="真实值", marker='^', ms=3)  # 颜色表示
    plt.plot(pre, color="r", label="填补值", marker='o', ms=3)
    # plt.axis([500, 700, 1, 115578100])  # 设定x轴 y轴的范围
    轴 = plt.gca()
    轴.set_xlim([500, 700])  # 设置X轴的区间
    轴.set_ylim(bottom=8 * pow(10, 7))  # Y轴下限
    plt.xlabel("荷花号40%数据缺失率")  # x轴命名表示
    plt.ylabel("幅值")  # y轴命名表示

    # plt.axis([0, 100, 0, 115578100.88])  # 设定x轴 y轴的范围

    plt.title("实际值与预测值折线图")
    plt.legend()  # 增加图例
    plt.show()  # 显示图片


if __name__ == '__main__':
    fix_seed = 2021
    # random.seed(fix_seed)
    np.random.seed(fix_seed)

    # Inputs for the main function
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_name',
        choices=['letter', 'spam', 'ec', 'uk', '1min'],
        default='1min',
        type=str)
    parser.add_argument(
        '--miss_rate',
        help='missing data probability',
        default=0.40,
        type=float)
    parser.add_argument(
        '--batch_size',
        help='the number of samples in mini-batch',
        default=128,
        type=int)
    parser.add_argument(
        '--hint_rate',
        help='hint probability',
        default=0.9,
        type=float)
    parser.add_argument(
        '--alpha',
        help='hyperparameter',
        default=100,
        type=float)
    parser.add_argument(
        '--iterations',
        help='number of training interations',
        default=10000,
        type=int)

    args = parser.parse_args()

    # Calls main function
    ori_data_x, imputed_data, rmse = main(args)
    show(ori_data_x[:, 1], imputed_data[:, 1])
    pd.DataFrame(ori_data_x).to_csv("ori_1min_40%.csv")
    pd.DataFrame(imputed_data).to_csv("impute_1min_40%.csv")
    # pd.DataFrame({'true_value':ori_data_x[:, 1], 'impute_value': imputed_data[:, 1]}).to_csv('1min_10%.csv')
