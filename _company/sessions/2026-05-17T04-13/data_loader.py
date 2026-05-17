import json
from typing import Dict, Any

class DataLoader:
    """
    KPI 측정 데이터 파이프라인을 위한 데이터 로더 모듈.
    AVD -> CTR -> CR 흐름에 맞춰 실제 데이터 소스에서 데이터를 로드하고 정제합니다.
    """
    def __init__(self, data_source: str):
        self.data_source = data_source
        print(f"DataLoader initialized for source: {self.data_source}")

    def _load_raw_data(self) -> Dict[str, Any]:
        """실제 API 또는 파일 I/O 연결 로직을 시뮬레이션합니다."""
        print("INFO: Attempting to connect to data source...")
        # 실제 환경에서는 여기에 API 호출이나 파일 읽기 로직이 들어갑니다.
        if self.data_source == "mock_api":
            return {
                "avd_data": [100, 200, 300],  # Average View Duration 데이터 예시
                "ctr_data": [5.5, 6.2, 4.8],   # Click-Through Rate 데이터 예시
                "cr_data": [0.02, 0.015, 0.03] # Conversion Rate 데이터 예시
            }
        else:
            raise FileNotFoundError(f"Data source '{self.data_source}' not found.")

    def load_and_process(self) -> Dict[str, Any]:
        """데이터를 로드하고 KPI 흐름에 따라 처리합니다."""
        raw_data = self._load_raw_data()
        print("INFO: Raw data loaded. Starting KPI processing...")

        # AVD -> CTR -> CR 흐름 기반의 데이터 정제 및 연결 로직 구현
        processed_data = {
            "metrics": {}
        }

        for i in range(len(raw_data["avd_data"])):
            avd = raw_data["avd_data"][i]
            ctr = raw_data["ctr_data"][i]
            cr = raw_data["cr_data"][i]

            # KPI 연계 로직 (예시: AVD가 높을수록 CR에 긍정적 영향)
            if avd > 150 and ctr > 5.0:
                status = "HIGH_PERFORMANCE"
            elif cr < 0.01:
                status = "LOW_CONVERSION"
            else:
                status = "NORMAL"

            processed_data["metrics"][f"sample_{i+1}"] = {
                "avd": avd,
                "ctr": ctr,
                "cr": cr,
                "status": status
            }

        print("INFO: Data processing complete.")
        return processed_data

# 테스트 데이터 통합 및 실행 함수
def run_pipeline_test(source: str):
    """데이터 로더를 실행하고 결과를 출력합니다."""
    try:
        loader = DataLoader(source)
        results = loader.load_and_process()
        print("\n--- FINAL PROCESSED RESULTS ---")
        print(json.dumps(results, indent=4))
        print("------------------------------")
        return results
    except Exception as e:
        print(f"\nERROR: Pipeline execution failed: {e}")
        return None

if __name__ == "__main__":
    # 테스트 실행 (mock_api 사용)
    run_pipeline_test("mock_api")
    # run_pipeline_test("real_file_path") # 실제 파일 I/O 연결 시도 시 오류 발생 예상