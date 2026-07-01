from PIL import Image, ImageDraw, ImageFont
import math

# 创建高清画布 1920×1080
width, height = 1920, 1080
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# 尝试加载字体， fallback到默认
font_paths = [
    "simhei.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]
font_title = font_step = font_text = None
for fp in font_paths:
    try:
        font_title = ImageFont.truetype(fp, 48)
        font_step = ImageFont.truetype(fp, 36)
        font_text = ImageFont.truetype(fp, 28)
        break
    except:
        continue
if font_title is None:
    font_title = ImageFont.load_default(size=48)
    font_step = ImageFont.load_default(size=36)
    font_text = ImageFont.load_default(size=28)

# 标题
title = "滚柱丝杠完整选型步骤（简洁版）"
draw.text((width//2, 60), title, font=font_title, fill="#003366", anchor="mm")

# 步骤内容
steps = [
    {
        "num": "步骤1",
        "title": "确定工况载荷",
        "content": "计算轴向最大负载、平均载荷、冲击系数\nFmax = 工作推力 × 安全系数(1.2~1.5)"
    },
    {
        "num": "步骤2",
        "title": "核算转速与行程",
        "content": "最高转速、往复行程、运行循环次数\n预估总工作寿命小时数"
    },
    {
        "num": "步骤3",
        "title": "选定结构类型",
        "content": "循环方式：端盖式/插管式\n传动形式：行星滚柱丝杠（重载）/普通滚柱丝杠"
    },
    {
        "num": "步骤4",
        "title": "初步选定公称直径&导程",
        "content": "由推力选直径；由运行速度选定导程\n兼顾速度、刚度、自锁要求"
    },
    {
        "num": "步骤5",
        "title": "校核额定动载荷与寿命",
        "content": "L10寿命校核，保证疲劳寿命满足使用年限\n动载荷Ca ≥ 当量载荷"
    },
    {
        "num": "步骤6",
        "title": "压杆稳定性+临界转速校核",
        "content": "细长杆压杆屈曲校验\n防止高速下共振、挠曲失稳"
    },
    {
        "num": "步骤7",
        "title": "精度等级与螺母配置",
        "content": "C1~C5精度等级选择\n单螺母/双螺母预紧消除间隙"
    },
    {
        "num": "步骤8",
        "title": "最终确定型号规格",
        "content": "整理参数：直径、导程、长度、预紧形式、精度\n完成正式型号选型"
    }
]

# 绘制步骤方框
box_w = 820
box_h = 130
start_y = 140
gap_y = 25
colors_fill = ["#e8f2fc"] * 8
color_line = "#004488"

for i, s in enumerate(steps):
    y0 = start_y + i*(box_h + gap_y)
    x0 = (width - box_w) // 2
    # 矩形框
    draw.rounded_rectangle([x0, y0, x0+box_w, y0+box_h], radius=12, fill=colors_fill[i], outline=color_line, width=2)
    # 步骤编号
    draw.text((x0+30, y0+22), s["num"], font=font_step, fill="#003366")
    # 标题
    draw.text((x0+160, y0+22), s["title"], font=font_step, fill="#002244")
    # 文字内容
    draw.text((x0+30, y0+70), s["content"], font=font_text, fill="#222222")

# 简易滚柱丝杠示意图（右侧小简图）
cx, cy = 1600, 540
# 丝杠轴
draw.line([cx-120, cy, cx+120, cy], fill="#333333", width=6)
# 螺母套筒
draw.ellipse([cx-70, cy-45, cx+70, cy+45], outline="#004488", width=4)
draw.text((cx, cy+70), "行星滚柱丝杠", font=font_text, fill="#003366", anchor="mm")

# 箭头串联步骤
arrow_color = "#004488"
for i in range(len(steps)-1):
    y1 = start_y + (i+1)*box_h + i*gap_y
    mid_x = width//2
    draw.line([mid_x, y1, mid_x, y1+gap_y], fill=arrow_color, width=3)
    # 箭头三角
    tri = [
        (mid_x-12, y1+gap_y),
        (mid_x+12, y1+gap_y),
        (mid_x, y1+gap_y+16)
    ]
    draw.polygon(tri, fill=arrow_color)

# 保存图片
img.save("滚柱丝杠选型步骤高清图.png", dpi=(300, 300))
print("图片已生成：滚柱丝杠选型步骤高清图.png")
