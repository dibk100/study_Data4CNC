# STUDY : Data4CNC 🏭📊
번외 실험
 
```
simclr_experiment/
├── config/
│   └── config.yaml               # 하이퍼파라미터 및 경로 설정
├── data/
│   └── dataset.py                # Custom Dataset 및 Data Augmentation 정의
├── models/
│   ├── simclr_encoder.py         # SimCLR encoder (e.g., 1D CNN, Transformer)
│   └── projection_head.py        # Projection head
├── simclr/
│   ├── train_simclr.py           # contrastive pretraining loop
│   └── nt_xent_loss.py           # NT-Xent contrastive loss 구현
├── downstream/
│   ├── train_classifier.py       # labeled data로 downstream classifier 학습
│   └── evaluate.py               # TP, FP, FN 및 custom metric 계산
├── utils/
│   └── scheduler.py              # Cosine Annealing 등 스케줄러
├── main.py                       # 전체 파이프라인 실행
└── wandb/ or logs/               # 실험 기록

```
