#!/usr/bin/env python3
"""cleanup.py — 清理临时文件

用法: python cleanup.py <目录> [--days 7]
效果: 删除指定目录下超过N天的 .tmp/.log/.bak 文件
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path


def cleanup(directory: str, days: int = 7) -> tuple[int, int]:
    """返回 (删除数, 释放字节数)"""
    target = Path(directory)
    if not target.is_dir():
        raise NotADirectoryError(f"不是有效目录: {directory}")

    cutoff = datetime.now() - timedelta(days=days)
    deleted, freed = 0, 0
    extensions = {".tmp", ".log", ".cache"}

    for f in target.rglob("*"):
        if f.is_file() and f.suffix in extensions:
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if mtime < cutoff:
                size = f.stat().st_size
                f.unlink()
                deleted += 1
                freed += size
                print(f"  🗑  删除: {f.name} ({size} bytes)")

    return deleted, freed


if __name__ == "__main__":
    days = 7
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        days = int(sys.argv[idx + 1])

    path = sys.argv[1] if len(sys.argv) > 1 else "."

    try:
        n, size = cleanup(path, days)
        print(f"\n✅ 清理完成: {n} 个文件, 释放 {size:,} bytes")
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)
