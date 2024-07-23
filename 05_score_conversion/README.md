# 05_score_conversion
## 환경설정
### pandas/matplotlib가 라이브러리에 포함되어있지 않을 경우
~~~bash
pip install pandas
pip install matplotlib
~~~
### 평가 결과 가져오기
~~~bash
cp -r 04_training_and_evaluation/exp/result/* 05_score_conversion/
~~~
### numpy 파일을 txt 파일로 변환
~~~bash
cd 05_score_conversion
python npy_2_txt.py
~~~
### 각 id에 해당하는 스코어 txt 파일로 병합
~~~bash
python merge_txt.py
~~~
### 노이즈에 해당하는 id는 score 값 0으로 변환
~~~bash
# 02 단계에서 분리된 test data의 음성중 노이즈로 검출된 파일들의 list를 file_path1으로 설정
python noise_removing.py
~~~
### 제출 형식으로 점수 변환 및 파일 출력
~~~bash
# cosine similarity -> tanh(4x)
python score_convert.py
~~~
### submission_csv 경로에 최종 결과 저장