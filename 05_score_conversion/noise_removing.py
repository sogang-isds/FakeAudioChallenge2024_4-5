from tqdm import tqdm

def remove_matching_lines(file1_path, file2_path, output_file_path):
    # 첫 번째 텍스트 파일 읽기
    with open(file1_path, 'r') as file1:
        lines_file1 = file1.readlines()

    # 두 번째 텍스트 파일 읽기
    with open(file2_path, 'r') as file2:
        lines_file2 = file2.readlines()

    # 첫 번째 텍스트 파일의 각 줄을 집합으로 변환하여 빠른 검색 가능하게 하기
    lines_file1_set = set(line.strip() for line in lines_file1)

    # 두 번째 텍스트 파일의 각 줄을 확인하여 조건에 맞는 줄을 non_matching_lines에 추가
    non_matching_lines = []
    for line in tqdm(lines_file2):
        if any(item in line for item in lines_file1_set):
            parts = line.strip().split()
            if len(parts) > 0:
                non_matching_lines.append(parts[0] + ' 0.0\n')
        if not any(item in line for item in lines_file1_set):
            non_matching_lines.append(line)

    # 결과를 출력 파일에 쓰기
    with open(output_file_path, 'w') as output_file:
        for line in non_matching_lines:
            output_file.write(line)

# 사용 예제
file1_path = 'exp/result/noise_list_sep_1.txt'  # 노이즈 텍스트 파일 경로
file2_path = 'exp/result/results_cl2_v1_4.txt'  # ID와 predict score가 합쳐진 결과 텍스트 파일 경로
output_file_path = 'exp/result/sep_only_removed_results_cl2_v1_4.txt'  # 노이즈가 제거된 결과를 저장할 파일 경로

remove_matching_lines(file1_path, file2_path, output_file_path)
