from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter


d = ['100111A','100213A','100522A','100704A','100727A','100728B','110212A','110318A','110420A','110519A','121117A','130420A','130427B','130502A','130609A','131030A','150212A','150222A','151031A','160119A','160220B','161219B','170317A','170711A','180404B','180630A','190604B','190630C','191011A','191221B','200215A','200216B']



# print(DLm)
# 在内存创建一个工作簿obj
wb = Workbook()
ws = wb.active
# ws.title = u'GRB数据'

for i in range(0, len(d)):
    

    # 工作簿保存到磁盘
    wb.save(d[i]+'.xlsx')

