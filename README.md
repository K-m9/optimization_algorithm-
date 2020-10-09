# optimization_algorithm
各种优化算法的原理和代码实现

## 离散优化问题常用的基本求解方法
离散优化问题：又称为**整数规划 (线性整数规划)**，整数规划是指规划中的变量（全部或部分）
限制为整数，若在线性模型中，变量限制为整数，则称为整数线性规划。
目前所流行的求解整数规划的方法往往只适用于整数线性规划，
这是一类要求问题的解中的全部或一部分变量为整数的数学规划。
从约束条件的构成又可细分为线性，二次和非线性的整数规划。
- （1）分支定界法<br>
    &emsp;&emsp;以一般线性规划之**单纯形法**解得最佳解后，**将非整数值之决策变量分割成为最接近的两个整数**，
    分列条件，加入原问题中，**形成两个子问题(或分枝)分别求解**，
    如此便可**求得目标函数值的上限（上界）或下限（下界），从其中寻得最佳解**。<br>
    &emsp;&emsp;分支的过程就是不断给树增加子节点的过程。而定界就是在分支的过程中**检查子问题的上下界，如果子问题不能产生一比当前最优解还要优的解，那么砍掉这一支**。
    直到所有子问题都不能产生一个更优的解时，算法结束。（[10分钟了解分支定界法](https://www.cnblogs.com/dengfaheng/p/11225612.html)）<br><br>
- （2）[动态规划法](https://baike.baidu.com/item/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/529408?fromtitle=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E6%96%B9%E6%B3%95&fromid=19136902)<br>
    &emsp;&emsp;其基本思想是将**待求解问题分解成若干个子问题**，
    **先求解子问题，然后从这些子问题的解得到原问题的解**。与分治法不同的是，
    适合于用动态规划求解的问题，经分解得到**子问题往往不是互相独立的**。
    若用[分治法](https://baike.baidu.com/item/%E5%88%86%E6%B2%BB%E6%B3%95)来解这类问题，则分解得到的子问题数目太多，
    有些子问题被重复计算了很多次。如果我们能够**保存已解决的子问题的答案，
    而在需要时再找出已求得的答案**，这样就可以避免大量的重复计算，节省时间。
    我们可以用一个表来记录所有已解的子问题的答案。不管该子问题以后是否被用到，
    只要它被计算过，就将其结果填入表中。这就是动态规划法的基本思路。
  - <font color=#00ffff>[floyd算法](https://github.com/K-m9/optimization_algorithms/blob/master/Floyd%E7%AE%97%E6%B3%95.pdf) 和  [python代码实现](https://zhuanlan.zhihu.com/p/63395403)</font><br><br>
- （3）[智能算法](https://baike.baidu.com/item/%E6%99%BA%E8%83%BD%E7%AE%97%E6%B3%95/3387637)</font><br>
  - <font color=#00ffff>[Dijkstra算法](https://my.oschina.net/thinwonton/blog/3133222) 和python代码实现<br>
    - 指导性搜索法
      - 模拟退火算法
      - <font color=#00ffff>遗传算法</font>
      - 禁忌搜索
    - 系统动态演化方法
      - <font color=#00ffff>神经网络算法</font>
      - 混沌搜索<br><br>
- （4）枚举或部分枚举法
- （5）松弛方法
- （6）其他
