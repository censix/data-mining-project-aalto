from math import log
class UtilityMethods:
    @staticmethod
    def InformationGain(patternSupport,labelSupport,patternLabelUnionSupport):
        return UtilityMethods.__InformationGainFormula(patternSupport,labelSupport,patternLabelUnionSupport/patternSupport)
    
    @staticmethod
    def InformationGainUpperBound(potentialSupport,labelSupport):
        
        upperBound = 0;
        
        if labelSupport >= potentialSupport:
            upperBound = UtilityMethods.__InformationGainFormula(potentialSupport,labelSupport,1)
        else:
            upperBound = UtilityMethods.__InformationGainFormula(potentialSupport,labelSupport,labelSupport/potentialSupport)
            
        return upperBound
    
    @staticmethod
    def __InformationGainFormula(o,p,q):
        #use binary conditional entropy formula from p.18 of HONG CHENG Thesis 
        conditionalProb_term1 = -o*q*(UtilityMethods.__Log2(q))-o*(1-q)*(UtilityMethods.__Log2(1-q))
        conditionalProb_term2 = (o*q-p)*(UtilityMethods.__Log2((p-o*q)/(1-o)))
        conditionalProb_term3 = (o*(1-q)-(1-p))*(UtilityMethods.__Log2(((1-p)-(o*(1-q)))/(1-o)))
        
        conditionalProb = conditionalProb_term1 + conditionalProb_term2 + conditionalProb_term3
        
        #use binary entropy formula to calculate entropy of the pattern
        #see http://en.wikipedia.org/wiki/Binary_entropy_function
        nonCondProb = -p*(UtilityMethods.__Log2(p))-(1-p)*(UtilityMethods.__Log2(1-p))
        
        #calculate and return information gain
        return (nonCondProb - conditionalProb)
    
    @staticmethod
    def __Log2(x):
        ans = 0
	if x != 0:
	    ans = log(x,2)
	return ans