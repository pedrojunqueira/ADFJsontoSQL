# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:08:28 2019

@author: pjunqueira

"""
#this is just a small change ;)

from pandas import Series, DataFrame
import pandas as pd

#DataTypeMapping ADF and SQL

SqlJsonMapping = {"Azure SQL Database data type":['bit',
                                                    'tinyint',
                                                    'binary',
                                                    'DateTime',
                                                    'Datetimeoffset',
                                                    'Decimal',
                                                    'Float',
                                                    'uniqueidentifier',
                                                    'smallint',
                                                    'int',
                                                    'bigint',
                                                    'sql_variant',
                                                    'real',
                                                    'nvarchar',
                                                    'time',
                                                    'xml',
                                                        ],
            "Data Factory interim data type":['Boolean',
                                                'Byte',
                                                'Byte[]',
                                                'DateTime',
                                                'DateTimeOffset',
                                                'Decimal',
                                                'Double',
                                                'Guid',
                                                'Int16',
                                                'Int32',
                                                'Int64',
                                                'Object',
                                                'Single',
                                                'String',
                                                'TimeSpan',
                                                'Xml',
                                                        ]
         }

        
#import ADFJsonFile for dataset

SqlJsonFrame= DataFrame(SqlJsonMapping)

adfdataset = pd.read_json(r'C:\Users\pjunqueira\Desktop\ADFDatasetfile.json')        

        
def jsontosql(adffile):
    tmpdict = adffile["properties"]["structure"]
    tmpframe = DataFrame(tmpdict)  
    tmpmergeleft = pd.merge(tmpframe,SqlJsonFrame, left_on='type',right_on='Data Factory interim data type', how='left')
    print('SET ANSI_NULLS ON \n GO \n SET QUOTED_IDENTIFIER ON \n GO \n CREATE TABLE [Schema][NameofTable] (')
    for i in tmpmergeleft.index :
        if tmpmergeleft['Azure SQL Database data type'][i] == 'nvarchar':
            print('[{}]'.format(tmpmergeleft['name'][i])+' [{}]'.format(tmpmergeleft['Azure SQL Database data type'][i])+' (50) NULL,')
        else:
            print('[{}]'.format(tmpmergeleft['name'][i])+' [{}]'.format(tmpmergeleft['Azure SQL Database data type'][i])+' NULL,')
    print(')')
        
        
# =============================================================================
# to run function 
# jsontosql(adfdataset)
# 
# =============================================================================


