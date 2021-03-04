library(tidyverse)


#' Title
#'
#' @param data_frame 
#' @param group_key 
#' @param lag_timestamp 
#'
#' @return
#' @export
#'
#' @examples
make_lag_table <- function(data_frame, group_key, time_stamp){
  if(!lubridate::is.Date(time_stamp)){
    data_frame[,time_stamp] <- lubridate::ymd(data_frame[,time_stamp])
  }
  
  
  local_usedata <- data_frame
  local_usedata <- local_usedata %>% 
    dplyr::group_by({{group_key}}) %>%
    dplyr::mutate(lag_timestamp = dplyr::lag({{time_stamp}}),
                  intervals     = {{time_stamp}} - lag_timestamp) %>% 
    dplyr::ungroup() 
  
  return(local_usedata)
}