import seaborn as sns
import matplotlib.pyplot as plt

x = {'prediction': {5: 'c1',
  4: 'c1',
  3: 'c1',
  2: 'c1',
  0: 'c1',
  1: 'c1',
  7: 'c1',
  6: 'c1'},
 'variable': {5: 'ft1',
  4: 'ft2',
  3: 'ft3',
  2: 'ft4',
  0: 'ft5',
  1: 'ft6',
  7: 'ft7',
  6: 'ft8'},
 'value': {5: 0.020915912763961077,
  4: 0.020388363414781133,
  3: 0.007204373035913109,
  2: 0.0035298765062560817,
  0: -0.002049702058734183,
  1: -0.004283512505036808,
  7: -0.01882610282871816,
  6: -0.022324439779323434}}

sns.barplot(data=x, x='value', y='variable', 
            hue='prediction', orient="h", facecolor='red')