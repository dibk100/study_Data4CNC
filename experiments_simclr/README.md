# STUDY : Data4CNC 🏭📊
번외 실험 및 구현하기.   
A Simple Framework for Contrastive Learning of Visual Representations(PMLR 22)   
- Self-supervised 방식으로 representation을 학습한 후, labeled 데이터를 사용해 classifier를 학습
- 라벨이 부족할 때, 데이터의 구조를 잘 학습할 수 있도록 representation을 먼저 만들기 위해 해달 모델을 활용하는 편.
- 데이터 구조를 벡터 공간 상의 유사도 학습하여 이해함.
 
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
