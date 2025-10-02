#!/usr/bin/env python3
"""
Convert instruction lists to TIP blocks for green highlighting.
"""

import re
import sys

def convert_instruction_lists_to_tips(content):
    """Convert instruction lists and certain sections to TIP blocks."""
    
    # Find standalone bullet lists that are instructions (not already in blockquotes)
    # Pattern: Look for bullet lists that aren't already quoted
    standalone_list_pattern = r'(\n\n)((?:\* [^\n]+(?:\n    \* [^\n]+)*\n){2,})'
    
    def replace_instruction_lists(match):
        prefix = match.group(1)
        list_content = match.group(2).strip()
        
        # Only convert lists that look like instructions
        instruction_keywords = [
            'install', 'open', 'click', 'select', 'download', 'extract', 'launch',
            'copy', 'paste', 'navigate', 'enter', 'type', 'run', 'execute',
            'right-click', 'left-click', 'drag', 'drop', 'add', 'remove',
            'go to', 'find', 'locate', 'create', 'delete', 'rename',
            'switch', 'enable', 'disable', 'check', 'uncheck'
        ]
        
        if any(keyword in list_content.lower() for keyword in instruction_keywords):
            # Convert to TIP block
            tip_lines = ['> [!TIP]']
            for line in list_content.split('\n'):
                if line.strip():
                    tip_lines.append('> ' + line)
                else:
                    tip_lines.append('>')
            
            return prefix + '\n'.join(tip_lines) + '\n\n'
        
        return match.group(0)
    
    # Apply conversion
    converted = re.sub(standalone_list_pattern, replace_instruction_lists, content, flags=re.MULTILINE | re.DOTALL)
    
    return converted

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_lists_to_tips.py <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Read the file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # Convert instruction lists to TIP blocks
    converted_content = convert_instruction_lists_to_tips(content)
    
    # Write backup
    backup_filepath = filepath + '.bak_lists'
    with open(backup_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup written to {backup_filepath}")
    
    # Write converted content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print(f"Converted instruction lists to TIP blocks in {filepath}")

if __name__ == '__main__':
    main()