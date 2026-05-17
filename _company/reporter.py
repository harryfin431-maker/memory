"""
# reporter.py - 결과 보고 모듈

def generate_kpi_report(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """최종 KPI 분석 결과를 보고서 형식으로 생성합니다."""
    print("Generating final KPI Report...")
    
    total_ltv = sum(metrics['ltv_metrics'].values())
    avg_conversion = sum(metrics['conversion_metrics'].values()) / len(metrics['conversion_metrics']) if metrics['conversion_metrics'] else 0

    report = {
        "Summary": {
            "Total LTV (Estimated)": round(total_ltv, 2),
            "Average Conversion Rate": round(avg_conversion, 2),
            "Data Points Analyzed": len(metrics['raw_transactions'])
        },
        "Detailed Metrics": metrics['raw_transactions'].to_dict('records') # 실제 데이터프레임에서 JSON으로 변환하여 저장할 구조를 준비
    }
    return report

def save_results(report: Dict[str, Any], file_path: str):
    """분석 결과를 지정된 경로에 JSON 파일로 저장합니다."""
    print(f"Saving results to {file_path}...")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    print("✅ 결과 저장 완료.")