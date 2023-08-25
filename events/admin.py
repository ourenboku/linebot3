#裡面是所有管理者可以使用的功能
from line_bot_api import *

from models.reservation import Reservation
import datetime
from extensions import db
from models.user import User
#用來顯示預約名單,過濾的條件為is_canceled.is_(False)為False
def list_reservation_event(event):
    reservations = Reservation.query.filter(Reservation.is_canceled.is_(False),
                                            Reservation.booking_datetime > datetime.datetime.now(),
                                            ).order_by(Reservation.booking_datetime.asc()).all()

    reservation_data_text = '## 預約名單: ## \n\n'
    #跑每一筆的預約資料
    for reservation in reservations:
        reservation_data_text += f'''預約日期: {reservation.booking_datetime}
預約服務: {reservation.booking_service}
姓名: {reservation.user.display_name}\n'''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reservation_data_text))











#透過get_audience_group_list來取得預約過的受眾
def create_audience_group(event):

    audience_group_list = line_bot_api.get_audience_group_list(description='預約過看衣', create_route='MESSAGING_API')
    if len(audience_group_list) > 0:#如果有受眾的話,就透過delete_audience_group並帶入group_id來刪除現有的受眾
        line_bot_api.delete_audience_group(audience_group_list[0].audience_group_id)
    #接著再搜尋Reservation裡面是按摩調理的透過all()取得全部
    massage_reservations = Reservation.query.filter(Reservation.booking_service_category == '預約看衣').all()

    audiences = []

    for r in massage_reservations:
        audiences.append(r.user.line_id)#將所有有預約的line_id加入audiences串列中

    audiences = [{'id': line_id} for line_id in list(set(audiences))]#整理成dict的型態

    line_bot_api.create_audience_group('預約過看衣', audiences=audiences)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='受眾已建立，請查看後台'))