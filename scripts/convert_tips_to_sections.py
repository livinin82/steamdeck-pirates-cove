#!/usr/bin/env python3
"""
Convert > [!TIP] admonition blocks to regular markdown sections.
"""

import re
import sys

def convert_tips_to_sections(content):
    """Convert TIP admonition blocks to regular markdown sections."""
    
    # Pattern to match TIP blocks with their content
    # Matches both: > [\!TIP] and > [!TIP] followed by blockquoted lines
    tip_pattern = r'> \[\\?!TIP\]\n(?:>\s*\n)?((?:>\s*.*\n)*)'
    
    def replace_tip_block(match):
        tip_content = match.group(1)
        if not tip_content.strip():
            return ""
        
        # Remove the > prefix from each line
        lines = tip_content.split('\n')
        converted_lines = []
        
        for line in lines:
            if line.startswith('> '):
                # Remove the "> " prefix
                converted_lines.append(line[2:])
            elif line.startswith('>'):
                # Remove just ">"
                converted_lines.append(line[1:])
            elif line.strip():
                converted_lines.append(line)
        
        # Join back and return
        return '\n'.join(converted_lines) + '\n'
    
    # Apply the conversion
    converted = re.sub(tip_pattern, replace_tip_block, content, flags=re.MULTILINE)
    return converted

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_tips_to_sections.py <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Read the file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # Convert TIP blocks
    converted_content = convert_tips_to_sections(content)
    
    # Write backup
    backup_filepath = filepath + '.bak_tips'
    with open(backup_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup written to {backup_filepath}")
    
    # Write converted content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print(f"Converted TIP blocks in {filepath}")

if __name__ == '__main__':
    main()