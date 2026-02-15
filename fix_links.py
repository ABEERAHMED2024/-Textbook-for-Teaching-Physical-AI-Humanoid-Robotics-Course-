import os
import re

filepath = r'd:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary.md'
temp_filepath = r'd:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary_temp.md'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '[' in line and '](' in line:
        # 1. Standardize to Doc ID (remove ../ and extensions)
        # Matches [Text](../path.md) or [Text](path.md)
        line = re.sub(r'\[([^\]]+)\]\((?:\.\./)?([^)]+?)(?:\.mdx?)?\)', r'[\1](\2)', line)
        
        # 2. Comment out any line with 'week-', 'chapter-', or 'module-' if it might be broken
        if '**Used In**:' in line:
            if 'week-' in line.lower() or 'chapter-' in line.lower() or ('module-' in line.lower() and 'index' not in line.lower()):
                if not line.strip().startswith('<!--'):
                    line = f"**Used In**: <!-- TODO: {line.replace('**Used In**: ', '').strip()} -->\n"
    new_lines.append(line)

with open(temp_filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Move temp to original
os.replace(temp_filepath, filepath)
print("✅ Entire glossary.md standardized to Doc ID format.")
