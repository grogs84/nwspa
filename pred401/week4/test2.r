#################################################################################
# 1
#
# Find the indicated probability.
#
# In a homicide case 4 different witnesses picked the same man from a line up. 
# The line up contained 5 men. If the identifications were made by random guesses, 
# find the probability that all 4 witnesses would pick the same person
#################################################################################

n <- 4
x <- 4
p <-.2 #probability of success
q <- 1-p #probability of failure

# the probability of all four witnesses choosing 1 of the suspects 
choose(n,x)*(p^x)*q^(n-x)

# there are 5 suspects so the probability of all four choosing 1 of the set of 5 is:
5*choose(n,x)*(p^x)*q^(n-x)
5*dbinom(4,4,.2)




set.seed(4695)
x=seq(1:5)
count=0
trials=100000
for (i in 1:trials){
  
  sample= sample(x,4,replace=TRUE)
  if( length(unique(sample))==1)
    count=count+1
}
prob=count/trials
prob



#################################################################################
# 2
#
# Find the indicated probability.
# A IRS auditor randomly selects 3 tax returns from 49 returns of 
# which 7 contain errors. What is the probability that she selects none of 
# those containing errors? Round to four decimal places.
#
#################################################################################

x <- 0 # zero errors
f <- 7 # 7 documents have errors
s <- (49-7) # 42 of the 49 documents are correct
n <- 3 # sample 3 WITHOUT replacement

dhyper(x,f,s,n)

x <- seq(1:49)
cnt <- 0
trials <-1000000
for (i in 1:trials){
  s <- sample(x,3,replace=FALSE)
  if (sum(s>7)==3) {
    cnt=cnt+1
  }
  
}

prob=cnt/trials
prob

############################################################################### 
# 3
#
# Use Bayes' theorem to find the indicated probability.
# 
# 3.8% of a population are infected with a certain disease. 
# There is a test for the disease, however the test is not completely accurate. 
# 93.9% of those who have the disease test positive. 
# However 4.1% of those who do not have the disease also test positive (false positives). 
# A person is randomly selected and tested for the disease.
# 
# What is the probability that the person has the disease given that the test result is positive
##############################################################################################


pop_prob <- 0.038
true_pos <- .939
false_pos <- .041

# P(A|B) = P(A&B)/P(B)

prob <- (pop_prob*true_pos) / ((pop_prob*true_pos)+((1-pop_prob)*false_pos))
prob

# ############################################################################################
# 4
# 
# Find the indicated z score. 
# The graph depicts the standard normal distribution with mean 0 and standard deviation 1.
# 
# Shaded area is 0.4013.
# ##############################################################################################

# Standard normal the mean, meadian, mode all are .5. Any value above or below that will tell you
# the percitle. We can use qnorm on .4013 to find the associated z-score

qnorm(.4013) #.2499999

#################################################################################################
# 5
# 
# Solve the problem.
# 
# A study of the amount of time it takes a mechanic to rebuild the transmission for a 2005 
# Chevrolet Cavalier shows that the mean is 8.4 hours and the standard deviation is 1.8 hours. 
# If 40 mechanics are randomly selected, find the probability that their mean rebuild time exceeds 8.7 hours.
###################################################################################################

u <- 8.4  # population mean
X <- 8.7  # sample mean
sd <- 1.8 # standard deviation
n <- 40
# to find the probability of the sample mean exceeds 8.7 find the z-score to calculate the area under
# the curve to the right of that score eg 1-pnorm(z)

z <- (X-u)/(sd/sqrt(40))
1-pnorm(z)


# 6

##########################################################################################################
# 7
#
# Solve the problem. Round to the nearest tenth unless indicated otherwise.
# 
# In one region, the September energy consumption levels for single-family homes 
# are found to be normally distributed with a mean of 1050 kWh and a standard deviation of 218 kWh. 
# Find P45, the 45th percentile of the distribution.
###########################################################################################################


# use qnorm function

qnorm(.45,1050,218)
