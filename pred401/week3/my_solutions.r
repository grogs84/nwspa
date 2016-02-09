
shoppers <- read.csv("../shoppers.csv")

# $40 or more
gte_forty <- sum(shoppers$Spending >=40)/length(shoppers$Spending)
gte_forty

# less than $10
lt_ten <- sum(shoppers$Spending < 10)/length(shoppers$Spending)
lt_ten

# prob of over $40 and <= $10 if two are picked:
A <- sum(shoppers$Spending >=40) * sum(shoppers$Spending < 10)
B <- choose(length(shoppers$Spending),2)
A/B

# If two shoppers are picked at random, what is the probability
# the pair will include two shoppers who spent no less than $10 and no more than $40?
A <- sum((shoppers$Spending>=10)*(shoppers$Spending<=40))
B <- choose(length(shoppers$Spending),2)
choose(A,2)/B

# If four shoppers are picked at random, what is the probability one shopper will have 
# spent less than $10, one shopper will have spent $40 or more dollars and two shoppers 
# will have spent no less than $10 and no more than $40?
A <- sum(shoppers$Spending < 10)
B <- sum(shoppers$Spending >= 40)
C <- sum((shoppers$Spending>=10)*(shoppers$Spending<=40))
D <- choose(C,2)

(A*B*D)/choose(50,4)

# 1) e) If we know a randomly picked shopper has spent more than $30, 
# what is the probability that shopper has spent more than $40?
# Let's try first reducing the set of shoppers to those spending more than $30

gt_30 <- shoppers$Spending[c(shoppers$Spending>30)]
sum(gt_30>40)/length(gt_30)

# 2) a) Draw 100 samples with replacement of size 22 from the 365 integers 
# (i.e. 1,2,...,365). Count the number of samples in which one or more 
# of the numbers sampled is duplicated. Divide by 100 to estimate the 
# probability of such duplication occurring.
set.seed(1234)
inc = 0
for (i in 1:100){
  s <- sample(1:365,22,replace=TRUE)
  t <- table(s)
  if (sum(t==1) < 22) inc = inc+ 1
}
inc/100

# (If 22 people are selected at random, what is the probability 
# of two or more matching birthdays?) This is known as the birthday problem,
# a classic problem in probability. We solved the problem using the method
# above with a for-loop. It can also be solved with one line of R code
# following our setting of the random number seed for reproducibility,
# so we can show that the two results are identical.
set.seed(1234)  # set random number seed for reproducibility

set.seed(1234)  # set random number seed for reproducibility
mean(replicate(100,any(duplicated(sample(1:365, 22, replace=TRUE)))))

# So, as it turns out, there is about a 50/50 chance of two people having
# the same birthday in a class of 22 students. Let's get a more precise estimate by increasing the number of iterations/replications
set.seed(1234)  # set random number seed for reproducibility
mean(replicate(10000,any(duplicated(sample(1:365, 22, replace=TRUE)))))


# 2) b) Suppose that 60% of marbles in a bag are black and 40% are white. 
# Generate a random sample of size 20 with replacement using uniform random numbers. 
# For the numbers in each sample, if a random number is 0.6 or less, code it as a 1. 
# If it is not 0.6 or less code it a zero. Add the twenty coded numbers. 
# Do this 50 times and calculate the proportion of times the sum is 11 or greater. 
# What have you estimated?

set.seed(1234)
sum(replicate(50,sum(runif(20)<=.6)>=11))/50


set.seed(1234)
k <- replicate(1000,sum(runif(20)<=.6))
