# 使用Node.js作为基础镜像
FROM node:18

# 设置工作目录
WORKDIR /app

# 将代码复制到镜像中
COPY . /app

# 安装依赖
RUN npm install

# 暴露需要的端口
EXPOSE 3366

# 运行应用
CMD ["node", "server.js"]

