####数値の入ったベクトルを数値別で01をとる行列へ変換する関数．
library(tidyverse)

Wide <- function(vec){
  matA <- matrix(0, length(vec), max(vec,na.rm = TRUE))
  for(i in 1:ncol(matA)){
    matA[vec == i,i] <- 1
  }
  matB <- matA %>% data.frame
  return(matB)
}

# Test
X <- c(1,2,3,4,5,6,7,8,9,0,NA)
Wide(X)
