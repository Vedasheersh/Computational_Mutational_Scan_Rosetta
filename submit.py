import os
jobs = ['./work/417_A/417_A.job',
 './work/417_C/417_C.job',
 './work/417_D/417_D.job',
 './work/417_E/417_E.job',
 './work/417_F/417_F.job',
 './work/417_G/417_G.job',
 './work/417_H/417_H.job',
 './work/417_I/417_I.job',
 './work/417_K/417_K.job',
 './work/417_L/417_L.job',
 './work/417_M/417_M.job',
 './work/417_N/417_N.job',
 './work/417_P/417_P.job',
 './work/417_Q/417_Q.job',
 './work/417_R/417_R.job',
 './work/417_S/417_S.job',
 './work/417_T/417_T.job',
 './work/417_V/417_V.job',
 './work/417_W/417_W.job',
 './work/417_Y/417_Y.job',
 './work/439_A/439_A.job',
 './work/439_C/439_C.job',
 './work/439_D/439_D.job',
 './work/439_E/439_E.job',
 './work/439_F/439_F.job',
 './work/439_G/439_G.job',
 './work/439_H/439_H.job',
 './work/439_I/439_I.job',
 './work/439_K/439_K.job',
 './work/439_L/439_L.job',
 './work/439_M/439_M.job',
 './work/439_N/439_N.job',
 './work/439_P/439_P.job',
 './work/439_Q/439_Q.job',
 './work/439_R/439_R.job',
 './work/439_S/439_S.job',
 './work/439_T/439_T.job',
 './work/439_V/439_V.job',
 './work/439_W/439_W.job',
 './work/439_Y/439_Y.job',
 './work/446_A/446_A.job',
 './work/446_C/446_C.job',
 './work/446_D/446_D.job',
 './work/446_E/446_E.job',
 './work/446_F/446_F.job',
 './work/446_G/446_G.job',
 './work/446_H/446_H.job',
 './work/446_I/446_I.job',
 './work/446_K/446_K.job',
 './work/446_L/446_L.job',
 './work/446_M/446_M.job',
 './work/446_N/446_N.job',
 './work/446_P/446_P.job',
 './work/446_Q/446_Q.job',
 './work/446_R/446_R.job',
 './work/446_S/446_S.job',
 './work/446_T/446_T.job',
 './work/446_V/446_V.job',
 './work/446_W/446_W.job',
 './work/446_Y/446_Y.job',
 './work/449_A/449_A.job',
 './work/449_C/449_C.job',
 './work/449_D/449_D.job',
 './work/449_E/449_E.job',
 './work/449_F/449_F.job',
 './work/449_G/449_G.job',
 './work/449_H/449_H.job',
 './work/449_I/449_I.job',
 './work/449_K/449_K.job',
 './work/449_L/449_L.job',
 './work/449_M/449_M.job',
 './work/449_N/449_N.job',
 './work/449_P/449_P.job',
 './work/449_Q/449_Q.job',
 './work/449_R/449_R.job',
 './work/449_S/449_S.job',
 './work/449_T/449_T.job',
 './work/449_V/449_V.job',
 './work/449_W/449_W.job',
 './work/449_Y/449_Y.job',
 './work/453_A/453_A.job',
 './work/453_C/453_C.job',
 './work/453_D/453_D.job',
 './work/453_E/453_E.job',
 './work/453_F/453_F.job',
 './work/453_G/453_G.job',
 './work/453_H/453_H.job',
 './work/453_I/453_I.job',
 './work/453_K/453_K.job',
 './work/453_L/453_L.job',
 './work/453_M/453_M.job',
 './work/453_N/453_N.job',
 './work/453_P/453_P.job',
 './work/453_Q/453_Q.job',
 './work/453_R/453_R.job',
 './work/453_S/453_S.job',
 './work/453_T/453_T.job',
 './work/453_V/453_V.job',
 './work/453_W/453_W.job',
 './work/453_Y/453_Y.job',
 './work/455_A/455_A.job',
 './work/455_C/455_C.job',
 './work/455_D/455_D.job',
 './work/455_E/455_E.job',
 './work/455_F/455_F.job',
 './work/455_G/455_G.job',
 './work/455_H/455_H.job',
 './work/455_I/455_I.job',
 './work/455_K/455_K.job',
 './work/455_L/455_L.job',
 './work/455_M/455_M.job',
 './work/455_N/455_N.job',
 './work/455_P/455_P.job',
 './work/455_Q/455_Q.job',
 './work/455_R/455_R.job',
 './work/455_S/455_S.job',
 './work/455_T/455_T.job',
 './work/455_V/455_V.job',
 './work/455_W/455_W.job',
 './work/455_Y/455_Y.job',
 './work/456_A/456_A.job',
 './work/456_C/456_C.job',
 './work/456_D/456_D.job',
 './work/456_E/456_E.job',
 './work/456_F/456_F.job',
 './work/456_G/456_G.job',
 './work/456_H/456_H.job',
 './work/456_I/456_I.job',
 './work/456_K/456_K.job',
 './work/456_L/456_L.job',
 './work/456_M/456_M.job',
 './work/456_N/456_N.job',
 './work/456_P/456_P.job',
 './work/456_Q/456_Q.job',
 './work/456_R/456_R.job',
 './work/456_S/456_S.job',
 './work/456_T/456_T.job',
 './work/456_V/456_V.job',
 './work/456_W/456_W.job',
 './work/456_Y/456_Y.job',
 './work/475_A/475_A.job',
 './work/475_C/475_C.job',
 './work/475_D/475_D.job',
 './work/475_E/475_E.job',
 './work/475_F/475_F.job',
 './work/475_G/475_G.job',
 './work/475_H/475_H.job',
 './work/475_I/475_I.job',
 './work/475_K/475_K.job',
 './work/475_L/475_L.job',
 './work/475_M/475_M.job',
 './work/475_N/475_N.job',
 './work/475_P/475_P.job',
 './work/475_Q/475_Q.job',
 './work/475_R/475_R.job',
 './work/475_S/475_S.job',
 './work/475_T/475_T.job',
 './work/475_V/475_V.job',
 './work/475_W/475_W.job',
 './work/475_Y/475_Y.job',
 './work/486_A/486_A.job',
 './work/486_C/486_C.job',
 './work/486_D/486_D.job',
 './work/486_E/486_E.job',
 './work/486_F/486_F.job',
 './work/486_G/486_G.job',
 './work/486_H/486_H.job',
 './work/486_I/486_I.job',
 './work/486_K/486_K.job',
 './work/486_L/486_L.job',
 './work/486_M/486_M.job',
 './work/486_N/486_N.job',
 './work/486_P/486_P.job',
 './work/486_Q/486_Q.job',
 './work/486_R/486_R.job',
 './work/486_S/486_S.job',
 './work/486_T/486_T.job',
 './work/486_V/486_V.job',
 './work/486_W/486_W.job',
 './work/486_Y/486_Y.job',
 './work/487_A/487_A.job',
 './work/487_C/487_C.job',
 './work/487_D/487_D.job',
 './work/487_E/487_E.job',
 './work/487_F/487_F.job',
 './work/487_G/487_G.job',
 './work/487_H/487_H.job',
 './work/487_I/487_I.job',
 './work/487_K/487_K.job',
 './work/487_L/487_L.job',
 './work/487_M/487_M.job',
 './work/487_N/487_N.job',
 './work/487_P/487_P.job',
 './work/487_Q/487_Q.job',
 './work/487_R/487_R.job',
 './work/487_S/487_S.job',
 './work/487_T/487_T.job',
 './work/487_V/487_V.job',
 './work/487_W/487_W.job',
 './work/487_Y/487_Y.job',
 './work/489_A/489_A.job',
 './work/489_C/489_C.job',
 './work/489_D/489_D.job',
 './work/489_E/489_E.job',
 './work/489_F/489_F.job',
 './work/489_G/489_G.job',
 './work/489_H/489_H.job',
 './work/489_I/489_I.job',
 './work/489_K/489_K.job',
 './work/489_L/489_L.job',
 './work/489_M/489_M.job',
 './work/489_N/489_N.job',
 './work/489_P/489_P.job',
 './work/489_Q/489_Q.job',
 './work/489_R/489_R.job',
 './work/489_S/489_S.job',
 './work/489_T/489_T.job',
 './work/489_V/489_V.job',
 './work/489_W/489_W.job',
 './work/489_Y/489_Y.job',
 './work/493_A/493_A.job',
 './work/493_C/493_C.job',
 './work/493_D/493_D.job',
 './work/493_E/493_E.job',
 './work/493_F/493_F.job',
 './work/493_G/493_G.job',
 './work/493_H/493_H.job',
 './work/493_I/493_I.job',
 './work/493_K/493_K.job',
 './work/493_L/493_L.job',
 './work/493_M/493_M.job',
 './work/493_N/493_N.job',
 './work/493_P/493_P.job',
 './work/493_Q/493_Q.job',
 './work/493_R/493_R.job',
 './work/493_S/493_S.job',
 './work/493_T/493_T.job',
 './work/493_V/493_V.job',
 './work/493_W/493_W.job',
 './work/493_Y/493_Y.job',
 './work/496_A/496_A.job',
 './work/496_C/496_C.job',
 './work/496_D/496_D.job',
 './work/496_E/496_E.job',
 './work/496_F/496_F.job',
 './work/496_G/496_G.job',
 './work/496_H/496_H.job',
 './work/496_I/496_I.job',
 './work/496_K/496_K.job',
 './work/496_L/496_L.job',
 './work/496_M/496_M.job',
 './work/496_N/496_N.job',
 './work/496_P/496_P.job',
 './work/496_Q/496_Q.job',
 './work/496_R/496_R.job',
 './work/496_S/496_S.job',
 './work/496_T/496_T.job',
 './work/496_V/496_V.job',
 './work/496_W/496_W.job',
 './work/496_Y/496_Y.job',
 './work/498_A/498_A.job',
 './work/498_C/498_C.job',
 './work/498_D/498_D.job',
 './work/498_E/498_E.job',
 './work/498_F/498_F.job',
 './work/498_G/498_G.job',
 './work/498_H/498_H.job',
 './work/498_I/498_I.job',
 './work/498_K/498_K.job',
 './work/498_L/498_L.job',
 './work/498_M/498_M.job',
 './work/498_N/498_N.job',
 './work/498_P/498_P.job',
 './work/498_Q/498_Q.job',
 './work/498_R/498_R.job',
 './work/498_S/498_S.job',
 './work/498_T/498_T.job',
 './work/498_V/498_V.job',
 './work/498_W/498_W.job',
 './work/498_Y/498_Y.job',
 './work/500_A/500_A.job',
 './work/500_C/500_C.job',
 './work/500_D/500_D.job',
 './work/500_E/500_E.job',
 './work/500_F/500_F.job',
 './work/500_G/500_G.job',
 './work/500_H/500_H.job',
 './work/500_I/500_I.job',
 './work/500_K/500_K.job',
 './work/500_L/500_L.job',
 './work/500_M/500_M.job',
 './work/500_N/500_N.job',
 './work/500_P/500_P.job',
 './work/500_Q/500_Q.job',
 './work/500_R/500_R.job',
 './work/500_S/500_S.job',
 './work/500_T/500_T.job',
 './work/500_V/500_V.job',
 './work/500_W/500_W.job',
 './work/500_Y/500_Y.job',
 './work/501_A/501_A.job',
 './work/501_C/501_C.job',
 './work/501_D/501_D.job',
 './work/501_E/501_E.job',
 './work/501_F/501_F.job',
 './work/501_G/501_G.job',
 './work/501_H/501_H.job',
 './work/501_I/501_I.job',
 './work/501_K/501_K.job',
 './work/501_L/501_L.job',
 './work/501_M/501_M.job',
 './work/501_N/501_N.job',
 './work/501_P/501_P.job',
 './work/501_Q/501_Q.job',
 './work/501_R/501_R.job',
 './work/501_S/501_S.job',
 './work/501_T/501_T.job',
 './work/501_V/501_V.job',
 './work/501_W/501_W.job',
 './work/501_Y/501_Y.job',
 './work/502_A/502_A.job',
 './work/502_C/502_C.job',
 './work/502_D/502_D.job',
 './work/502_E/502_E.job',
 './work/502_F/502_F.job',
 './work/502_G/502_G.job',
 './work/502_H/502_H.job',
 './work/502_I/502_I.job',
 './work/502_K/502_K.job',
 './work/502_L/502_L.job',
 './work/502_M/502_M.job',
 './work/502_N/502_N.job',
 './work/502_P/502_P.job',
 './work/502_Q/502_Q.job',
 './work/502_R/502_R.job',
 './work/502_S/502_S.job',
 './work/502_T/502_T.job',
 './work/502_V/502_V.job',
 './work/502_W/502_W.job',
 './work/502_Y/502_Y.job',
 './work/503_A/503_A.job',
 './work/503_C/503_C.job',
 './work/503_D/503_D.job',
 './work/503_E/503_E.job',
 './work/503_F/503_F.job',
 './work/503_G/503_G.job',
 './work/503_H/503_H.job',
 './work/503_I/503_I.job',
 './work/503_K/503_K.job',
 './work/503_L/503_L.job',
 './work/503_M/503_M.job',
 './work/503_N/503_N.job',
 './work/503_P/503_P.job',
 './work/503_Q/503_Q.job',
 './work/503_R/503_R.job',
 './work/503_S/503_S.job',
 './work/503_T/503_T.job',
 './work/503_V/503_V.job',
 './work/503_W/503_W.job',
 './work/503_Y/503_Y.job',
 './work/505_A/505_A.job',
 './work/505_C/505_C.job',
 './work/505_D/505_D.job',
 './work/505_E/505_E.job',
 './work/505_F/505_F.job',
 './work/505_G/505_G.job',
 './work/505_H/505_H.job',
 './work/505_I/505_I.job',
 './work/505_K/505_K.job',
 './work/505_L/505_L.job',
 './work/505_M/505_M.job',
 './work/505_N/505_N.job',
 './work/505_P/505_P.job',
 './work/505_Q/505_Q.job',
 './work/505_R/505_R.job',
 './work/505_S/505_S.job',
 './work/505_T/505_T.job',
 './work/505_V/505_V.job',
 './work/505_W/505_W.job',
 './work/505_Y/505_Y.job']

MAIN_DIR = os.getcwd()
for job in jobs:
    dir = job[:13]
    file = job[13:]
    print(dir,file)
    os.system('chdir '+dir)
    os.system('qsub '+file)
    os.chdir(MAIN_DIR)
    break