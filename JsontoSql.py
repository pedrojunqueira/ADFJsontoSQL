# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:41:09 2019

@author: pjunqueira
"""

      

        
        from pandas import Series, DataFrame
        import pandas as pd
        
        
        
        def jsontosql(adffile):
            strdict = adffile["properties"]["structure"]
            frame = DataFrame(strdict)
            
            for i in frame.index :
                print('[{}]'.format(frame['name'][i])+' [{}],'.format(frame['type'][i]))
        
        
        
        jsontosql(adfcode)
        
        
            