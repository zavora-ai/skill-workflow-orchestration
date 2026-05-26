#!/usr/bin/env python3
"""Check if all approval gates are satisfied for workflow advancement."""
import json, sys

def check(data):
    gates = data.get("gates", [])
    pending = [g for g in gates if g.get("status") == "pending"]
    approved = [g for g in gates if g.get("status") == "approved"]
    rejected = [g for g in gates if g.get("status") == "rejected"]
    return {
        "can_advance": len(pending) == 0 and len(rejected) == 0,
        "pending": len(pending),
        "approved": len(approved),
        "rejected": len(rejected),
        "blockers": [g["name"] for g in pending + rejected],
    }

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
