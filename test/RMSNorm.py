import torch
import torch.nn as nn
#RMSNorm是一层，是继承nn.Module的类
class RMSNorm(nn.Module):
    #__Init__,
    def __init__(self, dim:int, eps:float=1e-5):
        super.__init__()
        self.dim=dim
        self.eps=eps
        self.weight=nn.Parameter(torch.ones(dim))

#_NORM
    def _norm(self,x): #公式左边那一项
        pass

#,forward()
    def forward(self,x):
        pass