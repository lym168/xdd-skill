# 思维导图图片清单与备份计划

**更新时间**: 2026-05-22
**维护状态**: 待执行

---

## 图片清单

通过grep搜索所有包含阿里云OSS链接的文档：

### 已确认存在的图片

| 序号 | 文档路径 | 图片URL | 用途 | 状态 |
|------|---------|---------|------|------|
| 1 | career_design_meta_knowledge/2.0-认知os...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/g2y8qealozznbeol-... | 思维导图 | 🔴 需备份 |
| 2 | career_design_meta_knowledge/3.0-认知&机会...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/82xz94lp5bxqm6v7-... | 思维导图 | 🔴 需备份 |
| 3 | career_design_meta_knowledge/认知训练营第一讲...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/klrbn2w472pn5zyd-... | 思维导图 | 🔴 需备份 |
| 4 | career_design_meta_knowledge/认知训练营第五讲...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/p7g39586w559z654-... | 思维导图 | 🔴 需备份 |
| 5 | career_design_meta_knowledge/认知训练营第九讲...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/ro84nrr47jznkb3j-... | 思维导图 | 🔴 需备份 |
| 6 | career_design_meta_knowledge/认知训练营第十讲...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/pev8qd4wbzbqkgaw-... | 思维导图 | 🔴 需备份 |
| 7 | career_design_meta_knowledge/4.0-许单单的弟弟...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/58gmq68mvy8nzwoe-... | 思维导图 | 🔴 需备份 |
| 8 | origin_family/高考后...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/yg7k9w5p5am9xwd3-... | 思维导图 | 🔴 需备份 |
| 9 | origin_family/许单单-我的"穷人思维"...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/g2y8qeebelbqbeol-... | 思维导图 | 🔴 需备份 |
| 10 | origin_family/许单单-我们曾相信...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/47z39vp45jag9edg/39817210.png | PPT截图1 | 🔴 需备份 |
| 11 | origin_family/许单单-我们曾相信...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/47z39vp45jag9edg/39817211.png | PPT截图2 | 🔴 需备份 |
| 12 | origin_family/许单单-我们曾相信...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/47z39vp45jag9edg/39817212.png | PPT截图3 | 🔴 需备份 |
| 13 | origin_family/许单单-我们曾相信...md | tw-efficiency.biz.aliyun.com/api/export/get/v2/47z39vp45jag9edg/39817213.png | PPT截图4 | 🔴 需备份 |

**预估总数**: 至少13张图片（可能有遗漏）

---

## 备份执行计划

### Phase 1: 自动化下载（推荐）

```bash
#!/bin/bash
# backup_images.sh

# 创建备份目录
mkdir -p docs/assets/images/mindmaps
mkdir -p docs/assets/images/ppt

# 提取所有图片URL并下载
grep -r "tw-efficiency.biz.aliyun.com" docs/ --include="*.md" -o | sort -u | while read url; do
    filename=$(echo $url | md5sum | cut -d' ' -f1).jpg
    echo "Downloading: $url -> $filename"
    curl -s -o "docs/assets/images/mindmaps/$filename" "$url"
done
```

### Phase 2: 手动下载（备选）

如果自动化下载失败，按以下步骤：

1. 打开每个文档
2. 右键保存图片到 `docs/assets/images/` 对应目录
3. 记录原URL与新路径的映射

### Phase 3: Markdown替换

下载完成后，批量替换Markdown中的图片链接：

**旧格式**:
```markdown
![思维导图图片](https://tw-efficiency.biz.aliyun.com/api/export/get/v2/xxx.jpg)
```

**新格式**:
```markdown
![思维导图图片](../assets/images/mindmaps/hash.jpg)
```

**执行命令**:
```bash
# 创建替换脚本（需要先有URL到本地文件的映射表）
# 建议使用sed或Python脚本批量替换
```

### Phase 4: 验证

- [ ] 所有本地图片可正常访问
- [ ] Markdown渲染无误（图片显示正常）
- [ ] Git提交备份
- [ ] 更新元模型文档（标注备份完成）

---

## 备份优先级

| 优先级 | 文档 | 理由 |
|--------|------|------|
| P0 | 认知训练营全部（M1） | 核心方法论，使用频率最高 |
| P1 | 许单单访谈系列（M2） | 个人史，不可再生 |
| P1 | Satir原生家庭课程（M3） | 理论体系，使用频率高 |
| P2 | 冥想课程（M4） | 内容相对独立 |
| P3 | 商业思考（M5） | 单文档，已有本地备份可能性高 |

---

## 风险提示

1. **链接永久失效风险**: 阿里云OSS可能因欠费/过期被删除
2. **跨平台访问**: 本地备份后，GitHub等平台无法直接访问（需上传到图床）
3. **版本管理**: 图片应纳入Git LFS或单独仓库管理

---

## 下一步行动

- [ ] **立即**: 执行Phase 1自动化下载
- [ ] 1小时内: 验证下载完整性
- [ ] 3小时内: 完成Markdown替换
- [ ] 24小时内: Git提交并推送
- [ ] 本周内: 评估是否需要图床服务
