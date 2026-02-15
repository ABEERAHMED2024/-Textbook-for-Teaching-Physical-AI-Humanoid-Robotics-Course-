#!/usr/bin/env python3
"""
Duplication Detector Subagent

This subagent detects duplicated content or files in the textbook project.
"""

import os
import sys
import argparse
from pathlib import Path
import hashlib


def calculate_file_hash(filepath: Path) -> str:
    """
    Calculate the SHA-256 hash of a file.
    
    Args:
        filepath: Path to the file
        
    Returns:
        SHA-256 hash of the file content
    """
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def detect_content_duplication(docs_path: str = "./docs"):
    """
    Detect duplicated content or files in the textbook project.
    
    Args:
        docs_path: Path to the docs directory containing textbook content
    """
    print("🔍 Starting Duplication Detection...")
    
    docs_dir = Path(docs_path)
    if not docs_dir.exists():
        print(f"❌ Error: Docs directory '{docs_path}' does not exist.")
        return False
    
    # Dictionary to store file hashes and their paths
    file_hashes = {}
    duplicate_files = []
    
    # Walk through all markdown/mdx files
    for file_path in docs_dir.rglob("*"):
        if file_path.is_file() and (file_path.suffix.lower() in ['.md', '.mdx']):
            try:
                file_hash = calculate_file_hash(file_path)
                
                if file_hash in file_hashes:
                    # Duplicate found
                    original_path = file_hashes[file_hash]
                    duplicate_files.append((original_path, file_path))
                    print(f"❌ Duplicate content found:")
                    print(f"   {original_path}")
                    print(f"   {file_path}")
                else:
                    # Store the hash
                    file_hashes[file_hash] = file_path
            except Exception as e:
                print(f"⚠️  Could not process file {file_path}: {e}")
    
    # Check for similar filenames that might indicate duplication
    all_files = list(docs_dir.rglob("*"))
    all_files = [f for f in all_files if f.is_file() and f.suffix.lower() in ['.md', '.mdx']]
    
    # Group files by name (ignoring path)
    name_groups = {}
    for file_path in all_files:
        name = file_path.name
        if name not in name_groups:
            name_groups[name] = []
        name_groups[name].append(file_path)
    
    # Check for files with same name in different directories
    potential_duplicates = []
    for name, paths in name_groups.items():
        if len(paths) > 1:
            potential_duplicates.append((name, paths))
    
    print(f"\n📊 Duplication Detection Results:")
    if duplicate_files:
        print(f"❌ Found {len(duplicate_files)} sets of duplicate content:")
        for orig, dup in duplicate_files:
            print(f"   Original: {orig}")
            print(f"   Duplicate: {dup}")
            print()
        return False
    else:
        print("✅ No duplicate content found based on file hashes")
    
    if potential_duplicates:
        print(f"\n⚠️  Found {len(potential_duplicates)} sets of files with identical names:")
        for name, paths in potential_duplicates:
            print(f"   File name: {name}")
            for path in paths:
                print(f"     - {path}")
        print("\n💡 Note: These may or may not be actual duplicates - review manually")
    
    print(f"\n✅ Duplication check completed - no problematic duplicates found")
    return True


def main():
    parser = argparse.ArgumentParser(description="Duplication Detector Subagent")
    parser.add_argument("--docs-path", type=str, default="./docs", 
                       help="Path to the docs directory containing textbook content")
    
    args = parser.parse_args()
    
    success = detect_content_duplication(args.docs_path)
    
    if success:
        print("\n✅ Duplication detection PASSED")
        sys.exit(0)
    else:
        print("\n❌ Duplication detection FAILED - duplicates found")
        sys.exit(1)


if __name__ == "__main__":
    main()