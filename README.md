# System Monitor MCP Server

这是一个基于MCP (Message Control Protocol) 的系统监控服务器，可以监控Mac系统的CPU、内存和磁盘使用情况。

## 功能特点

- CPU使用率监控
  - 每个CPU核心的使用率
  - CPU频率信息
  - CPU核心数量
- 内存使用情况监控
  - 总内存
  - 可用内存
  - 内存使用率
  - 已用内存
  - 空闲内存
- 磁盘使用情况监控
  - 各分区使用情况
  - 文件系统类型
  - 总空间、已用空间和可用空间


### 可用工具

1. 系统监控：
   - `get_cpu_info()`: 获取CPU使用情况
   - `get_memory_info()`: 获取内存使用情况
   - `get_disk_info()`: 获取磁盘使用情况


## 依赖

- mcp[cli]: MCP协议实现
- psutil: 系统和进程监控

## 许可证

MIT