#!/usr/bin/env python3
"""
Command-line interface for dockerdump
"""

import click
import docker
from typing import Optional
import sys
import logging

from . import memory_dump

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.group()
@click.version_option()
def cli():
    """dockerdump - Docker memory forensics tool"""
    pass

@cli.command()
@click.argument('container_id')
@click.option('--output', '-o', help='Output directory for memory dump', default='./dump')
def dump(container_id: str, output: str):
    """Dump memory from a running Docker container"""
    try:
        memory_dump.dump_container_memory(container_id, output)
    except Exception as e:
        logger.error(f"Failed to dump memory: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    cli()
