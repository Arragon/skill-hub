# UI/UX Design Suite

> 版本：1.0.0  
> 定位：一套“外部专业 Skill 优先、内置 fallback 兜底”的全流程 UI/UX 编排 Skill。

## 它解决什么问题

普通 UI Skill 往往只擅长一个环节：有的会画界面，有的会做 UX，有的会写前端，有的会做审查。真正的产品 UI/UX 工作却要求把“产品目标 → 用户流程 → 信息架构 → 线框 → 视觉系统 → 原型 → 用户确认 → 实现 → 回归 → QA”串成一个完整且可控的流程。

本套件只有一个对外入口：`ui-ux-design-suite`。它先识别当前环境里是否已经存在更专业的 Intent、Product Design、Impeccable、Taste、frontend-design、UI UX Pro Max、Emil、Figma、Vercel 等能力。如果存在且当前环境能调用，就优先委派给它们；如果缺失、不可用或不适配，就加载本包内部对应的 fallback 子 Skill。因此，同一个 ZIP 可以在“技能丰富的环境”和“只有基础 Coding Agent 的环境”里使用。

## 两条主流程

### 从零设计

产品/用户目标 → 关键问题确认 → 用户/竞品/reference 研究 → UX strategy → journey → IA → wireframe → 用户确认 → visual direction → design system → prototype/demo → 用户确认 → implementation contract → 生产实现 → harden/a11y/responsive → motion（按需）→ QA → handoff。

### 已有 UI 整改

当前状态与真实流程 → UX/UI audit → 公共组件/回归影响图 → 关键问题排序 → 与用户确认方向 → reference 研究 → 必要的 journey/IA/wireframe → demo → 用户确认 → implementation contract → 实现 → regression/visual QA → 更新长期设计决策。

## 核心门禁

- 有实质疑问时不能带着猜测开工，但只问真正会改变方案的问题。
- 中等及以上 UI/UX 改动默认先做低成本 demo，再改生产 UI。
- 同一阶段只允许一个“生成型视觉权威”。其他 Skill 只能审查或提供专项建议。
- 修改共享组件前必须判断：这是系统性缺陷，还是当前页面的局部需求。
- 外部 Skill 不存在时不会自动安装，而是进入本套件 fallback。
- QA 是有限轮次，不允许无限 polish。

## 目录

```text
ui-ux-design-suite/
├── SKILL.md                     顶层编排器，唯一需要主动触发的入口
├── README.md                    本说明
├── manifest.json                套件结构和子 Skill 清单
├── references/fallback-*.md     内部 fallback 操作手册，不单独注册为 Skill
├── references/                  路由、流程、质量门禁与原始手册
└── scripts/                     校验脚本
```

## 安装

把整个 `ui-ux-design-suite` 文件夹放入当前 Agent 能识别的 skills 目录即可。不同 harness 的 skill 目录不同，本包不假设固定路径，也不会自动写入你的全局配置。

安装后主要调用：

```text
$ui-ux-design-suite
```

在本仓库中仅通过显式 `$ui-ux-design-suite` 调用；自然语言描述用于说明任务，不自动触发技能。

## 外部 Skill 与 fallback 的关系

外部专业 Skill 是“优先执行器”，本套件内置 fallback 操作手册是“兼容兜底”。例如环境中有 Intent `journey` 就直接用 Intent；没有才加载 `references/fallback-ui-ux-journey.md`。这意味着你不需要为了使用本套件把所有第三方 Skill 全装一遍。

## 原始设计依据

`references/UI-Design-manual.md` 是本套件的主要流程依据。套件没有机械复制手册，而是把其中的职责分层、单一视觉权威、PRODUCT/DESIGN 权威顺序、Intent/Impeccable/Taste/UI UX Pro Max/Vercel/Emil 的定位，重新整理成可动态编排、可 fallback 的统一流程。
