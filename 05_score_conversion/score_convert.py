import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt



def classify_scores(file_list, output_csv):
    data = {}
    
    # Read the file list
    with open(file_list, 'r') as f:
        lines = f.readlines()
    
    # Process each line
    for line in lines:
        line = line.strip()
        file_id, score = line.split(' ')
        base_id = file_id.rsplit('_', 1)[0]
        score_value = float(score)
        
        if base_id not in data:
            data[base_id] = {'real': 0, 'fake': 0}
        
        if score_value > 0:    
            if data[base_id]['real'] < np.tanh(4*score_value):
                data[base_id]['real'] = np.tanh(4*score_value)
        if score_value < 0:
            score_value=-score_value
            if data[base_id]['fake'] < np.tanh(4*score_value):
                data[base_id]['fake']= np.tanh(4*score_value)

    
    # Prepare data for DataFrame
    ids = []
    reals = []
    fakes = []
    for base_id, values in data.items():
        ids.append(base_id)
        reals.append(values['real'])
        fakes.append(values['fake'])
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame({
        'id': ids,
        'fake': fakes,
        'real': reals
    })
    
    df.to_csv(output_csv, index=False)

# Parameters
file_list = "noise_removed_results_cl2_v1_4.txt"  # 노이즈가 제거된 ID 및 predict score file
output_csv = "submission_csv/pre_cl2_v1_4_noise_removed_tanh4x.csv" # 최종 제출 결과물

# Run the classification
classify_scores(file_list, output_csv)

print(f"Scores have been classified and saved to {output_csv}.")
