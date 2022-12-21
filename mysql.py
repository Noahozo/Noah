import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy import String

username = 'root'  # 資料庫帳號
password = 'Passw0rd!'  # 資料庫密碼
host = 'localhost'  # 資料庫位址
port = '3306'  # 資料庫埠號
database = 'sql_tutorial'  # 資料庫名稱
# 连接到 MySQL 数据库
engine = db.create_engine(
    f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# 创建基类
Base = declarative_base()


# # 定義表
class MyTable(Base):
    __tablename__ = 'Tree'
    max_depth = Column(String(50), primary_key=True)
    R_squared = Column(String(50))
    MSE = Column(String(50))

    # 創建session


table = MyTable.__table__
#创建表
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 讀取 CSV 文件
with open(r'C:\Users\student\python_web_scraping-master\DecisionTree.csv',
          'r',
          encoding="utf-8") as f:
    reader = csv.DictReader(f, fieldnames=['max_depth', 'R_squared', 'MSE'])
    # 將數據導入到資料庫
    for row in reader:
        session.add(MyTable(**row))
    # 提交session
session.commit()

# 關閉連結
session.close()