"""
# data_loader.py - 데이터 로더 모듈

import json
import pandas as pd
from typing import Dict, Any

def load_subscriptions(file_path: str) -> Dict[str, Any]:
    """구독 데이터를 JSON 파일에서 로드합니다."""
    print(f"Loading subscriptions from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_transactions(file_path: str) -> pd.DataFrame:
    """거래 로그 데이터를 CSV 파일에서 로드하고 DataFrame으로 반환합니다."""
    print(f"Loading transactions from {file_path}...")
    df = pd.read_csv(file_path)
    return df

def load_bundle_options(file_path: str) -> Dict[str, Any]:
    """번들 옵션 데이터를 JSON 파일에서 로드합니다."""
    print(f"Loading bundle options from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data