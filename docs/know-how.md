# 项目知识

## 来源与筛选依据

本库的起始清单来自用户授权整理的已安装技能：用户维护目录中的通用包，以及当前启用的插件技能。插件缓存中未启用的其他版本或隐藏内部技能不自动收入。

本地维护区的 15 个包：`arch-roadmap`、`architecture-plan-synthesis`、`best-price`、`drive-project-handoff`、`experiment`、`guide-me`、`intel-rank`、`premortem`、`product-review`、`project-plan-audit`、`razor`、`tech-review`、`think-twice`、`ui-ux-design-suite`、`verify`。

其中 12 个有用户提供的本地 ZIP 包来源；`architecture-plan-synthesis`、`project-plan-audit`、`drive-project-handoff` 有本地定制创建与安装记录。正文以实际安装版为导入基线，后续本地修订可能不同于最初 ZIP。`user-maintained-installation` 说明维护来源，不宣称法律意义上的全部原创。原始包中引用第三方方法、项目或资料不改变对应权利；不得把引用误当成可复制其实现的许可。

两处用户技能目录中 12 个同名包在盘点时内容一致，按 ID 去重。移除 `agents/openai.yaml` 等平台展示配置，保留实际引用的资料、模板、资源与通用脚本。不要把本地安装路径、会话记录或原始压缩包上传作为来源证明。

## 外部来源策略

外部技能只登记引用。已定位来源包括 Intent、Impeccable、Taste、Emil Kowalski Skills、UI UX Pro Max、Vercel Agent Skills、Anthropic Skills、Alibaba Cloud AIOps Skills、Superpowers、Vercel Plugin、Supabase Plugin 和 OpenAI Plugins。项目地址、版本、入口与核对信息以 catalog 为准。

`name`、目录名、安装别名可能不同。例如 Taste 的 `design-taste-frontend` 在核对版本位于 `skills/taste-skill/SKILL.md`，不是历史 experimental 目录；Vercel 的 `vercel-react-best-practices` 也不同于目录名。必须完整读取 frontmatter 验证映射，不能仅凭文件路径猜测。

登记的是核对时的上游快照，不保证还原本机插件定制版。第三方许可证字段可能来自仓库元数据，具体文件许可优先；未知许可不授权复制。升级时重新核验，不复用过期结论。

OpenAI Plugins 的公开版本中已找到 Google Drive 的 5 个和 Notion 的 3 个同名入口，完整读取后登记固定版本。`notion:notion-database-designer` 与 `notion:notion-weekly-project-digest` 在核对快照中没有同名入口，因此保留为 `reference-only`，不使用旧版 knowledge-capture 等相似技能替代。当前登记共 15 个本地技能、89 个外部固定版本引用、2 个仅供参考条目。

## 不纳入本版的分发包

以下判断针对当前安装的具体版本，不表示对应领域或服务只能在 Codex 使用。

| 分发包或技能组 | 排除原因 |
| --- | --- |
| 系统 imagegen、openai-docs、skill-creator、skill-installer | 当前包面向平台工具、Codex 配置/安装或系统技能制作；未作为通用包迁移 |
| computer-history、visualize | 依赖当前客户端历史访问或专属可视化运行时 |
| documents、pdf、presentations、spreadsheets、excel-live-control、template-creator | 当前分发绑定文档会话、制品运行时、宿主依赖或专属编辑能力；不将通用文件格式等同于包可移植 |
| figma 全部当前技能 | 绑定此分发的 use_figma 等工具协议及插件运行时，未核实可独立分发的同版来源 |
| pages | 依赖 ChatGPT Space/Page 及其调度、写入能力 |
| product-design | 当前包含专属插件路由与运行时，且标注 Proprietary；不复制其原文件 |
| sites | 依赖专属 Sites 项目、凭据和发布流程 |
| plugin-management | 管理宿主插件状态与连接授权 |
| work-pets | 依赖专属宠物制品与账户状态 |

无技能正文的连接器不作为技能迁移。后续若有公开、可移植、许可明确的对应包，应按正常新增流程登记，不能自行借用同名第三方包冒充原版。

## 必要能力与通用性

`best-price` 是用户维护的服务协议技能，需要可访问的 Best Price 服务和相应授权，不适用于无法访问该服务的纯网页聊天环境。其 scripts 路径属于外部服务 checkout，不是本技能包漏带的脚本。
`drive-project-handoff` 需要授权 Drive 能力，Linear 为有对应项目时的可选联动；它不改变 Skill Hub 的 GitHub 唯一入口，也不建立技能 Drive 镜像。
项目审计与架构综合使用历史上下文时应选择当前环境可用工具，不能强制要求某个厂商的历史插件。

## 已采用的通用化修正

- `intel-rank` 删除重复的元数据段，保留完整工作方法。
- 两个项目规划/审计技能把专有历史工具名改成可用历史检索工具。
- UI/UX 套件说明服从本库的显式调用规则；内置 23 个 fallback 仍是普通参考文档，不成为 23 个独立技能。
- Best Price 的相对服务脚本路径明确为 `./scripts/...`；Drive/Linear 的链接模板改为文字占位，避免表现为真实断链。

技能正文原有的适用场景描述不意味着自动调用。ENTRY 统一决定何时加载；必要依赖按需读取，不自动安装缺失外部技能。

## 验证边界

入口可读取、校验器通过、技能工作流执行成功、外部系统实际生效、跨客户端可用是不同证据。结构校验不代替技能效果或客户端接入验收。
UI/UX 包原校验脚本把通配符当作文件名，且仅统计旧 subskills。仓库版本已修正为核验通配符实际命中，并逐个检查 manifest 中 23 个 `internal_fallback_playbooks` 文件；本库校验器也检查该清单。缺失 fallback 必须失败，不能把“0 subskills”理解成已检查全部 fallback。
