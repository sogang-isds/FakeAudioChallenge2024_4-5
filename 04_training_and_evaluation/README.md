# 04_training_and_evaluation
## 환경 설정 방법

~~~bash
# 가상 환경 설정
conda create -n sasv python=3.9 cudatoolkit=11.3
conda activate sasv

# 라이브러리 설치
pip3 install -r requirements.txt
~~~
## 평가 실행
### 주어진 sh파일 이용하기
~~~bash
bash run.sh
~~~
### 본인 경로로 인자 입력
~~~bash
cd 04_training_and_evaluation
~~~
~~~ bash
CUDA_VISIBLE_DEVICES=0 python trainSASVNet.py \
        --eval \
        --scoring \
        --eval_frames 0 \
        --num_eval 1 \
        --eval_list protocols/DA_eval.txt \
        --eval_path /path/to/dataset/ASVSpoof/ASVSpoof2019/DA/ASVspoof2019_DA_eval/flac \
        --model SKA_TDNN \
        --initial_model path/to/your_model/pretrained_weight.model
~~~

