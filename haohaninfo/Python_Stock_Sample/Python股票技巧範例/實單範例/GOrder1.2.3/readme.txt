GOrder_v1.2.3

���O�G
��J Order.exe Capital/Yuanta�d�ݻ���

�s�q
�U��: Order.exe #1 #2 #3 #4 #5 #6 #7
#1. Capital
#2. StockId(ex 2330)
#3. B: Buy, S: Sell
#4. Price
#5. Qty(�i��)
#6. 0: �@��, 1: �s��, 2: �L��
#7. 0: �{�f, 1: �ĸ�, 2: �Ĩ� 3: �L��
����: Order.exe Capital Delete �渹

���j
�U��: Order.exe #1 #2 #3 #4 #5 #6 #7
#1. Yuanta
#2. StockId(ex 2330)
#3. B: Buy, S: Sell
#4. Price
#5. Qty(�i��)
#6. 0: �@��, 1: �s��, 2: �L��
#7. 0: �{�f, 1: �ĸ�, 2: �Ĩ� 3: �ɨ�
����: Order.exe Yuanta Delete �渹

�Ͱ��Ҩ�
�U��: Order.exe #1 #2 #3 #4 #5 #6 #7
#1. Kgi
#2. StockId(ex 2330)
#3. B: Buy, S: Sell
#4. Price
#5. Qty(�i��)
#6. 0: �@��, 1: �s��, 2: �w��
#7. 0: �{�f, 1: �۸�, 2: �ۨ�, 3: ��R�ĸ�, 4: ��R�Ĩ�, 5: �L��
����: Order.exe Kgi Delete �渹

�Ͱ���f
�U��: Order.exe #1 #2 #3 #4 #5 #6 #7
#1. Kgi_Future
#2. ProductId(ex TXFI8)
#3. B: Buy, S: Sell
#4. Price
#5. Qty(�f��)
#6. ROD / IOC / FOK
#7. LMT / MKT
����: Order.exe Kgi Delete �渹

�������f
�U��: Order.exe #1 #2 #3 #4 #5 #6 #7
#1. Simulator
#2. ProductId(ex TXFI8)
#3. B: Buy, S: Sell
#4. Price
#5. Qty(�f��)
#6. ROD / IOC / FOK
#7. LMT / MKT
����: Order.exe Simulator Delete �渹
 
��J GetAccount.exe Capital/Yuanta/Kgi/Simulator/Kgi_Future �渹/All �d�b��
��J MatchAccount.exe Capital/Yuanta/Kgi/Simulator/Kgi_Future  �渹/All �d�����
��J GetInStock.exe Capital/Yuanta/Simulator/Kgi_Future �d�w�s
(�Ͱ�: GetInStock.exe Kgi �Ѳ��N��)
��J MatchStock.exe Capital/Yuanta/Kgi/Simulator/Kgi_Future �d�ߦ����

