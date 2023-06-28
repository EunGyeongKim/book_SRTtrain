
import asyncio
import sys
# pip install SRTrain
from SRT import SRT
from SRT import SeatType
import time
# pip install python-telegram-bot
import telegram
import nest_asyncio
nest_asyncio.apply()


async def main():
    token = 'token'
    bot = telegram.Bot(token=token)
    chat_id = 111111
    await bot.sendMessage(chat_id=chat_id, text='예약시작')
    flag = False
    i = 0
    while flag == False:
        try:
            
            i += 1
            print(f"{i}번째 시도")
            srt = SRT("010-0000-0000", 'password!')
            dep = '정읍'
            arr = '영등포'
            date = '20230401'
            time = '130000'
            trains = srt.search_train(dep, arr, date, time)
            
            reservation = srt.reserve(trains[0], special_seat=SeatType.GENERAL_ONLY)
            print(reservation)
            
            flag = True
            await bot.sendMessage(chat_id=chat_id, text='예약성공')
            if i == 3:
                break
        except:
            pass
        
asyncio.run(main())

