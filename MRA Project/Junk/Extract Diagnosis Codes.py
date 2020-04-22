import pandas as pd
import numpy as np

df = pd.read_excel('Review.xlsx',sheet_name = 'Review')

def get_dx(text, mid):
    text = str(text)
    words_list = text.strip().replace('.','').replace(';','; ').split(' ')
    dx = [{mid:i[:-1]} for i in words_list if ':' in i]
    dx = [{mid:''}] if len(dx) == 0 else dx
    return dx

df['s_dx'] = df['Suggested Codes'].apply(get_dx)
    
