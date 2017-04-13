"""
    p0 --> Probability of Disease
    p1 --> Sensitivity of the Test (Getting Test = Positive, When having the disease)
    p2 --> Specificity of the Test (Getting Test = Negative, When being disease-free)
    
"""

def bayes_rule_disease(p0, p1, p2):
    
    print("\nThere is a disease that affects only ", p0 * 100, " % of the population.")
    print("\nThere is a Test that detects the possibility of having that disease.")
    print("\n\nBut this Test has some error-rates associated with it:\n")
    print("\nSensitivity: ", p1 * 100, " % And")
    print("\nSpecificity: ", p2 * 100, " %")
    print("\nSuppose Someone takes this Test;\n\nSo,Chances of having that disease: ")

    prob_disease = p0
    prob_disease_free = 1 - p0 
    
    sense_pos = p1
    sense_neg = 1 - p1
    
    spec_neg = p2
    spec_pos = 1 - p2
    
    pos_joint_disease = prob_disease * sense_pos
    pos_joint_disease_free = prob_disease_free * spec_pos
    
    normalizer_pos = pos_joint_disease + pos_joint_disease_free
    
    pos = (pos_joint_disease / normalizer_pos)
    print("\n\nWhen, Test = Positive: ", pos * 100, " %")

    """
        You need not store values in variables, Following code will also work:
        
        pos = ((p0 * p1) / ((p0 * p1) + ((1 - p0) * (1 - p2))))
    
        But I think, This is Clumsy!!
    """
    
    neg_joint_disease = prob_disease * sense_neg
    neg_joint_disease_free = prob_disease_free * spec_neg
    
    normalizer_neg = neg_joint_disease + neg_joint_disease_free
    
    false_neg = (neg_joint_disease / normalizer_neg)
    print("\n\nWhen, Test = Negative: ", false_neg * 100, " %")
    
    """
        You again need not store values in variables:
        
        false_neg = ((p0 * (1 - p1)) / ((p0 * (1 - p1)) + ((1 - p0) * p2)))
    
        This is so Clumsy!!
    """
    
bayes_rule_disease(0.01, 0.9, 0.9)