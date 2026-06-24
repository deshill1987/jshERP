江东ERP V3.6 发布包

目录结构：
  backend/  - 后端服务 (jshERP.jar)
  frontend/ - 前端静态资源 (dist)
  sql/      - 数据库脚本 (jsh_erp.sql)

启动说明：
  1. 导入 sql/jsh_erp.sql 到 MySQL 数据库
  2. 启动后端：java -jar backend/jshERP.jar
  3. 将 frontend/ 部署到 Nginx 或其他 Web 服务器
  4. 默认账号：jsh / 123456
