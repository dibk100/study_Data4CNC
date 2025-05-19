# STUDY : Data4CNC 🏭📊
CNC Milling data preprocessing & analysis   
 
```
Assignment01_CNC/
├── data_analysis.ipynb                        # 데이터 분석 및 시각화
├── performance_metrics_suggestions            # 성능 평가 지표 개발
└── experiments_simclr/                        # 번외 실험(ing) : 분류모델개발
```


Wrap-up.   
---
- 👍🏻Good
    - 활용하는 데이터 자체를 뜯어봄(kaggle에 공유된 오픈데이터 설명도 참고)
    - 제조 공정 데이터를 처음 사용해서 분석을 진행해봄. 
    - pseudo-labeling 방식의 semi-supervised learning 구현
    
- 🙏🏻Bad
    - 제안한 성능지표 설계에 아쉬운 부분이 많음. 시계열성을 참고하고 싶었는데 갖고 있는 데이터 자체에 추가 전처리 및 매뉴얼한 부분이 있음.
    - SNC를 시계열 대체 변수로 활용했지만, 실험마다 속도가 달라서 시간 단위가 다를 것 같음. 시간적 정밀도 부족..

- 👏🏻Challenge(도전 및 개선할 점)
    - (ing)분류 모델 개발 (paper : A Simple Framework for Contrastive Learning of Visual Representations)
        - 공정 센서 기반 시계열 유사 데이터
        - Random Forest로 beseline성능 확인 용도로만 사용
        - (challenge) SimCLR + Classifier 구조를 활용하여 모델 개발해보기
    - 다른 성능 지표 찾아보기(시계열, 공정 etc)
    
- ✍🏻KeyWord
    - 수치 및 시계열성 데이터 기반 AI모델은 독립변수, 피처가 중요한 것 같음. 상황에 따라 매뉴얼하게 or 전문가가 개입하여 조정되는 느낌이 많이 듦.
    - 이런 데이터가 많은 제조업에서 LLM이 어떻게 활용될 수 있을지 아직도 감을 잡기 어렵다
       - 제조업 특화 LLM을 학습 시켜서 운영조건(변수)를 추천하는 모델?
       - 변수들이 물리적으로 어떤 관계가 있는지 잠재적 학습도 필요할 것 같음.

