#!/usr/bin/env python
'''

Welcome to combine_chiSq.py

 - This script takes in the csv files made by ntuples_to_chiSq.py.
 - Once the signal regions are specified, the script combines the chiSqs from their corresponding files.
 - Currently combines by evaluating the sum and maximum of the given chiSqSyst1pc
 - Outputs a single csv file containing the combined chiSq values
'''

# So Root ignores command line inputs so we can use argparse
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from ROOT import *
import os, sys, time, argparse, math, datetime, csv
from pprint import pprint
import pandas as pd


#____________________________________________________________________________
def main():
  
  t0 = time.time()

  print('\nCombine chi squares script\n')
  
  # ------------------------------------------------------
  # Input dir
  my_dir = 'loose_preselection' 
  #
  # ------------------------------------------------------
  #
  # Column header whose value we want to combine
  #
  l_to_sum_vars = ['chiSq', 'chiSqSyst0p3pc']#, 'chiSqSyst1pc']
 
  d_SR_sets = {
    # Inclusive baseline 
    'SR'        : ['SR-res',
                   'SR-int',
                   'SR-bst'],

    # Multibin baseline (no DNN)
    'SR_res_multibin' : [
                'SR-res-200mHH250',
                'SR-res-250mHH300',
                'SR-res-300mHH350',
                'SR-res-350mHH400',
                'SR-res-400mHH500',
                'SR-res-500mHH',
    ],
                
    'SR_int_multibin' : [
                'SR-int-200mHH400',
                'SR-int-400mHH600',
                'SR-int-600mHH',
    ],
                
    'SR_bst_multibin' : [
                'SR-bst-500mHH700',
                'SR-bst-700mHH900',
                'SR-bst-900mHH',
               ],

    'SR_all_multibin' : [
                'SR-res-200mHH250',
                'SR-res-250mHH300',
                'SR-res-300mHH350',
                'SR-res-350mHH400',
                'SR-res-400mHH500',
                'SR-res-500mHH',
                
                'SR-int-200mHH400',
                'SR-int-400mHH600',
                'SR-int-600mHH',
                
                'SR-bst-500mHH700',
                'SR-bst-700mHH900',
                'SR-bst-900mHH',
               ],
                
    # Multibin baseline with DNN cut trained on k(lambda)=1
    'SRNN_res_multibin_lam1' : [
                'SRNN-res-200mHH250-lam1',
                'SRNN-res-250mHH300-lam1',
                'SRNN-res-300mHH350-lam1',
                'SRNN-res-350mHH400-lam1',
                'SRNN-res-400mHH500-lam1',
                'SRNN-res-500mHH-lam1',
    ],
                
    'SRNN_int_multibin_lam1' : [
                'SRNN-int-200mHH400-lam1',
                'SRNN-int-400mHH600-lam1',
                'SRNN-int-600mHH-lam1',
    ],

    'SRNN_bst_multibin_lam1' : [
                'SRNN-bst-500mHH700-lam1',
                'SRNN-bst-700mHH900-lam1',
                'SRNN-bst-900mHH-lam1', 
                ],
    
    
    'SRNN_all_multibin_lam1' : [
                'SRNN-res-200mHH250-lam1',
                'SRNN-res-250mHH300-lam1',
                'SRNN-res-300mHH350-lam1',
                'SRNN-res-350mHH400-lam1',
                'SRNN-res-400mHH500-lam1',
                'SRNN-res-500mHH-lam1',

                'SRNN-int-200mHH400-lam1',
                'SRNN-int-400mHH600-lam1',
                'SRNN-int-600mHH-lam1',

                'SRNN-bst-500mHH700-lam1',
                'SRNN-bst-700mHH900-lam1',
                'SRNN-bst-900mHH-lam1', 
                ],

    # Multibin baseline with DNN cut trained on k(lambda)=5
    'SRNN_res_multibin_lam5' : [
                'SRNN-res-200mHH250-lam5',
                'SRNN-res-250mHH300-lam5',
                'SRNN-res-300mHH350-lam5',
                'SRNN-res-350mHH400-lam5',
                'SRNN-res-400mHH500-lam5',
                'SRNN-res-500mHH-lam5',
    ],
                
    'SRNN_int_multibin_lam5' : [
                'SRNN-int-200mHH400-lam5',
                'SRNN-int-400mHH600-lam5',
                'SRNN-int-600mHH-lam5',
    ],

    'SRNN_bst_multibin_lam5' : [
                'SRNN-bst-500mHH700-lam5',
                'SRNN-bst-700mHH900-lam5',
                'SRNN-bst-900mHH-lam5', 
                ],
    
    
    'SRNN_all_multibin_lam5' : [
                'SRNN-res-200mHH250-lam5',
                'SRNN-res-250mHH300-lam5',
                'SRNN-res-300mHH350-lam5',
                'SRNN-res-350mHH400-lam5',
                'SRNN-res-400mHH500-lam5',
                'SRNN-res-500mHH-lam5',

                'SRNN-int-200mHH400-lam5',
                'SRNN-int-400mHH600-lam5',
                'SRNN-int-600mHH-lam5',

                'SRNN-bst-500mHH700-lam5',
                'SRNN-bst-700mHH900-lam5',
                'SRNN-bst-900mHH-lam5', 
                ],

    # Multibin baseline with DNN cut trained on k(lambda)=10
    'SRNN_res_multibin_lam10' : [
                'SRNN-res-200mHH250-lam10',
                'SRNN-res-250mHH300-lam10',
                'SRNN-res-300mHH350-lam10',
                'SRNN-res-350mHH400-lam10',
                'SRNN-res-400mHH500-lam10',
                'SRNN-res-500mHH-lam10',
    ],
                
    'SRNN_int_multibin_lam10' : [
                'SRNN-int-200mHH400-lam10',
                'SRNN-int-400mHH600-lam10',
                'SRNN-int-600mHH-lam10',
    ],

    'SRNN_bst_multibin_lam10' : [
                'SRNN-bst-500mHH700-lam10',
                'SRNN-bst-700mHH900-lam10',
                'SRNN-bst-900mHH-lam10', 
                ],
    
    
    'SRNN_all_multibin_lam10' : [
                'SRNN-res-200mHH250-lam10',
                'SRNN-res-250mHH300-lam10',
                'SRNN-res-300mHH350-lam10',
                'SRNN-res-350mHH400-lam10',
                'SRNN-res-400mHH500-lam10',
                'SRNN-res-500mHH-lam10',

                'SRNN-int-200mHH400-lam10',
                'SRNN-int-400mHH600-lam10',
                'SRNN-int-600mHH-lam10',

                'SRNN-bst-500mHH700-lam10',
                'SRNN-bst-700mHH900-lam10',
                'SRNN-bst-900mHH-lam10', 
                ]
  }

  for SR_set in d_SR_sets:
    combine_set_of_SRs( SR_set, d_SR_sets, 'chiSq_ij_Sys0p3pc', my_dir, True )
    for var in l_to_sum_vars:    
      combine_set_of_SRs( SR_set, d_SR_sets, var, my_dir )
  
#____________________________________________________________________________
def combine_set_of_SRs(SR_set, d_SR_sets, to_sum_var, my_dir, do_2dlambda=False):
  
  # Join SRs as the combined name output
  if do_2dlambda:
    out_file = 'data/CHISQ_2Dlambda_{0}_{1}_combined_{2}.csv'.format(my_dir, SR_set, to_sum_var)
  else:
    #out_file = 'data/CHISQ_{0}_{1}_combined_{2}.csv'.format(my_dir, '_'.join(l_SRs), to_sum_var)
    out_file = 'data/CHISQ_{0}_{1}_combined_{2}.csv'.format(my_dir, SR_set, to_sum_var)

  #
  # Columns to delete in new dataframe 
  l_del = ['N_bkg','N_sig','N_sig_raw',
    'SoverB','SoverSqrtB','SoverSqrtBSyst1pc','SoverSqrtBSyst0p3pc',
    'chiSq','chiSqSyst1pc','chiSqSyst0p3pc','acceptance','xsec'] 
  
  # Get the list of SRs to combine
  l_SRs = d_SR_sets[SR_set]
  
  print('-----------------------------------\n')
  print('List of SRs to combine:')
  pprint(l_SRs)
  print('Variable to combine: {0}'.format(to_sum_var) ) 
  print('\n-----------------------------------\n')
  
  # ------------------------------------------------------
  # Import data files for each SR into pandas dataframe
  # ------------------------------------------------------
  d_df = {}
  for SR in l_SRs:
    print( 'Processing {0}'.format(SR) )
    
    # Input CSV file
    if do_2dlambda:
      in_file = 'data/CHISQ_2Dlambda_{0}_{1}.csv'.format(my_dir, SR)
    else:
      in_file = 'data/CHISQ_{0}_{1}.csv'.format(my_dir,SR)
    
    # Read in CSV as pandas dataframe (like an excel spreadsheet but python-able)
    d_df[SR] = pd.read_csv( in_file )
    #print(d_df[SR])

  # ------------------------------------------------------
  # Clone the first dataframe into a new dataframe
  # ------------------------------------------------------
  combo_df = d_df[l_SRs[0]].copy()

  if not do_2dlambda:
    for var in l_del:
      del combo_df[var]

  # ------------------------------------------------------
  # Import chiSq from other dataframes and add to combo_df
  # ------------------------------------------------------
  for SR in l_SRs:
    new_col_name = SR + '_' + to_sum_var
    combo_df[new_col_name] = d_df[SR][to_sum_var]

  # ------------------------------------------------------
  # List the columns we want to sum by header name
  # ------------------------------------------------------
  l_cols_to_combine = [SR + '_' + to_sum_var for SR in l_SRs]

  # ------------------------------------------------------
  # Perform the combination of the values as new column
  # ------------------------------------------------------
  combo_sum = 'sum_' + to_sum_var
  combo_max = 'max_' + to_sum_var
  # Sum the chiSqs
  combo_df[combo_sum] = combo_df[l_cols_to_combine].astype(float).sum(axis=1)
  # Find the maximum of the chiSqs
  combo_df[combo_max] = combo_df[l_cols_to_combine].astype(float).max(axis=1)

  # ------------------------------------------------------
  # Save new combined dataframe as 
  # ------------------------------------------------------
  #print(combo_df)
  print('Saving as: {0}'.format(out_file))
  combo_df.to_csv(out_file, float_format='%g', index=False)

if __name__ == "__main__":
  main()
