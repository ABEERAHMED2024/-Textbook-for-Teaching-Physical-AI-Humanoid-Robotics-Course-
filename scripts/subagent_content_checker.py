#!/usr/bin/env python3
"""
Content Completeness Checker Subagent

This subagent checks the completeness of textbook content against the Hackathon PDF requirements.
"""

import os
import sys
import argparse
from pathlib import Path
import re


def check_content_completeness(docs_path: str = "./docs"):
    """
    Check the completeness of textbook content against the Hackathon PDF requirements.
    
    Args:
        docs_path: Path to the docs directory containing textbook content
    """
    print("🔍 Starting Content Completeness Check...")
    
    # Define the expected modules and weeks based on the Hackathon PDF
    expected_structure = {
        "module-1-ros2": ["chapter-1-intro-ros2", "chapter-2-nodes-topics", "chapter-3-services-actions-parameters", 
                         "chapter-4-urdf-robot-modeling", "chapter-5-launch-files-packages", "index"],
        "module-2-digital-twin": ["week-6-gazebo", "week-7-unity-sensors", "index"],
        "module-3-isaac": ["week-8-isaac-sim", "week-9-isaac-ros-vslam", "week-10-nav2-rl", "index"],
        "module-4-vla-humanoids": ["week-11-kinematics", "week-12-manipulation", "week-13-conversational-vla", "index"],
        "setup": ["workstation", "edge-kit", "cloud"],
        "references": ["glossary", "notation", "ros2-quick-ref", "troubleshooting"],
        "capstone": ["index"],
        "instructors": ["index"]
    }
    
    # Check if docs directory exists
    docs_dir = Path(docs_path)
    if not docs_dir.exists():
        print(f"❌ Error: Docs directory '{docs_path}' does not exist.")
        return False
    
    print(f"📁 Checking content in: {docs_dir.absolute()}")
    
    missing_items = []
    found_items = []
    
    # Check each expected module/directory
    for module, expected_files in expected_structure.items():
        module_path = docs_dir / module
        
        if not module_path.exists():
            missing_items.append(f"Missing module directory: {module}")
            continue
        
        # Get actual files in the module directory (without extensions)
        actual_files = []
        for file_path in module_path.iterdir():
            if file_path.is_file():
                # Get stem (filename without extension)
                actual_files.append(file_path.stem)
        
        # Check for missing files
        for expected_file in expected_files:
            if expected_file not in actual_files:
                missing_items.append(f"Missing file in {module}: {expected_file}")
            else:
                found_items.append(f"Found: {module}/{expected_file}")
    
    # Check for introduction files
    intro_files = ["intro", "week-1-foundations", "week-2-sensors"]
    for intro_file in intro_files:
        intro_path = docs_dir / f"{intro_file}.mdx"
        if not intro_path.exists():
            missing_items.append(f"Missing introduction file: {intro_file}.mdx")
        else:
            found_items.append(f"Found: {intro_file}.mdx")
    
    # Print results
    print("\n📊 Results:")
    if found_items:
        print(f"✅ Found {len(found_items)} items:")
        for item in found_items[:10]:  # Show first 10
            print(f"   - {item}")
        if len(found_items) > 10:
            print(f"   ... and {len(found_items) - 10} more")
    
    if missing_items:
        print(f"\n❌ Found {len(missing_items)} missing items:")
        for item in missing_items:
            print(f"   - {item}")
        print(f"\n💡 Tip: Create the missing content based on the Hackathon PDF requirements")
        return False
    else:
        print(f"\n🎉 All expected content is present!")
        return True


def main():
    parser = argparse.ArgumentParser(description="Content Completeness Checker Subagent")
    parser.add_argument("--docs-path", type=str, default="./docs", 
                       help="Path to the docs directory containing textbook content")
    
    args = parser.parse_args()
    
    success = check_content_completeness(args.docs_path)
    
    if success:
        print("\n✅ Content completeness check PASSED")
        sys.exit(0)
    else:
        print("\n❌ Content completeness check FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()