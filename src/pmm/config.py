"""Environment-driven config. No secrets in code; load from files outside the repo."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


DEFAULT_KEY_DIR = Path.home() / ".midpoint" / ".claude" / "prediction_mm_keys"
DEFAULT_DATA_DIR = Path.home() / "personal" / "prediction-mm" / "research" / "data"

# Kalshi production base URL. Override with env var KALSHI_BASE_URL if needed.
# As of early 2026 Kalshi has used a few hosts: api.elections.kalshi.com is the
# main prod host for event contracts; api.kalshi.com is the newer umbrella.
DEFAULT_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"


@dataclass(frozen=True)
class Config:
    base_url: str
    key_id: str
    private_key_path: Path
    data_dir: Path

    @classmethod
    def from_env(cls) -> "Config":
        key_dir = Path(os.environ.get("PMM_KEY_DIR", str(DEFAULT_KEY_DIR)))

        key_id_path = Path(os.environ.get("KALSHI_KEY_ID_PATH", str(key_dir / "kalshi_key_id.txt")))
        private_key_path = Path(
            os.environ.get("KALSHI_PRIVATE_KEY_PATH", str(key_dir / "kalshi_private.pem"))
        )

        key_id = os.environ.get("KALSHI_KEY_ID")
        if not key_id:
            key_id = key_id_path.read_text().strip()

        data_dir = Path(os.environ.get("PMM_DATA_DIR", str(DEFAULT_DATA_DIR)))
        data_dir.mkdir(parents=True, exist_ok=True)

        base_url = os.environ.get("KALSHI_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

        if not private_key_path.exists():
            raise FileNotFoundError(f"Kalshi private key not found at {private_key_path}")
        if not key_id:
            raise ValueError("Kalshi key id is empty")

        return cls(
            base_url=base_url,
            key_id=key_id,
            private_key_path=private_key_path,
            data_dir=data_dir,
        )
