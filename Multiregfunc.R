MultiReg <- function(ymat,xmat,Filename = NULL){
  result <- list(ncol(y))
  for(i in 1:ncol(ymat)){
    result[[i]] <- summary(lm(ymat[,i] ~ xmat))
  }
  print(list)
}
