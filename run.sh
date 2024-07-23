CUDA_VISIBLE_DEVICES=0

cd 04_training_and_evaluation
python trainSASVNet.py \
        --eval \
        --scoring \
        --eval_frames 0 \
        --num_eval 1 \
        --eval_list protocols/DA_eval.txt \
        --eval_path dataset/ASVSpoof/ASVSpoof2019/DA/ASVspoof2019_DA_eval/flac \
        --model SKA_TDNN \
        --initial_model save/sasv_baseline_stage3/model/model000000007.model