import matplotlib.pyplot as plt
import pandas as pd 

eps_ls=['1e-5','5e-5','1e-4','1e-6']
f_ls=['1.log','2.log','3.log','4.log']

for i in range(4):
    f = f_ls[i]
    eps = eps_ls[i]
    
    with open(f) as handler:
        data = handler.readlines()
        data = [d.strip().split() for d in data if 'Nats' in d]
        data = [float(d[3].split('(')[0]) for d in data]
        series = pd.Series(data,name=eps)
        series.plot()
plt.legend()
plt.title('Power loss')
plt.savefig('1.png')