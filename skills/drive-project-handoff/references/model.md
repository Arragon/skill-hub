# 信息模型与可复制模板

导航：最小结构 → 标识与事实状态 → 冲突与依赖 → INDEX / OVERVIEW / STATE / 决定模板。

## 最小结构

从已有目录和文件开始；仅补缺项，不为套模板重建用户资料库。独立项目只需一个根入口；跨项目库可在其上加一个轻量项目目录。

```text
Knowledge/                         # 可选的跨项目库
  INDEX.md                         # 项目 ID → 各项目入口；共享政策链接
  common/                          # 仅真正共享的约束/规范
  projects/<project>/
    INDEX.md                       # 此项目唯一权威入口、文档 ID 映射
    OVERVIEW.md                    # 全局目标、边界、系统全貌与阶段
    STATE.md                       # 当前已验证状态、阻塞、下一步
    topics/                        # 按任务需要的完整主题文档
    artifacts/                     # 完整原件、图、报告、代码/日志等
    archive/                       # 失效版本/有意保留的快照；默认不读
```

上面是逻辑结构，不强制 Drive 文件类型或精确文件名。小项目可把 OVERVIEW、STATE 作为 INDEX 的明确章节；内容增长后再拆，不复制同一事实到多个“权威”位置。多个项目不可共用一个含糊的 STATE。

主题文档按责任拆分，例如产品/需求、架构、接口/数据、执行计划、验证。每份完整文档有一个权威归属；当前决定就近写在相关主题，不强制再建重复决策总表。STATE 只引用影响当前工作的决定。

## 标识、来源与事实状态

- `project_id`、`doc_id`、`decision_id`、`source_id`：首次确定后稳定复用，与标题和路径分离。Drive `file_id` 是存储定位，不等于逻辑 `doc_id`。重命名保持 file ID；真的迁移文件才更新映射。
- `session_id`：一次连续工作会话；同一会话多次保存沿用。`change_id`：一份语义变更的稳定标识，重试沿用；已经保存的结论不因新会话重复入库。
- `store_revision`：工具实际返回的修订/版本；`content_digest`：能获取时记录的内容摘要；`logical_revision`：资料库自己的内容版本。三者分开，不凭空把自增序号当 Drive 修订锁。
- 每个关键结论最少包含：内容、状态、适用范围、来源定位、依据/验证时间。批准决定还要批准者/批准来源；失效决定标 `superseded_by` 与生效范围。
- 来源优先用可验证文件 ID+修订+章节、提交/测试链接、消息或会话链接。没有可用链接时保存最短准确原话、角色、日期及“原始链接不可用”，不得编造可访问性。凭证和无关敏感信息不入库。

暂缓是处置状态，不是批准状态：未决方案用 `status: proposed` + `disposition: deferred`；待处理用 `disposition: open`。明确暂缓不等于方案已选定，也不推翻现行批准决定。

事实状态：`approved` 已批准决定；`proposed` 待批准方案；`observed` 实际观察/验证（注明环境和证据）；`unknown` 未知；`superseded` 已被明确替代；`deprecated` 已停用但保留定位。实施状态单独记录，如 `not_started/in_progress/blocked/reported_done/verified_done`，避免把“批准了方案”误写成“实现已验证”。

## 冲突与依赖

先比较来源权限、适用范围、批准状态、证据可靠性，再看时间。同一有权决策者对同一范围的明确新决定可替代旧决定；“考虑一下”“先比较”只是提案。实现与规格不同是偏差，不是自动批准的新规格；失败测试可推翻“已验证成功”的事实，不能自行授予更改需求的权限。不能确定的重大冲突放入 STATE 并问最小必要问题。

一项结论改变时，沿直接依赖检查目标、验收、计划、实现、测试与引用。只使受影响内容失效，保留无关决定；标注 `needs_review`，不能把尚未检查的整条链宣布更新完毕。

跨项目依赖引用 `project_id/doc_id@approved_revision`，注明适用章节、用途和负责人/批准来源。共享政策使用稳定 ID 和已采用修订；发现新版，先比较影响再批准升级，不能静默漂移。引用图有环时用 visited 集合停止重复读取，记录循环；若执行互相等待，则上报循环阻塞，不能递归加载整个库。每项目仍保留独立状态和入口。

## 模板：INDEX

```yaml
project_id: <稳定项目ID>
doc_id: <项目ID>:index
logical_revision: 1
publication_status: verified # 实际未验证时写 pending/partial/unknown
last_verified_at: <含时区时间>
last_change_id: <本次变更ID>
writer: <当前约定的写入者或 unknown>
documents:
  - doc_id: <项目ID>:overview
    role: overview
    file_id: <实际Drive文件ID>
    link: <实际链接>
    path: OVERVIEW.md
    mime_type: <实际文件类型>
    logical_revision: 1
    store_revision: <实际值或 unavailable>
    status: current
# 继续列 state 和必要主题/附件；为下一位读者给出 read_when
shared_dependencies: [] # doc_id、固定修订、范围、用途
```

入口正文补：一句话项目目标；必读顺序；任务→主题的导航；尚未验证的文件/冲突；停用项的旧 doc_id→新 doc_id 映射。一次多文件发布可额外记录 `publication_id` 与精确成员版本。

## 模板：OVERVIEW

```markdown
project_id: … | doc_id: …:overview | logical_revision: …
# 目标与成功标准
解决谁的什么问题；可判定的成功/验收条件
# 范围与非目标
硬约束；刻意不做的内容；批准来源
# 系统全貌
关键模块、关系、外部边界；完整架构文档链接
# 路线与当前阶段
整体里程碑；本阶段为何必要；下一阶段条件
# 有效决定与依赖
只列影响全局的 decision_id 和权威位置；共享政策固定版本
```

## 模板：STATE

```markdown
project_id: … | doc_id: …:state | logical_revision: …
session_id: … | last_change_id: … | as_of: …
# 当前目标与范围
本任务→项目成功标准的关联；本次授权边界
# 进展
已验证完成：结果 + 证据 + 环境/版本
正在执行：具体动作、产物位置、恢复点
报告完成但未验证：声明来源 + 缺失验证
# 阻塞、冲突与未知
问题；影响；需要谁做何决定；可继续的无关工作
# 下个安全动作
按顺序列少量动作，各含依赖、验收条件、证据位置
# 交接基线
读过的 doc_id@revision；未读关键来源；本地产物/待应用补丁
# 同步状态
已验证文件；部分成功/失败/未知文件；恢复方式
```

## 模板：主题内的当前决定

```yaml
decision_id: D-01
status: approved
# 未决方案另用 status: proposed + disposition: open/deferred
scope: <影响范围>
conclusion: <当前有效结论>
rationale: <足以解释取舍的最少依据>
approved_by_source: <批准来源定位>
evidence: [<实际证据定位>]
depends_on: [<doc_id或decision_id及修订>]
supersedes: []
needs_review: false
```

模板占位符只能用实际已知值替换；未知留 unknown/unavailable，不为了填满模板虚构信息。源文档完整保留，不要求改造成这些模板。
