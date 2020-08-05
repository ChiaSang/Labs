import datetime
import os

import xlwt

today = datetime.date.today().strftime('%Y%m%d')
path = "/mnt/d/Documents/DAI" + today
os.chdir(path)
files = os.listdir(path)
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        with open(path+"/"+file, 'r', encoding='utf-8') as f:
            info = f.readlines()
            runtime_item = info[61].rstrip()
            temperature_item = info[33].rstrip()
            fan_item = info[42].rstrip()
            power_item = info[48].rstrip()
            cpu_item = info[25].rstrip()
            temp_info1 = info[36].rstrip()
            temp_info2 = info[37].rstrip()
            temp_info3 = info[38].rstrip()
            temp_info4 = info[39].rstrip()
            fan_info = info[45].rstrip()
            power_info1 = info[49].rstrip()
            power_info2 = info[50].rstrip()
            cpu_info1 = info[27].rstrip()
            cpu_info2 = info[28].rstrip()
            cpu_info3 = info[29].rstrip()
            cpu_info4 = info[30].rstrip()

# ---------------------------------------------------------------------------巡检项目基本信息
            print(runtime_item[19:], temperature_item[:-1],
                  fan_item[:-1], cpu_item[:15], power_item[:7],
                  cpu_info1[3:12], cpu_info2[3:12], cpu_info3[3:12],
                  cpu_info4[3:12], temp_info1[18:20], temp_info2[18:20],
                  temp_info3[18:20], temp_info4[18:20],
                  power_info1[24:29], power_info2[24:29], fan_info[20:30])


workbook = xlwt.Workbook()  # 创建表格
workbook = xlwt.Workbook(encoding='utf-8')
Switch = workbook.add_sheet('Sheet 1')
# ------------------------------------设置单元格的边框格式
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

# ------------------------------------设置单元格的列宽
Switch.col(0).width = 256 * 30  # Set the column width
Switch.col(1).width = 256 * 20  # Set the column width
Switch.col(2).width = 256 * 20  # Set the column width
Switch.col(3).width = 256 * 50  # Set the column width

# ------------------------------------设置单元格的对齐格式

style = xlwt.XFStyle()  # Create Style
style.borders = borders  # Add Borders to Style

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = False
font.height = 20 * 12

al = xlwt.Alignment()
al.horz = 0x02      # 设置水平居中
al.vert = 0x01      # 设置垂直居中

style.alignment = al
style.font = font


# ------添加附加样式
# add_style = "font: bold off; font: heigh 20 * 10"
# style_item = xlwt.easyxf(add_style)


Switch.write_merge(0, 0, 0, 3, '许昌区域技术中心自动化巡检一览表', style)
Switch.write(1, 0, '设备名称', style)
Switch.write(1, 1, '巡检项目', style)

# Switch.write(1, 2, '巡检结果', style)
Switch.write_merge(1, 1, 2, 3, '巡检结果', style)
Switch.write_merge(2, 16, 0, 0, 'Co-XCxuc-FH-S7803-1', style)
Switch.write(2, 1, '运行时间', style)
Switch.write_merge(3, 6, 1, 1, '设备温度', style)
Switch.write_merge(7, 8, 1, 1, '风扇状态', style)
Switch.write_merge(9, 10, 1, 1, '电源状态', style)
Switch.write_merge(11, 14, 1, 1, 'CPU状态', style)
Switch.write(15, 1, '端口状态', style)
Switch.write(16, 1, '路由条目', style)
# ---insert item
# ---fill item info in excel blank one bye one
Switch.write_merge(2, 2, 2, 3, runtime_item[19:], style)
Switch.write(3, 3, temp_info1[18:20], style)
Switch.write(4, 3, temp_info2[18:20], style)
Switch.write(5, 3, temp_info3[18:20], style)
Switch.write(6, 3, temp_info4[18:20], style)
Switch.write(7, 2, fan_item[:-1], style)
Switch.write(8, 2, fan_info[20:30], style)
Switch.write(9, 3, power_info1[24:29], style)
Switch.write(10, 3, power_info2[24:29], style)
Switch.write(11, 2, cpu_info1[3:12], style)
Switch.write(12, 2, cpu_info2[3:12], style)
Switch.write(13, 2, cpu_info3[3:12], style)
Switch.write(14, 2, cpu_info4[3:12], style)
workbook.save(path + '.xls')
