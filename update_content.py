import os
import re

def update_chapters():
    docs_dir = 'docs'
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.mdx') and not file.startswith('_'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add ChapterControls after front matter
                if '---' in content:
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        body = parts[2].strip()
                        if '<ChapterControls />' not in body:
                            new_content = f"---{parts[1]}---\n\n<ChapterControls />\n\n{body}"
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Updated {path}")

def fix_glossary():
    path = 'docs/references/glossary.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Example mapping: [Week 3: ROS 2 Architecture](../module-1-ros2/week-3-architecture.md)
    # to: [Week 3: ROS 2 Architecture](../module-1-ros2/chapter-1-intro-ros2)
    
    replacements = {
        '../module-1-ros2/week-3-architecture.md': '../module-1-ros2/chapter-1-intro-ros2',
        '../module-1-ros2/week-4-topics-services.md': '../module-1-ros2/chapter-2-nodes-topics',
        '../module-1-ros2/week-5-urdf.md': '../module-1-ros2/chapter-4-urdf-robot-modeling',
        '../module-2-digital-twin/week-6-gazebo.md': '../module-2-digital-twin/week-6-gazebo',
        '../module-2-digital-twin/week-7-unity-sensors.md': '../module-2-digital-twin/week-7-unity-sensors',
        '../module-3-isaac/week-8-isaac-sim.md': '../module-3-isaac/week-8-isaac-sim',
        '../module-3-isaac/week-9-isaac-ros-vslam.md': '../module-3-isaac/week-9-isaac-ros-vslam',
        '../module-3-isaac/week-10-nav2-rl.md': '../module-3-isaac/week-10-nav2-rl',
        '../module-4-vla-humanoids/week-11-kinematics.md': '../module-4-vla-humanoids/week-11-kinematics',
        '../module-4-vla-humanoids/week-12-manipulation.md': '../module-4-vla-humanoids/week-12-manipulation',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Glossary links")

if __name__ == "__main__":
    update_chapters()
    fix_glossary()
