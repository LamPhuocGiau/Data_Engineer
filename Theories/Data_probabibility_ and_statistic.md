#   DATA PROBIBILITY AND STATISTIC
## Table of contents
- [Random variables](#Random-variables)
- [The binomial distribution](#The-binomial-distribution)
- [The normal distribution](#The-normal-distribution)
- [Source](https://www.mathsisfun.com/data/confidence-interval.html)

## Random variables

Random variable is possible values of random events. It is saved on capital letter (X,Y,...)to be sepecified algebra and probility. A Random Variable's set of values is the Sample Space.

<details>
<summary>Example tossing a coin:</summary>

we could get Heads or Tails.Let's give them the values Heads=0 and Tails=1 and we have a Random Variable "X":

X = random variable.

possible value = 0 or 1.

random event = Head or Tails.

X = {0, 1} = sample space

</details>

**Probability**.

P(X = value) = probability of that value.

<details>
<summary>Example two dice are tossed</summary>

The Random Variable is X = "The sum of the scores on the two dice".

1st Die : 1	2	3	4	5	6.

2nd Die	1	2	3	4	5	6	7.

Let's make a table of all possible values:

2	3	4	5	6	7	8
3	4	5	6	7	8	9
4	5	6	7	8	9	10
5	6	7	8	9	10	11
6	7	8	9	10	11	12

There are 6 × 6 = 36 possible outcomes, and the Sample Space (which is the sum of the scores on the two dice) is {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.

Let's count how often each value occurs, and work out the probabilities:

2 occurs just once, so P(X = 2) = 1/36.

3 occurs twice, so P(X = 3) = 2/36 = 1/18.

4 occurs three times, so P(X = 4) = 3/36 = 1/12.

5 occurs four times, so P(X = 5) = 4/36 = 1/9.

6 occurs five times, so P(X = 6) = 5/36.

7 occurs six times, so P(X = 7) = 6/36 = 1/6.

8 occurs five times, so P(X = 8) = 5/36.

9 occurs four times, so P(X = 9) = 4/36 = 1/9.

10 occurs three times, so P(X = 10) = 3/36 = 1/12.

11 occurs twice, so P(X = 11) = 2/36 = 1/18.

12 occurs just once, so P(X = 12) = 1/36.

</details>

**A Range of Values**.

<details>
<summary>Example: What is the probability that the sum of the scores is 5, 6, 7 or 8?</summary>

In other words: What is P(5 ≤ X ≤ 8)?.

P(5 ≤ X ≤ 8) = P(X=5) + P(X=6) + P(X=7) + P(X=8).

             = (4+5+6+5)/36.

             = 20/36.

             = 5/9.

</details>

**Solving**

<details>
<summary>Example: If P(X=x) = 1/12, what is the value of x?</summary>

P(X=4) = 1/12, and P(X=10) = 1/12.

So there are two solutions: x = 4 or x = 10.

Notice the different uses of X and x:

X is the Random Variable "The sum of the scores on the two dice".

x is a value that X can take.

</details>

**Uniform distribution**

It has equal probability for all values of the Random variable between a and b.

uniform distribution p=1/(b-a).

The probability of any value between a and b is p.

We also know that p = 1/(b-a), because the total of all probabilities must be 1, sothe area of the rectangle = 1.

p × (b−a) = 1.

p = 1/(b−a).

**Cumulative uniform distribution**.

We can have the Uniform Distribution as a cumulative (adding up as it goes along) distribution. The probability starts at 0 and builds up to 1. This type of thing is called a "Cumulative distribution function", often shortened to "CDF".

**Mean of random variables**.

```
μ = Σxp
```
<details>
<summary>Example</summary>
x  	  1  	  2  	  3  	  4  	  5  	  6.

p	0.1	0.1	0.1	0.1	0.1	0.5.

xp	0.1	0.2	0.3	0.4	0.5	3.

μ = Σxp = 0.1+0.2+0.3+0.4+0.5+3 = 4.5.

The expected value is 4.5.

</details>

**Variance**.

```
Var(X) = Σx**2p − μ**2
```
<details>
<summary>Example</summary>
x  	  1  	  2  	  3  	  4  	  5  	  6.

p	0.1	0.1	0.1	0.1	0.1	0.5.

x2p	0.1	0.4	0.9	1.6	2.5	18.

Σx2p = 0.1+0.4+0.9+1.6+2.5+18 = 23.5.

Var(X) = Σx\*\*2p − μ\*\*2 = 23.5 - 4.52 = 3.25.

The variance is 3.25.

</details>

**Standard Deviation: σ**.

The Standard Deviation is the square root of the Variance.

```
σ = √Var(X)
```
<details>

<summary>Example</summary>

x  	  1  	  2  	  3  	  4  	  5  	  6.

p	0.1	0.1	0.1	0.1	0.1	0.5.

x2p	0.1	0.4	0.9	1.6	2.5	18.

σ = √Var(X) = √3.25 = 1.803.

The Standard Deviation is 1.803.

</details>

## The binomial distribution

**Number of outcomes**.

Pascal's Triangle formula is used. It is called "n choose k". n = total number and k = Number we want.

![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Theories/Images/pascal_triangle.png)

<details>

<summary>Example</summary>

Example: with 3 tosses, what are the chances of 2 Heads?

We have n=3 and k=2:

n!/k!(n-k)! = 3!/2!(3-2)! = (3×2×1)/(2×1 × 1) = 3.

So there are 3 outcomes that have "2 Heads".

</details>

**Probability of each outcome**.

```
= p^k * (1-p)^(n-k)
```
p is the probability of each choice we want.

k is the the number of choices we want.

n is the total number of choices.

**The General Binomial Probability Formula**.

Probability of k out of n ways:

```
P(k out of n) = (n!/ k!(n-k)!) * p^k * (1-p)^(n-k)
```
<details>
<summary>Example</summary>

Example: Sam says "70% choose chicken, so 7 of the next 10 customers should choose chicken" ... what are the chances Sam is right?. So we have:

p = 0.7.

n = 10.

k = 7.

And we get:

p^k * (1-p)^(n-k) =0.7^7 * (1-0.7)^(10-7) =0.7^7 * (0.3)^(3) =0.0022235661.

That is the probability of each outcome.

And the total number of those outcomes is:

(n!) / (k!(n-k)!) = (10!) / (7!(10-7)!) = (10×9×8×7×6×5×4×3×2×1) / (7×6×5×4×3×2×1 × 3×2×1) = (10×9×8)/(3×2×1) =120.

And we get:

Number of outcomes we want	   	Probability ofeach outcome	 	 
            120	  ×  	                0.0022235661	  =  	0.266827932.
 
So the probability of 7 out of 10 choosing chicken is only about 27%.

Moral of the story: even though the long-run average is 70%, don't expect 7 out of the next 10.

</details>

**Mean**.

```
μ = np
```
**Variance**.

```
Variance: σ^2 = np(1-p)
```
**Standard Deviation**.

```
σ = √(np(1-p))
```
## The normal distribution

The Normal Distribution has:

mean = median = mode.

symmetry about the center.

50% of values less than the mean and 50% greater than the mean.

![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Theories/Images/normal_distribution.svg)

