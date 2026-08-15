# Ecommerce AI OS — Software Architecture Boundary Baseline V0.1

- **版本**：V0.1
- **状态**：Not Yet Designed
- **文档类型**：Software Architecture Boundary Baseline
- **目标路径**：`docs/03_software/00_SOFTWARE_ARCHITECTURE.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档当前不设计完整 Software Architecture。

它只负责明确：

> **Software Architecture 现在还没有被正式设计，当前仓库中的代码目录只是一套 Project Scaffold，不能被解释为已批准的软件架构。**

---

# 1. 当前层级关系

当前设计顺序：

```text
Product Requirements
        ↓
Product Architecture
        ↓
System Architecture
        ↓
Software Architecture
        ↓
Code / Schema / Tests
```

含义：

- Product Architecture 先回答用户能做什么；
- System Architecture 再回答系统由什么组成；
- Software Architecture 最后决定这些系统职责如何落成软件；
- Code / Schema / Tests 记录已经真正实现的事实。

---

# 2. 当前 Software Architecture 状态

当前状态：

# **Not Yet Designed**

原因：

- Product Architecture 已有工作基线；
- System Architecture V0.2 已完成当前 Candidate 边界收敛，但仍不是 Approved；
- System Detailed Contracts 尚未设计；
- Capability / Provider / Skill Contract 尚未设计；
- 选定 Vertical Slice 所需的 Minimal Software Architecture 尚未设计；
- 现在过早冻结软件架构会反过来污染 System Architecture。

---

# 3. 当前 src 只是 Project Scaffold

当前仓库可能存在：

```text
src/ecommerce_ai_os/
├── kernel/
├── capabilities/
├── skills/
├── providers/
├── services/
└── applications/
```

这些目录当前只代表：

> **Project Scaffold / Candidate Package Boundary**

它们不代表：

> **Approved Software Architecture**

---

# 4. 禁止从当前目录反推 System Architecture

不能因为存在：

```text
src/ecommerce_ai_os/kernel/
```

就认为：

> Kernel Python package 已经设计完成。

不能因为存在：

```text
src/ecommerce_ai_os/services/
```

就认为：

> Knowledge / Evidence / Research 一定全部进入同一个 services package。

不能因为存在：

```text
src/ecommerce_ai_os/applications/
```

就认为：

> Chat / Workspace / Operator Console 的软件结构已经确定。

原则：

> **Software Scaffold 不得反向定义 System Architecture。**

---

# 5. 当前尚未设计的软件问题

以下全部保持：

```text
Python package design        Not Yet Designed
Module boundaries            Not Yet Designed
Interface implementation     Not Yet Designed
Dependency direction         Not Yet Designed
Dependency injection         Not Yet Designed
Sync / Async                 Not Yet Designed
Task execution model         Not Yet Designed
Event / Message model        Not Yet Designed
Database                     Not Yet Designed
Persistence                  Not Yet Designed
API                          Not Yet Designed
Deployment                   Not Yet Designed
Process topology             Not Yet Designed
Caching                      Not Yet Designed
Queue                        Not Yet Designed
Scheduling                   Not Yet Designed
Error model                  Not Yet Designed
Configuration model          Not Yet Designed
Observability                Not Yet Designed
Security implementation      Not Yet Designed
Storage implementation       Not Yet Designed
Schema strategy              Not Yet Designed
Migration strategy           Not Yet Designed
```

---

# 6. 当前不批准的技术结论

当前不因为流行或未来可能需要，就提前批准：

- LangGraph；
- MCP Runtime；
- RAG；
- Vector Database；
- Kafka；
- Redis；
- Celery；
- Temporal；
- Kubernetes；
- Event-driven Architecture；
- Microservices；
- Monolith；
- Postgres；
- SQLite；
- Any specific Agent Framework。

这些都属于后续 Software Architecture 决策。

---

# 7. Software Architecture 未来应该回答什么

等 System Architecture 继续收敛后，本文件未来需要回答：

- Python package 如何拆；
- module dependency 如何控制；
- Stable Core 如何实现；
- Skill 如何加载；
- Capability Contract 如何实现；
- Provider Resolution 如何实现；
- Foundation Service 如何组织；
- Runtime 如何执行 Task；
- State / Checkpoint 如何保存；
- Error 如何传播；
- Event / Message 是否需要；
- Persistence 如何设计；
- Schema 如何版本化；
- API 如何暴露；
- Application 如何调用；
- 测试边界是什么；
- Deployment 如何组织。

当前这些都不展开。

---

# 8. 实现事实的权威

未来一旦进入实现阶段：

```text
Architecture Document
→ 解释为什么这样设计、边界是什么

Code / Schema / Tests
→ 解释现在实际上实现了什么
```

如果软件架构文档与已经实现的代码事实冲突：

> **实现事实必须被识别，文档需要更新。**

但低层实现也不能悄悄重新定义已经批准的高层架构。

---

# 9. 当前 Software Architecture 的唯一批准边界

当前可以确认的只有：

```text
Product Architecture
        ↓
System Architecture
        ↓
Software Architecture
        ↓
Code
```

以及：

> 当前 `src/` 是 scaffold，不是最终架构。

其他软件设计全部：

**Not Yet Designed**

---

# 10. Human Review Gate

当前文档状态：

# **Not Yet Designed / Boundary Baseline Only**

批准本文件只代表：

> **当前项目明确拒绝把现有空代码目录解释为正式 Software Architecture，并确认软件设计必须建立在 Product Architecture 与 System Architecture 进一步收敛之后。**

批准本文件不代表：

- Python 模块结构已批准；
- Runtime 已批准；
- Database 已批准；
- Event Model 已批准；
- API 已批准；
- Deployment 已批准；
- 可以开始全面实现。
