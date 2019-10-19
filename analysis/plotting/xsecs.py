'''
Welcome to xsecs.py

Here we have configure_xsecs()
It returns a dictionary of cross-sections d_xsec 
so a common set is used for normalisation of samples. 
Cross-section is in pb.

For some samples the cross-section is multiplied by a k-factor, for signal samples the k-factors are taken from https://arxiv.org/pdf/1903.08137.pdf 
beyond kappa lambda we extrapolate by assuming flat i.e. use 1.95 k-factor for lambdas below -5, and use k-factor 2.10 for lambdas above 12

'''

#____________________________________________________________________________
def configure_xsecs():
  d_xsecs = {
             'loose_noGenFilt_wh': (1.3607),
             'loose_noGenFilt_zh': (0.71930),
             'loose_noGenFilt_zz': (11.532),
             'loose_noGenFilt_bbh': (0.07640),
             'loose_noGenFilt_tth': (0.43542),
             'loose_noGenFilt_ttbb': (2.7053),
             'loose_noGenFilt_ttbar': (532.64),
             'loose_ptj1_1000_to_infty_4b': (0.00055),
             'loose_ptj1_500_to_1000_4b': (0.04227),
             'loose_ptj1_200_to_500_4b': (2.8203),
             'loose_ptj1_20_to_200_4b': (65.302),
             'loose_ptj1_1000_to_infty_2b2j': (0.72362),
             'loose_ptj1_500_to_1000_2b2j': (35.262),
             'loose_ptj1_200_to_500_2b2j': (1538.8),
             'loose_ptj1_20_to_200_2b2j': (22659.0),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m20.0' : (0.51342*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m10.0' : (0.1438*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m7.0'  : (0.077355*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m5.0'  : (0.044446*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m3.0'  : (0.020674*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m2.0'  : (0.012206*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m1.0'  : (0.0060154*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_m0.5'  : (0.0037762*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_0.5'   : (0.0010049*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_1.0'   : (0.00047415*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_2.0'   : (0.0011231*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_3.0'   : (0.0040518*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_5.0'   : (0.016746*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_7.0'   : (0.038557*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_10.0'  : (0.088394*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_0.5_SlfCoup_20.0'  : (0.40269*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m20.0' : (1.4078*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m10.0' : (0.41912*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m7.0'  : (0.23617*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m5.0'  : (0.14345*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m3.0'  : (0.074079*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m2.0'  : (0.048166*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m1.0'  : (0.028062*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_m0.5'  : (0.020193*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_0.5'   : (0.0088491*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_1.0'   : (0.0053661*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_2.0'   : (0.0027707*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_3.0'   : (0.0060114*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_5.0'   : (0.029995*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_7.0'   : (0.077325*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_10.0'  : (0.19209*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_0.8_SlfCoup_20.0'  : (0.95416*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m10.0' : (0.55292*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m7.0'  : (0.3161*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m5.0'  : (0.19517*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m3.0'  : (0.10379*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m2.0'  : (0.069191*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m1.0'  : (0.041957*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_m0.5'  : (0.031105*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_0.5'   : (0.01494*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_1.0'   : (0.0096347*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_2.0'   : (0.0045515*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_3.0'   : (0.0068599*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_5.0'   : (0.033622*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_7.0'   : (0.089949*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_10.0'  : (0.22978*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_0.9_SlfCoup_20.0'  : (1.1762*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m20.0' : (2.3008*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m15.0' : (1.3919*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m10.0' : (0.71114*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m9.0'  : (0.60241*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m8.0'  : (0.50274*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m7.0'  : (0.41211*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m6.0'  : (0.33079*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m5.0'  : (0.25842*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m4.0'  : (0.19529*1.94),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m3.0'  : (0.14117*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m2.0'  : (0.096246*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m1.5'  : (0.07717*1.87),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m1.0'  : (0.060419*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_m0.5'  : (0.04591*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_0.5'   : (0.023744*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_0.8'   : (0.018863*1.69),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_1.0'   : (0.016078*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_1.2'   : (0.013651*1.62),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_1.5'   : (0.010691*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_2.0'   : (0.0075864*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_3.0'   : (0.0082156*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_4.0'   : (0.01797*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_5.0'   : (0.036819*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_6.0'   : (0.064829*2.14),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_7.0'   : (0.10192*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_8.0'   : (0.14813*2.12),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_9.0'   : (0.2035*2.11),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_10.0'  : (0.26794*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_15.0'  : (0.72691*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.0_SlfCoup_20.0'  : (1.4143*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m20.0' : (2.8461*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m10.0' : (0.89591*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m7.0'  : (0.52603*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m5.0'  : (0.33467*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m3.0'  : (0.18749*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m2.0'  : (0.1304*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m1.0'  : (0.084344*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_m0.5'  : (0.06546*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_0.5'   : (0.035942*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_1.0'   : (0.025329*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_2.0'   : (0.012381*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_3.0'   : (0.010459*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_5.0'   : (0.03971*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_7.0'   : (0.11313*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_10.0'  : (0.30598*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.1_SlfCoup_20.0'  : (1.6661*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m20.0' : (3.4621*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m10.0' : (1.1095*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m7.0'  : (0.65961*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m5.0'  : (0.42544*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m3.0'  : (0.24384*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m2.0'  : (0.17275*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m1.0'  : (0.11473*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_m0.5'  : (0.090659*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_0.5'   : (0.052327*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_1.0'   : (0.038111*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_2.0'   : (0.019517*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_3.0'   : (0.014026*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_5.0'   : (0.042466*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_7.0'   : (0.12343*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_10.0'  : (0.3433*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.2_SlfCoup_20.0'  : (1.9299*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m20.0' : (5.7703*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m10.0' : (1.9438*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m7.0'  : (1.1967*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m5.0'  : (0.80087*1.95),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m3.0'  : (0.48725*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m2.0'  : (0.3612*1.89),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m1.0'  : (0.25562*1.85),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_m0.5'  : (0.21048*1.82),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_0.5'   : (0.13571*1.73),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_1.0'   : (0.10598*1.66),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_2.0'   : (0.061942*1.58),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_3.0'   : (0.038406*1.92),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_5.0'   : (0.052931*2.15),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_7.0'   : (0.14951*2.13),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_10.0'  : (0.44814*2.10),
             'loose_noGenFilt_signal_hh_TopYuk_1.5_SlfCoup_20.0'  : (2.7778*2.10), 
            }
  return d_xsecs 
