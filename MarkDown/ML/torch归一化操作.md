**归一化操作的实现**

我们今天只来考虑如何实现，至于归一化的原理我们就不再赘述，知乎和博客都写的很多了，对于这几种归一化的方法，比如BN(Batch),LN(Layer),IN(Instance),GN(Group)这四种，在GN的论文中有一幅图可以清晰的描述，我们不用看公式，只要把下面这个图记住就好了！（蓝色区域即为其归一化的区域，说白了我们每个归一化时使用的均值和方差就是由蓝色区域计算得来的，然后作用到这个蓝色区域进行归一化，从而对整体X进行归一化）。

![img](../pic/torch normalize.jpeg)

那么我们可以看下简单实现（仅归一化）

**Batch Normalization**

```javascript
import torch
from torch import nn
bn = nn.BatchNorm2d(num_features=, eps=, affine=False, track_running_stats=False)
x = torch.rand(, , , )*
official_bn = bn(x)   # 官方代码

x1 = x.permute(, , , ).reshape(, -1) # 对(N, H, W)计算均值方差
mean = x1.mean(dim=).reshape(, , , )
# x1.mean(dim=1)后维度为(3,)
std = x1.std(dim=, unbiased=False).reshape(, , , )
my_bn = (x - mean)/std
print((official_bn-my_bn).sum())  # 输出误差
```

**Layer Normalization**

```javascript
import torch
from torch import nn
ln = nn.LayerNorm(normalized_shape=[, , ], eps=, elementwise_affine=False)
x = torch.rand(, , , )*
official_ln = ln(x)   # 官方代码

x1 = x.reshape(, -1)  # 对（C,H,W）计算均值方差
mean = x1.mean(dim=).reshape(, , , )
std = x1.std(dim=, unbiased=False).reshape(, , , )
my_ln = (x - mean)/std
print((official_ln-my_ln).sum())
```

**Instance Normalization**

```javascript
import torch
from torch import nn
In = nn.InstanceNorm2d(num_features=, eps=, affine=False, track_running_stats=False)
x = torch.rand(, , , )*
official_In = In(x)   # 官方代码

x1 = x.reshape(, -1)  # 对（H,W）计算均值方差
mean = x1.mean(dim=).reshape(, , , )
std = x1.std(dim=, unbiased=False).reshape(, , , )
my_In = (x - mean)/std
print((official_In-my_In).sum())
```

**Group Normalization**

```javascript
import torch
from torch import nn
gn = nn.GroupNorm(num_groups=, num_channels=, eps=, affine=False)
# 分成了4组，也就是说蓝色区域为（5，5, 5）
x = torch.rand(, , , )*
official_gn = gn(x)   # 官方代码

x1 = x.reshape(,,-1)  # 对（H,W）计算均值方差
mean = x1.mean(dim=).reshape(, , -1)
std = x1.std(dim=, unbiased=False).reshape(, , -1)
my_gn = ((x1 - mean)/std).reshape(, , , )
print((official_gn-my_gn).sum())
```