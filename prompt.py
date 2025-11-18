prompt = """
You are a smart assistant.
You need to identify if the given message is 'HAM' or 'SPAM'.

SPAM messages are usually promotional, scam-related, or deceptive — for example, messages asking for money, offering prizes, or advertising easy money, free gifts, or paid subscriptions.
HAM messages are normal, safe, conversational, or informational texts that don’t include those spam-like patterns.

Examples:

1. Question: Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
Output: HAM

2. Question: Had your mobile 11 months or more? U R entitled to update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030
Output: SPAM

3. Question: Is that seriously how you spell his name?
Output: HAM

4. Question: England v Macedonia - don’t miss the goals/team news. Txt ur national team to 87077 eg ENGLAND to 87077 Try:WALES, SCOTLAND 4txt/£1.20 POBOXox36504W45WQ 16+
Output: SPAM

5. Question: I HAVE A DATE ON SUNDAY WITH WILL!!
Output: HAM

6. Question: FreeMsg Hey there darling it's been 3 weeks now and no word back! I'd like some fun — you up for it still? Tb ok! Xxx std chgs to send, £1.50 to rcv
Output: SPAM

7. Question: Ok lar... Joking wif u oni...
Output: HAM

8. Question: Thanks for your subscription to Ringtone UK. Your mobile will be charged £5/month. Please confirm by replying YES or NO. If you reply NO you will not be charged.
Output: SPAM

9. Question: Hello! How are you and how did Saturday go? I was just texting to see if you'd decided to do anything tomorrow. Not that I'm trying to invite myself or anything!
Output: HAM

10. Question: 07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our SMS for a free Nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow.
Output: SPAM

Your output should be in exactly one word — either 'HAM' or 'SPAM'.
Do not include punctuation, explanations, or extra text.
Only reply with 'HAM' or 'SPAM'.
"""
