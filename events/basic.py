from line_bot_api import *


def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 13,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]

    text_message = TextSendMessage(text='''$ 寶石服飾 $
唯美、氣質、清新、時尚，女孩們是待琢磨的寶石，舒適自在的購物空間，韓國嚴選材質，期待與妳的美麗邂逅。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )

    about_us_img = 'https://imgur.com/LTLB1La'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])


def location_event(event):
    location_message = LocationSendMessage(
        title='寶石服飾',
        address='高雄市左營區裕誠路338號',
        latitude=22.66540,
        longitude=120.30776
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)