import os
import pandas as pd

# 대상 폴더 경로 설정
folder_path = r"C:\Users\SAMSUNG\Downloads\세원화성 2025.04월 수출신고필증 31건"

# 폴더 내 모든 파일 이름 리스트로 추출 (폴더는 제외)
file_names = [name for name in os.listdir(folder_path)
              if os.path.isfile(os.path.join(folder_path, name))]

# 데이터프레임으로 변환
df = pd.DataFrame(file_names, columns=["파일명"])

# 엑셀로 저장
output_path = os.path.join(folder_path, "파일목록.xlsx")
df.to_excel(output_path, index=False)

print("엑셀 저장 완료:", output_path)
