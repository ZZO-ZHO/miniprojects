# 이메일 보내기앱
import smtplib
from email.mime.text import MIMEText

send_email = 'xstar202@naver.com'
send_pass = '**********'    # 비밀번호

recv_email = 'young5190@icloud.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = '''메일 내용입니다'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목 입니다'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

mail = smtplib.SMTP(smtp_name,smtp_port)
mail.starttls()
mail.login(send_email, send_pass)
mail.sendmail(send_email , recv_email, msg=msg.as_string())
mail.quit()
print('전송완료')
