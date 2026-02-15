#!/usr/bin/env python3
"""
Validate all chapter frontmatter metadata against the schema
Uses ajv to validate all markdown files in docs/ against chapter-metadata-schema.json
"""

import json
import os
from pathlib import Path
import yaml
from typing import List, Dict, Any, Tuple

def load_schema() -> Dict[str, Any]:
    """Load the JSON Schema for validation"""
    schema_path = Path("specs/001-book-master-plan/contracts/chapter-metadata-schema.json")
    with open(schema_path, 'r') as f:
        return json.load(f)

def find_markdown_files(docs_dir: Path) -> List[Path]:
    """Recursively find all markdown files in docs directory"""
    markdown_files = []
    for ext in ['.md', '.mdx']:
        markdown_files.extend(docs_dir.rglob(f'*{ext}'))
    return [f for f in markdown_files if 'node_modules' not in str(f)]

def extract_frontmatter(file_path: Path) -> Dict[str, Any]:
    """Extract frontmatter from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        # Find the end of frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_str = parts[1]
            try:
                # Parse as YAML
                frontmatter = yaml.safe_load(frontmatter_str)
                return frontmatter or {}
            except yaml.YAMLError as e:
                print(f"  ❌ YAML parsing error in {file_path}: {e}")
                return {}
    
    return {}

def validate_field_types(frontmatter: Dict[str, Any], schema: Dict[str, Any], file_path: str) -> List[str]:
    """Validate field types according to schema"""
    errors = []
    
    # Check required fields exist
    required_fields = schema.get('required', [])
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    # Check field types and constraints
    properties = schema.get('properties', {})
    for field, field_def in properties.items():
        if field in frontmatter:
            value = frontmatter[field]
            field_type = field_def.get('type')
            
            # Type checking
            if field_type == 'string':
                if not isinstance(value, str):
                    errors.append(f"Field '{field}' should be string, got {type(value).__name__}")
                # Check string length constraints
                if 'minLength' in field_def and len(value) < field_def['minLength']:
                    errors.append(f"Field '{field}' length {len(value)} is less than minimum {field_def['minLength']}")
                if 'maxLength' in field_def and len(value) > field_def['maxLength']:
                    errors.append(f"Field '{field}' length {len(value)} exceeds maximum {field_def['maxLength']}")
                    
            elif field_type == 'number':
                if not isinstance(value, (int, float)):
                    errors.append(f"Field '{field}' should be number, got {type(value).__name__}")
                # Check numeric constraints
                if 'minimum' in field_def and value < field_def['minimum']:
                    errors.append(f"Field '{field}' value {value} is less than minimum {field_def['minimum']}")
                if 'maximum' in field_def and value > field_def['maximum']:
                    errors.append(f"Field '{field}' value {value} exceeds maximum {field_def['maximum']}")
                    
            elif field_type == 'integer':
                if not isinstance(value, int):
                    errors.append(f"Field '{field}' should be integer, got {type(value).__name__}")
                # Check integer constraints
                if 'minimum' in field_def and value < field_def['minimum']:
                    errors.append(f"Field '{field}' value {value} is less than minimum {field_def['minimum']}")
                if 'maximum' in field_def and value > field_def['maximum']:
                    errors.append(f"Field '{field}' value {value} exceeds maximum {field_def['maximum']}")
                    
            elif field_type == 'array':
                if not isinstance(value, list):
                    errors.append(f"Field '{field}' should be array, got {type(value).__name__}")
                else:
                    # Check array constraints
                    if 'minItems' in field_def and len(value) < field_def['minItems']:
                        errors.append(f"Field '{field}' has {len(value)} items, less than minimum {field_def['minItems']}")
                    if 'maxItems' in field_def and len(value) > field_def['maxItems']:
                        errors.append(f"Field '{field}' has {len(value)} items, exceeding maximum {field_def['maxItems']}")
                    
                    # Check array item types if defined
                    items_def = field_def.get('items', {})
                    if 'type' in items_def and items_def['type'] == 'string':
                        for i, item in enumerate(value):
                            if not isinstance(item, str):
                                errors.append(f"Array item {i} in field '{field}' should be string, got {type(item).__name__}")
                                
            elif field_type == 'null':
                if value is not None:
                    errors.append(f"Field '{field}' should be null, got {type(value).__name__}")
            
            # Check enum values
            if 'enum' in field_def and value not in field_def['enum']:
                errors.append(f"Field '{field}' value '{value}' is not in allowed values: {field_def['enum']}")
    
    return errors

def validate_chapter_metadata(docs_dir: Path) -> Tuple[int, int, List[Tuple[str, List[str]]]]:
    """Validate all chapter metadata in the docs directory"""
    schema = load_schema()
    markdown_files = find_markdown_files(docs_dir)
    
    total_files = len(markdown_files)
    validated_count = 0
    errors_found = []
    
    print(f"\nValidating {total_files} markdown files...\n")
    
    for file_path in markdown_files:
        print(f"📄 {file_path}")
        
        frontmatter = extract_frontmatter(file_path)
        
        if not frontmatter:
            print(f"  ⏭️  Skipped (no frontmatter)")
            continue
        
        errors = validate_field_types(frontmatter, schema, str(file_path))
        
        if errors:
            print(f"  ❌ Invalid")
            for error in errors:
                print(f"     • {error}")
            errors_found.append((str(file_path), errors))
        else:
            print(f"  ✅ Valid")
            validated_count += 1
    
    return total_files, validated_count, errors_found

def main():
    docs_dir = Path("docs")
    
    if not docs_dir.exists():
        print(f"❌ Directory {docs_dir} does not exist")
        return 1
    
    total, valid, errors = validate_chapter_metadata(docs_dir)
    invalid = total - valid
    
    print(f"\n{'='*60}")
    print(f"Validation Results:")
    print(f"  Total files: {total}")
    print(f"  Valid: {valid}")
    print(f"  Invalid: {invalid}")
    print(f"{'='*60}\n")
    
    if errors:
        print("Validation Errors Found:\n")
        for file_path, file_errors in errors:
            print(f"File: {file_path}")
            for error in file_errors:
                print(f"  • {error}")
            print()
        
        return 1  # Return error code
    else:
        print("✅ All markdown files have valid frontmatter metadata\n")
        return 0

if __name__ == "__main__":
    exit(main())