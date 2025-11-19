import pandas as pd
import matplotlib.pyplot as plt

values = pd.Series([False, False, True, True])
v_counts = values.value_counts()

def autopct_format(pct, allvals):
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{pct:.4f}%\n({absolute})"

fig = plt.figure()
plt.pie(v_counts, labels=v_counts.index, autopct=lambda pct: autopct_format(pct, v_counts), shadow=True)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
