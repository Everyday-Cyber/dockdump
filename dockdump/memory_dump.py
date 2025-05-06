"""
Core functionality for Docker memory dumping
"""

import docker
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def dump_container_memory(container_id: str, output_dir: str) -> None:
    """
    Dump the memory of a running Docker container
    
    Args:
        container_id: The ID or name of the container
        output_dir: Directory to save the memory dump
    """
    client = docker.from_env()
    
    try:
        container = client.containers.get(container_id)
        if container.status != 'running':
            raise RuntimeError(f"Container {container_id} is not running")
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Get container PID
        container_info = container.attrs
        pid = container_info['State']['Pid']
        
        if not pid:
            raise RuntimeError(f"Could not get PID for container {container_id}")
        
        # Dump memory maps
        maps_file = output_path / f"{container_id}_maps"
        mem_file = output_path / f"{container_id}_mem"
        
        # Read memory mapping information
        with open(f"/proc/{pid}/maps", 'r') as f:
            maps_content = f.read()
            with open(maps_file, 'w') as mf:
                mf.write(maps_content)
        
        # Dump memory segments
        with open(f"/proc/{pid}/mem", 'rb') as f:
            with open(mem_file, 'wb') as mf:
                # Read memory in chunks
                chunk_size = 1024 * 1024  # 1MB chunks
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    mf.write(chunk)
        
        logger.info(f"Successfully dumped memory for container {container_id}")
        logger.info(f"Memory maps saved to: {maps_file}")
        logger.info(f"Memory dump saved to: {mem_file}")
        
    except docker.errors.NotFound:
        raise RuntimeError(f"Container {container_id} not found")
    except PermissionError:
        raise RuntimeError("Insufficient permissions to access container memory. Run as root/sudo")
