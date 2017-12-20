library(data.table)

data <- fread("input.txt")
data[, names(data) := lapply(.SD, as.double)]

positions <- data[, c("px", "py", "pz")]
velocity <- data[, c("vx", "vy", "vz")]
acceleration <- data[, c("ax", "ay", "az")]

min_vecs <- rep(-1, 2000)
min_vecs[99] <- -2
index <- 1

while(length(unique(min_vecs)) != 1) {
  velocity <- velocity + acceleration
  positions <- positions + velocity
  
  min_dist <- which.min(positions[, abs(px) + abs(py) + abs(pz)])
  min_vecs[index] <- min_dist
  index <- (index + 1) %% 2001 
}

print(min_dist-1)

# part 2
positions <- data[, c("px", "py", "pz")]
velocity <- data[, c("vx", "vy", "vz")]
acceleration <- data[, c("ax", "ay", "az")]

lengths <- rep(-1, 2000)
lengths[99] <- -2
index <- 1

while(length(unique(lengths)) != 1) {
  velocity <- velocity + acceleration
  positions <- positions + velocity
  
  dups <- duplicated(positions) | duplicated(positions, fromLast=TRUE)
  acceleration <- acceleration[!dups]
  velocity <- velocity[!dups]
  positions <- positions[!dups]
    
  lengths[index] <- nrow(positions)
  index <- (index + 1) %% 2001 
}

print(nrow(positions))