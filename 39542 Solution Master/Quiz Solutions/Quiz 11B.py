#11b:  capture variance with parameter

def capture(sv, threshold=.85):
    cv = (sv**2)/sum(sv**2)
    v = 0
    for i in range(len(sv)):
        v = v + cv[i]
        if v > threshold:
            return(i+1)
    return(i+1)
