import qrcode
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=3,
    border=2,
)
qr_asset_info = '名称：{0} 型号：{1}\n所有人：{2} 部门：{3}'
qr.add_data(qr_asset_info)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

with Image.open('/Users/victor/Desktop/AssetSystem/apps/asset/static/BOSH_model.jpg') as background:
    background.paste(img, (22, 11))
    font1 = ImageFont.truetype("/Users/victor/Desktop/AssetSystem/apps/asset/static/FZFSJW.TTF", 20)
    font2 = ImageFont.truetype("/Users/victor/Desktop/AssetSystem/apps/asset/static/FZFSJW.TTF", 30)
    bd = ImageDraw.Draw(background)
    bd.text((160, 30), '名称：办公组合柜', (0, 0, 0), font=font1)
    bd.text((160, 65), '型号：MKD-1224', (0, 0, 0), font=font1)
    bd.text((160, 100), '所有人：杨小姐', (0, 0, 0), font=font1)
    bd.text((160, 135), '部门：信息化办公室领导小组', (0, 0, 0), font=font1)
    bd.text((160, 170), '标识码：GDFT543H', (0, 0, 0), font=font1)
    bd.text((160, 205), '日期：2020-08-19', (0, 0, 0), font=font1)
    bd.text((30, 125), '许昌市', (0, 0, 0), font=font2)
    bd.text((30, 160), '统计局', (0, 0, 0), font=font2)
    bd.text((30, 195), '资产统', (0, 0, 0), font=font2)
    bd.text((30, 230), '一标识', (0, 0, 0), font=font2)
    buffer = BytesIO()  # 创建一个BytesIO临时保存生成图片数据
    background.save(buffer, format="PNG")  # 将图片字节数据放到BytesIO临时保存
    image_stream = buffer.getvalue()  # 在BytesIO临时保存拿出数据
    background.show()