#!/usr/bin/env python3
"""hello.py — 第一个脚本，练手用"""

def greet(name: str = "World") -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Git"))
