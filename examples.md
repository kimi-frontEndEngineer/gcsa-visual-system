# GCSA 视觉体系样例

这些样例展示产出深度与结构，不规定具体框架。使用真实项目资料替换占位内容，不复制产品叙事。

## 样例一：新建安全产品官网

### 输入

```text
为 GCSA AI Gateway 设计官网首页。面向企业技术负责人，主目标是申请试用。
产品能力：多模型路由、数据脱敏、策略审计。要求深浅主题与移动端。
```

### 推荐输出

```markdown
视觉命题：把每次模型调用表现为一条经过策略闸门验证的可信路径。

主锚点：Hero 右侧不是通用聊天框，而是“请求 → 脱敏 → 策略 → 模型”的实时路径图。

页面节奏：
1. Hero：一句定位、两个可信证据、单一主 CTA“申请试用”、路径图。
2. 证据带：延迟、策略命中率、供应商覆盖；不包成三张大卡。
3. 机制区：以一条纵向请求链解释治理过程。
4. 场景区：按研发、安全、合规三类角色切换，不再重复能力卡片。
5. 信任与 CTA：审计留痕、部署方式、最终申请入口。

品牌继承：#00BBCC primary、近黑深色背景、Orbitron 只用于产品名和短标题。
产品差异：视觉语义是“策略闸门与请求路径”，避免盾牌、锁和代码雨。
动效：请求节点依次通过；reduced-motion 下直接显示最终状态。
验收：375/768/1440px，无横向滚动；两主题路径状态均清楚；CTA 全页只有一个 primary 层级。
```

## 样例二：控制台告警页审查

### 输入

```text
审查一个深色威胁告警列表：顶部 6 个指标卡，下面有筛选区、表格和右侧详情抽屉。
当前问题是“看起来很乱”。
```

### 推荐输出

```markdown
结论：混乱主要来自三个层级同时争夺注意力，而不是颜色不够统一。

[P1] 告警严重度只靠红/橙/黄区分
位置：表格严重度列、抽屉标题。
原因：色盲与低亮度环境下难辨识，且无法快速扫读。
修改：增加 Critical/High/Medium 文案和稳定图标形状，颜色只作强化。
验收：灰度截图中仍能正确区分严重度。

[P1] 六个指标卡与页面主任务竞争
位置：页面标题下方。
原因：等尺寸、等边框、等亮度导致无主次。
修改：保留一个“待处置”主指标；其余压缩为无容器的指标带。
验收：首次扫视时先看到待处置数量，再进入筛选和列表。

[P2] 筛选、批量操作与创建规则都使用实心 primary
修改：当前任务只保留一个 primary；筛选用普通控件，批量操作按选择后出现，创建规则降为 secondary。

验证范围：深/浅主题、键盘遍历、无结果、加载失败、详情抽屉打开、1280px 与 1440px。
```

## 样例三：移动安全工具首页

### 输入

```text
设计一款 GCSA 移动端隐私扫描工具首页，用户打开后要立即开始扫描。
```

### 推荐输出

```markdown
视觉命题：从设备表面向内收敛风险，而不是展示复杂安全仪表盘。

结构：
- 顶部：产品名、最近扫描时间、设置入口。
- 中部：设备轮廓与三层风险环，作为唯一主视觉。
- 底部拇指区：44px 以上“开始扫描”主按钮。
- 扫描后：同一主视觉渐进显示检查阶段，避免跳到另一套页面结构。

交互状态：idle / scanning / paused / complete / partial failure / offline。
触觉：开始和完成可使用一次轻反馈；每个扫描项不震动。
主题：跟随系统；亮色减少 glow，依靠层级和边界。
验收：最大动态字体、底部 safe area、横屏、系统返回手势、reduced motion。
```

## 样例四：品牌发布主视觉

### 输入

```text
为 GCSA 全球节点能力发布制作 16:9 发布会封面和社交媒体方图。
```

### 推荐输出

```markdown
视觉命题：一组经过验证的节点形成稳定、可追踪的全球信任网络。

构图：左侧标题与发布日期，右侧偏心节点网络；主节点形成 GCSA 盾牌轮廓的负空间，而不是直接放大 Logo。
颜色：近黑底，#00BBCC 作为路径焦点，成功节点使用克制绿色；不使用多彩渐变。
字体：Orbitron 用于英文短标题，正文与日期使用中性 sans；中文保持正常字距。
适配：16:9 保留右侧网络展开；1:1 裁切时将标题上移、减少外围节点，不缩小全部内容。
禁区：地球素材、代码雨、六边形边框、无意义 HUD 标尺。
导出检查：小尺寸缩略图标题可读，Logo 留白正确，深浅展示背景均有边界。
```

## 组件规格输出模板

```markdown
组件：{名称}
职责：{只解决一个什么问题}

Anatomy：{组成部分与语义}
Variants：{必要变体，不按页面复制变体}
Sizes：{视觉尺寸 + 点击热区}
States：default / hover / pressed / focus-visible / disabled / loading / error
Theme：{深浅主题 token 映射}
Responsive：{窄屏与宽屏变化}
Accessibility：{角色、名称、键盘、焦点、公告}
Motion：{时长、属性、reduced-motion}
Do：{正确使用}
Don't：{误用边界}
验收：{可观察结果}
```

## 设计系统输出模板

```markdown
# {产品} Visual Direction

## Brief
- Surface:
- Audience:
- Primary task / CTA:
- Density:
- Theme:
- Constraints:

## Visual thesis
一句话说明视觉隐喻与产品能力的关系。

## Foundation
- Color roles:
- Typography roles:
- Spacing / radius / elevation:
- Icon and illustration language:
- Motion rhythm:

## Composition
- Primary anchor:
- Page or screen rhythm:
- Responsive transformation:

## Product differentiation
- Inherit from GCSA:
- Make product-specific:
- Explicitly avoid:

## States and accessibility
- Interaction states:
- Empty/loading/error/success:
- Keyboard/touch/screen reader:
- Reduced motion:

## Acceptance criteria
以视口、主题、状态和可观察行为描述。
```
