#!/usr/bin/env python3
"""
PDF Alignment Validator Subagent

This subagent validates that the textbook content aligns with the Hackathon PDF requirements.
"""

import os
import sys
import argparse
from pathlib import Path
import re


def validate_pdf_alignment(pdf_path: str = "./Hackathon I_ Physical AI & Humanoid Robotics Textbook.md", 
                          docs_path: str = "./docs"):
    """
    Validate that the textbook content aligns with the Hackathon PDF requirements.
    
    Args:
        pdf_path: Path to the Hackathon PDF (as text/markdown)
        docs_path: Path to the docs directory containing textbook content
    """
    print("🔍 Starting PDF Alignment Validation...")
    
    # Read the PDF content (as markdown/text)
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        print(f"❌ Error: PDF file '{pdf_path}' does not exist.")
        return False
    
    with open(pdf_file, 'r', encoding='utf-8') as f:
        pdf_content = f.read().lower()
    
    # Define key topics and concepts from the PDF that should be covered
    key_topics = [
        "physical ai", "humanoid robotics", "embodied intelligence",
        "ros 2", "robot operating system", "nodes", "topics", "services", "actions",
        "urdf", "unified robot description format", "gazebo", "digital twin",
        "unity", "nvidia isaac", "ai-robot brain", "vision-language-action", "vla",
        "conversational robotics", "humanoid robot", "kinematics", "manipulation",
        "nav2", "path planning", "vslam", "visual slam", "reinforcement learning",
        "sim-to-real", "physics simulation", "computer vision", "sensor fusion",
        "robotics middleware", "human-robot interaction", "robotics simulation"
    ]
    
    # Check if these topics are mentioned in the textbook content
    docs_dir = Path(docs_path)
    if not docs_dir.exists():
        print(f"❌ Error: Docs directory '{docs_path}' does not exist.")
        return False
    
    # Collect all content from the docs
    all_textbook_content = ""
    for mdx_file in docs_dir.rglob("*.mdx"):
        with open(mdx_file, 'r', encoding='utf-8') as f:
            all_textbook_content += f.read().lower() + " "
    
    for md_file in docs_dir.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            all_textbook_content += f.read().lower() + " "
    
    # Check alignment
    aligned_topics = []
    missing_topics = []
    
    for topic in key_topics:
        if topic in all_textbook_content:
            aligned_topics.append(topic)
        else:
            missing_topics.append(topic)
    
    # Print results
    print(f"\n📊 PDF Alignment Results:")
    print(f"✅ Aligned topics ({len(aligned_topics)}):")
    for topic in aligned_topics[:10]:  # Show first 10
        print(f"   - {topic}")
    if len(aligned_topics) > 10:
        print(f"   ... and {len(aligned_topics) - 10} more")
    
    if missing_topics:
        print(f"\n❌ Missing topics ({len(missing_topics)}):")
        for topic in missing_topics[:10]:  # Show first 10
            print(f"   - {topic}")
        if len(missing_topics) > 10:
            print(f"   ... and {len(missing_topics) - 10} more")
        print(f"\n💡 Tip: Add content covering these missing topics based on the PDF")
        return False
    else:
        print(f"\n🎉 All key topics from the PDF are covered in the textbook!")
        return True


def main():
    parser = argparse.ArgumentParser(description="PDF Alignment Validator Subagent")
    parser.add_argument("--pdf-path", type=str, 
                       default="./Hackathon I_ Physical AI & Humanoid Robotics Textbook.md",
                       help="Path to the Hackathon PDF (as text/markdown)")
    parser.add_argument("--docs-path", type=str, default="./docs", 
                       help="Path to the docs directory containing textbook content")
    
    args = parser.parse_args()
    
    success = validate_pdf_alignment(args.pdf_path, args.docs_path)
    
    if success:
        print("\n✅ PDF alignment validation PASSED")
        sys.exit(0)
    else:
        print("\n❌ PDF alignment validation FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()