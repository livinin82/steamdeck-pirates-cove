#!/usr/bin/env python3
"""
Fix escaped admonition blocks for proper GitHub rendering.
"""

import re
import sys

def fix_admonition_escaping(content):
    """Fix escaped admonition blocks like [\!TIP] to [!TIP] for proper GitHub rendering."""
    
    # Fix escaped admonitions
    fixes = [
        (r'> \[\\!TIP\]', r'> [!TIP]'),
        (r'> \[\\!NOTE\]', r'> [!NOTE]'),
        (r'> \[\\!WARNING\]', r'> [!WARNING]'),
        (r'> \[\\!CAUTION\]', r'> [!CAUTION]'),
        (r'> \[\\!IMPORTANT\]', r'> [!IMPORTANT]'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_admonition_escaping.py <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Read the file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # Fix escaped admonitions
    fixed_content = fix_admonition_escaping(content)
    
    # Write backup
    backup_filepath = filepath + '.bak_escape'
    with open(backup_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup written to {backup_filepath}")
    
    # Write fixed content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Fixed admonition escaping in {filepath}")

if __name__ == '__main__':
    main()