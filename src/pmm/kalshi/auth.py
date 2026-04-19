"""Kalshi request signing.

Kalshi uses RSA-PSS (SHA-256, MGF1-SHA256, salt length = digest length = 32)
over the message `timestamp_ms + method + path`. Path is the URL path only
(no scheme, no host, no query string? Kalshi docs have been inconsistent here
historically; we include the path that comes after the base URL's `/trade-api/v2`).
"""
from __future__ import annotations

import base64
import time
from dataclasses import dataclass
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


@dataclass
class KalshiSigner:
    key_id: str
    private_key: rsa.RSAPrivateKey

    @classmethod
    def from_pem_file(cls, key_id: str, pem_path: Path) -> "KalshiSigner":
        with open(pem_path, "rb") as f:
            key = serialization.load_pem_private_key(f.read(), password=None)
        if not isinstance(key, rsa.RSAPrivateKey):
            raise TypeError(f"Expected RSA private key, got {type(key).__name__}")
        return cls(key_id=key_id, private_key=key)

    def sign(self, method: str, path: str, timestamp_ms: int | None = None) -> dict[str, str]:
        if timestamp_ms is None:
            timestamp_ms = int(time.time() * 1000)
        message = f"{timestamp_ms}{method.upper()}{path}".encode("utf-8")
        signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.DIGEST_LENGTH,
            ),
            hashes.SHA256(),
        )
        return {
            "KALSHI-ACCESS-KEY": self.key_id,
            "KALSHI-ACCESS-SIGNATURE": base64.b64encode(signature).decode("ascii"),
            "KALSHI-ACCESS-TIMESTAMP": str(timestamp_ms),
        }
