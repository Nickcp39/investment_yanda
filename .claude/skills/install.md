# Project-Level Skills Install Guide

本目录的 Skills 都是<strong>项目级</strong> — 仅在 lab 工作目录下的
Claude Code 会话中生效, 不会污染其他项目。

`.claude/skills/*/` 在 `.gitignore` 里, 不进 lab 的 git。换设备需要按
本文档重装。

---

## 已安装清单

| Skill | 上游仓库 | 安装日期 | 用途 |
| --- | --- | --- | --- |
| buffett-perspective | https://github.com/will2025btc/buffett-perspective | 2026-05-05 | Warren Buffett 灵魂 (Persona 派, 单体) |
| expert-engine | https://github.com/AskRoundtable/expert-skills (subdir) | 2026-05-05 | 通用 expert 思维引擎 (Gary Klein RPD), 与 expert-* 模块配合 |
| expert-munger | https://github.com/AskRoundtable/expert-skills (subdir) | 2026-05-05 | Charlie Munger 思维模块 (Mental Models 派), 配合 expert-engine |

---

## 安装命令 (在 lab 根目录执行)

```bash
mkdir -p .claude/skills

# Buffett (Persona 派, 单体)
git clone https://github.com/will2025btc/buffett-perspective.git \
  .claude/skills/buffett-perspective

# Munger (Mental Models 派, 模块, 需要配合 expert-engine)
git clone https://github.com/AskRoundtable/expert-skills.git \
  .claude/skills/_staging-expert-skills
cp -r .claude/skills/_staging-expert-skills/skills/expert-engine \
  .claude/skills/expert-engine
cp -r .claude/skills/_staging-expert-skills/skills/expert-munger \
  .claude/skills/expert-munger
rm -rf .claude/skills/_staging-expert-skills
```

---

## 验证 Skill 已生效

在 lab 目录启动 Claude Code, 输入:

```
用巴菲特的视角看一下苹果
```

预期: 回复用第一人称 ("我"), 大量类比, 自嘲, 引 Charlie。

如果回复像普通分析师, Skill 没被检测到 — 检查 `.claude/skills/<name>/SKILL.md`
是否存在 + frontmatter 格式正确。

---

## 验证<em>未</em>污染其他项目

退出当前 Claude Code, 在<strong>非 lab 目录</strong> (如桌面) 启动新
会话, 输入同样的"用巴菲特的视角看苹果"。

预期: 回复用平常分析师口气, <em>没有</em>巴菲特特征。

如果触发了巴菲特口气, 说明 Skill 被错装到了用户级 (`~/.claude/skills/`),
检查并清理。

---

## 添加新 Skill 时的检查清单

- [ ] 在<strong>项目级</strong> `.claude/skills/<name>/` 而不是 `~/.claude/skills/`
- [ ] 上面"已安装清单"添加一行
- [ ] 安装命令追加到上方
- [ ] 按"验证未污染其他项目"测试隔离
- [ ] 如果是 fork 而非直接 clone, 在清单里标注 fork 地址
