from pathlib import Path
import os
import json
from typing import List, Optional, Any, Union

def input_to_file(*value,path,mode='w',end='',sep="\n")->None:
    all_input_value:str = ""
    for input_value in value:
        all_input_value += input_value + sep
    all_input_value+=end
    with open(path,mode) as f:
        f.write(all_input_value)

def read_lines(path: str, strip_newline: bool = True, encoding: str = 'utf-8') -> List[str]:
    with open(path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    if strip_newline:
        lines = [line.rstrip('\n\r') for line in lines]
    return lines

def write_lines(path: str, lines: List[str], mode: str = 'w', encoding: str = 'utf-8') -> None:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, mode, encoding=encoding) as f:
        for line in lines:
            f.write(line + '\n')

def tail(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]:
    with open(path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        buffer = bytearray()
        lines = []
        pos = file_size
        while pos > 0 and len(lines) < n:
            chunk_size = min(4096, pos)
            pos -= chunk_size
            f.seek(pos)
            chunk = f.read(chunk_size)
            buffer[:0] = chunk
            lines = buffer.splitlines()
            if len(lines) > n:
                lines = lines[-n:]
        lines = [line.decode(encoding) for line in lines]
        return lines

def head(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]:
    lines = []
    with open(path, 'r', encoding=encoding) as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip('\n\r'))
    return lines

def safe_read_json(path: str, default: Any = None) -> Any:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def safe_write_json(path: str, data: Any, indent: int = 2) -> None:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

def get_file_size(path: str, human_readable: bool = False) -> Union[int, str]:
    size_bytes = os.path.getsize(path)
    if not human_readable:
        return size_bytes
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"

def ensure_dir(path: str) -> None:
    if path:
        os.makedirs(path, exist_ok=True)

def atomic_write(path: str, data: Union[str, bytes], mode: str = 'w', encoding: str = 'utf-8') -> None:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    fd, tmp_path = os.mkstemp(dir=dirname or '.', text=(mode == 'w'))
    try:
        if mode == 'w':
            data_bytes = data.encode(encoding) if isinstance(data, str) else data
            os.write(fd, data_bytes)
        else:
            os.write(fd, data if isinstance(data, bytes) else data.encode(encoding))
        os.fsync(fd)
        os.close(fd)
        os.replace(tmp_path, path)
    except Exception:
        os.close(fd) if not fd.closed else None
        os.unlink(tmp_path)
        raise

def find_files(directory: str, pattern: str = '*', recursive: bool = True) -> List[str]:
    import fnmatch
    result = []
    directory = os.path.abspath(directory)
    if recursive:
        for root, dirs, files in os.walk(directory):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    full = os.path.join(root, name)
                    result.append(os.path.relpath(full, directory))
    else:
        for name in os.listdir(directory):
            full = os.path.join(directory, name)
            if os.path.isfile(full) and fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

if __name__ == "__main__":
    print("this is a test file.py 's def , if you want use there , don't open the there , use 'import foxange'")
    print("down is test file.py")
    print("i will print can return value 's def and all def 's return path")
    
    print("我已急苦QAQ")