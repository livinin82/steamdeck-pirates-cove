#!/usr/bin/env python3
"""
Convert plain markdown sections back to > [!TIP] blocks without titles for green highlighting.
"""

import re
import sys

def convert_to_tip_blocks(content):
    """Convert specific markdown sections back to TIP blocks without titles."""
    
    # Find sections that were originally TIP blocks by looking for specific patterns:
    # - Multi-line bullet lists that were in the methods sections
    # - Lists that follow installation/setup patterns
    
    # Pattern 1: Method sections (Method 1, Method 2, etc.)
    method_pattern = r'(\*\*Method \d+:?[^*]*\*\*\n\n)((?:\* [^\n]+\n(?:    \* [^\n]+\n)*)+)'
    
    def replace_method_section(match):
        method_title = match.group(1).strip()
        content_lines = match.group(2).strip()
        
        # Convert to TIP block format without the title
        tip_lines = []
        for line in content_lines.split('\n'):
            if line.strip():
                tip_lines.append('> ' + line)
            else:
                tip_lines.append('>')
        
        return '> [!TIP]\n' + '\n'.join(tip_lines) + '\n\n'
    
    # Pattern 2: Standalone bullet list sections that are tips
    standalone_list_pattern = r'(\n\n)((?:\* [^\n]+\n(?:    \* [^\n]+\n)*){3,})'
    
    def replace_standalone_lists(match):
        prefix = match.group(1)
        list_content = match.group(2).strip()
        
        # Only convert lists that look like installation/setup instructions
        if any(keyword in list_content.lower() for keyword in ['install', 'open', 'click', 'select', 'download', 'extract', 'launch']):
            tip_lines = []
            for line in list_content.split('\n'):
                if line.strip():
                    tip_lines.append('> ' + line)
                else:
                    tip_lines.append('>')
            
            return prefix + '> [!TIP]\n' + '\n'.join(tip_lines) + '\n\n'
        
        return match.group(0)
    
    # Apply conversions
    converted = re.sub(method_pattern, replace_method_section, content, flags=re.MULTILINE | re.DOTALL)
    converted = re.sub(standalone_list_pattern, replace_standalone_lists, converted, flags=re.MULTILINE | re.DOTALL)
    
    return converted

def main():
    if len(sys.argv) != 2:
        print("Usage: python restore_tip_highlights.py <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Read the file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # Convert sections to TIP blocks
    converted_content = convert_to_tip_blocks(content)
    
    # Write backup
    backup_filepath = filepath + '.bak_restore'
    with open(backup_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup written to {backup_filepath}")
    
    # Write converted content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print(f"Restored TIP highlighting in {filepath}")

if __name__ == '__main__':
    main()