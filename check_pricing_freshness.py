#!/usr/bin/env python3
"""
Pricing Freshness Audit

Flags provider mappings whose pricing/metadata has not been reviewed recently so
maintainers can re-verify them against official provider rate cards. This does not
fetch official prices automatically; it produces a review checklist.

Usage:
    python check_pricing_freshness.py
    python check_pricing_freshness.py --max-age-days 30 --recent-days 120
    python check_pricing_freshness.py --fail-on-stale
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


def _parse_timestamp(value: Any) -> Optional[datetime]:
    """Parse an ISO 8601 timestamp like 2026-07-15T00:00:00.000Z."""
    if not isinstance(value, str) or not value:
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _load_yaml(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with open(path, "r") as handle:
            data = yaml.safe_load(handle)
        return data if isinstance(data, dict) else None
    except (yaml.YAMLError, OSError) as exc:
        print(f"Warning: could not read {path}: {exc}", file=sys.stderr)
        return None


def _load_model_created(models_dir: Path) -> Dict[str, Optional[datetime]]:
    created: Dict[str, Optional[datetime]] = {}
    if not models_dir.exists():
        return created
    for yaml_file in models_dir.glob("*.yaml"):
        data = _load_yaml(yaml_file)
        if data and "id" in data:
            created[data["id"]] = _parse_timestamp(data.get("created_at"))
    return created


def _format_price(pricing: Dict[str, Any]) -> str:
    if not isinstance(pricing, dict):
        return "n/a"
    currency = pricing.get("currency", "USD")
    inp = pricing.get("input_per_million")
    out = pricing.get("output_per_million")
    return f"{inp} / {out} {currency} per 1M"


def audit(
    registry_path: Path,
    max_age_days: int,
    recent_days: int,
    all_models: bool = False,
) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    model_created = _load_model_created(registry_path / "models")

    stale: List[Dict[str, Any]] = []
    undated: List[Dict[str, Any]] = []
    total_mappings = 0
    considered_mappings = 0

    mappings_dir = registry_path / "mappings"
    if mappings_dir.exists():
        for yaml_file in sorted(mappings_dir.rglob("*.yaml")):
            # Skip hidden/example files (e.g. .example-extended-pricing.yaml).
            if any(part.startswith(".") for part in yaml_file.relative_to(registry_path).parts):
                continue

            data = _load_yaml(yaml_file)
            if not data or "model_id" not in data or "provider_id" not in data:
                continue
            total_mappings += 1

            model_id = data["model_id"]
            created = model_created.get(model_id)
            is_recent = created is not None and (now - created).days <= recent_days

            # By default only audit fast-moving, recently released models; use
            # --all-models to sweep the entire catalog including legacy models.
            if not all_models and not is_recent:
                continue
            considered_mappings += 1

            updated = _parse_timestamp(data.get("updated_at"))
            rel = yaml_file.relative_to(registry_path)
            entry = {
                "path": str(rel),
                "model_id": model_id,
                "provider_id": data["provider_id"],
                "price": _format_price(data.get("pricing", {})),
                "recent": is_recent,
            }

            if updated is None:
                undated.append(entry)
                continue

            age_days = (now - updated).days
            entry["age_days"] = age_days
            if age_days > max_age_days:
                stale.append(entry)

    # Recent models first, then oldest data first.
    stale.sort(key=lambda e: (not e["recent"], -e.get("age_days", 0)))

    return {
        "now": now,
        "total_mappings": total_mappings,
        "considered_mappings": considered_mappings,
        "stale": stale,
        "undated": undated,
        "max_age_days": max_age_days,
        "recent_days": recent_days,
        "all_models": all_models,
    }


def format_report(result: Dict[str, Any]) -> str:
    stale = result["stale"]
    undated = result["undated"]
    lines: List[str] = []
    scope = (
        "all models"
        if result["all_models"]
        else f"models released in the last {result['recent_days']} days"
    )
    lines.append("## Weekly pricing freshness audit")
    lines.append("")
    lines.append(
        f"Audited {result['considered_mappings']} of {result['total_mappings']} "
        f"provider mappings ({scope}) on {result['now'].date().isoformat()} (UTC)."
    )
    lines.append("")

    if not stale and not undated:
        lines.append(
            f"All audited mapping pricing has been reviewed within the last "
            f"{result['max_age_days']} days. Nothing to do."
        )
        lines.append("")
        lines.append(f"<!-- pricing-freshness: stale_count=0 recent_stale=0 -->")
        return "\n".join(lines)

    recent_stale = sum(1 for e in stale if e["recent"])
    lines.append(
        f"**{len(stale)} mapping(s)** have not been reviewed in over "
        f"{result['max_age_days']} days. Re-verify each against the provider's "
        f"official rate card, then bump `updated_at`. Entries marked ⭐ belong to "
        f"models released in the last {result['recent_days']} days and change most often."
    )
    lines.append("")

    if stale:
        lines.append("### Stale pricing to re-verify")
        lines.append("")
        lines.append("| | Model | Provider | Current price | Age (days) | File |")
        lines.append("|---|---|---|---|---|---|")
        for e in stale:
            star = "⭐" if e["recent"] else ""
            lines.append(
                f"| {star} | `{e['model_id']}` | `{e['provider_id']}` | "
                f"{e['price']} | {e['age_days']} | `{e['path']}` |"
            )
        lines.append("")

    if undated:
        lines.append("### Missing `updated_at`")
        lines.append("")
        for e in undated:
            lines.append(f"- `{e['path']}` (`{e['model_id']}` @ `{e['provider_id']}`)")
        lines.append("")

    lines.append(
        f"<!-- pricing-freshness: stale_count={len(stale)} recent_stale={recent_stale} -->"
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit provider-mapping pricing freshness.")
    parser.add_argument("--registry-path", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--max-age-days", type=int, default=30)
    parser.add_argument("--recent-days", type=int, default=90)
    parser.add_argument(
        "--all-models",
        action="store_true",
        help="Audit the entire catalog, not just recently released models.",
    )
    parser.add_argument(
        "--fail-on-stale",
        action="store_true",
        help="Exit with code 1 when stale mappings are found (for CI gating).",
    )
    args = parser.parse_args()

    result = audit(args.registry_path, args.max_age_days, args.recent_days, args.all_models)
    print(format_report(result))

    if args.fail_on_stale and (result["stale"] or result["undated"]):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
