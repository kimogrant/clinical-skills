# Hippocrates（clinical-skills）

面向 AI Agent 的**全科临床技能包**：病历、诊断、处方审查、检验解读、医患沟通、循证医学与临床计算器。

面向 AI Agent 的**全科临床技能包**：病历、诊断、处方审查、检验解读、医患沟通、循证医学与临床计算器。

---

## 安装

```bash
git clone https://github.com/kimogrant/clinical-skills.git
cd clinical-skills
chmod +x skill.sh
./skill.sh install /path/to/your/project
```

安装路径：`your-project/.cursor/skills/clinical-skills/`（须包含 `references/`）。

重载 Cursor 后使用 **`/clinical-skills`**。

---

## 模块

| # | 内容 |
|---|------|
| 1 | 临床文书（SOAP、入院记录等） |
| 2 | 诊断推理（VINDICATE-M、鉴别诊断） |
| 3 | 处方五步审查 |
| 4 | 检验与影像 |
| 5 | 沟通（SPIKES 等） |
| 6 | 循证（PICO、证据表） |
| 7 | 计算器（Wells、CURB-65、CHA₂DS₂-VASc 等） |

模板在 `references/module-*.md`，由 Agent **按需加载**，勿一次读入全部。

---

## 安全

- **急症**：先输出 HALT 转急诊文案（911/120），**不要**先写长免责声明  
- **非急症**：Pre-Action 清单齐全后才生成内容  
- 详见 `references/safety-boundaries.md`

---

## 版本

当前 **1.2.0**（见 `VERSION`）：Agent Skills 规范 frontmatter、模块拆分、急症硬规则。

---

## 免责声明

仅供临床参考，不能替代执业医师判断。急症请立即就医。

MIT · [LICENSE](LICENSE)
