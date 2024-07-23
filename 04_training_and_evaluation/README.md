# 04_training_and_evaluation
## 환경 설정 방법

~~~bash
# 가상 환경 설정
conda create -n sasv python=3.9 cudatoolkit=11.3
conda activate sasv

# 라이브러리 설치
pip3 install -r requirements.txt
~~~
~~~bash
# pre-trained weight는 save/sasv_baseline_stage3/model/model000000001.model로 저장
~~~
## 평가 실행
~~~bash
# 프로토콜의 각 행은 ’SPEAKER 파일명(확장자명 제외) - - -‘
# e.g. 'SPEAKER TEST_00000_3 - - -'
# 평가 실행시 SASVNet.py의 line 101의 protocol이 올바른지 확인해야함
# e.g. sh 파일로 실행할 경우 'protocols/DA_meta.txt'
# 해당 프로토콜은 eval_path 경로에 'SPEAKER' + train data set 중 real에 해당하는 파일명(확장자 제외)과 연결되어 있어야 함
~~~
### 주어진 sh파일 이용
~~~bash
bash run.sh
~~~
### 본인 경로로 인자 입력
#### libri23mix로 분리된 음성 파일이 모두 들어가야하며 각 파일은 _1,_2,_3으로 구분되며 flac 파일이어야 함
~~~bash
cd 04_training_and_evaluation
~~~
~~~ bash
CUDA_VISIBLE_DEVICES=0 python trainSASVNet.py \
        --eval \
        --scoring \
        --eval_frames 0 \
        --num_eval 1 \
        --eval_list path/to/protocols/DA_eval.txt \
        --eval_path /path/to/your/evaldata \
        --model SKA_TDNN \
        --initial_model path/to/your_model/pretrained_weight.model
~~~

## 훈련 실행
~~~bash
# 훈련 실행 전 각 train data를 랜덤하게 8:2 비율로 나누어 train data와 dev(validation) data로 분리한 뒤 각각의 프로토콜 작성
# 프로토콜의 각 행은 'SPEAKER 파일명(확장자명 제외) - - bonafide' or 'SPEAKER 파일명(확장자명 제외) - A01 spoof'로 이루어져야 함
# e.g. 'SPEAKER AAAQOZYI_v1 - A01 spoof'
# 훈련 실행시 SASVNet.py의 line 101의 protocol이 올바른지 확인해야함
# e.g. sh 파일로 실행할 경우 'protocols/DA_meta_dev.txt'
# 해당 프로토콜은 eval_path 경로에 'SPEAKER' + train data set 중 real에 해당하는 파일명(확장자 제외)과 연결되어 있어야 함
~~~
## stage 1
### 주어진 sh 파일 이용
~~~bash
# clean한 train data로 2 epoch training
bash train_stage1.sh
~~~

### 본인 경로로 인자 입력
~~~bash
cd 04_training_and_evaluation
~~~
~~~bash
CUDA_VISIBLE_DEVICES=0 python trainSASVNet.py \
        --max_frames 500 \
        --num_spk 1 \
        --num_utt 2 \
        --batch_size 4 \
        --max_epoch 3 \
        --trainfunc sasv_e2e_v1 \
        --optimizer adamW \
        --scheduler cosine_annealing_warmup_restarts \
        --lr_t0 8 \
        --lr_tmul 1.0 \
        --lr_max 1e-4 \
        --lr_min 0 \
        --lr_wstep 0 \
        --lr_gamma 0.8 \
        --margin 0.2 \
        --scale 30 \
        --num_class 2 \
        --save_path ./save/sasv_baseline_stage3 \
        --train_list /path/to/protocols/DA_clean_train.txt \
        --eval_list /path/to/protocols/DA_clean_dev.txt \
        --train_path /path/to/your/tarindata \
        --eval_path /path/to/your/devldata \
        --model SKA_TDNN
~~~
## stage 2
### 주어진 sh 파일 이용
~~~bash
# noise mixed train data로 4 epoch training
bash train_stage2.sh
~~~

### 본인 경로로 인자 입력
~~~bash
cd 04_training_and_evaluation
~~~
~~~bash
CUDA_VISIBLE_DEVICES=0 python trainSASVNet.py \
        --max_frames 500 \
        --num_spk 1 \
        --num_utt 2 \
        --batch_size 4 \
        --max_epoch 7 \
        --trainfunc sasv_e2e_v1 \
        --optimizer adamW \
        --scheduler cosine_annealing_warmup_restarts \
        --lr_t0 8 \
        --lr_tmul 1.0 \
        --lr_max 1e-4 \
        --lr_min 0 \
        --lr_wstep 0 \
        --lr_gamma 0.8 \
        --margin 0.2 \
        --scale 30 \
        --num_class 2 \
        --save_path ./save/sasv_baseline_stage3 \
        --train_list /path/to/protocols/ASVspoof2019.DA.train.trn.txt \
        --eval_list /path/to/protocols/ASVspoof2019.DA.dev.trn.txt \
        --train_path /path/to/your/tarindata \
        --eval_path /path/to/your/devldata \
        --model SKA_TDNN
~~~