# LHY RL

Neural Network as Actor → DRL

Goodness of Actor

1. Generalization

Randomness in the actor and the game

expected value

Sample:

Gradient Ascent



![image](../pic/RL1.png)









![image-20211113155856639](../pic/RL2.png)





![image-20211113160510446](../pic/RL4.png)







![image-20211113161107280](../pic/RL5.png)

#### b means baseline here.





Critic (Q-learning)





## Policy Gradient



Supervised learning

Yet Reward exists, so weighted by R($t^n$)







### On-policy -> Off-policy

Importance Sampling:
$$
E_{x～p}[f(x)] = E_{x～q}[f(x)\frac{p(x)}{q(x)}]
$$
