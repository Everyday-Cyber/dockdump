# dockdump

A powerful Docker container memory forensics tool that allows you to dump and analyze memory from running Docker containers.

## Features

- Dump memory from running Docker containers
- Save memory maps and raw memory content
- CLI interface for easy usage
- Can be run as a standalone tool or within a Docker container

## Installation

```bash
# Install from source
git clone https://github.com/yourusername/dockerdump
cd dockdump
pip install -e .

# Or using Docker
docker build -t dockdump .
```

## Usage

```bash
# Using CLI
dockdump dump <container_id> --output ./output_dir

# Using Docker
docker run --privileged -v /proc:/proc -v $(pwd)/output:/output dockdump dump <container_id> --output /output
```

## Requirements

- Python 3.8 or higher
- Docker API access
- Root/sudo privileges (for memory access)

## Security Note

This tool requires privileged access to read container memory. Always be cautious when using memory forensics tools and ensure you have proper authorization.

## License

MIT License
