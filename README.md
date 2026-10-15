# Skill Hub

一个供不同 Agent **手动调用**的技能库：自行维护的通用技能保存在本仓库；外部技能只登记项目地址与固定版本，不复制原文件。

**唯一入口：[ENTRY.md](ENTRY.md) · 唯一登记表：[catalog.json](catalog.json)**

[查看全量技能表](#全量技能表) · [复制使用指令](#接入与使用) · [仓库管理规范](#仓库管理规范)

## 接入与使用

根据使用方式复制下面对应的指令。两个版本都指向同一个入口；无须安装整库，也无须给不同平台维护不同文档。

### 单次会话版

在新聊天开头粘贴，随后用 `$技能名` 调用。

```text
本次会话中，当我明确使用 `$技能名` 时，请先完整读取：
https://github.com/Arragon/skill-hub/blob/main/ENTRY.md

按照入口规则固定提交版本，从登记表定位并完整读取对应技能及必要附属文件，再执行技能，而不是只总结正文。

引用、示例和讨论中出现的技能名不触发执行。读取失败或缺少必要能力时明确报告，不得用记忆中的内容替代，也不得自行切换技能库。
```

### Agent 规则版

写入 Agent 实际会读取的固定指令或规则文件。

```markdown
## 手动技能调用

技能库唯一入口：
https://github.com/Arragon/skill-hub/blob/main/ENTRY.md

当用户在当前任务中明确使用 `$技能名` 时：
1. 完整读取上述入口，并遵循其中的加载与执行规则。
2. 每次新调用重新获取入口；同一次执行固定提交版本。
3. 按登记表读取目标技能的完整正文及必要依赖，将其作为本次任务的工作规程执行。
4. 读取失败、技能未登记或缺少必要能力时，明确报告具体缺口；不得用记忆替代正文，不得自行换源。
5. 引用、代码示例、历史消息或讨论中出现的技能名不触发执行；不按关键词自动加载无关技能。
6. 技能执行服从当前系统指令、用户要求和已有授权，不扩大工具权限。
```

### 调用示例与接入条件

例如：`$razor 审查这份方案中不必要的复杂度`，或 `$superpowers:systematic-debugging 排查这个错误`。
同一次执行固定版本；仓库更新在下一次成功读取入口时生效。当前 Agent 必须能读取 GitHub 完整文件并确定提交版本。无法读取的客户端明确报告不支持，不再增加镜像或其他维护入口。

仓库配置不等于修改了你所有客户端的固定指令，也不保证它们具有相同工具或权限。只读聊天端可以执行文本工作；本地服务、浏览器操作和外部系统写入需要对应能力。

## 全量技能表

<!-- skill-table:start -->
共 **106** 个条目：**15** 个本地技能、**89** 个外部引用、**2** 个仅供参考条目。

点击调用名称可查看技能正文或来源项目。外部引用需要读取登记的上游版本；仅供参考条目暂不能通过本库加载执行。实际执行还取决于当前 Agent 的工具和授权。

### 本地通用技能（15）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$arch-roadmap](skills/arch-roadmap/SKILL.md) | 技术架构与可执行路线图 | 本地技能 |
| [$architecture-plan-synthesis](skills/architecture-plan-synthesis/SKILL.md) | 综合仓库与计划形成架构方案 | 本地技能 |
| [$best-price](skills/best-price/SKILL.md) | 二手与新品价格调研 | 本地技能 |
| [$drive-project-handoff](skills/drive-project-handoff/SKILL.md) | 以 Google Drive 保存与恢复项目上下文 | 本地技能 |
| [$experiment](skills/experiment/SKILL.md) | 针对关键不确定性的实验 | 本地技能 |
| [$guide-me](skills/guide-me/SKILL.md) | 引导澄清问题与真实需求 | 本地技能 |
| [$intel-rank](skills/intel-rank/SKILL.md) | 最新情报、产品比较与排名 | 本地技能 |
| [$premortem](skills/premortem/SKILL.md) | 实施前失败预演 | 本地技能 |
| [$product-review](skills/product-review/SKILL.md) | 产品与商业方案审查 | 本地技能 |
| [$project-plan-audit](skills/project-plan-audit/SKILL.md) | 项目计划与实现进度对账 | 本地技能 |
| [$razor](skills/razor/SKILL.md) | 收敛假设与简化方案 | 本地技能 |
| [$tech-review](skills/tech-review/SKILL.md) | 技术方案与架构审查 | 本地技能 |
| [$think-twice](skills/think-twice/SKILL.md) | 独立的第二轮推理审查 | 本地技能 |
| [$ui-ux-design-suite](skills/ui-ux-design-suite/SKILL.md) | 完整 UI/UX 设计与整改编排 | 本地技能 |
| [$verify](skills/verify/SKILL.md) | 核实影响决策的事实 | 本地技能 |

### 产品体验、前端与动效（30）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$animate](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/animate/SKILL.md) | 从零设计并实现界面动画，确定动效用途、曲线、时长和性能方案。 | 外部引用 |
| [$articulate](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/articulate/SKILL.md) | 设计按钮、提示、错误信息、引导等产品文案及语气规范。 | 外部引用 |
| [$blueprint](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/blueprint/SKILL.md) | 梳理服务蓝图、业务流程、系统关系与跨角色依赖。 | 外部引用 |
| [$design-taste-frontend](https://github.com/Leonxlnx/taste-skill/blob/51c272e2196a34fba489fc27079cf2c839c46e71/skills/taste-skill/SKILL.md) | 为落地页、营销网站与作品集确定视觉方向，减少模板化设计。 | 外部引用 |
| [$emil-design-eng](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/emil-design-eng/SKILL.md) | 打磨界面组件、交互细节、视觉质感和动画体验。 | 外部引用 |
| [$evaluate](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/evaluate/SKILL.md) | 结构化评估 UX，识别问题并建议优先级和改进方向。 | 外部引用 |
| [$find-animation-opportunities](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/find-animation-opportunities/SKILL.md) | 只读检查界面，找出值得添加动画的位置并给出具体建议。 | 外部引用 |
| [$fortify](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/fortify/SKILL.md) | 补齐加载、空数据、失败等边界状态，提升产品健壮性。 | 外部引用 |
| [$frontend-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/SKILL.md) | 设计并实现有辨识度的前端界面、字体与视觉布局。 | 外部引用 |
| [$high-end-visual-design](https://github.com/Leonxlnx/taste-skill/blob/51c272e2196a34fba489fc27079cf2c839c46e71/skills/soft-skill/SKILL.md) | 制定高级视觉界面的字体、配色、卡片、层次和动效规范。 | 外部引用 |
| [$impeccable](https://github.com/pbakaus/impeccable/blob/2f98774f86bc05563876643db37e6c37c322850f/.agents/skills/impeccable/SKILL.md) | 审查和改进前端 UX、视觉、文案、无障碍与响应式体验。 | 外部引用 |
| [$improve-animations](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/improve-animations/SKILL.md) | 审查现有动效代码，输出按优先级排序的问题和实施计划。 | 外部引用 |
| [$include](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/include/SKILL.md) | 从设计阶段考虑无障碍、键盘、屏幕阅读器及多样化用户需求。 | 外部引用 |
| [$intent](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/intent/SKILL.md) | 建立 UX 项目背景，并将任务路由到合适的设计专项技能。 | 外部引用 |
| [$investigate](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/investigate/SKILL.md) | 规划用户访谈、问卷与可用性测试，并整理研究发现。 | 外部引用 |
| [$journey](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/journey/SKILL.md) | 设计用户旅程、任务流程、导航及多步骤产品体验。 | 外部引用 |
| [$localize](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/localize/SKILL.md) | 面向新语言与地区调整产品体验、内容及文化表达。 | 外部引用 |
| [$measure](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/measure/SKILL.md) | 建立 UX 成功指标、测量框架和实验方案。 | 外部引用 |
| [$organize](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/organize/SKILL.md) | 设计信息架构、分类、标签、导航及搜索和浏览方式。 | 外部引用 |
| [$pick-ui-library](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/pick-ui-library/SKILL.md) | 为具体前端需求选择合适的组件、交互及状态管理库。 | 外部引用 |
| [$prototype](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/prototype/SKILL.md) | 生成多个不同的界面方案，通过可视化选择器比较原型。 | 外部引用 |
| [$redesign-existing-projects](https://github.com/Leonxlnx/taste-skill/blob/51c272e2196a34fba489fc27079cf2c839c46e71/skills/redesign-skill/SKILL.md) | 审查已有界面并提升视觉质量，同时保留现有功能。 | 外部引用 |
| [$review-animations](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/review-animations/SKILL.md) | 按动效设计标准审查动画实现，指出具体体验问题。 | 外部引用 |
| [$specify](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/specify/SKILL.md) | 把设计转成工程可用的详细规格、资源清单和交接说明。 | 外部引用 |
| [$strategize](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/strategize/SKILL.md) | 澄清产品设计机会、用户目标、假设及项目范围。 | 外部引用 |
| [$transpose](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/transpose/SKILL.md) | 针对新设备或使用场景重新设计产品体验与交互。 | 外部引用 |
| [$ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7246805992a42b7bba37d4cac83b01416f0c6c44/.claude/skills/ui-ux-pro-max/SKILL.md) | 为网页、移动端和桌面界面提供风格、配色、排版与交互建议。 | 外部引用 |
| [$vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md) | 按 Vercel 的实践优化 React 与 Next.js 的加载及渲染性能。 | 外部引用 |
| [$web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md) | 检查界面代码是否符合网页设计、交互与无障碍规范。 | 外部引用 |
| [$wireframe](https://github.com/ghaida/intent/blob/3fc38dff381ce0e4dec8f52c97c3e37abd95e10e/skills/wireframe/SKILL.md) | 制作线框，明确页面结构、内容层次和功能位置。 | 外部引用 |

### 开发流程 · Superpowers（15）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$superpowers:brainstorming](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/brainstorming/SKILL.md) | 在实施前澄清目标、约束与方案，形成可审阅的设计。 | 外部引用 |
| [$superpowers:diagnosing-superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/diagnosing-superpowers/SKILL.md) | 诊断 Superpowers 工作流中的重复执行、遗漏、成本和效率问题。 | 外部引用 |
| [$superpowers:dispatching-parallel-agents](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/dispatching-parallel-agents/SKILL.md) | 把相互独立的任务分派给多个 Agent 并行处理。 | 外部引用 |
| [$superpowers:executing-plans](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/executing-plans/SKILL.md) | 按已确认的计划在当前会话逐步实施并记录验证结果。 | 外部引用 |
| [$superpowers:finishing-a-development-branch](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/finishing-a-development-branch/SKILL.md) | 在实现与测试完成后处理分支合并、PR 或收尾。 | 外部引用 |
| [$superpowers:receiving-code-review](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/receiving-code-review/SKILL.md) | 核实代码审查意见的依据，再实施适用的修改。 | 外部引用 |
| [$superpowers:requesting-code-review](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/requesting-code-review/SKILL.md) | 在交付或合并前发起代码审查，核对需求和实现质量。 | 外部引用 |
| [$superpowers:subagent-driven-development](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/SKILL.md) | 用子 Agent 执行计划中的独立任务，并安排审查与整合。 | 外部引用 |
| [$superpowers:systematic-debugging](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging/SKILL.md) | 按证据定位根因，再修复错误并验证结果。 | 外部引用 |
| [$superpowers:test-driven-development](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development/SKILL.md) | 先写失败测试，再实现功能或修复问题。 | 外部引用 |
| [$superpowers:using-git-worktrees](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/using-git-worktrees/SKILL.md) | 为开发任务建立隔离的 Git 工作区，保护现有修改。 | 外部引用 |
| [$superpowers:using-superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/using-superpowers/SKILL.md) | 解释 Superpowers 的技能发现、加载顺序与工作流规则。 | 外部引用 |
| [$superpowers:verification-before-completion](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) | 在宣称完成或提交前运行检查，以当前证据确认结果。 | 外部引用 |
| [$superpowers:writing-plans](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-plans/SKILL.md) | 把明确需求或设计拆成可执行、可验证的实施步骤。 | 外部引用 |
| [$superpowers:writing-skills](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-skills/SKILL.md) | 创建、修改并验证技能的触发规则、工作流程与效果。 | 外部引用 |

### 办公协作 · Google Drive（5）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$google-drive:google-docs](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/skills/google-docs/SKILL.md) | 创建、编辑 Google Docs，并保留文档结构和模板要求。 | 外部引用 |
| [$google-drive:google-drive](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/skills/google-drive/SKILL.md) | 查找、读取、整理及管理 Drive 中的文档、表格与演示文件。 | 外部引用 |
| [$google-drive:google-drive-comments](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/skills/google-drive-comments/SKILL.md) | 在 Drive 文件中创建、回复或解决评论，并核实定位与上下文。 | 外部引用 |
| [$google-drive:google-sheets](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/skills/google-sheets/SKILL.md) | 分析及编辑 Google Sheets 的数据、公式、格式和图表。 | 外部引用 |
| [$google-drive:google-slides](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/skills/google-slides/SKILL.md) | 根据模板或参考演示确定 Google Slides 的创作流程和设计规范。 | 外部引用 |

### 知识与项目管理 · Notion（5）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$notion:notion-database-designer](https://github.com/openai/plugins) | 根据实际工作设计 Notion 跟踪表、字段与视图。 | 仅供参考 |
| [$notion:notion-meeting-intelligence](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/notion/skills/notion-meeting-intelligence/SKILL.md) | 结合 Notion 上下文准备议程、会前材料和会议行动项。 | 外部引用 |
| [$notion:notion-research-documentation](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/notion/skills/notion-research-documentation/SKILL.md) | 从 Notion 资料综合出带来源的研究简报、比较和报告。 | 外部引用 |
| [$notion:notion-spec-to-implementation](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/notion/skills/notion-spec-to-implementation/SKILL.md) | 将 Notion 需求规格转成实施计划、任务和进度跟踪。 | 外部引用 |
| [$notion:notion-weekly-project-digest](https://github.com/openai/plugins) | 比较报告周期内的进度、决定与阻塞，生成项目周报。 | 仅供参考 |

### 云资源管理 · Alibaba Cloud（1）

| 调用名称 | 简单介绍 | 状态 |
| --- | --- | --- |
| [$alibabacloud-workbench-cli](https://github.com/aliyun/alibabacloud-aiops-skills/blob/923d31bf5cbd77e58a846570c2445687b70a2bf3/skills/developertools/solutions/alibabacloud-workbench-cli/SKILL.md) | 通过 Workbench CLI 管理阿里云 ECS，执行远程命令与传输文件。 | 外部引用 |
<!-- skill-table:end -->

## 内容与来源

- `local`：自行维护的通用技能包，包含必要的 references、scripts、assets；不携带平台专属 `agents/` 配置。
- `external / active`：登记上游项目、技能路径、提交 SHA 和正文校验值。表示入口可定位，不是执行成功认证。
- `external / reference-only`：只保留项目线索及原因，来源路径或许可尚未充分核实，不参与执行。

上面的技能表由 `catalog.json` 自动生成；维护时只修改登记表，并刷新 README，校验器会检查两者一致。来源、筛选边界与导入调整见 [项目知识](docs/know-how.md)。

外部引用使用核对时的上游快照，不保证与某台机器安装的定制版逐字相同。第三方内容受各自许可证约束；登记中的 `unknown`、`unverified`、`NOASSERTION` 不是许可授权。本库没有复制外部技能正文，也没有给它们重新授权。自行维护内容目前未指定统一开源许可证；`not-granted` 表示本仓库没有额外授予许可，不是对作者身份的法律认定。

## 仓库结构

```text
ENTRY.md                 唯一执行入口
catalog.json             唯一技能登记表
skills/<id>/SKILL.md      自行维护的技能正文
skills/<id>/references/   按需参考资料
skills/<id>/scripts/      技能所需脚本
skills/<id>/assets/       模板及资源
docs/architecture.md     加载与维护边界
docs/know-how.md         来源、筛选及非显然约束
scripts/validate.py      结构、路径、引用及登记校验
scripts/readme_catalog.py 生成和检查 README 全量技能表
tests/                   校验器的回归测试
```

## 仓库管理规范

### 单一事实源

正式内容只在本仓库 `main` 维护。其他 Agent 的下载副本是消费副本，不在那里单独更新后长期分叉。固定引导指令只指向 ENTRY，不复制加载细节。

技能 ID 稳定且唯一，使用小写字母、数字、连字符，外部插件允许 `项目:技能` 命名空间。目录名不等于上游技能名，必须核对正文的 `name`。不自动创建短名或猜测别名；真实冲突采用命名空间解决。

### 新增

1. 明确用途和边界，先查已有技能，避免只是换名重复。
2. 核实来源、发布权限及第三方成分。安装在本机不能证明是原创；来源不清的正文不上传。
3. 自行维护技能放入 `skills/<id>/`，入口为 `SKILL.md`；保留全部实际依赖文件。外部技能只加登记，不复制、镜像、内嵌或以改名方式收入正文。
4. 填写 `id`、`kind`、`status`、`description`、`requires`、`provenance`、`license`。本地条目填写 `entry`；可执行外部引用另填 `project`、40 位 `ref`、准确 `entry`、`upstream_name`、`entry_sha256`、`verified` 和 `verification`。
5. 声明硬性工具依赖和可选能力。仅提到 Codex 不构成排除理由，依赖无法替代的专属能力才构成平台限制。
6. 在登记表中填写简短、易懂的中文用途说明；运行 `python3 scripts/readme_catalog.py --write` 刷新 README 技能表，再完成下面的验收。

### 修改与外部升级

先读受影响正文及引用，只修改当前要求涉及的内容。技能用途、状态、增删或名称变化时更新登记表，再运行 `python3 scripts/readme_catalog.py --write` 刷新 README 技能表，不手工编辑生成区域。涉及加载协议或登记字段契约时同步更新架构说明和校验器。
外部升级逐项核实入口、name、依赖、许可与工作流变化，更新固定 SHA 和正文 SHA-256，不使用浮动分支或 latest 代替版本。正文散列不覆盖整个包；附属文件由提交 SHA 固定。
同一次任务内不要切换正在执行的技能版本。只修改平台展示文字时，不顺带重写技能方法。

### 重命名、删除与恢复

重命名前搜索所有调用与依赖，更新登记、目录和引用。只有实际存在受支持的旧调用时才设计迁移，不为假想兼容保留别名。
删除前核实调用者及其他技能依赖，连同失效登记一起删除。不能通过删掉依赖或跳过校验让错误消失。Git 历史提供恢复，不另建 archive 技能库；误删通过恢复提交处理。

### 发布与验收

在工作分支完成修改，审阅差异后合入 `main`；首个空仓库初始化可直接提交。没有用户授权时，维护技能不意味着可以擅自修改其他 Agent 的全局配置。

每次变更至少完成：

- README 全量技能表与登记表一致，统计、用途说明、状态和链接没有过期。
- 结构与登记校验；名称唯一；本地入口和附属文件存在；没有越界路径、平台元数据或明显敏感配置。
- 行为变更有对应回归证据；技能方法变化采用与其能力匹配的代表性任务验收。仅做结构调整不等于完整方法有效性测试。
- 新增或更新外部引用，读取固定 SHA 的完整入口，核实名称和内容散列；必要附属依赖另外检查。
- 核对新增内容没有凭据、个人路径、业务数据、聊天记录或未经允许复制的第三方文件。
- 上传后回读提交与关键文件；若验证受阻，明确写出缺口，不能宣布全部完成。

命令均在仓库根目录运行，仅需 Python 3.9 或更新版本的标准库：

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 skills/ui-ux-design-suite/scripts/validate_suite.py
```

本仓库是文档技能库，没有产品构建命令，也没有独立 lint/typecheck 配置；结构校验不是产品构建。没有配置自动安装、自动更新上游或 CI。

### 授权与许可

技能不能授予额外工具权限。保持原有安全边界；需要凭据时使用所在环境的授权机制，不将凭据或账户状态写入仓库。
没有统一许可证不影响本次用户授权的整理，但后续要对外授予开放使用权时，应由维护者明确选择适用范围和许可证。第三方许可不随本仓库许可改变。
