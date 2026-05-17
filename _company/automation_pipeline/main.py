"""
# automation_pipeline/main.py - 수익화 지표 자동 계산 파이프라인 메인 진입점

import os, time
import json
from data_loader import load_subscriptions, load_transactions, load_bundle_options
from data_transformer import calculate_ltv, analyze_conversion, merge_and_validate
from reporter import generate_kpi_report, save_results

def main():
    print("--- Connect AI: 수익화 지표 자동 계산 파이프라인 시작 ---")
    
    # 1. 데이터 로드 단계 (실제 파일 경로를 여기에 지정해야 함)
    try:
        subscriptions = load_subscriptions("data/subscriptions.json")
        transactions = load_transactions("data/transactions.csv")
        bundles = load_bundle_options("data/bundles.json")
        print("✅ 데이터 로드 완료.")
    except FileNotFoundError as e:
        print(f"❌ 파일 누락 오류 발생: {e}. 데이터 경로를 확인하십시오.")
        return

    if not all([subscriptions, transactions, bundles]):
        print("❌ 필수 데이터 중 일부가 로드되지 않아 분석을 중단합니다.")
        return

    # 2. 데이터 변환 및 계산 단계 (핵심 로직)
    print("🚀 KPI 연계 및 데이터 변환 시작...")
    processed_data = {}
    try:
        ltv_results = calculate_ltv(subscriptions, transactions)
        conversion_results = analyze_conversion(bundles, transactions)
        final_merged_data = merge_and_validate({
            "ltv": ltv_results,
            "conversions": conversion_results,
            "subs": subscriptions,
            "trans": transactions,
            "bundles": bundles
        })
        processed_data['metrics'] = final_merged_data
        print("✅ 데이터 변환 및 KPI 계산 완료.")
    except Exception as e:
        print(f"❌ 데이터 처리 중 오류 발생: {e}")
        return

    # 3. 결과 보고 및 저장 단계
    print("📊 최종 보고서 생성 시작...")
    report = generate_kpi_report(processed_data['metrics'])
    save_results(report, "results/kpi_analysis_report.json")
    
    print("\n🎉 모든 작업이 성공적으로 완료되었습니다. 결과는 results/kpi_analysis_report.json 에 저장되었습니다.")

if __name__ == "__main__":
    main()