def merge_files(id_file, score_file, output_file):
    try:
        # 파일 읽기
        with open(id_file, 'r', encoding='utf-8') as f:
            ids = f.readlines()
        
        with open(score_file, 'r', encoding='utf-8') as f:
            scores = f.readlines()
        
        # 두 파일의 행 수가 같은지 확인
        if len(ids) != len(scores):
            raise ValueError("The number of lines in the ID file and the score file must be the same.")
        
        # 합친 결과를 새로운 파일에 쓰기
        with open(output_file, 'w', encoding='utf-8') as f:
            for id_line, score_line in zip(ids, scores):
                merged_line = f"{id_line.strip()} {score_line.strip()}\n"
                f.write(merged_line)
        
        print(f"Merged data has been saved to: {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# 사용 예시
id_file = 'ids.txt'  # ID가 있는 파일 경로
score_file = 'predict_scores.txt'  # 스코어가 있는 파일 경로
output_file = 'results_cl2_v1_4.txt'  # 합쳐진 결과를 저장할 파일 경로
merge_files(id_file, score_file, output_file)
