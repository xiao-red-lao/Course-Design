
import pymysql # 导入操作MySQL数据库的模块

userName="1234" # 记录用户名
Uclass="" #记录用户名类型

# 打开数据库连接
def open():
    db = pymysql.connect(host="localhost", user="1234",passwd= "1111", database="db_book",charset="utf8")
    return db # 返回连接对象

# 执行数据库的增、删、改操作
def exec(sql):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql) # 执行增删改的SQL语句
        db.commit() # 提交数据
        return 1 # 执行成功
    except Exception as e:
        print(str(e))
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败
    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接

# 带参数的精确查询
def query(sql,*keys):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql,keys) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果

# 不带参数的模糊查询
def query2(sql):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果

if __name__ == '__main__':
    # db=open()
    # result = exec(
    #     "insert into tb_user(Uname,Uuser,Upassword,Uclass) values({},{},{},'普通';".format('算法', 124, 111111))
    # print(result)
    result = exec(
        "insert into tb_user(Uname,Uuser,Upassword,Uclass) values('nkasd','asd','fsd','zx');")
    print(result)