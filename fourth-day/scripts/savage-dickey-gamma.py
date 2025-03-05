#!/usr/bin/python3

import sys
import pandas as pd
import scipy

def savage_dickey(cutoff, column, alpha, beta, mcmc_filename):
  
  # read the MCMC file for model 2 as a table
  data = pd.read_table(mcmc_filename)
  
  # posterior is the proportion of phi samples smaller than cutoff
  posterior = len(data.loc[data[column] < cutoff]) / len(data)
  
  # prior
  prior = scipy.stats.gamma.cdf(cutoff, alpha, scale=1/beta)

  # calculate bayes factor
  bf = prior / posterior 
  
  print("Prior: {}".format(prior))
  print("Posterior: {}".format(posterior))
  print("Bayes factor: {}".format(bf))

if __name__ == "__main__":
  if len(sys.argv) != 6:
    print(" usage: " + sys.argv[0] + " cutoff column gamma_prior_a gamma_prior_b mcmcfile")
    print(" example: " + sys.argv[0] + " 0.01 \"w_x<-w\" 1 1 mcmc.txt")
    sys.exit(0)

  cutoff = sys.argv[1]
  param = sys.argv[2]
  alpha = float(sys.argv[3])
  beta = float(sys.argv[4])
  mcmcfile = sys.argv[5]
  print("Cutoff: {}".format(cutoff))
  print("Prior: Gamma({},{})".format(alpha, beta))
  print("Parameter: {}".format(param))
  print("MCMC file: {}\n".format(mcmcfile))
  savage_dickey(float(sys.argv[1]), sys.argv[2], alpha, beta, mcmcfile)


