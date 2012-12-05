import fp_growth

#Input: An FP-tree P, min sup s
#Output: A set of selected features Fs
#Procedure DDPMine(P; s)
#1: if P = empty
#2: return;
#3: a := branch and bound(P; s; null);
#4: if a = null
#5: return;
#6: Compute the transaction id list T(a) containing a;
#7: P0 := update tree(P; T(a));
#8: Fs := fg[ DDPMine(P0; s);
#9: return Fs;

def ddpmine(P,s) :
    
    a = branchAndBound(P,s,null)
    
    if a is None :
        return



#Procedure branch and bound(P; s; ?)
#1: if P = ?
#2: return;
#3: for each item ai in P do
#4: generate pattern ? = ai [ ? with support=ai.support;
#5: compute information gain IG(?);
#6: if IG(?) > maxIG
#7: maxIG := IG(?);
#8: bestP at := ?;
#9: construct pattern ?'s conditional database D?;
#10: IGub(jD?j) := upper bound(jD?j);
#11: if maxIG ? IGub(D?)
#12: skip mining on D?;
#13: else
#14: construct ?'s conditional FP-tree P?;
#15: branch and bound(P?; s; ?);
    
def branchAndBound(P,s,null) :
    