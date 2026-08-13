# -*- coding: utf-8 -*-
"""目次ファイルの整合性検査
使い方: python3 toc_check.py 数学書_全巻目次案.md
検査内容:
  1. 章番号(行頭 "N. ")が各巻内で 1 から連番か
  2. 節番号(4スペース + "N. ")が各章内で 1 から連番か
  3. 完全に同一の行の重複(二重挿入事故の検出)
編集のたびに回すこと。異常なし ✓ が出るまでコミットしない。
"""
import re
import sys
from collections import Counter


def check(path: str) -> int:
    lines = open(path, encoding="utf-8").read().split("\n")
    problems = []
    cur_vol = cur_ch = expected = None
    for i, l in enumerate(lines, 1):
        mv = re.match(r"^## (\S+)：", l)
        if mv:
            cur_vol, cur_ch = mv.group(1), None
            continue
        mc = re.match(r"^(\d+)\. ", l)
        if mc:
            n = int(mc.group(1))
            if cur_ch is not None and n not in (cur_ch + 1, 1):
                problems.append(f"L{i} [{cur_vol}] 章番号飛び: {cur_ch}→{n}")
            cur_ch, expected = n, 1
            continue
        ms = re.match(r"^    (\d+)\. ", l)
        if ms:
            n = int(ms.group(1))
            if expected is not None and n != expected:
                problems.append(
                    f"L{i} [{cur_vol} {cur_ch}章] 節番号異常: "
                    f"期待{expected} 実際{n} :: {l.strip()[:40]}"
                )
            expected = n + 1

    cnt = Counter(
        l for l in lines if l.strip() and not l.startswith(">") and l.strip() != "---"
    )
    dups = [(l, c) for l, c in cnt.items() if c > 1]

    print("=== 番号検査 ===")
    print("\n".join(problems) if problems else "異常なし ✓")
    print("=== 同一行重複検査 ===")
    if dups:
        for l, c in dups:
            print(f"{c}回: {l.strip()[:60]}")
    else:
        print("なし ✓")
    return 1 if (problems or dups) else 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "数学書_全巻目次案.md"
    sys.exit(check(target))
