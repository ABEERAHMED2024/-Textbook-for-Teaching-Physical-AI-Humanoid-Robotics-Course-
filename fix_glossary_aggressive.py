import os
import re

def aggressive_fix_glossary():
    path = 'docs/references/glossary.md'
    if not os.path.exists(path):
        return
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all .md) and .mdx) with )
    # This handles both standard and extended extensions
    content = re.sub(r'\.mdx?\)', ')', content)
    
    # Also fix common incorrect names if any left
    replacements = {
        'week-3-architecture': 'chapter-1-intro-ros2',
        'week-4-topics-services': 'chapter-2-nodes-topics',
        'week-5-urdf': 'chapter-4-urdf-robot-modeling',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Glossary links cleaned aggressively.")

if __name__ == "__main__":
    aggressive_fix_glossary()
