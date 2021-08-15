

def BestScinence(g, p, pr, gr, s):
    spt = 4
    totals = 0
    turns = 0
    pop = 1
    foodsave = 0
    foodpt = 0
    m1 = 0
    m2 = 0
    m3 = 0
    mf1 = 0
    mf2 = 0
    
    while totals < 77568:
        foodpt = (((3*pop) * (1 + mf1)) - 2*(pop -1)) * (1 + mf2)
        foodsave += foodpt
        
        if foodsave >= (6*pop + 4):
            foodsave = foodsave - (6*pop + 4)
            pop +=1
            
        spt = (3 + pop) * (1 + m1 + m2 + m3) 
        
        # Library 
        if turns >= 55:
            spt += (pop/2) * (1 + m1 + m2 + m3)
            
        # NC
        if turns == 65:
            m1 = 0.5
            
        # Trad
        if turns == 65:
            mf1 = 0.15
            mf2 = 0.1
            
        # Uni
        if turns == 78:
            m2 = 0.33
            
        # Public School
        if turns >= 110:
            spt += (pop/2) * (1 + m1 + m2 + m3)
            
        # Lab
        if turns == 140:
            m3 = 0.5
        
        totals += spt
        turns += 1
        
    return turns


    
    
    

print(BestScinence(10, 12, 15, 12, 12))