import smtplib
from email.header import Header
from email.mime.text import MIMEText

# smtp服务器
mail_host = "smtp.163.com"
# 邮箱账户
mail_account = "xxxxx"
# 授权码
pwd = "zxxxxx"
# 接收邮箱
receive = 'xxxx'

# 邮件标题
context = "测试python发件"
message = MIMEText(context, 'plain', 'utf-8')
message["From"] = mail_account
message["To"] = receive
message["Subject"] = "活得真累"


try:
    smtp_obj = smtplib.SMTP_SSL(mail_host, 465,timeout=30)
    smtp_obj.login(mail_account, pwd)
    smtp_obj.set_debuglevel(1)
    smtp_obj.sendmail(mail_account,receive,message.as_string())
    print("发送成功")
    smtp_obj.quit()
except Exception as e:
    print(e)
