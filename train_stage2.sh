CUDA_VISIBLE_DEVICES=0
cd 04_training_and_evaluation
python trainSASVNet.py \
          --max_frames 500 \
          --num_spk 1 \
          --num_utt 2\
          --batch_size 4 \
          --max_epoch 7 \
          --trainfunc sasv_e2e_v1 \
          --optimizer adamW \
          --scheduler cosine_annealing_warmup_restarts \
          --lr_t0 8 \
          --lr_tmul 1.0 \
          --lr_max 1e-4 \
          --lr_min 0 \tr
          --lr_wstep 0 \
          --lr_gamma 0.8 \
          --margin 0.2 \
          --scale 30 \
          --num_class 2 \
          --save_path save/sasv_baseline_stage3 \
          --train_list protocols/ASVspoof2019.DA.train.trn.txt \
          --eval_list protocols/ASVspoof2019.DA.dev.trn.txt \
          --train_path dataset/ASVSpoof/ASVSpoof2019/DA \
          --eval_path dataset/ASVSpoof/ASVSpoof2019/DA/ASVspoof2019_DA_dev/flac \
          --model SKA_TDNN
