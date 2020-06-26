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
如图所示给出了Newton法的集和图性。要求出$f(x) = 0$d根，初始估计$x_0$是给定的，画出函数$f$在x_0的切线。切线朝着根的方向贴近函数向下到$x$轴


![Newton](https://github.com/rfhklwt/algorithm010/tree/master/Week03/Newton.png)

## Mathematical formula `$y = x^2$`
Math block: