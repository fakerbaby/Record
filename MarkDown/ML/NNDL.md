[toc]

## 特征学习

特征抽取（Feature Extraction）:构造一个新的特征空间，并将原始的特征投影到新的空间中得到新的表示。



<img src="/Users/fakerbaby/Library/Application Support/typora-user-images/image-20211008124218279.png" alt="image-20211008124218279" style="zoom: 33%;" />

​	特征选择和特征抽取的优点是可以用较少的特征来表示原始特征中的大部 分相关信息，去掉噪声信息，并进而提高计算效率和减小维度灾难(Curse of Dimensionality).对于很多没有正则化的模型，特征选择和特征抽取非常必要. 经过特征选择或特征抽取后，特征的数量一般会减少，因此特征选择和特征抽取 也经常称为维数约减或降维(Dimension Reduction）

### 深度学习

传统的特征抽取一般是和预测模型的学习分离的.我们会先通过主成分分析或线性判别分析等方法抽取出有效的特征，然后再基于这些特征来训练一个具体的机器学习模型.

如果我们将特征的表示学习和机器学习的预测学习有机地统一到一个模型中，建立一个**端到端**的学习算法，就可以有效地避免它们之间准则的不一致性. 这种表示学习方法称为深度学习(Deep Learning，DL).深度学习方法的难点 是如何评价表示学习对最终系统输出结果的贡献或影响，即**贡献度分配问题**.目前比较有效的模型是**神经网络**，即将最后的输出层作为**预测学习**，其他层作为**表示学习**.





## 评价指标

#### 准确率(accuracy)

#### 错误率(error rate)

#### 精确率(Precsion)&召回率(Recall)

#### F值(F Measure)

$$\cal {F_c} =\frac{(1+\beta^2)\times{ P_c}\times R_C]}{\beta^2 \times P_c +R_C}$$

$\beta = 1$就是F1值 精确率和召回率的调和平均



计算分类算法的总体准确率、召回率以及F1值

使用Macro & Micro Average（宏平均和为平均）

<img src="/Users/fakerbaby/Library/Application Support/typora-user-images/image-20211008130402352.png" alt="image-20211008130402352" style="zoom:33%;" />



==有些文献的F1值宏平均值$\cal F_{1_{macro}} = \frac{1}{C}\sum_{c=1}^C F_{1_{c}}$==

微平均是每一个样本的性能指标的算术平均值.对于单个样本而言，它的精 确率和召回率是相同的(要么都是 1，要么都是 0).因此精确率的微平均和召回 率的微平均是相同的.同理，F1 值的微平均指标是相同的.当不同类别的样本数 量不均衡时，使用宏平均会比微平均更合理些.宏平均会更关注小类别上的评价

指标.



#### 交叉验证（Cross-Validation）

是一种比较好的衡量机器学习模型的统计分析方法，可以有效避免划分训练集和测试集时的随机性对评价结果造成的影响.我们可以把原始数据集平均分为 𝐾 组不重复的子集，每次选 𝐾 − 1 组子 集作为训练集，剩下的一组子集作为验证集.这样可以进行 𝐾 次试验并得到 𝐾 个模型，将这 𝐾 个模型在各自验证集上的错误率的平均作为分类器的评价.

==K一般大于3==





## 理论和定理

##### PAC学习理论

一个PAC 可学习(PAC-Learnable)的算法是指该学习算法能够在多项式时间内从合理数量的训 练数据中学习到一个近似正确的 𝑓(𝒙).

PAC 学习可以分为两部分:
 (1) 近似正确(Approximately Correct):一个假设 𝑓 ∈ F 是“近似正确”的，是指其在泛化错误 𝒢𝒟 (𝑓) 小于一个界限 𝜖.𝜖 一般为 0 到 21 之间的数，0 < 𝜖 < 21 .如果 𝒢𝒟 (𝑓) 比较大，说明模型不能用来做正确的“预测”.

(2) 可能(Probably):一个学习算法 𝒜 有“可能”以 1 − 𝛿 的概率学习到这样一个“近似正确”的假设.𝛿 一般为 0 到 1 之间的数，0 < 𝛿 < 1 .

PAC学习可以描述为：
$$
P(\cal{R(f)-R^{emp}_D(f)}\leqslant \epsilon)\geqslant \rm 1-\delta
$$


其中 𝜖,𝛿 是和样本数量 𝑁 以及假设空间$\cal F$ 相关的变量.如果固定 𝜖,𝛿，可以反过来 计算出需要的样本数量:
$$
N(\epsilon,\delta) \geqslant \frac{1}{2\epsilon^2(log|\cal F|+log\frac{2}{\delta})}
$$

##### No Free lunch

##### Occam's Razor

##### Ugly Duckling Theorem

##### Inductive Bias





## 机器学习类型比较

<img src="/Users/fakerbaby/Library/Application Support/typora-user-images/image-20211008133131171.png" alt="image-20211008133131171" style="zoom: 33%;" />









# 线性模型

### Logistic回归

二分类问题

### Softmax回归

多分类问题

 $\frac{\partial exp(x)}{\partial x} -> {diag(exp(x)}$ ?

按位计算的向量函数及其导数

<img src="/Users/fakerbaby/Library/Application Support/typora-user-images/image-20211008143835559.png" alt="image-20211008143835559" style="zoom:33%;" />

### 感知机

错误驱动的在线学习算法 [Rosenblatt, 1958].先 初始化一个权重向量 𝒘 ← 0(通常是全零向量)，然后每次分错一个样本 (𝒙, 𝑦) 时，即 𝑦𝒘T 𝒙 < 0，就用这个样本来更新权重.

##### 感知机收敛性



##### 广义感知机和广义感知机收敛性



### 线性分类器

KKT -> 不等式约束优化问题



KKT:







### 支持向量机



