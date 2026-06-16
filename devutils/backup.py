#!/usr/bin/env python3
"""backup.py — 带时间戳的备份工具

用法: python backup.py <文件路径>
效果: 在文件同目录下生成 文件名_YYYYMMDD_HHMMSS.bak
"""

import shutil
from datetime import datetime
from pathlib import Path
import sys


def backup(filepath: str) -> Path:
    src = Path(filepath)
    if not src.exists():
        raise FileNotFoundError(f"文件不存在: {filepath}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = src.parent / f"{src.stem}_{timestamp}.bak"
    shutil.copy2(src, dst)
    return dst


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python backup.py <文件路径>")
        sys.exit(1)

    result = backup(sys.argv[1])
    print(f"✅ 备份完成: {result}")
