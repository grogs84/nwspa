
shoppers <- read.csv("shoppers.csv")

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
A <- sum(shoppers$Spending < 10)/length(shoppers$Spending)
B <- sum(shoppers$Spending >= 40)/length(shoppers$Spending)
C <- sum((shoppers$Spending>=10)*(shoppers$Spending<=40))
D <- choose(length(shoppers$Spending),2)
E <- choose(C,2)

(A*B*E)/choose(50,4)