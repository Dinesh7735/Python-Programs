class UserMainCode(object):
    @classmethod
    def theMismatch(cls, input1, input2):
        """
        input1 : int (Length of the string N)
        input2 : string (The binary string S)
        
        Expected return type : int
        """
        
        mismatch_count = 0
        
        
        for i in range(input1 // 2):
            
            if input2[i] != input2[input1 - 1 - i]:
                mismatch_count += 1
        
        return mismatch_count
