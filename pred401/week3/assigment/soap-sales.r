soap <- read.csv("soap_sales.csv")

# 1) Execute summary(), stem(), histogram() and boxplot(). Observe the results.

summary(soap$sales)
hist(soap$sales)
stem(soap$sales)
boxplot(soap$sales)
100*sd(soap$sales)/mean(soap$sales)  # Compute percent CV.
# 2) Calculate and compare the 20% trimmed mean to the mean from summary().

mean(soap$sales)
mean(soap$sales, trim=.2)

# 3) Calculate the skewness and kurtosis, plot qqnorm(), qqline() and plot.ecdf(). Compare to the
# results of Parts 1 and 2.

sk <- skewness(soap$sales)
ku <- kurtosis(soap$sales)
sk
ku

qq <- qqnorm(soap$sales)
ql <- qqline(soap$sales)
plot(qq)
plot(ql)

mu <- mean(soap$sales)
std <- sd(soap$sales)
sales <- (soap$sales - mu)/std


normal <- rnorm(1000, mean = 0, sd = 1)
plot.ecdf(normal, xlab = "Standard Normal Variable x", main = "Comparison to Standard Normal")
plot.ecdf(sales, col = "blue", pch =2, add=TRUE)
abline(v = 0.0, lty = 2, col = "red")

# 4) Construct a six-cell relative frequency table with lower cell boundary starting at 10 and cell
# width of 5. Calculate the mean and standard deviation from the grouped data.

cells <- seq(from = 10, to =40, by = 5)
center <- seq(from = 12.5, to =40-2.5, by = 5)

sales <- soap$sales
buckets <- cut(sales, cells, include.lowest = TRUE, right=FALSE)
buckets <- prop.table(table(buckets))
df.buckets <- data.frame(buckets, center)

count <- df.buckets$Freq*length(soap$sales)
df.buckets <- data.frame(df.buckets, count)

hist(soap$sales, breaks=cells, main = "Frequency in Each Cell", right = FALSE)
lines(df.buckets$center, df.buckets$count, type = "b", col = "red")

mean <- sum(df.buckets$Freq*df.buckets$center)
mean
mean(soap$sales)

delta2 <- (df.buckets$center - mean)**2
std <- sqrt(sum(delta2*df.buckets$Freq))
std
