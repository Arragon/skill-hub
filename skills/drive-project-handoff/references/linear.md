# 已有 Linear 项目的双向联动

## 激活与绑定

仅在 Linear 服务可用、对应项目确实存在、身份可验证且所需读写已授权时启用。先实际读取服务、项目与相关 issue；不能仅凭连接标志或同名项目确认绑定。用既有 Drive/Linear 交叉链接、明确项目 ID、仓库/团队和用户提供的信息消歧；仍有多候选时询问。发现没有对应项目则继续 Drive 单独工作，不自行创建 Linear 项目。

已绑定项目的 Linear 暂不可用属于“待同步/无法核验”，不是悄悄退回 Drive-only 并报告成功。只读权限允许读取与准备补丁，不允许自动写描述、评论、issue 状态或权限。

把以下最小绑定加到项目 INDEX，不另建独立镜像库：

```yaml
linear_binding:
  status: active # unbound / unavailable / read_only
  workspace_id: <已核验ID或 unavailable>
  project_id: <实际Linear项目ID>
  project_url: <工具返回的真实链接>
  verified_at: <含时区时间>
  drive_index_file_id: <实际Drive文件ID>
  drive_index_url: <真实链接>
  ownership:
    specification_and_approved_decisions: drive
    execution_plan_status_and_issue_dependencies: linear
```

用户已有明确字段归属时保留其安排。绑定不是授权；本协议不扩展允许修改的项目、字段、受众或信息范围。

## 双向引用与唯一归属

默认 Drive 保存目标、完整规格、架构、批准决定与验收依据；Linear 保存执行计划、issues、任务状态、执行依赖与工作负责人。两者各自保留权威原件，对方只存最小摘要、影响和精确链接，不复制整套开发计划或全文规格。

- Drive 主题/STATE：“开发计划以 ABC-123：实现登录（填写真实 issue URL） 为准；关联验收 AC-04；上次核验状态/修订……”。已有里程碑/项目计划同样使用真实链接和对象 ID。
- Linear 项目/相关 issue：“规格参考 登录接口（填写真实 Drive 文档 URL），doc_id=P1:auth，章节 AUTH-ERR-02「错误恢复」，采用修订 R4；关联验收 AC-04。”
- 使用真实 section/bookmark 链接时先验证目标；工具不支持 Drive Markdown 章节深链时只给文档链接+稳定章节 ID/标题，不伪造 `#slug`。文件重命名仍按 file ID 找回。
- 保留机器稳定 ID 与可读标题；Linear 的 `ABC-123`、内部 issue ID、URL 一起登记，不能只依赖可改标题。评论/描述链接也用工具实际返回值。

## 双向变更检查

每次恢复、保存和运行中的检查点，都读取上次联动基线之后与当前任务相关的两边变化。支持可靠增量查询时使用；否则按绑定对象 ID 直接读取，不只看搜索摘要。第一次没有基线就读取相关对象当前实际内容，并标明历史覆盖范围未知，不装作全量审计。

维护最小影响映射 `Drive doc_id/section_id/decision_id ↔ Linear project/issue ID`，放在主题或 INDEX 的关联处。已完成对象不重复翻查；任务涉及的依赖、安全约束或验收变化仍必须核验。

- Drive 改了批准规格/验收：定位相关 Linear issues，更新引用、摘要、验收或依赖；若增加工作/改承诺超出授权，只提出变更并记待决，不擅自改排期或指派人员
- Linear 改了执行计划/状态/依赖：更新 Drive STATE 的最小进展、阻塞和下一步摘要，引用 Linear 权威计划；保持完整设计原文
- Linear 标 Done 不等于验收已验证：记录其实际状态与证据缺口，不能据此伪造测试通过，也不未经授权反改 Done
- 在非归属侧发现新提案：保存提案/观察并链接；有明确批准与范围后才更新归属侧。归属不是忽略新证据的理由，冲突仍按批准来源、适用范围和实际证据判断
- 更新后追踪受影响的引用/验收/依赖；未核验的影响标 needs_review，不能宣布整个项目全部一致

## 一起更新，不冒充原子事务

旧同步记录只能说明当时记录了什么，不能替代这次实际核验；未获取旧变化内容或当前正文时，写“此前记录成功，本次核验待完成”。结果未知继续标 unknown，不擅自改成失败。

Drive 与 Linear 无共同事务。为一次语义变化复用 `sync_change_id`，与普通 `change_id` 关联；同一变化重试沿用 ID；新的独立语义变化使用新 ID，不能把今天的新决定塞进旧失败操作。联动记录保存在 STATE 的紧凑同步区，完整待处理补丁必要时单独保存：

```yaml
sync_change_id: sync-P1-032
source: <Drive或Linear对象ID、修订/更新时间、证据>
base_versions: {drive: <实际基线>, linear: <实际基线>}
impacted_objects: [<双方稳定ID>]
changes: <本次需要对齐的最小语义变化>
drive: {status: pending, verified_revision: null}
linear: {status: pending, verified_revision: null}
next_action: <补写哪一边，先读取什么>
```

可用状态为 pending/verified/failed/unknown；同一侧多个对象需逐项记录，不把一侧部分成功折叠为 verified。仅更新时间并不是内容相同的证明，条件不足时记录核验过的字段/内容摘要。

1. 读取双方基线与既有同步记录，判断相同变化是否已应用；规划本次影响范围
2. 按各对象的安全增量协议写归属侧，并重读验证；来源本来已变更时只核验来源，不再写一次
3. 更新另一侧的关联摘要/计划/引用，再重读验证；保留人工无关编辑
4. 双方目标字段和引用全部核验后，才把本次联动标 verified；Drive 发布入口仍最后更新
5. 并发变化以新基线做三方合并；不冲突的字段合并，批准/范围/承诺等实质冲突询问，不用“最新时间戳胜出”

优先更新已有明确维护区或指定描述，不每次追加“同步完成”评论。确有授权且评论是必要途径时，用稳定标识查重并复用既有记录；评论创建超时先查实际评论，不能盲重发。缺少安全写入能力时保留补丁，不降低安全边界。

任一边失败或结果未知：留下待对齐对象、基线、已成功部分、下次恢复步骤；不能回执“全部同步”。如果连记录都无法写回，在已授权本地交接文件和用户回执中保留。下一次运行/恢复时优先读取双方实际状态，跳过已应用变化，只重试缺失部分；在当前会话可安全恢复时继续处理，不能仅因需要重试就另建后台监控。阻塞依赖未同步决定的危险操作；不阻塞与其无关的安全工作。

## 示例：双向、失败、重试

已有 P1 ↔ Linear 项目 L1，D1 位于 Drive AUTH-ERR-02，执行 issue 为 ABC-123。

1. Drive 获批准增加 AC-04“断网后保留表单”。读取 ABC-123 后，以 sync-P1-033 更新 Drive 决定和 Linear 验收/引用；两边读回一致才回执已同步
2. 开发者在 Linear 把 ABC-123 改为 Blocked，新增依赖 ABC-129。下一次检查读取这些实际字段，更新 Drive STATE 的阻塞与下一步，并链接两条 issue；不重写整份规格
3. Linear 更新已成功但 Drive 写入失败：回执“Linear 已验证；Drive STATE 待同步”，记录 sync-P1-034 的未完成目标
4. 重试前重读，发现 Linear 另有人工新增备注，保留它；若原同步变化已在 Linear，跳过写入和重复评论，只应用 Drive 缺失增量并核验。若 Drive 此时出现相反批准决定，先解决冲突而不是旧补丁覆盖
