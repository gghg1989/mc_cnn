import math
import sys

def metric(TP, FN,FP,TN):
    if ((int(TP + FP))) == 0 or (int((FN + TN)) == 0 ) or (int((FP + TN)) ==0)or (int((TP + FN))==0) :
        pass
    else:
        metric = {}
        TP = int(TP)
        FN = int(FN)
        FP = int(FP)
        TN = int(TN)
        ACCURACY = float((TP + TN)/(TP + FP + FN + TN))
        PRECISION = float(TP/(TP + FP))
        RECALL = float(TP/(TP + FN))
        if ((PRECISION == 0) or (RECALL == 0)):
            pass
        else:
            F1 = float(2*PRECISION*RECALL/(PRECISION + RECALL))
            MCC = float((TP * TN - FP * FN)/ math.sqrt((TP + FP) * (FN + TN) * (FP + TN) * (TP + FN)))
            SPECIFICITY = float(TN/(TN + FP))
            metric['TP'] = float(TP/(TP + FN))
            metric['FN']  = float(FN /(TP + FN))
            metric['TN'] = float(TN /(TN + FP))
            metric['FP']  =float(FP /(TN + FP))
            metric['ACCURACY'] = ACCURACY
            metric['PRECISION'] =PRECISION
            metric['RECALL']= RECALL
            metric['F1'] = F1
            metric['MCC'] = MCC
            metric['Cohen_kappa'] = 2 * (TP * TN - FN * FP) / (TP * FN + TP * FP + 2 * TP * TN + FN^2 + FN * TN + FP^2 + FP * TN)
            metric['SPECIFICITY'] = SPECIFICITY
            return metric

def main(argv):
    TP = 111 
    TN = 19
    FP = 69 
    FN = 1
    current_metric = metric(TP,FN,FP,TN)
    print(TP, TN, FP, FN, current_metric)

if __name__ == "__main__":
    main(sys.argv[1:])




