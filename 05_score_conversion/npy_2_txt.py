import numpy as np

def npy_to_txt(npy_file, txt_file):
    # .npy 파일 읽기
    data = np.load(npy_file)

    # .txt 파일로 저장
    np.savetxt(txt_file, data, fmt='%s')

    print(f"{npy_file} 파일이 {txt_file}로 변환되었습니다.")

# 사용 예시
npy_file = 'exp/result/predict_scores.npy' #trainSASVnet.py에서 저장한 npy파일
txt_file = 'exp/result/predict_scores.txt' #npy를 txt로 변환
npy_to_txt(npy_file, txt_file)
