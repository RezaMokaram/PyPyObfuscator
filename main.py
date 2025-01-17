import logging
import os

from receiver.receiver import receive_file_content
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from obfuscator import obfuscate

BOT_TOKEN: Final = "<bot token>"
BOT_USERNAME: Final = "<bot name>"

logging.basicConfig(format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
                    datefmt='%H:%M:%S',
                    encoding='utf-8',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("error %s update %s", context.error, update)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("user %s started bot", update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is a bot to obfuscate your python code\n"
             "Please just send your code here as a file like -> <file name>.py \n"
             "And do not write your code as message!!\n",
        reply_to_message_id=update.effective_message.id,
    )


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("hi")
    new_file = await update.message.effective_attachment.get_file()
    print(new_file.file_path)
    url_to_download = new_file.file_path
    plain_code = await receive_file_content(url_to_download)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="i am doing some thing ...\n\n" + plain_code,
        reply_to_message_id=update.effective_message.id,
    )

    obfuscated_code = obfuscate(plain_code)

    with open("Obfuscated_Code.py", "w") as obf_file:
        obf_file.write(obfuscated_code)

    with open("Obfuscated_Code.py", "rb") as obf_file:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=obf_file,
            filename="Obfuscated_Code.py",
        )
    
    os.remove("Obfuscated_Code.py")

    
    # # await context.bot.send_document(
    # #     chat_id=update.message.chat_id,
    # #     document=obf_name,
    # #     filename=obf_name,
    # # )
    # obf_file = open(obf_name, "rb")
    # await context.bot.send_document(
    #     chat_id=update.effective_chat.id,
    #     document=obf_file,
    #     filename=obf_name,
    #     reply_to_message_id=update.effective_message.id,
    # )
    # print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        # os.remove("Obfuscated_Code.py")

    # file = update.effective_message.effective_attachment
    # file_name = file.file_name
    #
    # if not file_name.endswith('.py'):
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="Please send a Python file.",
    #         reply_to_message_id=update.effective_message.id,
    #     )
    #     return
    #
    # file_id = file.file_id
    # file_path = await context.bot.get_file(file_id)
    # await file_path.download_to_drive(file_path)
    # plain_code = ""
    # with open(file_name, "rb") as code:
    #     plain_code = code
    # try:
    #     with open("another.py", "wb") as new_file:
    #         new_file.write(plain_code)
    #
    #     with open("another.py", "rb") as new_file:
    #         await context.bot.send_document(
    #             chat_id=update.message.chat_id,
    #             document=new_file,
    #             filename="another.py",
    #         )
    # except:
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="Sry, error while sending your obf code !!!",
    #         reply_to_message_id=update.effective_message.id,
    #     )
    #
    # os.remove("another.py")


# async def talk_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):


if __name__ == '__main__':
    logger.info("starting bot ...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler(["start", "help"], start_handler))
    app.add_handler(MessageHandler(filters.ATTACHMENT, file_handler))
    app.add_error_handler(error_handler)
    logger.info("start polling ...")
    app.run_polling()
