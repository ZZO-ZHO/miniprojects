# 전국 대학교 지도 표시
# pip install pandas
import pandas as pd

filePath = './studyPython/university_list_2020.xlsx'
df_excel = pd.read_excel(filePath, engine='openpyxl')
df_excel.columns = df_excel.loc[4].tolist()
df_excel = df_excel.drop(index=list(range(0,5)))    # 실제데이터 이외의 행 날림


print(df_excel.head())  # 상위 5개만 출력

print(df_excel['학교명'].values)
print(df_excel['주소'].values)