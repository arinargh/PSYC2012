# -*- coding: utf-8 -*-
"""
@author: arina
"""

import pandas as pd

##### INPUT (cc: class code) #####

tut = 6
cc = None

#####

filepath = 'C:\\Users\\arina\\Desktop\\PSYC2012_2023\\attendance_lists\\by_tute\\'
df = pd.read_excel(filepath + 'psyc2012_attendancelist_tut{}.xlsx'.format(tut))
df_prev = pd.read_excel(filepath + 'psyc2012_attendancelist_tut{}.xlsx'.format(tut-1))

#####

def weekly_recap(filepath=filepath, df=df): 
    """Generate names of all enrolled students as per class list.
    All students will receive weekly recap slides, regardless of attendance status""" 
    
    if cc != None:
        df = df[ df.SHORT_CODE==cc ].copy()
    
    email = df['EMAIL_ADDRESS'].tolist()
    
    print("\nTotal: {}".format(len(email)))
    print("______________________\n")
    for i in email: 
        print("{},".format(i))
    print("______________________")
    
    return 0

#####

def slides_only(filepath=filepath, df=df, df_prev=df_prev):
    """Generate names of students who've attended the current week's tutorial, but not the previous week's.
    These students would only receive the tutorial slides.
    (Unless a valid reason was given for missed attendance - why notnull is used instead of attendance=yes)""" 
    
    # get df of students who attended previous tute and those who didn't attend current tute
    if cc != None: 
        df_a = df_prev[ (df_prev.ATTENDANCE.isnull()) & (df_prev.SHORT_CODE==cc) ].copy()
        df_b = df[ (df.ATTENDANCE.notnull()) & (df.SHORT_CODE==cc) ].copy()
    else:
        df_a = df_prev[ df_prev.ATTENDANCE.isnull() ].copy()
        df_b = df[ df.ATTENDANCE.notnull() ].copy()
    
    # get email list for slides only
    df_final = df_a.merge(df_b, how='inner', on=['STUDENT_CODE']).copy()
    email_final = df_final['EMAIL_ADDRESS_x'].tolist()
    
    print("\nMAILING LIST - SLIDES ONLY")
    print("Total: {}".format(len(email_final)))
    print("______________________\n")
    for i in email_final: 
        print("{},".format(i))
    print("______________________") 
    
    return 0

#####

def quiz_only(filepath=filepath, df=df, df_prev=df_prev): 
    """Generate names of students who've attended the previous week's tutorial, but not the current week's.
    These students would only receive an explanation of quiz answers."""
        
    # get df of students who attended previous tute and those who didn't attend current tute
    if cc != None: 
        df_a = df_prev[ (df_prev.ATTENDANCE.notnull()) & (df_prev.SHORT_CODE==cc) ].copy()
        df_b = df[ (df.ATTENDANCE.isnull()) & (df.SHORT_CODE==cc) ].copy()
    else:
        df_a = df_prev[ df_prev.ATTENDANCE.notnull() ].copy()
        df_b = df[ df.ATTENDANCE.isnull() ].copy()
    
    # get email list for quiz answers only
    df_final = df_a.merge(df_b, how='inner', on=['STUDENT_CODE']).copy()
    email_final = df_final['EMAIL_ADDRESS_x'].tolist()
    
    print("\nMAILING LIST - QUIZ ANSWERS ONLY")
    print("Total: {}".format(len(email_final)))
    print("______________________\n")
    for i in email_final: 
        print("{},".format(i))
    print("______________________")
    
    return 0

#####

def slides_quiz(filepath=filepath, df=df, df_prev=df_prev):
    """Generate names of students who've attended both the current and previous weeks' tutorials.
    These students will receive the tutorial slides and explanation of quiz answers
    (Unless a valid reason was given for missed attendance - why notnull is used instead of attendance=yes)"""
    
    # get df of students who attended previous tute and those who didn't attend current tute
    if cc != None: 
        df_a = df_prev[ (df_prev.ATTENDANCE.notnull()) & (df_prev.SHORT_CODE==cc) ].copy()
        df_b = df[ (df.ATTENDANCE.notnull()) & (df.SHORT_CODE==cc) ].copy()
    else:
        df_a = df_prev[ df_prev.ATTENDANCE.notnull() ].copy()
        df_b = df[ df.ATTENDANCE.notnull() ].copy()
    
    # get email list for quiz answers only
    df_final = df_a.merge(df_b, how='inner', on=['STUDENT_CODE']).copy()
    email_final = df_final['EMAIL_ADDRESS_x'].tolist()
    
    print("\nMAILING LIST - EVERYTHING")
    print("Total: {}".format(len(email_final)))
    print("______________________\n")
    for i in email_final: 
        print("{},".format(i))
    print("______________________")
    
    return 0
    
