# Week03总结

## 深入理解递归-生成括号问题
##### 题目：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
```
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```
首先根据递归模板我们可以写出第一种版本：
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self._generate(0, 0, n, "", res)
        return res


    def _generate(self, left, right, MAX, s, res):
        if right == MAX:
            res.append(s)
        if left < MAX:
            self._generate(left + 1, right, MAX, s + '(', res)
        if right < left:
            self._generate(left, right + 1, MAX, s + ')', res)
```
left和right都设置为0然后不断增加，结束条件是达到了括号的数量MAX = n就可以结束。同时给子函数传进去一个res，来保存每一个可能的结果。这样的写法比较逻辑清晰，但是代码稍微冗余。改进的点：
1. 稍微想一下，可以考虑把_generate函数写进到generateParenthesis函数里面，而不是并行的，同时把res的定义放到函数声明里面，利用默认参数这个功能，这样每次递归函数的时候函数的参数可以写少。
2. 另一个就是可以去掉MAX，只要把left和right的初始值就设置成MAX，然后每次递归都减一就好了，这样我们就可以省去2个参数。于是得到的比较简短的代码如下：
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens.append(p)
            return parens
        return generate("", n, n)
```
应该注意的是我们的parens的return是跟if语句并行的，而不是在递归终结条件if not right下面。这是因为，每次判断递归结束的时候，我们需要把括号的类型P放到Parens里。但是return是我们把所有的递归树都经历了后才需要返回的，因此是与if并行的。

**另外，parens.append(p)语句也可以写成parens += p,（有逗号）。**


## Newton-Raphson法
[注：以下公式需要在浏览器添加MathJax Plugin for Github扩展程序才能正确显示]
如图所示给出了Newton法的集和图性。要求出$f(x) = 0$的根，初始估计$x_0$是给定的，画出函数$f$在$x_0$的切线。切线朝着根的方向贴近函数向下到$x$轴.切线与$x$轴的交点就是近似根，但是如果$f$弯曲，很可能不准确，因此**这一步要反复进行**。

![Newton](https://raw.githubusercontent.com/rfhklwt/algorithm010/master/Week03/Newton.png)

从这个几何图形可以建立Newton方法的代数公式。切线在$x_0$的斜率由导数$f'(x_0)$给出，切线上的一点是$(x_0, f(x_0))$。直线方程的点斜式是$y - f(x_0) = f'(x_0)(x - x_0)$，所以求切线与$x$轴的交点等同于在直线方程中取$y = 0$：

$\begin{aligned} f^{\prime}\left(x_{0}\right)\left(x-x_{0}\right) &=0-f\left(x_{0}\right) \\ x-x_{0} &=-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)} \\ x &=x_{0}-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)} \end{aligned}$

