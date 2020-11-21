mydata=read.csv("C:/Users/mtszb/Desktop/kraby.csv")
# Logistic Regression w R
# where y is a binary factor and satell poisson factor
# color spine width weight y n dark are continuous predictors
f <- glm(satell ~ weight+kolor+I(weight^2),data=mydata,family=poisson())
summary(f) # display results
confint(f) # 95% CI for the coefficients
exp(coef(f)) # exponentiated coefficients
exp(confint(f)) # 95% CI for exponentiated coefficients
predict(f, type="response") # predicted values
residuals(f, type="deviance") # residuals


