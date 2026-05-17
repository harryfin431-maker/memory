# 경쟁사 ROI 분석 모델 데이터 구조 정의

본 문서는 수익화 Funnel과 기술 실행 계획을 통합하여 경쟁사 ROI 분석에 필요한 데이터 구조를 정의합니다.

## 1. 🎯 경쟁사 식별 및 컨텍스트 레이어 (Identification & Context Layer)

| 필드명 | 데이터 타입 | 설명 | Funnel 연관성 | 비고/예시 |
| :--- | :--- | :--- | :--- | :--- |
| **Competitor_ID** | String | 경쟁사 고유 식별자 (예: 'Competitor_A') | - | 분석 대상의 명확한 구분 |
| **Niche_Focus** | String | 경쟁사가 주력하는 시장/틈새시장 (Niche) | Inbound/Awareness | 예: AI 교육, 시니어 금융 컨설팅 등 |
| **Positioning_Strategy** | String | 경쟁사의 핵심 포지셔닝 전략 (프리미엄 vs. 대중성) | Awareness | 예: '최고가 프리미엄', '대중적 접근성' |
| **Target_Audience** | String | 경쟁사가 설정한 주요 타깃 청중 | Acquisition | 예: 40대 이상 은퇴자, IT 개발자 등 |

## 2. 💰 투자 및 성과 레이어 (Input & Output Layer)

### A. 투자 데이터 (Investment Data)

| 필드명 | 데이터 타입 | 설명 | Funnel 연관성 | 비고/예시 |
| :--- | :--- | :--- | :--- | :--- |
| **Acquisition_Cost** | Float | 해당 경쟁사로부터 잠재 고객 1명을 유입시키는 데 소요된 총 마케팅 비용 (CAC) | Acquisition | 광고비, 콘텐츠 제작비 등 합산 |
| **Content_Investment** | Float | 경쟁사가 생성한 핵심 콘텐츠(영상/리드마그넷)에 투자된 내부 리소스 비용 (또는 추정 가치) | Awareness/Consideration | 디자인, 스크립트 작성 등에 투입된 시간 및 인력 가치 |

### B. 성과 데이터 (Performance Data)

| 필드명 | 데이터 타입 | 설명 | Funnel 연관성 | 비고/예시 |
| :--- | :--- | :--- | :--- | :--- |
| **Revenue_Generated** | Float | 해당 경쟁사를 통해 발생한 총 매출액 (또는 추정 수익) | Conversion/Revenue | 월별 또는 분기별 데이터 필요 |
| **Conversion_Rate** | Float | 트래픽 대비 실제 전환(구매, 리드 등록 등) 비율 | Conversion | 예: 1.5% |
| **LTV_Estimate** | Float | 해당 고객의 예상 생애 가치 (Lifetime Value) 추정치 | Revenue/Retention | 이탈률 및 재구매율 기반 산출 |

## 3. 🔗 기여도 및 효율성 레이어 (Attribution & Efficiency Layer)

| 필드명 | 데이터 타입 | 설명 | 핵심 가치 연결 | 비고/예시 |
| :--- | :--- | :--- | :--- | :--- |
| **Efficiency_Score** | Float | (경험의 깊이 $\times$ AI 효율성)을 기반으로 산출한 상대적 효율 점수 | Wisdom & Efficiency | 내부 모델링 결과 |
| **Value_Alignment** | String | 경쟁사의 가치 제안(Value Proposition)이 우리의 핵심 원칙과 얼마나 일치하는가? | 신뢰도 | High/Medium/Low |
| **Gap_Analysis** | Text | 우리의 전략 대비 경쟁사가 놓치고 있는 핵심 기회 또는 우리가 따라잡아야 할 기술적 격차 분석. | 의사결정 | 구체적인 실행 방안 제시 |