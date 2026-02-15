import re

# Read the glossary file
with open(r'd:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match lines with week-X links
# Matches: **Used In**: [text](../path/week-X-something.md)
pattern = r'(\*\*Used In\*\*:.*?)(week-\d+-[^)]+\.md[^\n]*)'

def replace_func(match):
    prefix = match.group(1)
    week_links = match.group(2)
    
    # If the line contains week-X links, comment them out
    if 'week-' in week_links:
        # Keep any existing valid links (like intro.mdx, index.mdx)
        # Extract valid links before week- links
        valid_links = []
        remaining = prefix
        
        # Find all links in the prefix
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        for link_match in re.finditer(link_pattern, prefix):
            link_text = link_match.group(1)
            link_url = link_match.group(2)
            if 'week-' not in link_url:
                valid_links.append(f'[{link_text}]({link_url})')
        
        # Reconstruct the line
        if valid_links:
            result = f"**Used In**: {', '.join(valid_links)}\n<!-- TODO: Add links when chapter files are created: {week_links} -->"
        else:
            result = f"**Used In**: <!-- TODO: Add links when chapter files are created -->\n<!-- {week_links} -->"
        
        return result
    
    return match.group(0)

# Replace all occurrences
fixed_content = re.sub(pattern, replace_func, content, flags=re.MULTILINE | re.DOTALL)

# Write back
with open(r'd:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary.md', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("✅ Fixed all broken week-X links in glossary.md")
