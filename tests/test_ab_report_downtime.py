import importlib.util
import json
from pathlib import Path

_spec = importlib.util.spec_from_file_location("ab_report", Path(__file__).resolve().parents[1] / "scripts" / "ab_report.py")
ab = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ab)


def test_downtime_days_are_not_scored_as_zero_days(tmp_path, monkeypatch):
    down = tmp_path / "downtime.json"
    down.write_text(json.dumps({"windows": [{"start": "2026-10-02", "end": "2026-10-03"}]}))
    monkeypatch.setattr(ab, "DOWNTIME", down)
    monkeypatch.setattr(ab, "score_arm", lambda name, *a: {"name": name, "pnl": 0.0, "fills": 0})
    monkeypatch.setattr(ab, "live_markouts", lambda p: None)
    monkeypatch.setattr(ab, "ladder_of", lambda n: None)
    monkeypatch.setattr(ab, "latency_curve", lambda arms: [])
    rows = [{"date": f"2026-10-0{i}", **{a: float(i) for a in ab.ARMS}} for i in range(1, 5)]
    (tmp_path / "daily.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))

    doc = ab.build(tmp_path, client=None, with_markouts=False, day="2026-10-05")

    assert next(a for a in doc["arms"] if a["name"] == "baseline")["units"] == 2   # 10/04 and 10/05
    assert [r["date"] for r in doc["daily"] if r.get("excluded")] == ["2026-10-02", "2026-10-03"]
    assert doc["headline"].startswith("Collecting: day 2 of")
