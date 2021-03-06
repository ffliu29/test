# -*- coding: utf-8 -*-
from threading import Event
from dolphindb import session
from streaming_scripts import streaming_pathway_creating_script, streaming_start_script

DDB_server_port=8851
DDB_datanode_host= "192.168.100.3"
DDB_user_name= "admin"
DDB_password= "123456"

#流表共享名
stream_table_shared_name= "result_stream"
#流订阅行为名
action_name= "python_subscribe"

#python端回调函数，流表传入数据以后在此下游处理python端的业务
def python_callback_handler(msg):
	#显示传入的流数据
	print("流表传来数据:")
	print(msg)
	pass

def main():
	current_ddb_session=session()

	current_ddb_session.connect(DDB_datanode_host,
					DDB_server_port,
					DDB_user_name,
					DDB_password)
	
	执行结果=current_ddb_session.run(streaming_pathway_creating_script)
	print("流创建执行完成",执行结果)

	try:

		#python端收听端口
		python_receiving_port=24555

		current_ddb_session.enableStreaming(python_receiving_port)
		print(f"DDB将订阅的流发送到客户端{python_receiving_port}端口")

		current_ddb_session.subscribe(
			host=DDB_datanode_host,
			port=DDB_server_port,
			handler=python_callback_handler,
			tableName=stream_table_shared_name,
			actionName=action_name,
			offset=0,
			resub=False,
			filter=None
		)
	except Exception as current_error:
		print(current_error)

	脚本result=current_ddb_session.run(streaming_start_script)
	#阻塞函数退出，保证DDB会话不析构
	Event().wait()

	pass

if __name__ == '__main__':
	main()

