# vocabulary
V <- c("goal","tutor","variance","speed","drink","defence","performance","field","type")
# labels for training (sport or data science)
lables <- c("s","s","s","s","s","s","d","d","d","d","d")

# The past examples, the first 6 are sport the remaining are data science.
M <- matrix(c(1,0,0,0,1,1,1,1,
              0,0,1,0,1,1,0,0,
              0,1,0,1,0,1,1,0,
              1,0,0,1,0,1,0,1,
              1,0,0,0,1,0,1,1,
              0,0,1,1,0,0,1,1,
              0,1,1,0,0,0,1,0,
              1,1,0,1,0,0,1,1,
              0,1,1,0,0,1,0,0,
              0,0,0,0,0,0,0,0,
              0,0,1,0,1,0,1,0), nrow=11, ncol=8, byrow=TRUE)


m <- length(M_row_lables)
n <- length(M[1,])

sports <- M[1:6,]
data <- M[7:11,]

sports_word_counts <- c()
data_word_counts <- c()

for (i in 1:length(sports[1,])) { 
  sports_word_counts[i] = sum(sports[,i])
}

for (i in 1:length(data[1,])) { 
  data_word_counts[i] = sum(data[,i])
}

sports_word_counts
data_word_counts

sports_likelihood = sports_word_counts/6
data_likelihood = data_word_counts/5

sports_likelihood
data_likelihood

# New examples to classify
b1 <- c(1,0,0,1,1,1,0,1)
b2 <- c(0,1,1,0,1,0,1,0)

s <- (b1*sports_likelihood)+((1-b1)*(1-sports_likelihood))
d <- (b1*data_likelihood)+((1-b1)*(1-data_likelihood))
likelihood_s <- prod(s)*(6/11)
likelihood_d <- prod(d)*(5/11)

if (likelihood_s > likelihood_d) { 
  print("Classify as Sport")
} else {
    print("Classify as Data")
  }
