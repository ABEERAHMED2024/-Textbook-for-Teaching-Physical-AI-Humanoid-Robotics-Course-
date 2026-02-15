import os

def fix_glossary():
    path = 'docs/references/glossary.md'
    if not os.path.exists(path):
        return
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapping old file names to new ones
    replacements = {
        '../module-1-ros2/week-3-architecture.md': '../module-1-ros2/chapter-1-intro-ros2',
        '../module-1-ros2/week-4-topics-services.md': '../module-1-ros2/chapter-2-nodes-topics',
        '../module-1-ros2/week-5-urdf.md': '../module-1-ros2/chapter-4-urdf-robot-modeling',
        '../module-4-vla-humanoids/week-11-kinematics.md': '../module-4-vla-humanoids/week-11-kinematics',
        '../module-4-vla-humanoids/week-12-manipulation.md': '../module-4-vla-humanoids/week-12-manipulation',
        '../module-1-ros2/week-4-topics-services': '../module-1-ros2/chapter-2-nodes-topics',
        '../module-1-ros2/week-3-architecture': '../module-1-ros2/chapter-1-intro-ros2',
        '../module-1-ros2/week-5-urdf': '../module-1-ros2/chapter-4-urdf-robot-modeling'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Also remove any trailing .md from other links to be safe
    content = content.replace('.md)', ')')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Glossary links fixed.")

if __name__ == "__main__":
    fix_glossary()
