import pandas as pd

import main_letter_spam as ml

if __name__ == '__main__':
    acc = pd.read_csv("./ori_1min_40%.csv")
    pre = pd.read_csv("./impute_1min_40%.csv")
    ml.show(acc.iloc[:, 1], pre.iloc[:, 1])
