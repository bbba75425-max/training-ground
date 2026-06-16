# Training Ground 🏋️

Git & DevOps 技能训练仓库 — 从零到工程习惯养成。

## 训练路线

| 阶段 | 内容 | 状态 |
|------|------|------|
| 🟢 环境 | Ubuntu 安装、文件系统、权限管理 | ✅ |
| 🟢 Shell | grep/find/管道/重定向、SSH远程 | ✅ |
| 🟢 工具 | VSCode Remote-SSH、conda/venv | ✅ |
| 🟡 Git | commit规范、分支策略、远程协作 | 🔄 |
| ⬜ CI/CD | GitHub Actions | ⬜ |
| ⬜ 容器 | Docker基础 | ⬜ |

## Commit 规范

```
<type>(<scope>): <subject>

type: feat | fix | docs | style | refactor | test | chore
scope: 影响范围（可选）
subject: 简短描述（<50字符）
```

### 示例
```
feat(shell): add backup script with timestamp
fix(ssh): correct known_hosts permission
docs: add git branching strategy guide
```

## 分支策略

- `main` — 稳定版本，通过PR合并
- `dev` — 开发分支
- `feature/*` — 功能分支
- `fix/*` — 修复分支

---

> 所有代码全部入Git仓库。每个练习一个目录，带README说明。
