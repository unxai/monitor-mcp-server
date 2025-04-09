from typing import Any, Dict

import psutil
from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP server
mcp = FastMCP("monitor-mcp-server")

@mcp.tool()
def get_cpu_info() -> Dict[str, Any]:
    """获取CPU使用情况"""
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()
    return {
        "cpu_percent": cpu_percent,
        "cpu_freq_current": cpu_freq.current if cpu_freq else None,
        "cpu_freq_min": cpu_freq.min if cpu_freq else None,
        "cpu_freq_max": cpu_freq.max if cpu_freq else None,
        "cpu_count": cpu_count
    }

@mcp.tool()
def get_memory_info() -> Dict[str, Any]:
    """获取内存使用情况"""
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "available": memory.available,
        "percent": memory.percent,
        "used": memory.used,
        "free": memory.free
    }

@mcp.tool()
def get_disk_info() -> Dict[str, Any]:
    """获取磁盘使用情况"""
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.mountpoint] = {
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent,
                "fstype": partition.fstype
            }
        except (PermissionError, OSError):
            continue
    return disk_info

if __name__ == "__main__":
    # 初始化并运行 server
    mcp.run(transport='stdio')