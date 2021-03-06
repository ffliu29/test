## DolphinDB 教程

- 安装和部署
    - [安装使用指南](安装和部署/dolphindb_user_guide.md)
    - [单节点部署](安装和部署/standalone_server.md)
    - [单节点部署(嵌入式ARM版本)](安装和部署/ARM_standalone_deploy.md)
    - [DolphinDB 单节点基本操作入门教程](安装和部署/Single_Node_Tutorial.md)
    - [单服务器集群部署](安装和部署/single_machine_cluster_deploy.md)
    - [多服务器集群部署](安装和部署/multi_machine_cluster_deployment.md)
    - [基于Docker的集群部署教程](安装和部署/docker_deployment.md)
    - [基于K8s的集群部署教程](安装和部署/k8s_deployment.md)
    - [高性能集群配置](安装和部署/cluster_high_performance_configuration.md)
    - [高可用集群部署教程](安装和部署/ha_cluster_deployment.md)
    - [如何扩展集群节点和存储](安装和部署/scale_out_cluster.md)
    - [DolphinDB客户端软件教程](安装和部署/client_tool_tutorial.md)
    - [DolphinDB技术支持攻略](安装和部署/dolphindb_support.md)
- 数据库
    - [分区数据库设计和操作](数据库/database.md)
    - [数据导入教程](数据库/import_data.md)
    - [数据备份恢复教程](数据库/restore-backup.md)
    - [动态增加字段和计算指标](数据库/add_column.md)
    - [内存表数据加载与操作](数据库/partitioned_in_memory_table.md)
    - [文本数据加载教程](数据库/import_csv.md)
    - [集群间数据库同步](数据库/data_synchronization_between_clusters.md)
    - [CacheEngine与数据库日志教程](数据库/redoLog_cacheEngine.md)
    - [内存表详解](数据库/in_memory_table.md)
- 编程语言
    - [脚本语言的混合范式编程](编程语言/hybrid_programming_paradigms.md)
    - [函数化编程案例](编程语言/functional_programming_cases.md)
    - [模块复用教程](编程语言/module_tutorial.md)
    - [通用计算教程](编程语言/general_computing.md)
    - [即时编译(JIT)教程](编程语言/jit.md)
    - [元编程教程](编程语言/meta_programming.md)
    - [自定义聚合函数](编程语言/udaf.md)
    - [矩阵计算](编程语言/matrix.md)
    - [日期/时间类型](编程语言/date_time.md) 
    - [DolphinDB SQL案例教程](编程语言/DolphinDB_SQL_Case_Tutorial.md)
    - [DolphinDB SQL执行计划教程](编程语言/DolphinDB_Explain.md)
- 流计算
    - [流数据教程](流计算/streaming_tutorial.md)
    - [流数据时序聚合引擎](流计算/stream_aggregator.md)
    - [流数据横截面引擎](流计算/streaming_crossSectionalAggregator.md)
    - [流数据异常检测引擎](流计算/Anomaly_Detection_Engine.md)
    - [历史数据回放教程](流计算/historical_data_replay.md)
    - [流数据高可用](流计算/haStreamingTutorial.md)
- 系统管理
    - [权限管理和安全](系统管理/ACL_and_Security.md)
    - [作业管理](系统管理/job_management_tutorial.md)
    - [内存管理](系统管理/memory_management.md)
    - [启动脚本教程](系统管理/Startup.md)
    - [定时作业](系统管理/scheduledJob.md)
    - [使用Prometheus监控告警](系统管理/DolphinDB_monitor.md)
    - [如何正确定位节点宕机的原因](系统管理/how_to_handle_crash.md)
    - [从一次SQL查询的全过程看DolphinDB 的线程模型](系统管理/thread_model_SQL.md)
- API
    - [Python API使用教程](../../../api_python3/blob/master/README_CN.md)
    - [Java API使用教程](../../../api-java/blob/master/README_CN.md)
    - [Java API使用实例](../../../api-java/blob/master/example/README_CN.md)
    - [JDBC](../../../jdbc/blob/master/README_CN.md)
    - [C# API使用教程](../../../api-csharp/blob/master/README_CN.md)
    - [C++ API使用教程](../../../api-cplusplus/blob/master/README_CN.md)
    - [用VS2017编译DolphinDB C++ API动态库](API/cpp_api_vs2017_tutorial.md)
    - [C++ API 数据读写指南](API/c%2B%2Bapi.md)
    - [Go API使用教程](../../../api-go/blob/master/README.md)
    - [Go API使用实例](../../../api-go/blob/master/example/README_CN.md)
    - [R API使用教程](../../../api-r/blob/master/README_CN.md)
    - [Json API使用教程](../../../api-json/blob/master/README_CN.md)
    - [NodeJS API使用教程](../../../api-nodejs/blob/master/README.md)
    - [JavaScript API使用教程](../../../api-javascript/blob/master/README.md)
    - [redash连接DolphinDB数据源的教程](API/data_interface_for_redash.md)
    - [DolphinDB整合前端chart组件展示数据教程](API/web_chart_integration.md)
    - [Grafana连接DolphinDB数据源](../../../grafana-datasource/blob/master/README.zh.md)
    - [帆软报表软件连接DolphinDB数据源](API/FineReport_to_dolphindb.md)
    - [API交互协议](API/api_protocol.md)

- 插件
    - [插件开发教程](插件/plugin_development_tutorial.md) 
    - [插件开发深度解析](插件/plugin_advance.md)
    - [AWS S3](../../../DolphinDBPlugin/blob/master/aws/README_CN.md)
    - [DolphinDB VSCode 插件](插件/vscode_extension.md)
    - [Excel](../../../excel-add-in)
    - [HBase](../../../DolphinDBPlugin/blob/master/hbase/README.md)
    - [HDF5](../../../DolphinDBPlugin/blob/master/hdf5/README_CN.md)
    - [HDFS](../../../DolphinDBPlugin/blob/master/hdfs/README.md)
    - [HttpClient](插件/send_messages_external_systems.md)
    - [Kafka](../../../DolphinDBPlugin/blob/master/kafka/README.md)
    - [Matching Engine](../../../DolphinDBPlugin/blob/master/MatchingEngine/README.md)
    - [Matlab](../../../DolphinDBPlugin/blob/master/mat/README.md)
    - [MongoDB](../../../DolphinDBPlugin/blob/master/mongodb/README.md)
    - [MQTT](../../../DolphinDBPlugin/blob/master/mqtt/README_CN.md)
    - [MSeed](../../../DolphinDBPlugin/blob/master/mseed/README.md)
    - [MySQL](../../../DolphinDBPlugin/blob/master/mysql/README_CN.md)
    - [ODBC](../../../DolphinDBPlugin/blob/master/odbc/README.md)
    - [OPC](../../../DolphinDBPlugin/blob/master/opc/README_CN.md)
    - [OPCUA](../../../DolphinDBPlugin/blob/master/opcua/README_CN.md)
    - [Parquet](../../../DolphinDBPlugin/blob/master/parquet/README_CN.md)
    - [Py](../../../DolphinDBPlugin/blob/master/py/README.md)
    - [SVM](../../../DolphinDBPlugin/blob/master/svm/README_CN.md)
    - [XGBoost](../../../DolphinDBPlugin/blob/master/xgboost/README_CN.md)
    - [ZLib](../../../DolphinDBPlugin/blob/master/zlib/README_CN.md)

- 模块
    - [技术分析(Technical Analysis)指标库](模块/ta.md) 
    - [mytt (My麦语言 T通达信 T同花顺)指标库](../../../DolphinDBModules/blob/master/mytt/README.md)
- 应用场景示例
    - [DolphinDB在工业物联网的应用](应用场景示例/iot_demo.md)
    - [加密货币逐笔交易数据回放](../../../applications/blob/master/cryptocurr_replay/README.md)
    - [在DolphinDB中计算K线](应用场景示例/OHLC.md) 
    - [使用DolphinDB进行机器学习](应用场景示例/machine_learning.md)
    - [DolphinDB流计算引擎实现传感器数据异常检测](应用场景示例/iot_anomaly_detection.md)
    - [实时计算高频因子](应用场景示例/hf_factor_streaming.md)
    - [DolphinDB教程：面板数据的处理](应用场景示例/panel_data.md)
    - [金融高频因子的流批统一计算：DolphinDB响应式状态引擎](应用场景示例/reactive_state_engine.md)
    - [股票行情数据导入实例](应用场景示例/stockdata_csv_import_demo.md)
    - [快照引擎](应用场景示例/snapshot_engine.md)
    - [节点启动时的流计算自动订阅教程](应用场景示例/streaming_auto_sub.md)
    - [DolphinDB窗口计算综述](应用场景示例/window_cal.md)   
    - [DolphinDB机器学习在金融行业的应用：实时实际波动率预测](应用场景示例/machine_learning_volatility.md)
    - [DolphinDB流计算在金融行业的应用：实时计算分钟资金流](应用场景示例/streaming_capital_flow_order_by_order.md)
    - [基于DolphinDB的因子计算最佳实践](应用场景示例/best_practice_for_factor_calculation.md)
    - [SQL优化案例：深度不平衡、买卖压力指标、波动率计算](应用场景示例/sql_performance_optimization_wap_di_rv.md)
    - [DolphinDB流计算在金融行业的应用：实时计算日累计逐单资金流](应用场景示例/streaming_capital_flow_daily.md)
    - [SQL优化案例：外汇掉期估值计算](应用场景示例/FxSwapValuation.md)
- 入门和测试
    - [DolphinDB入门：量化金融范例](入门和测试/quant_finance_examples.md)
    - [DolphinDB入门：物联网范例](入门和测试/iot_examples.md)
- 测试报告
    - [DolphinDB API性能基准测试报告](测试报告/api_performance.md)
    - [金融市场高频数据应当如何管理 - DolphinDB与pickle的性能对比测试和分析](测试报告/DolphinDB_pickle_comparison.md)
    - [DolphinDB集群水平扩展性能测试](测试报告/Cluster_scale_out_performance_test.md)
