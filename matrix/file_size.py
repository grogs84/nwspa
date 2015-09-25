import heapq
import os, os.path
import sys
import operator

def file_sizes(directory):
    for path, _, filenames in os.walk(directory):
        for name in filenames:
            full_path = os.path.join(path, name)
            yield full_path, os.path.getsize(full_path)

