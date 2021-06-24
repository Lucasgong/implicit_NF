# Implicit Normalizing Flows (ICLR 2021 Spotlight)[[arxiv](https://arxiv.org/abs/2103.09527)][[slides](https://docs.google.com/presentation/d/1reCHEBjy9ygJ0bM_jvItEGU1jHDn7NfYBeC7FBqK-1Y/edit?usp=sharing)]

Implicit Normalizing Flows generalize normalizing flows by allowing the invertible mapping to be **implicitly** defined by the roots of an equation F(z, x) = 0. Building on [Residual Flows](https://arxiv.org/abs/1906.02735), we propose:

+ A **unique** and **invertible** mapping defined by an equation of the latent variable and the observed variable.
+ A **more powerful function space** than Residual Flows, which relaxing the Lipschitz constraints of Residual Flows.
+ A **scalable algorithm** for generative modeling.


## Improved experiments we made on the basis of the article
1. use anderson (rather than broyden) to solve fixed-point problem.
2. observes how threshold value impact trainning time and accuracy.

## How to run 
、、、
bash run_cifar10_by.sh
、、、

## How to get the datasets
Downdload the datasets from: https://zenodo.org/record/1161203#.Wmtf_XVl8eN
Unpack the downloaded file, and place it in the same folder as the code.
Make sure the code reads from the location the datasets are saved at.
Run the code as described above.
All datasets used in the experiments are preprocessed versions of public datasets. None of them belongs to us. The original datasets are:

### POWER:
http://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

### CIFAR-10
https://www.cs.toronto.edu/~kriz/cifar.html

